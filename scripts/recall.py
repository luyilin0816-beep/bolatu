#!/usr/bin/env python3
"""Read-only recall across every saved post and the full interview transcript.

Examples: recall.py 牛肉面 沙县 --source posts --limit 5
          recall.py 自由 意义 --source interview --limit 4
          recall.py --at 02:23:00 --window 90
Terms use OR matching; more matching terms rank first. No API or model needed.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def stamp(seconds):
    value = int(seconds)
    return f"{value // 3600:02d}:{value // 60 % 60:02d}:{value % 60:02d}"


def seconds(value):
    parts = value.split(":")
    if not 1 <= len(parts) <= 3:
        raise argparse.ArgumentTypeError("Use seconds, MM:SS or HH:MM:SS")
    try:
        result = 0.0
        for part in parts:
            result = result * 60 + float(part)
        if result < 0:
            raise ValueError
        return result
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid timestamp")


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*")
    parser.add_argument("--source", choices=["both", "posts", "interview"], default="both")
    parser.add_argument("--limit", type=int, default=6, help="Maximum results per source")
    parser.add_argument("--at", type=seconds, help="Read an interview time window")
    parser.add_argument("--window", type=float, default=60, help="Seconds before/after --at")
    args = parser.parse_args()
    if args.limit < 1 or args.window < 0:
        parser.error("limit must be positive; window must be nonnegative")
    if not args.terms and args.at is None:
        parser.error("Provide search terms or --at")
    terms = [term.casefold() for term in args.terms]

    def score(text):
        text = text.casefold()
        return sum(term in text for term in terms)

    if args.at is None and args.source in ("both", "posts"):
        posts = load("references/sources/posts/posts-corpus.json")
        rows = [(score(row["text"]), row) for row in posts]
        rows = sorted((item for item in rows if item[0]), key=lambda item: item[0], reverse=True)
        print(f"# X 帖子：{len(rows)} 条命中 / {len(posts)} 条保存文本")
        for _, row in rows[:args.limit]:
            print(f"\n## {row['created_at_utc']} | {row['url']}\n{row['text']}")

    if args.at is not None or args.source in ("both", "interview"):
        segments = load("references/sources/transcripts/interview-asr-segments.json")
        print("\n# 指定访谈（机器转写，可能错字；对话包含双方）")
        if args.at is not None:
            selected = [row for row in segments if row["end"] >= args.at - args.window and row["start"] <= args.at + args.window]
            for row in selected:
                print(f"[{stamp(row['start'])}] {row['text'].strip()}")
            if not selected:
                print("没有该时间范围的内容。")
        else:
            windows = []
            for index, row in enumerate(segments):
                if score(row["text"]):
                    nearby = segments[max(0, index - 3):index + 4]
                    rank = score(" ".join(item["text"] for item in nearby))
                    windows.append((rank, index))
            windows.sort(key=lambda item: item[0], reverse=True)
            used = set()
            emitted = 0
            for _, index in windows:
                if index in used:
                    continue
                start, end = max(0, index - 3), min(len(segments), index + 4)
                used.update(range(start, end))
                print(f"\n## {stamp(segments[start]['start'])}–{stamp(segments[end-1]['end'])}")
                for row in segments[start:end]:
                    print(f"[{stamp(row['start'])}] {row['text'].strip()}")
                emitted += 1
                if emitted >= args.limit:
                    break
            if not emitted:
                print("无字面命中；可尝试同义词，或按时间阅读完整转写。")


if __name__ == "__main__":
    main()
