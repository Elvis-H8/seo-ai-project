> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（八）：Cloudflare Turnstile 人机检测 | Web.Cafe

- 文档ID: `GH5edCpKjoU8R7xzbcIcq7Ojnid`
- URL: https://zcnalei7zaql.feishu.cn/docx/GH5edCpKjoU8R7xzbcIcq7Ojnid
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（八）：Cloudflare Turnstile 人机检测 | Web.Cafe
- 正文字符: 4191
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:17 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普专栏第（八）篇。介绍 Cloudflare Turnstile 作为免费、尽量少打扰的人机验证，用于 SaaS 用户变多后防自动化滥用。本章明确按 Nexty 当时基于 Supabase Auth 的版本来写：创建 Widget，把密钥接到 Supabase Attack Protection，并指出 Nexty 登录页已预集成，配环境变量即可。

## 方法 / 阈值
在 Cloudflare Turnstile 点 Add Widget，加入生产域名，并手动加 localhost 做本地测试（文称一个 Widget 最多约 10 个主机名）。Widget Mode：Managed（推荐，可信用户直接过、可疑的要点击）、Non-interactive（动画后台完成）、Invisible（完全静默）。pre-clearance 用于已验证用户后续是否少做挑战，正文按 No（每次完整验证）和 Yes（按模式豁免）解释，截图里该项也选了 Managed，和文字分法不完全对齐，配置时以控制台说明为准。创建后得到 Site Key（前端，环境变量 NEXT_PUBLIC_TURNSTILE_SITE_KEY）和 Secret Key（后端）。下一步到 Supabase Authentication → Attack Protection，把 Secret Key 填进 Captcha secret；这一节没有截图，也没写清还要不要在后台选择 Turnstile 作为验证码提供方。代码示例是 @marsidev/react-turnstile，仅当存在 Site Key 时渲染，onSuccess 把 token 存进 captchaToken state。正文没有写出把 token 交给 supabase.auth 的完整调用。

## 案例
示例 Widget 名 nexty auth，主机名为 nexty.dev 与 localhost。效果图是 Nexty 登录页邮箱登录处出现 Verify you are human。文中小节标题有拼写 Cloudfalre。

## 风险 / 冲突 / 实操注意
Secret Key 不得进入前端或仓库。非 Nexty 项目不能只配环境变量。Supabase 侧步骤写得很短，可能不完整，需对照当时 Supabase 文档。人机验证会误伤真实用户，模式选择要权衡。标题「免费」以 Cloudflare 当时配额为准。

## 证据位置
创建 Widget 与三种模式、密钥和环境变量、Attack Protection 一句说明、登录页预集成代码和效果图。
