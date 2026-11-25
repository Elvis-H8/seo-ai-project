> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（三）：Stripe支付配置与开发 | Web.Cafe

- 文档ID: `Spekduby7oR28nxiEhVc7N4onBg`
- URL: https://zcnalei7zaql.feishu.cn/docx/Spekduby7oR28nxiEhVc7N4onBg
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（三）：Stripe支付配置与开发 | Web.Cafe
- 正文字符: 9538
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:53:30 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2025-08-14 的 Nexty.dev 模板专栏第 3 篇，讲在模板里接 Stripe：沙箱密钥、Webhook、产品和几项账户设置。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]另给了两篇港卡办理外链，本轮未读，不能算已掌握。正文和配图说明里出现过测试密钥前缀、隧道地址和产品编号，摘要不转抄。

## 方法 / 阈值
先注册并按 Dashboard 指引完成开户前置。开发阶段进入 Sandbox，流程调通后再把产品等信息复制到 Live。在 Developers → API keys 把 Secret key、Publishable key 分别写入 STRIPE_SECRET_KEY、STRIPE_PUBLISHABLE_KEY。在 Webhooks 创建端点。本地调试时，作者让在 Cursor 或 VSCode 把端口转发设为 Public，把生成的地址加上模板路径 /api/stripe/webhook 填为 Endpoint URL；并称转发有时会失效，重设通常可保留同一地址，失败则可看社区帖或改用其他内网穿透。要勾选 7 类事件：charge.refunded、checkout.session.completed、customer.subscription.created / updated / deleted、invoice.paid、invoice.payment_failed，作者认为足够覆盖一次性支付和订阅，且模板里已有对应处理。创建后把签名密钥写入 STRIPE_WEBHOOK_SECRET。在 Product catalog 建产品，示例是一次性价、税类选 SaaS personal use、不含税；详情页的 Product ID、Price ID 会用在模板管理后台的定价计划。订阅产品按同样步骤再建。Radar 可加拦截规则，但正式环境是收费功能，Sandbox 可免费试用；文中给了若干按每周用卡数、客户账龄、风险分、同 IP 次数拦截的示例规则，只作作者建议，正式启用前要按 Stripe 当前语法和自身误拦风险检查。若希望同时段只能有 1 个订阅，在 Payments 相关设置里打开限制（文称仅对新增订阅生效），并把客户门户指向自己的网站，作者认为有助于减少重复订阅和争议；即使争议申诉成功，仍可能被扣约 15 美元手续费。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]该权限通常只支持一次性付款，订阅若也要用需另向客服申请。最后设置 Customer portal，方便用户看账单和改支付方式。Sandbox 调通后，产品可一键复制到 Live，其余步骤要手工再做，本篇可当检查清单。

## 案例
产品填写以 Nexty 模板自身为示例。价格在不同截图说明里出现过不一致的一次性标价，不能当准确售价。一张事件选择图的分类名称与正文列出的 7 个事件不完全对应，以正文事件名为准。限制订阅的示例域名有截断，只作界面示意。

## 风险 / 冲突 / 实操注意
把本地端口转成 Public，等于把开发服务暴露到公网，有安全风险；本库实践不照做，调试 Webhook 应优先用官方 CLI 或其他可控方式。密钥和签名密钥不得提交仓库或出现在前端。Radar 规则可能误伤正常用户。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]本文几乎不讲开户主体和税务，需与收款开户类资料分开看。本阶段只读，不配置真实支付。

## 证据位置
沙箱密钥与 Webhook 步骤、7 个事件、产品与 Radar、订阅限制、支付方式和 Portal，以及 Live 检查说明。
