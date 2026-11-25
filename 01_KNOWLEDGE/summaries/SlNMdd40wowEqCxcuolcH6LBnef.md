> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260201 独立开发省钱指南：Supabase 一个数据库给多个产品使用 | Web.Cafe

- 文档ID: `SlNMdd40wowEqCxcuolcH6LBnef`
- URL: https://zcnalei7zaql.feishu.cn/docx/SlNMdd40wowEqCxcuolcH6LBnef
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260201 独立开发省钱指南：Supabase 一个数据库给多个产品使用 | Web.Cafe
- 正文字符: 4965
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:45:02 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2026-02-01 的省钱方案：用 PostgreSQL 的 Schema，让多个低流量产品共用同一个 Supabase 数据库，避免每做一个产品就新建一个 Project。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]作者认为独立开发者选库常在「贵」和「麻烦」之间：Supabase 免费账号只能建 2 个 Project，付费后每多一个约加 10 美元；Neon 虽号称免费可建很多 Project，但靠流量收费，实际流量费很贵；自建 Postgres 又要操心性能和安全。本方案适合「即使合并，流量也不超过免费额度」的情形；作者写当时免费账号约有 5GB 出站流量，小产品用不完。额度会变，要以官网为准。

## 方法 / 阈值
把 Schema 比作文件夹：同一 Database 下多个 Schema，表互不干扰；Supabase 默认表在 public。迁移示例是 Next.js + Drizzle，从 Neon 迁到 Supabase：1) drizzle.config.ts 加 schemaFilter，只管理本产品的 schema，避免误删 public 里其他表。2) 用 pgSchema 定义同名 schema，把原来的 pgTable、pgEnum 改成该 schema 下的 table 和 enum。3) 全量迁移时不要在旧迁移上打补丁，作者建议删除 lib/db/migrations/ 后重新 generate 再 migrate，让 Drizzle 自动建 schema 和表。4) 在环境变量里配置旧库、新库连接串，按外键顺序用脚本从旧库 public 表查出数据，做列名映射后每 100 行批量写入，冲突策略是 onConflictDoNothing。5) 生产环境把 DATABASE_URL 换成新连接并重启。Nexty 用户可用模板内置 SKILL，非模板用户也可把文档交给 AI 辅助。

## 案例
没有给出真实迁移的数据量或故障记录，表例包括 user、pricing_plans、orders。总结称同一库可跑 10 个甚至 20 个低流量副业，各有「干净的数据空间」。

## 风险 / 冲突 / 实操注意
「既省钱又安全」不完整：共用一个 Project，连接数、出站流量、故障和误操作的影响面会变大。本文主要处理 Drizzle 里的业务表，几乎没谈 Supabase Auth、Storage、RLS 如何按产品隔离；认证用户通常在项目级的 auth schema，多产品共用可能互相看见或共用用户体系。删除迁移目录只适合作者说的全量搬迁，已有生产迁移链的人不能照搬。连接串和密钥不能进仓库。脚本里的 SQL 拼接和字段映射要自己验证，避免漏列或外键顺序错误。onConflictDoNothing 会静默跳过冲突行。

## 证据位置
成本对比、Schema 说明、五步迁移和文末适用规模。
