> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260508 开 gsc、ga4 API步骤 | Web.Cafe

- 文档ID: `CyQmdCUSuoiTzfxZ2xKc3AVBnrg`
- URL: https://zcnalei7zaql.feishu.cn/docx/CyQmdCUSuoiTzfxZ2xKc3AVBnrg
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260508 开 gsc、ga4 API步骤 | Web.Cafe
- 正文字符: 1856
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:42:27 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者随风整理开通 Google Search Console API 和 GA4 API 的步骤，供服务器脚本、定时任务或数据看板自动拉数。开头说可以把全文发给 AI，让它操作浏览器完成。这是权限配置说明，不含完整拉数代码。

## 方法 / 阈值
1) 在 Google Cloud Console 建或选项目，到「API 和服务→库」启用 Search Console API、Analytics Data API、Analytics Admin API。2) 在凭据里创建服务账号，到详情页添加 JSON 密钥，保存到后端且不要提交到 Git；后续授权用服务账号邮箱。3) 在 Search Console 对应资源的「设置→用户和权限」添加该邮箱：只读选「受限」，若要提交 sitemap 等则选「完整」；多个站点要分别授权。4) 在 GA4「管理→访问权限管理」添加同一邮箱，角色用 Viewer 即可读报表。5) 只读常用 scope 为 webmasters.readonly 与 analytics.readonly；Search Console 写操作改用 webmasters。常见错误：403 多半没把服务账号加进 GSC 或 GA4；property not found 是媒体资源未授权或 ID 填错；no matching site 可能是授权了 URL 前缀资源、代码却查域名资源，或资源本身不存在。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 案例
无实际拉数样例。

## 风险 / 冲突 / 实操注意
界面和角色名称会变，应以当时 Google 后台为准。把整份流程交给会操作浏览器的助手时，仍不要让它接触或上传真实密钥文件。「完整」权限大于只读，按最小权限开。

## 证据位置
六节流程、scope、错误与安全提醒。
