> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260429 Cloudflare 开源一套代码，搞定多域名邮件统一收发 ｜ Web.Cafe

- 文档ID: `SEp2dmvikoXaRMxOZbmc5EzunEJ`
- URL: https://zcnalei7zaql.feishu.cn/docx/SEp2dmvikoXaRMxOZbmc5EzunEJ
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260429 Cloudflare 开源一套代码，搞定多域名邮件统一收发 ｜ Web.Cafe
- 正文字符: 1964
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:42:27 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者禾火介绍 Cloudflare 开源项目 agentic-inbox（仓库 cloudflare/agentic-inbox）：一个程序、一个账号管理多个域名邮箱，客户写到哪个地址，就从哪个地址回，避免用个人 Gmail 回信损害信任。

## 方法 / 阈值
项目自称完整邮件客户端，经 Email Routing 收发，带编辑器、线程、搜索和附件；每个邮箱用独立 Durable Object 和 SQLite，附件放 R2；侧边栏有 AI agent 和多个邮件工具，可自动起草但发送前需确认。作者解释此前 Email Routing 只能收不能发，此次升级为 Email Service（文中称 Agents Week 期间公测），添加域名时 SPF、DKIM、DMARC 自动配置。部署跟 README；坑是：若没开过 Cloudflare Access 要先开通（文称 0 元套餐即可），否则会卡在 Access；多域名在环境变量里用逗号分隔，不必每个域名单独部署；不要直接从公共仓库部署（作者称当时公共仓部署可能有问题），应先克隆再推到自己的私有仓库再部署。还提到内置 MCP，可让 Claude Code 等起草后确认发送；开源可自己加未读计数、Discord/飞书通知、按客户域打标签、非工作时间自动回执等。

## 案例
费用转述：发信需要 Workers 的 5 美元/月套餐，该套餐下每天 1000 封免费、各产品共用，作者折合每月约 3 万封；超出按量计费；Email Routing 收信仍免费。已订 Workers Paid 则边际成本被说成基本为零。这些是文章当时的说法，要以官方报价和限额为准。

## 风险 / 冲突 / 实操注意
公测功能和限额会变。把收件箱接给外部 agent 仍有误发和隐私问题，应保持人工确认发送。从公共仓部署的限制是否还在，需看当时 Cloudflare 文档。本篇是产品介绍加部署提醒，不是逐步截图教程。

## 证据位置
问题场景、特性列表、费用、MCP/开源加分和三个部署坑。
