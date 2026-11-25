> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（五）：域名邮箱配置教程 | Web.Cafe

- 文档ID: `Kovvdk0fhoDw3SxajuAcyyMdnlg`
- URL: https://zcnalei7zaql.feishu.cn/docx/Kovvdk0fhoDw3SxajuAcyyMdnlg
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（五）：域名邮箱配置教程 | Web.Cafe
- 正文字符: 5583
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:17 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普专栏第（五）篇，标题与内容一致：用 Cloudflare 免费邮件转发接收域名邮箱，再用 Resend SMTP 让 Gmail 以该地址回信。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]前置要求先完成域名解析和「Resend 集成」；由于（四）的正文并没有真正讲 Resend 开户，这个前置在本库里是缺口。

## 方法 / 阈值
1) Cloudflare Email Routing：Get started，自定义地址（示例 hi）转发到个人邮箱，验证目的地后添加 MX、TXT 并启用。成功标志是 Routing Enabled、Email DNS records Configured。2) 回复：Gmail 全部设置 → Accounts and Import → Add another email address，填写姓名和域名邮箱；到 Resend Setting-SMTP 复制 Host/Port/User，密码用 API 密钥，启用 SSL；到确认邮件里点 Confirm，之后在 From 里选择域名邮箱。

## 案例
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。][去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]MX 示例图注出现 nextrt.cn.com，与 nexty.dev 可能是识别误差。比（四）多出的内容主要是这些界面细节，不是另一套方法。

## 风险 / 冲突 / 实操注意
与（四）相同：API 密钥保管、Gmail 代发和 DNS 认证。转发只解决收信，回信依赖 Resend；这不是完整的托管邮箱（没有独立收件箱界面）。确认链接不要从截图转发出去。Cloudflare 后来还有 Email Service / agentic-inbox 等方案（见禾火那篇），与本篇的「转发+Gmail」不是同一套。

## 证据位置
前置说明、Routing 配置到 Enabled，以及比（四）更完整的 Gmail 添加与确认截图。
