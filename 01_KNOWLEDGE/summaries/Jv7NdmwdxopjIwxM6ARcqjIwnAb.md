> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260728 Cloudflare Pages 如何返回 410 Gone（\_redirects 不支持的坑）

- 文档ID: `Jv7NdmwdxopjIwxM6ARcqjIwnAb`
- URL: https://zcnalei7zaql.feishu.cn/docx/Jv7NdmwdxopjIwxM6ARcqjIwnAb
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260728 Cloudflare Pages 如何返回 410 Gone（_redirects 不支持的坑）
- 正文字符: 2286
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:42:27 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者 Junyi 用回收域名上新站后，Search Console 出现大量 /post/xxx、/category-xxx 这类旧 WordPress 路径的 404。他认为搜索引擎对 404 会反复重试，不如返回 410 Gone 表示内容已永久不存在。接着记录了 Cloudflare Pages 的一个坑和对应做法。

## 方法 / 阈值
先试在 _redirects 里写 /post/* 和 /category-* 为 410，部署后仍是 404。查官方文档后确认 _redirects 只支持 301、302、303、307、308，写 410 会被静默忽略且不报错。还发现测试 301 无效是因为列顺序写反：正确是「源路径 → 目标路径 → 状态码」。解决办法是用 Pages Functions，在项目根目录（不要放进 src 或 public）放 functions/[[path]].js，用正则匹配旧 WP 路径，命中则返回 410 纯文本，其余 context.next() 交给静态资源。部署日志里会出现 Uploading Functions bundle。用 curl 看状态码验证：旧路径 410，首页仍 200。小结：3xx 用 _redirects，4xx/5xx 用 Functions，更复杂的限流鉴权用 Functions 或 Workers。

## 案例
文中示例还包含一条精确路径 GONE_EXACT（一串以 /. 开头的随机路径），应是该域名上的具体垃圾 URL，不是通用规则。验证命令里的域名是 example.com 占位。

## 风险 / 冲突 / 实操注意
410 是否比 404 更能加快取消索引，要以 Google 当时说明为准，本篇是作者经验。Functions 代码和目录约定可能随 Pages 产品更新。不要把文中那条特殊精确路径抄到自己的站上。

## 证据位置
背景、_redirects 限制与格式、Functions 示例、部署和验证、文末对照表。
