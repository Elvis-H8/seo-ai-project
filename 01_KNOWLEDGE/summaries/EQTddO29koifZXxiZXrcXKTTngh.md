> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（七）：Cloudflare R2 免费图片存储 | Web.Cafe

- 文档ID: `EQTddO29koifZXxiZXrcXKTTngh`
- URL: https://zcnalei7zaql.feishu.cn/docx/EQTddO29koifZXxiZXrcXKTTngh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（七）：Cloudflare R2 免费图片存储 | Web.Cafe
- 正文字符: 4870
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:43:00 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普同一专栏的第（七）篇：把 Cloudflare R2 配成对象存储，用于头像、AI 生成的图视频、博客图等。标题强调「免费」，正文没有展开当时的免费额度细节，需对照官方。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 方法 / 阈值
在 R2 概览创建 Bucket（名称、Location 可选 Automatic、存储类 Standard）。到 Settings 复制 R2_BUCKET_NAME，并从 S3 API 地址里取出 R2_ACCOUNT_ID。添加自定义域名，按提示确认 CNAME 后 Connect，再把「https://自定义域」写入 R2_PUBLIC_URL。配置 CORS，限制哪些来源可用 GET/PUT/HEAD 访问。回到 R2 首页 Use R2 with APIs → Manage API tokens，创建密钥，写入 R2_ACCESS_KEY_ID 和 R2_SECRET_ACCESS_KEY。

## 案例
截图和正文里的名称不完全一致：桶名有 my-nextjs-dev 与 my-nexty-dev，自定义域有 cdn.nexly.dev 与 cdn.nexty.dev，属于示例笔误，不能当真实配置。文中 .env 示例写成 R2_PUBLIC_URL=https://R2_PUBLIC_URL，显然是占位没改完。CORS 正文列出的来源是 127.0.0.1:3006、localhost:3006、https://kontextimage.com、https://flux-kontext.nexty.dev，MaxAgeSeconds 为 3600，允许头和暴露头也写在 JSON 里；图注则出现过 localhost:3000 和 nexty.dev、MaxAge 3000 秒，两套不要混用，应按自己的站和端口改 AllowedOrigins。

## 风险 / 冲突 / 实操注意
Access Key/Secret 是密钥。CORS 若把生产域配错或过宽，会放大跨域写入风险。自定义域和 TLS 设置要在 Cloudflare 帐号里完成验证。本篇是控制台配置，没有给出应用里上传文件的代码。

## 证据位置
场景说明、建桶、自定义域、有瑕疵的环境变量示例、CORS JSON 和创建 API 令牌。
