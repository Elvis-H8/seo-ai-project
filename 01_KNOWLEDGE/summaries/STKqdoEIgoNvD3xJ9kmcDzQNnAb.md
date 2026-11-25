> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 养网站防老第8步：添加统计代码，提交到 Google Search Console，增加外链，等待被收录 | Web.Cafe

- 文档ID: `STKqdoEIgoNvD3xJ9kmcDzQNnAb`
- URL: https://zcnalei7zaql.feishu.cn/docx/STKqdoEIgoNvD3xJ9kmcDzQNnAb
- 路径: 出海seo资源分享V1.0/养网站防老/20240812 养网站防老第8步：添加统计代码，提交到 Google Search Console，增加外链，等待被收录 | Web.Cafe
- 正文字符: 4967
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:21:25 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 概念
上线后三件事：加统计、提交 GSC（含 Sitemap）、用外链吸引爬虫等待收录。强调用 GitHub 做源、Vercel/Cloudflare 托管，源码在自己手里，避免绑定单一在线文档平台。

## 方法
一、GA4：创建媒体资源（例域 phone-number-generator.com）→行业与小型规模→业务目标选「获取基准报告」→平台选网站→创建数据流→复制安装代码。作者把代码放在每个 HTML 的 </body> 前、包在 style=display:none 的 div 里，理由是避免统计脚本拖慢首屏，统计挂了也不影响访问。静态站每个文件都要加；改完 git push，Vercel 自动部署。二、GSC 细节指向另一篇已有教程，并强调「一定要制作好 Sitemap 并提交」。三、外链：到谷歌爬虫常去的网站留新站链接，收录快慢取决于蜘蛛访问那些页面的频率。等几天仍未收录则检查页面质量，并看 GSC 提醒。之后进入全网宣传阶段。

## 阈值 / 主张
作者称用外链引收录「最快 1 个小时，慢的话也一天足够」。这是经验口吻，不是保证。

## 案例
演示站 phone-number-generator.com（与第1步找词案例相连）；提交记录「add analytics code」。

## 依赖
Google Analytics 4、GSC、GitHub、Vercel、Cloudflare；GSC 与外链细节依赖系列里其他教程。

## 风险 / 不宜无依据背书
文中谷歌安装说明截图写的是把代码放到 </head> 之后，作者实践却放到隐藏 div 且在 </body> 前，两者不一致。用 display:none 包裹统计代码是否影响采集，需以 GA 当前文档为准，不宜照搬。『1 小时到 1 天必收录』过于乐观，新站常更慢。例域与演示代码 ID 已出现在公开文档中。

## 证据位置
「今天我们聊第8步」下的三小步；「一、添加统计代码」逐步截图至隐藏 div 说明；「二、提交到 Google Search Console」；「三、提交外链」及等待收录的时效与排查。
