# 素材与图片来源

## 指定访谈

- 发布者：[邵艾伦Alan（薄肌版）@AlanShao111](https://x.com/AlanShao111)。
- 原帖：[对话孙宇晨：年轻人如何抓住AI时代的机会？](https://x.com/AlanShao111/status/2108406850727076182)。
- 发布于2026-10-09；视频长15749.336秒，即4:22:29.336。
- 27个连续分块覆盖全部音频，机器转写已完成；另有10756帧画面字幕OCR，采用1/2秒间隔抽样。
- 双方观点、追问、玩笑、分歧、轶事都参与整理。机器识别不是人工逐字听校，人名、术语和数字可能识别错；03:40分块开头有识别异常。
- [完整机器转写](references/sources/transcripts/interview-asr.md)、[段落JSON](references/sources/transcripts/interview-asr-segments.json)、[OCR文字](references/sources/transcripts/interview-ocr-complete.md)。原视频和转写模型不随仓库分发。

README互动快照：2026-10-09通过原帖读取6619赞、520转发。只表示采集时状态，不是实时计数，也不是全平台热度排名。

## X文字

保存1111条去重后的Alan本人文字，日期跨度2025-09-05至2026-10-09 UTC。915条普通帖、74条引用帖自写文字、122条按文本特征识别的回复/提及；类型存在启发式误差。

这不是历史全量保证：早期较稀疏，没有逐一解读所有附图、其他视频和外链。引用帖中的他人内容单独存为上下文，不冒作Alan本人发言。未扩大到其他平台。

- [原帖文字](references/sources/posts/posts-corpus.md)
- [结构化文本](references/sources/posts/posts-corpus.json)
- [全部帖子索引](references/knowledge/posts-topic-index.json)：1111条全部保留，关键词未命中的记录也在。

## 页面只使用三张图片

| 文件 | 来源 | 用途 |
|---|---|---|
| `assets/interview-cover-ai.png` | [指定访谈原帖](https://x.com/AlanShao111/status/2108406850727076182)，[原图](https://pbs.twimg.com/media/HUIkbsIbYAAML93.jpg?name=orig) | README首屏；基于原封面经AI辅助改编，保留人物访谈构图，重新设计背景与文字，不是原发布者提供的新版封面 |
| `assets/alan-avatar.jpg` | [Alan的X主页](https://x.com/AlanShao111)，[头像文件](https://pbs.twimg.com/profile_images/2086673168098570240/6K719ph7_200x200.jpg) | 人物识别；主页公开资料确认同一头像 |
| `assets/lifestyle.png` | 用户指定图片；[对应Alan公开帖子](https://x.com/AlanShao111/status/2098887661918536127) | 生活方式梗图；图中原署名为@thegymhighlights，不标作Alan住宅实拍 |

没有发布聊天记录截图、其他人物照片或未选中的候选图片。页面徽章只表示材料数量、形式与非官方身份，不表示认证或授权。

原帖、访谈与图片归相应权利人。公开访问不代表原作者授予本项目开源许可；本项目没有以统一MIT等许可证覆盖第三方素材。所有出处均保留，方便回看原作。

## 构建方法

采用[女娲·Skill造人术](https://github.com/alchaincyf/nuwa-skill)的思维提炼与表达建模方法，按本项目指定的两类来源适配。方法创建者[花叔](https://x.com/AlchainHust)。

本项目没有训练/微调模型，没有声称准确统计过一亿Token消耗。模拟回答不等于本人新发表的观点。
