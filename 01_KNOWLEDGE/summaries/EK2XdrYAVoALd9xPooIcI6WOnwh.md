> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（二）：Supabase 登录与数据库配置 | Web.Cafe

- 文档ID: `EK2XdrYAVoALd9xPooIcI6WOnwh`
- URL: https://zcnalei7zaql.feishu.cn/docx/EK2XdrYAVoALd9xPooIcI6WOnwh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（二）：Supabase 登录与数据库配置 | Web.Cafe
- 正文字符: 14933
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:52:17 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2025-08-14 的 Nexty.dev 模板专栏第 2 篇，讲如何把模板接到 Supabase 的数据库和 Auth。获取 API 密钥被写成模板的必要步骤。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]这是模板配置说明，不是从零设计后端。原文档和配图说明里出现过 OAuth 客户端、项目地址等敏感信息，摘要不转抄；若那些截图来自真实项目，应视为可能已暴露，需要当事人自行轮换，本库实践也不会去使用这些值。

## 方法 / 阈值
先装或更新 Supabase CLI（文中给了 macOS/Linux 的 brew 和 Windows 的 scoop）。建项目：用官网 New Project，记下数据库密码；再从项目 Connect 或 App Frameworks（Next.js）复制变量到 .env 或 .env.local。初始化走模板脚本：pnpm db:login（按提示完成浏览器登录）、pnpm db:link（粘贴刚才的数据库密码，输入时不回显）、pnpm db:update。Windows 上若 db:update 报 Invalid project ref format，作者让把 package.json 里该脚本的 && 改成分号后再跑。完成后可在 Table Editor 看到模板内置表，文中出现过 orders、pricing_plans、subscriptions、usage、users；在 Database 里还能看到索引、触发器、函数和行安全策略。自行改表：pnpm db:new-migration <名称>，在 supabase/migrations 新文件里写 SQL，再 db:update；不懂表设计时可先和 AI 讨论再写入文件。Auth 默认三种：Google、GitHub、邮箱 Magic Link。注意不要用 QQ 邮箱调试，因 QQ 会在后台访问链接导致 Magic Link 失效；建议先调 GitHub，配置更简单；作者还提到在中国用 ClashX 本地调 Google 登录可能失败，需开 Tun。邮箱登录默认开着，OTP/链接过期默认 1 小时，建议改成 600 秒（10 分钟），并可改 Magic Link 邮件模板。GitHub：在 Supabase 启用并复制 Callback URL，到 GitHub OAuth Apps 新建应用，Homepage 可用生产或本地地址，Authorization callback URL 用刚才的回调，再把 Client ID 和 Secret 填回 Supabase。Google：同样先启用并复制回调，在 Google Cloud 建项目并配置 Google Auth Platform（受众选 External 等），创建 Web application 的 OAuth 客户端；本地需加 http://localhost:3000 和 http://localhost 为 Authorized JavaScript origins，重定向 URI 用 Supabase 回调；把 Client ID、Secret 填回 Supabase，并把 Client ID 放到 NEXT_PUBLIC_GOOGLE_CLIENT_ID 以开 Google One Tap。再在 Data Access 勾选 userinfo.email、userinfo.profile、openid。URL Configuration：Site URL 是默认回跳，有生产地址就填生产，域名未启用可先填开发地址；Redirect URLs 可同时放生产和开发，发布后建议删掉开发地址。最后在 Project Settings 的 Data API 把项目 URL 写入 NEXT_PUBLIC_SUPABASE_URL，在 API Keys 把 anon key 和 service_role key 分别写入 NEXT_PUBLIC_SUPABASE_ANON_KEY 和 SUPABASE_SERVICE_ROLE_KEY。service_role 不得加 NEXT_PUBLIC，也不得提交到仓库或贴到对话里。

## 案例
截图以 nexty demo、nexty.dev 组织的免费额度项目为例，区域选美国西部等，仅作界面示意。Windows 报错有截图。作者写「只要 GitHub 登录成功且 Google 配置正确，Google 登录肯定没问题」，这是经验判断，不是保证。

## 风险 / 冲突 / 实操注意
整篇绑定 Nexty 脚本和目录，换模板不能照抄命令。把 service_role 暴露到前端等于放开数据库。截图中的客户端编号和项目引用不要复制。ClashX Tun 只是作者的本地调试备注，不是网络配置教程。用 AI 写迁移仍要自己看 SQL 和 RLS。本阶段只读不部署。

## 证据位置
CLI 与建项目步骤、Windows 脚本修改、迁移命令、三种登录和重定向配置，以及环境变量清单。
