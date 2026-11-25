> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（四）：Resend邮件服务 | Web.Cafe

- 文档ID: `CWo8dIZImoq3woxaQaGcAybdnob`
- URL: https://zcnalei7zaql.feishu.cn/docx/CWo8dIZImoq3woxaQaGcAybdnob
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（四）：Resend邮件服务 | Web.Cafe
- 正文字符: 5003
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:17 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
标题是「（四）Resend 邮件服务」，原文链接对应 Resend 那一章，但抓取到的正文主体是 Cloudflare Email Routing 收信、再用 Resend SMTP 在 Gmail 里用域名邮箱回信。这与第（五）篇域名邮箱教程高度同构，不能互相替代，也不能当成已经教过 Resend 控制台里的注册、验证域名、建 API 密钥和在应用里发信。前置步骤反而把「Resend 集成」链回本篇自己的链接，结构是乱的。

## 方法 / 阈值
正文步骤与（五）相同主线：在 Cloudflare Email 里 Get started，建自定义地址（示例 hi）转发到个人邮箱，验证目的地，添加 MX/TXT 并启用，看到 Routing Enabled、DNS Configured。然后在 Gmail 设置里添加另一个发信地址，把 Resend SMTP 的 Host smtp.resend.com、Port 465、User resend 填进去，密码填 RESEND_API_KEY 字符串，用 SSL，提交后到 Gmail 确认，之后发信可选域名邮箱。

## 案例
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]部分图注含 Gmail 确认链接，摘要不转写这些链接。

## 风险 / 冲突 / 实操注意
本篇没有写出如何在 Resend 创建账号、验证发信域和生成 API 密钥，只假设已有 RESEND_API_KEY。密钥不能进仓库或聊天。Gmail「用自己的 SMTP 代发」政策可能变化，送达率还取决于 SPF/DKIM/DMARC 是否与转发、Resend 一起配好。不要把标题理解成已覆盖 Resend 产品集成。与（五）对照阅读，记录差异而不是跳过。

## 证据位置
标题与前置链接的错位，以及 Email Routing 到 Gmail SMTP 的全过程。
