> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250926 如何利用 Google 最新的 MCP 服务，将网站性能从 83 分优化到 97 分

- 文档ID: `UUDRdcjcWox5lTxjKUPcz1Bsn14`
- URL: https://zcnalei7zaql.feishu.cn/docx/UUDRdcjcWox5lTxjKUPcz1Bsn14
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250926 如何利用 Google 最新的 MCP 服务，将网站性能从 83 分优化到 97 分
- 正文字符: 4689
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:47 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者布衣记录用 Google 的 chrome-devtools-mcp，在 Cursor 里分析并改项目，自称把某站移动端 Lighthouse 性能从 83（黄）提到 97（绿），并认为有助于 Core Web Vitals、体验和 SEO。这是一次个人优化过程，不是 Google 官方「保证提分」教程。对比图注有一处写「优化前后性能得分均为 83」，和标题、正文的 97 不一致，引用分数要以原图和作者陈述对照，不能两边都当精确值。

## 方法 / 阈值
演示环境是 Cursor 1.6.45。安装：官方页的 Add to Cursor，或在 Cursor Settings → MCP → New MCP Server，用 npx 启动 chrome-devtools-mcp 的最新包（文中给出 command，args 默认可空），然后重启。分析：打开项目对话，模式选 Agent，先让它对目标网址做 Chrome DevTools 性能分析（示例是 developers.chrome.com，需换成自己的站）。过程中会弹出权限，作者点允许。分析完成后，可附上 package.json、next.config.ts（非必须），把模型改成文中写的 gtp-5-high（拼写应为某个 GPT-5 高推理档，名称会过时），再请它按报告改项目；失败就输入继续。文末对 Next.js 且部署在 Vercel 的站点给了一条经验：若「不需要 Image 组件的性能优化」，在 next.config 的 images 里只保留 domains 并设 unoptimized: true。作者同时声明这套方法只适用于简单站点，不含企业级或复杂应用，局限性很大。

## 案例
优化前移动端性能 83，无障碍、最佳做法、SEO 均为 100；优化后性能称 97，其余仍 100。分析示例站时，图注提到 TTFB 约 884ms（目标写小于 600ms）、字体 font-display 为 block 造成 FOIT 约 130ms、以及 CDN、分包、第三方脚本等建议。这些是对 Chrome 开发者站点或作者项目的分析摘录，不能直接当成用户站点的诊断。

## 风险 / 冲突 / 实操注意
实验室 Lighthouse 分数不等于实地 Core Web Vitals，更不能保证排名提升。把自动改代码的权限交给 Agent，需要人工审查，避免误关优化或引入错误。images.unoptimized 和已过时的 domains 字段可能让图片更差，只是作者在特定 Vercel 场景下的权宜，不是通用建议。MCP 包名、Cursor 菜单和模型名都会变，以当时官方说明为准。演示分析的是别人的网站，对自己的项目才有改代码的意义。

## 证据位置
前后对比图、两种安装方式、分析与改代码指令，以及注意事项里的 Vercel 图片配置和适用范围声明。
