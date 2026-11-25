# 分块015 / 17

这是ALL_KNOWLEDGE的传输分块，不是独立证据集。先读README，不要把读本块当全部读完。


---

## 源文件：01_KNOWLEDGE/summaries/LDIpdOOFtoEp0dxQc7zcJ5cSntg.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20241129 Google Ads 经理账号(MCC)注册并获取ADS API Token拿关键词搜索量

- 文档ID: `LDIpdOOFtoEp0dxQc7zcJ5cSntg`
- URL: https://zcnalei7zaql.feishu.cn/docx/LDIpdOOFtoEp0dxQc7zcJ5cSntg
- 路径: 出海seo资源分享V1.0/广告投放/20241129 Google Ads 经理账号(MCC)注册并获取ADS API Token拿关键词搜索量
- 正文字符: 3383
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:58:22 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者袁智翔 2024-11-29 说明为什么要开 Google Ads 经理账号（MCC），以及如何在 API 中心申请开发者令牌，用来查关键词规划里的搜索量。他列的 MCC 好处包括集中管理多个子账号、看跨账户数据、用规则和脚本；但对他当时最必要的原因是：使用 Google Ads API 需要 MCC。本篇没有把 API 调用的完整授权流程写出来。

## 方法 / 阈值
注册：进入经理账户相关页面，点 Go to Manager Accounts，填写显示名称（可自定），个人使用可选「管理我的账号」，账单地址如实填，时区和币种作者写「按默认」，再完成人机验证，出现恭喜页后即可进入。截图里默认币种是美元，这与同文件夹多篇「结算国选中国、币种选人民币或港币且创建后不能改」的提醒不一致，不能随便跟默认。API：在顶部搜索 API，进入 API 中心，填常用 Gmail、自拟公司名称、公司网址、公司类型（他选独立开发者）、预期用途（他填「自动化分析及规划广告」）、主要营业地点（他选实际地点，默认中国），同意条款后创建令牌。令牌要复制并妥善保存。文称刚创建时是测试账号访问权限，用来做关键词规划和搜索量预测够用；若要与正式账号互动，需另申请基本访问权限。后面的 Python 示例只展示了以某个词为核心扩展出若干相关词及其平均月搜索量，作者说这是「最权威的谷歌搜索量」，但同时写明走 Python API 还要配置授权，过程较复杂，完整步骤不在本篇，只说有兴趣可另开帖。文中把这部分授权写成还要「创建 GSC 账号并配置 OAuth2」，表述容易和 Search Console 混淆，实际接 Ads API 通常要走谷歌云与广告账号授权，本篇不能当完整接入手册。作者还提到若还没有网站，就先随便买域名、用 Vercel 上一个站再填网址，这不是本阶段的实践建议。

## 案例
演示输出里列出若干与「ai image」相关的扩展词及月搜索量，其中最高的词图注约为 335 万。这是一次接口结果，受地区、网络和权限级别影响，不能直接当成全球稳定需求。

## 风险 / 冲突 / 实操注意
开发者令牌是敏感凭证，摘要不转抄，也不能提交到仓库或对话里。测试权限与正式权限不同，搜索量也有区间和口径问题，不宜写成「最权威、可直接当选词标准」。MCC 的币种若跟默认选成美元，可能与之后付款、赠金和验证安排冲突。为填表而临时搭一个站，没有独立价值。本阶段不申请 MCC 或 API。

## 证据位置
MCC 注册页与成功页、API 中心填表和测试权限说明，以及关键词扩展结果截图。


---

## 源文件：01_KNOWLEDGE/summaries/EDtodKv87oJuQxxgL6xcM5TVnpR.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20241128 Google Ads注册投流教程【中文界面】 | Web.Cafe

- 文档ID: `EDtodKv87oJuQxxgL6xcM5TVnpR`
- URL: https://zcnalei7zaql.feishu.cn/docx/EDtodKv87oJuQxxgL6xcM5TVnpR
- 路径: 出海seo资源分享V1.0/广告投放/20241128 Google Ads注册投流教程【中文界面】 | Web.Cafe
- 正文字符: 6899
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 01:00:10 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者良辰美 2024-11-28 的中文界面教程，与同日英文界面那篇不是同一路径：这篇实际上顺着向导建并发布了一个搜索广告系列，目的写成「先快速打开后台、拿到看数据的权限」。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]文中还提到要靠网络环境才能完成验证，只记作者遇到了加载失败，不写成配置方法。配图里出现过账号编号和一次性验证码，摘要不转抄。

## 方法 / 阈值
在已有谷歌账号并完成两步验证后进入 Ads。作者有一个状态为已删除、需重新激活的旧账号截图，也有 2021 年创建的系列，说明演示不一定是全新账号。新建系列时目标选网站流量，类型选搜索；出价界面出现过转化次数，也出现过点击次数并设置每次点击费用上限（示例为 10 元）。作者写后面多点继续、先用默认项，真要投放再回头研究。预算页数字较乱，还有「未能保存更改」提示，他正想调低金额时弹出身份确认；当时可跳过，但页面警告 2024-12-12 之后不能再跳过。填完验证码后页面多次加载失败，刷新后才到检查页。检查页里该系列是最大化点击、新老客户同样出价，网络勾了搜索合作伙伴和展示广告网络，地理位置为所有国家和地区，语言为英语，优化得分图注约 88.5%。检查通过后即可发布。发布后提示账号无法展示广告，要补结算：账单国家选中国、币种人民币，填国内真实姓名和地址；付款方式可见卡或 PayPal。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。][去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]税务信息图注为和中国个人、非增值税纳税人相关。

## 案例
这是作者自己走通一次发布向导的记录，不是一组经过优化的投放结果。默认把范围做成全球、并打开合作伙伴和展示网络，与同文件夹冉云、Ku3c「先只投搜索、取消合作伙伴和展示、地理位置选所在地」的建议相反。

## 风险 / 冲突 / 实操注意
购买或用接码得到的谷歌账号不能用。为「先看后台」就按默认发布广告，可能在未设好转化、预算和定向时就开始消耗。跳过身份确认的窗口早已过去。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]本阶段不注册、不买号、不发布广告。

## 证据位置
两步验证、创建并发布搜索系列、身份确认期限，以及补结算和待审核界面。


---

## 源文件：01_KNOWLEDGE/summaries/G6sddZ6PfoOxKexYvCJchPDbnJh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260508 codex连接stripe，分析网站收入 ｜ Web.Cafe

- 文档ID: `G6sddZ6PfoOxKexYvCJchPDbnJh`
- URL: https://zcnalei7zaql.feishu.cn/docx/G6sddZ6PfoOxKexYvCJchPDbnJh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260508 codex连接stripe，分析网站收入 ｜ Web.Cafe
- 正文字符: 1154
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者吴勰用 Codex 做日常收入分析：接上只读数据和 Stripe 后，每天早上出一份 CEO 日报，并监控异常支付和订阅结构。称实践一周后省了不少时间。

## 方法 / 阈值
1) 把套餐档位告知 Codex，连接网站数据库，只给只读权限（作者用 Supabase 建只读角色，并做了按表查询的 skill）。2) 在 Stripe 建只读 token 给 Codex，以便和数据库互查。3) 按需求监控，例如是否有人用不同信用卡多次支付（疑似盗刷，作者会手动封号），以及新购和续订谁更多（新购多为健康，续费偏多则要找新流量）。4) 把以上做成 skill 定时跑。后来还接到谷歌文档做成表格，并接到邮箱：用户要取消或退款时，让 Codex 查使用记录再起草回复。

## 案例
配了一张 2026-05-02、时区 Asia/Shanghai、数据来自 Stripe 的日报图，图注有成功/失败/退款和按 invoice billing_reason 的拆分，具体数字以原图为准。

## 风险 / 冲突 / 实操注意
即使是只读，把数据库和 Stripe 令牌交给助手也有泄露与误用风险，范围要尽可能小。自动查使用记录写退款邮件涉及用户隐私，发出前应人工审。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 证据位置
四步做法、日报图和后续表格/邮件扩展。


---

## 源文件：01_KNOWLEDGE/summaries/SEp2dmvikoXaRMxOZbmc5EzunEJ.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260429 Cloudflare 开源一套代码，搞定多域名邮件统一收发 ｜ Web.Cafe

- 文档ID: `SEp2dmvikoXaRMxOZbmc5EzunEJ`
- URL: https://zcnalei7zaql.feishu.cn/docx/SEp2dmvikoXaRMxOZbmc5EzunEJ
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260429 Cloudflare 开源一套代码，搞定多域名邮件统一收发 ｜ Web.Cafe
- 正文字符: 1964
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:42:27 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者禾火介绍 Cloudflare 开源项目 agentic-inbox（仓库 cloudflare/agentic-inbox）：一个程序、一个账号管理多个域名邮箱，客户写到哪个地址，就从哪个地址回，避免用个人 Gmail 回信损害信任。

## 方法 / 阈值
项目自称完整邮件客户端，经 Email Routing 收发，带编辑器、线程、搜索和附件；每个邮箱用独立 Durable Object 和 SQLite，附件放 R2；侧边栏有 AI agent 和多个邮件工具，可自动起草但发送前需确认。作者解释此前 Email Routing 只能收不能发，此次升级为 Email Service（文中称 Agents Week 期间公测），添加域名时 SPF、DKIM、DMARC 自动配置。部署跟 README；坑是：若没开过 Cloudflare Access 要先开通（文称 0 元套餐即可），否则会卡在 Access；多域名在环境变量里用逗号分隔，不必每个域名单独部署；不要直接从公共仓库部署（作者称当时公共仓部署可能有问题），应先克隆再推到自己的私有仓库再部署。还提到内置 MCP，可让 Claude Code 等起草后确认发送；开源可自己加未读计数、Discord/飞书通知、按客户域打标签、非工作时间自动回执等。

## 案例
费用转述：发信需要 Workers 的 5 美元/月套餐，该套餐下每天 1000 封免费、各产品共用，作者折合每月约 3 万封；超出按量计费；Email Routing 收信仍免费。已订 Workers Paid 则边际成本被说成基本为零。这些是文章当时的说法，要以官方报价和限额为准。

## 风险 / 冲突 / 实操注意
公测功能和限额会变。把收件箱接给外部 agent 仍有误发和隐私问题，应保持人工确认发送。从公共仓部署的限制是否还在，需看当时 Cloudflare 文档。本篇是产品介绍加部署提醒，不是逐步截图教程。

## 证据位置
问题场景、特性列表、费用、MCP/开源加分和三个部署坑。


---

## 源文件：01_KNOWLEDGE/summaries/EQVbd334noTuWdxUViHcYZlRnEe.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260802 用 mihomo 实现「每个请求/每个站点换出口 IP」的技术方案 | Web.Cafe

- 文档ID: `EQVbd334noTuWdxUViHcYZlRnEe`
- URL: https://zcnalei7zaql.feishu.cn/docx/EQVbd334noTuWdxUViHcYZlRnEe
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260802 用 mihomo 实现「每个请求/每个站点换出口 IP」的技术方案 | Web.Cafe
- 正文字符: 4246
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:47 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者王焱称应群友询问，让 Kimi 整理了自己的自用方案。开篇写明用途是浏览器自动化、批量投放、采集等需要按站点轮换出口 IP，并说文档自包含、可直接交给 AI 照做。核心事实是：mihomo（Clash.Meta 内核）带本地控制 API，可以在不重启的情况下改代理组里当前选中的节点，从而改变出口 IP。这是一篇操作向技术文，不是官方文档。

## 方法 / 阈值
作者的架构是：本机脚本或浏览器走本地混合代理端口，流量进入一个 select 类型的代理组，组内节点来自多节点订阅；再用控制端口的 API 查看当前节点、切换节点，并用第三方查 IP 服务确认出口是否真的变了。文中还写了按目标列表逐个切换、跳过不通节点、接到 Playwright 一类浏览器自动化，以及切换是全局的、节点会失效、不要用错健康检查接口、数据中心 IP 仍可能被信誉库拒绝、打码服务与浏览器出口不一致会导致验证失效、订阅会过期、调试时不要让系统代理把控制面请求带走等踩坑。完整配置、接口调用和脚本都写在原文里。

## 案例
作者称实测某份约 71 个节点的订阅里，有约 10 个 SSL 不通。其余没有给出业务站点名。

## 风险 / 冲突 / 实操注意
轮换出口 IP 去采集、批量操作或绕过 IP 信誉、并与打码服务联用，很容易违反目标网站和代理服务的条款，也可能用于规避检测。本库实践不执行、不复现这些步骤，摘要只保留主张和风险，不抄可运行的配置、接口和脚本。购买「机场」订阅、把控制接口暴露在未设令牌的本机端口，也有安全和合规问题。不能把这套当成正当的 SEO 或上站步骤。

## 证据位置
开篇用途说明、架构与前提、API 与脚本段落，以及第 6、7 节踩坑和自检。可运行细节见原文，此处不转写。


---

## 源文件：01_KNOWLEDGE/summaries/Jv7NdmwdxopjIwxM6ARcqjIwnAb.md

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


---

## 源文件：01_KNOWLEDGE/summaries/U72ZdqEf5oeuSPxvwHpc0W5Snkd.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260629 Ahrefs 认证考试流程 | Web.Cafe

- 文档ID: `U72ZdqEf5oeuSPxvwHpc0W5Snkd`
- URL: https://zcnalei7zaql.feishu.cn/docx/U72ZdqEf5oeuSPxvwHpc0W5Snkd
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260629 Ahrefs 认证考试流程 | Web.Cafe
- 正文字符: 2943
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者 Summerized 介绍可以免费考 Ahrefs Certification，并在复习后用很长的文学化文字整理了自己记住的产品知识点。证书图上的姓名是 CYCLONIX，发证 2026-06-29，有效至 2027-06-29。作者认为这套材料适合当 Ahrefs 初学笔记，不是官方教材原文。

## 方法 / 阈值
考试图注：还有 3 次机会，15 天后重置；姓名拼写在出证后不能改。正文规则：67 题，至少 51 题（75%）通过，60 分钟，必须一次考完不能保存进度，计时期间可以改答案。后半是复习摘要，覆盖爬虫按链接流行度抓取、不统计 iframe/PDF/页内重复链接、号称超大反链库并较频繁更新、DR 看域名反链配置整体强度、UR 看页面、nofollow 不传递权重、同一域名后续链接不再加分、链接域名流量与评分无关、搜索量可看单月或 12 个月均值、KD 只看前十页面的引用域名而不看搜索量和点击率、流量潜力是页面所有排名词的流量之和、内容差距（自己没有而最多十个对手有的词）、链接交集、站点诊断健康分、页面资源与内容衰退、排名追踪器和笔记、内容浏览器与网络浏览器的库规模及 -site: / intitle: / inurl:、未链接品牌提及、各种提醒、仪表盘来源与约 12 小时刷新、连接 GSC 可存超过 16 个月历史、品牌雷达看 ChatGPT/Perplexity 等提及，以及文中提到的 AI 内容助手评分。

## 案例
证书认证内容为 Certified in Ahrefs' Marketing Platform。文中「超过三十五万亿条链接、每十五到三十分钟刷新」等是作者转述的产品宣传量级，未在本篇给出官方出处页。

## 风险 / 冲突 / 实操注意
诗意改写可能把规则写得比官方更绝对，参数和题量会变，应以考试页和帮助中心为准。AI 助手把文章从 60 分改到 90 分是产品叙述，不能当成内容质量保证。考证本身不是做站的必要步骤。

## 证据位置
考试规则、复习长文和证书图。


---

## 源文件：01_KNOWLEDGE/summaries/VlLtdSgCQoFkqZxOw9hchxTrnQg.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260607 一次对话无痛把项目迁移到cloudflare，不花token | Web.Cafe

- 文档ID: `VlLtdSgCQoFkqZxOw9hchxTrnQg`
- URL: https://zcnalei7zaql.feishu.cn/docx/VlLtdSgCQoFkqZxOw9hchxTrnQg
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260607 一次对话无痛把项目迁移到cloudflare，不花token | Web.Cafe
- 正文字符: 680
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者 Simon 把原来基于 mksaas、部署在 VPS 上不稳定的项目，迁到 Cloudflare 加 D1。标题「不花 token」指用 ChatGPT 网页版 Pro 的进阶思考，而不消耗 Codex 额度。

## 方法 / 阈值
把现有项目打包成 zip，再上传对应模板的 Cloudflare/D1 版 zip（mksaas 或 shipany），向 ChatGPT 说明：把 myproject.zip 全部搬进模板的 CF 版，保留原有页面和功能，使用 CF 部署和 D1，安装 pnpm 依赖，反复跑 dev、类型检查和构建直到通过，并「在各个方面改进」。作者称可能跑几个小时，最后得到代码压缩包，需自己按 CF 流程部署，并删掉残留测试脚本后自行测试。

## 案例
无公开仓库或迁移前后对照，只是个人经验。

## 风险 / 冲突 / 实操注意
要把完整项目上传到对话里，注意密钥和私钥不要打进压缩包。「各方面改进」不可控，不能默认输出可直接上线。部署和 D1 绑定仍要自己查官方文档。这是针对特定模板的一次迁移，不是通用教程。

## 证据位置
迁移动机、提示词和收尾说明。


---

## 源文件：01_KNOWLEDGE/summaries/CyQmdCUSuoiTzfxZ2xKc3AVBnrg.md

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


---

## 源文件：01_KNOWLEDGE/summaries/KrQldb6UMoYuJLx9dkScEuDmnDe.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20251104 Semrush、Similarweb、Ahrefs 到底怎么选择？ | Web.Cafe

- 文档ID: `KrQldb6UMoYuJLx9dkScEuDmnDe`
- URL: https://zcnalei7zaql.feishu.cn/docx/KrQldb6UMoYuJLx9dkScEuDmnDe
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20251104 Semrush、Similarweb、Ahrefs 到底怎么选择？ | Web.Cafe
- 正文字符: 490
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞 2025-11-04 谈三个工具怎么买。建议初学者看关键词和网页先只买 Semrush，称最便宜；做了几个站赚到一些钱再买 Similarweb；赚到更多再买 Ahrefs。若只看自己网站的数据，用 Ahrefs 免费版、验证网站所有权即可，并推荐群友都去用一用免费版。

## 方法 / 阈值
购买顺序按阶段加工具，而不是一上来三件套。

## 案例
文中价格：Semrush「一个月十几块钱」；Similarweb「一个月 70 块、一年 840」。作者写明前两个在淘宝能找到共享账号，上面的价格就是共享账号价。Ahrefs 因风控严，一般直接买正版，Lite 29 美元/月，入门 249 美元/月，认为完全不适合新手。

## 风险 / 冲突 / 实操注意
共享账号违反工具服务条款，有封号和安全风险，不能作为练习或采购建议。官方订阅价格会变，文中数字只反映作者当时所说的共享价或约数。免费版能看的范围以 Ahrefs 当时规则为准。

## 证据位置
三段购买建议与免费版说明。


---

## 源文件：01_KNOWLEDGE/summaries/UUDRdcjcWox5lTxjKUPcz1Bsn14.md

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


---

## 源文件：01_KNOWLEDGE/summaries/DEQodNKv9o789Zx8FMzcnQ1Xn5b.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250928 代码推送到Github,但是Vercel不自动部署的问题. | Web.Cafe

- 文档ID: `DEQodNKv9o789Zx8FMzcnQ1Xn5b`
- URL: https://zcnalei7zaql.feishu.cn/docx/DEQodNKv9o789Zx8FMzcnQ1Xn5b
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250928 代码推送到Github,但是Vercel不自动部署的问题. | Web.Cafe
- 正文字符: 1632
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者 Hx.org 记录一次「代码已推到 GitHub，但 Vercel 没有自动部署」。结论是大概率代码有问题，他自己是 vercel.json 配错，修好后自动部署恢复。

## 方法 / 阈值
检查顺序：打开对应应用的 Deployments 页；用右上角菜单手动 Create Deployment；选好分支。若这里看不到正常的 git 提交，可能是没有正确推到 GitHub，先查网络或推送；若提交记录正常，手动部署会给出失败原因，把报错交给 Claude Code 或 Cursor 处理。作者因赶时间直接修了，没有留下失败原因的截图。

## 案例
截图里出现 main Production 和提交 52702ce 等界面元素，没有写出 vercel.json 的具体错误内容。

## 风险 / 冲突 / 实操注意
这是一条排障思路，不是完整的 Vercel 配置教程。自动部署失败还有 Webhook、权限、忽略设置等原因，不能只归因于 vercel.json。界面会随产品改版。

## 证据位置
开篇结论和手动部署检查步骤。


---

## 源文件：01_KNOWLEDGE/summaries/D5D7d5KR4oGdoyx1x8Gc4G8RnOh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250930 similarweb 关键词列表数据如何免费导出并让AI分析做SEO优化？ | Web.Cafe

- 文档ID: `D5D7d5KR4oGdoyx1x8Gc4G8RnOh`
- URL: https://zcnalei7zaql.feishu.cn/docx/D5D7d5KR4oGdoyx1x8Gc4G8RnOh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250930 similarweb 关键词列表数据如何免费导出并让AI分析做SEO优化？ | Web.Cafe
- 正文字符: 909
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:41:58 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者银河星游嫌 Similarweb 官方导出要积分，改用 Chrome 插件 Table Extractor 从页面表格导出 JSON、Markdown 或 CSV，再交给 Claude Code，配合一套开源 Agents 做竞品词分析。

## 方法 / 阈值
插件商店地址在文中给出。Agents 安装是让 Claude Code 按小排一篇文章的说法，去安装 https://github.com/wshobson/agents 并跳过重复项。分析时把导出文件 @ 进对话，先让它给出调用方案和需要决策的点，确认后再优化。作者说油猴和 XPath 都不好用，要不断适配 Similarweb，也不能一键导出。

## 案例
无分析前后的效果数据。

## 风险 / 冲突 / 实操注意
用第三方插件绕过付费导出，可能违反 Similarweb 条款，不能写成推荐做法。把竞品数据交给本地或云端助手时也要注意账号与数据范围。开源 Agents 和插件都要自行判断权限与安全。

## 证据位置
导出、安装 Agents、分析三步和文末踩坑。


---

## 源文件：01_KNOWLEDGE/summaries/WW2vdpinnoST4kxEAZFcGrK6nUc.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260201 使用 Coolify 部署 Next.js 项目

- 文档ID: `WW2vdpinnoST4kxEAZFcGrK6nUc`
- URL: https://zcnalei7zaql.feishu.cn/docx/WW2vdpinnoST4kxEAZFcGrK6nUc
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260201 使用 Coolify 部署 Next.js 项目
- 正文字符: 11548
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:57:20 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2026-02-01 写的 Nexty 模板文档，介绍用自托管 Coolify 在 VPS 上部署 Next.js。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]作者明确：Coolify 对 VPS 性能要求比 Dokploy 高，配置较低时应改用 Dokploy 并看对应文档。这是模板部署说明，本阶段只读，不实际购买服务器或上线。原文配图和命令里出现过管理域名、服务器地址和 Redis 端口等，摘要不转抄。

## 方法 / 阈值
部署前建议在 next.config 里设置 output: standalone，以便减小 Docker 镜像。Coolify 被介绍为开源自托管 PaaS，可替代部分云部署平台。先自购 VPS，按控制台完成初始化。作者提醒某服务商默认没有防火墙、端口全开有风险，需自行添加规则，开放 22、80、443，以及安装阶段用的 8000；管理后台改用自定义域名并确认可访问后，应关掉 8000，只走域名。安装可用官方命令，或在该服务商面板里选带面板的系统并安装 Coolify，然后用服务器 IP 加 8000 端口进入。注册后为后台设置自定义域名，在 DNS（文中以 Cloudflare 为例）添加指向服务器 IP 的 A 记录；解析生效后再绑 Git，通常是创建 GitHub App 并安装到仓库。部署：在项目里添加资源，选通过 GitHub App 的私有仓库，示例为 main 分支、Nixpacks 构建、根目录、端口 3000。再为应用配置域名和 www 与非 www 的跳转，在 DNS 为apex 和 www 各加一条指向服务器 IP 的 A 记录（文中示例开了代理）。SSL/TLS 作者写可选 Full 或 Flexible；Flexible 不是源站全程加密，若源站已有证书，通常更稳妥的是更严格的模式，不能把 Flexible 当成默认安全选项。环境变量可在界面粘贴并保存，示例出现过 Node 版本和站点 URL 等变量名，然后点 Deploy，之后每次提交会自动部署。高级用法：若用 Pino 打日志，可用持久存储把容器内日志目录挂到宿主机，保存后需 Redeploy；正文写的宿主机路径与另一张截图说明不完全一致，挂载前要核对。可在服务器上查看或从本机拷出日志目录。部署 Redis 与加应用类似，资源类型选 Redis；同一台机器上的生产应用可用内部连接。端口映射（如把容器 6379 映到其他宿主机端口）只建议给本地临时调试，用完关闭。若要经公网访问，作者建议开 SSL（连接串常改为 rediss）、代理公开访问，并设不常见的公共端口，同时在防火墙放行相应端口。数据持久化可在自定义配置里打开 AOF，保存并重启后用容器终端登录检查配置项。即使开了加密和冷门端口，把 Redis 暴露到公网仍有风险。

## 案例
界面示例使用了 nexty 相关的后台域名和应用域名，以及 Nixpacks 的环境变量名，只作操作示意。一篇 Redis 配置图注明实例状态为已退出，说明截图不一定是正在运行的生产状态。

## 风险 / 冲突 / 实操注意
默认开放全部端口、用 IP 加 8000 访问管理后台、把 Redis 映射到公网，都是安全隐患，实践中不能照抄。文档中的具体主机和端口不要复用。SSL 选 Flexible、日志挂载路径前后不一致，都需要单独核对。推广价和配置会过时。本阶段不执行安装、解析或部署。

## 证据位置
standalone 前置、防火墙与关闭 8000、域名和 GitHub App、Nixpacks 部署与环境变量，以及日志挂载和 Redis 的配置说明。


---

## 源文件：01_KNOWLEDGE/summaries/BL9td0k1KogvvoxciYZcBMqZnPd.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260201 一行命令就能自动同步环境变量到 GitHub Actions，告别手动配置的烦恼 | Web.Cafe

- 文档ID: `BL9td0k1KogvvoxciYZcBMqZnPd`
- URL: https://zcnalei7zaql.feishu.cn/docx/BL9td0k1KogvvoxciYZcBMqZnPd
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20260201 一行命令就能自动同步环境变量到 GitHub Actions，告别手动配置的烦恼 | Web.Cafe
- 正文字符: 18467
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 01:03:33 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2026-02-01 的 Nexty 专栏文，针对自建时用 GitHub Actions 构建镜像、却要在仓库里逐个填写几十个环境变量、易花十几分钟还可能抄错的问题。文首同样有模板折扣与联系方式，购买不是学习前提。配套脚本全文贴在文末，本摘要只记行为，不复述可运行源码，本阶段也不安装 CLI、不登录、不执行脚本。它与刚读的 Dokploy 篇直接衔接：那边要求把公共变量放 Variables、其余放 Secrets，并提到手动配置费时。

## 方法 / 阈值
思路是用已登录的 GitHub CLI，读本地环境文件，按变量名是否以 NEXT_PUBLIC_ 开头自动分流，并发写入目标仓库（默认检测当前仓库，也可手动指定），作者称几十个变量大约数秒到十几秒。需要先安装 CLI 并完成网页登录，且对目标仓库要有管理员权限才能管理密钥和变量；可用仓库设置里是否出现新建密钥按钮来自查。建议在 package 脚本里加同步和清理两条快捷命令。文中把清理写成可先做的可选步骤，容易让人以为会清空仓库里全部变量；实际清理脚本只删除本地环境文件里出现过的同名项，并先列出将删除的键名，默认要确认，可用跳过确认的开关。它不会清理文件里已删除、但仍留在 GitHub 上的旧键，也不能替代对仓库权限和目标仓库名的核对。同步脚本会跳过空值，把公共前缀写入 Variables、其余写入 Secrets，最后统计成功、跳过和失败。解析会去掉注释、首尾空白和成对引号。公开变量在 Actions 日志里通常不会被遮盖，公开仓库更要确认这些值本来就可以出现在前端打包里。分类规则只看前缀，命名不当仍可能把不该公开的值送进 Variables。把变量值拼进命令行去设置 Variable 时，特殊字符存在注入或不完整转义的风险；设置 Secret 走标准输入，相对更稳。命令行参数对路径和仓库名的启发式解析也可能误判。清理带跳过确认时破坏性更强，执行前必须确认仓库和文件都是对的。

## 案例
示例输出提到一次处理四十余项、约十几秒内分别写入十几个变量和二十多个密钥，并跳过若干空值。这是演示数量，不是固定规模。

## 风险 / 冲突 / 实操注意
脚本会把本地密钥送到 GitHub，权限过大或仓库选错会造成泄露或误删。不把环境文件提交进仓库。公开变量不等于可以随意公开所有键。本阶段不运行这些命令。

## 证据位置
文首问题陈述、安装与权限前提、两条脚本的分流规则与清理范围，以及输出统计方式。


---

## 源文件：01_KNOWLEDGE/summaries/SlNMdd40wowEqCxcuolcH6LBnef.md

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


---

## 源文件：01_KNOWLEDGE/summaries/CoqrdFlM2ouGZqxmoZxclrD7nyh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20251024 出海技术栈教程（九）：使用 Dokploy 部署 Next.js 项目

- 文档ID: `CoqrdFlM2ouGZqxmoZxclrD7nyh`
- URL: https://zcnalei7zaql.feishu.cn/docx/CoqrdFlM2ouGZqxmoZxclrD7nyh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20251024 出海技术栈教程（九）：使用 Dokploy 部署 Next.js 项目
- 正文字符: 22118
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 01:03:06 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普 2025-10-24 的 Nexty 专栏第 9 篇，介绍用自托管 Dokploy 部署 Next.js，作为利润低、资源占用高、在 Vercel 上不划算时的开源替代。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]与已读的 Coolify 篇对照：作者在 Coolify 文中已写明其对 VPS 要求更高，本文把初期配置写成约 2 核 8G 量级，价格会过时。原文安装命令、配图里的邮箱、令牌、镜像路径和 Webhook 地址，摘要不转抄。本阶段只读，不安装、不购买、不部署。

## 方法 / 阈值
部署前同样建议在 next.config 里打开 standalone，以减小 Docker 镜像。需自购 VPS 并配置防火墙：作者提醒某服务商默认端口全开有风险，示例放行 22、80、443 和 3000。3000 是安装后管理后台端口；Coolify 篇要求自定义域名可用后关掉临时管理端口，本文没有同样写明关闭 3000，若一直对公网开放，管理面风险较高。安装方式是把官网脚本交给 shell 执行，存在供应链风险，实践前应自行审查，不能盲目管道执行。安装后先给后台设自定义域名和证书邮箱，在 DNS 添加指向服务器 IP 的 A 记录，再生效后绑 Git。方案一是在面板里选仓库直接构建，作者明确：弱机器上容易因资源不足崩溃或重启，只适合很小的项目，不是推荐做法。步骤包括建项目和服务、选 GitHub 仓库和分支、填环境变量后 Deploy、再为应用加域名。DNS 示例写了 apex 用 A 记录、www 用 CNAME 且目标填服务器 IP——CNAME 的目标应是域名而不是 IP，Coolify 篇则是 apex 与 www 都用 A 记录，这里的 CNAME 写法是错误的，不能照抄。SSL/TLS 仍写可选 Full 或 Flexible，Flexible 不是源站全程加密，通常更稳妥的是更严格的模式。还可在高级设置里把 www 重定向到非 www。方案二（推荐）是用 GitHub Actions 在云端构建镜像，Dokploy 只负责拉取启动，以减轻 VPS 压力。前置只需一次：创建 GitHub 个人访问令牌（配图出现过不过期选项，官方更建议设过期时间），权限面向容器镜像的读写，把令牌当作 Dokploy Registry 的密码，仓库地址用 GitHub 的容器注册表。服务改为 Docker 提供者，镜像名按 ghcr.io/用户/仓库:分支 的形式填写，并把部署用的 Webhook 地址放到工作流末尾，在构建推送后请求一次以触发更新。工作流在推送 main 或手动触发时运行，用仓库内置令牌登录注册表、构建并推送，构建参数里公共变量走 Variables、其余走 Secrets；模板在构建阶段还用到对象存储公网地址和数据库连接串。Dockerfile 分依赖、构建、运行三阶段，构建阶段把 NEXT_PUBLIC 变量以及上述两个构建期变量写入，运行阶段改用非 root 用户启动 standalone，运行时密钥由 Dokploy 注入。另加了较简短的 .dockerignore。作者声称这样可避免重要密钥泄漏，但把数据库连接串作为构建参数和构建期环境变量，仍可能进入构建日志或镜像层，.dockerignore 也未排除 .env，不能当成已经安全。运行期变量还要在 Dokploy 的 Environment 里配置；文中为了方便说可以把全部变量再贴一份进去，操作时仍须避免把密钥写进仓库或对话。无代码变更时，可在 Actions 里手动跑工作流。什么时候用：作者建议只有 Vercel 性价比很低时才考虑，并举例不重要、不赚钱或利润低、页面很多的导航或文档站；他自己用来跑分析工具、文档、导航、轻量和定时任务。把「不重要就无需考虑安全风险」当成选型理由是不妥当的，自托管更要管好端口、令牌和密钥。

## 案例
界面以 Nexty 相关项目名为示例。作者列出了自己用 Dokploy 部署的几类站点，包括文档和导航，只作他的使用范围说明，不是必须采用的架构。

## 风险 / 冲突 / 实操注意
脚本管道安装、管理端口长期开放、错误的 CNAME、较弱的 SSL 模式、不过期的个人令牌、构建期数据库地址，以及未受保护的部署 Webhook，都是安全隐患。价格和面板界面会变。本阶段不执行。

## 证据位置
standalone 与防火墙、两种部署方案、Actions 与 Dockerfile 的环境变量约定，以及文末的适用场景说明。


---

## 源文件：01_KNOWLEDGE/summaries/EQTddO29koifZXxiZXrcXKTTngh.md

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


---

## 源文件：01_KNOWLEDGE/summaries/Kovvdk0fhoDw3SxajuAcyyMdnlg.md

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


---

## 源文件：01_KNOWLEDGE/summaries/MuaGdKX9rokfPtxoBQMcoaRWnNh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（一）：域名解析与配置 | Web.Cafe

- 文档ID: `MuaGdKX9rokfPtxoBQMcoaRWnNh`
- URL: https://zcnalei7zaql.feishu.cn/docx/MuaGdKX9rokfPtxoBQMcoaRWnNh
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（一）：域名解析与配置 | Web.Cafe
- 正文字符: 4096
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:44:17 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
程普为 Nexty.dev 模板整理的专栏第一篇，经哥飞邀请把通用配置发到社群。作者称即使不用 Nexty 也用得上。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]本篇实际只讲到买域名、把 NS 改到 Cloudflare 并等到 Active，没有写如何添加站点的 A/CNAME，也没有接到 Vercel 或其他主机。

## 方法 / 阈值
推荐注册商：Namesilo（价格适中、免费隐藏 WHOIS）、Porkbun（便宜、免费隐藏 WHOIS）、Cloudflare（便宜、免费隐藏 WHOIS，且方便和其他 CF 功能一起用）、Namecheap（只写了便宜，未提 WHOIS）。比价和查询可注册用 tld-list.com、query.domains。解析建议放在 Cloudflare：全球 DNS、免费套餐可配自动 SSL。步骤：登录 Cloudflare 添加域名（示例 nexty.dev，推荐 Quick scan），选 Free 计划，按提示到注册商改 nameserver；作者以 Namesilo 为例，把 NS 改成 Cloudflare 提供的主机（截图为 adi.ns.cloudflare.com 与 quinton.ns.cloudflare.com，这是该域名当时分到的 NS，不能当成所有人通用的地址）。改完后在 Cloudflare DNS 页看到 Active 即添加成功。页面提示还要为 www 和根域添加 A/AAAA/CNAME，以及根域 MX，正文没有继续演示这些记录。

## 案例
全程以 nexty.dev / Namesilo 为示例。套餐图注还列出 Pro 约 20 美元/月、Business 约 200 美元/月，以当时官网为准。

## 风险 / 冲突 / 实操注意
改 NS 前应备份原 DNS，生效需要时间。Cloudflare 免费套餐功能会变。隐藏 WHOIS 是否免费取决于注册商政策。本篇不能单独当成「站点已经解析到应用」的完整教程。系列目录不能代替已读其他篇。

## 证据位置
专栏前言、注册商表、添加域名到 Active 的步骤和截图。


---

## 源文件：01_KNOWLEDGE/summaries/Spekduby7oR28nxiEhVc7N4onBg.md

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


---

## 源文件：01_KNOWLEDGE/summaries/CWo8dIZImoq3woxaQaGcAybdnob.md

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


---

## 源文件：01_KNOWLEDGE/summaries/EWHqd6InRoNdTVx0cdicIN1HnTc.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20250814 出海技术栈集成教程（六）：Upstash 集成 Redis 与请求限流器 | Web.Cafe

- 文档ID: `EWHqd6InRoNdTVx0cdicIN1HnTc`
- URL: https://zcnalei7zaql.feishu.cn/docx/EWHqd6InRoNdTVx0cdicIN1HnTc
- 路径: 出海seo资源分享V1.0/出海技术栈教程/20250814 出海技术栈集成教程（六）：Upstash 集成 Redis 与请求限流器 | Web.Cafe
- 正文字符: 2434
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:43:00 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者程普把 Nexty.dev 模板的通用配置写成专栏，本篇是第（六）篇，讲 Upstash Redis。开头自我介绍和八篇目录在本系列各篇都会出现，不能把目录当成已经读完其它篇。标题写了「Redis 与请求限流器」，但本篇抓取到的正文只覆盖注册、建库和复制 REST 凭证，没有限流器代码或模板里的用法。

## 方法 / 阈值
简述 Upstash 是无服务器数据服务，商业项目里常用 Redis 做缓存和限流。步骤：到 Dashboard 点 Create database，填名称（示例 my-nexty-dev）和主区域（示例美西 us-west-1），可选读区域，Eviction 在截图里是关的；选套餐后进入详情，在 REST API 模块把 UPSTASH_REDIS_REST_URL 和 UPSTASH_REDIS_REST_TOKEN 拷进环境变量。正文「1.」后面是空的，注册入口链接没有写出来。

## 案例
免费套餐图注：Hobby 永久免费，最大 256MB、每月带宽 10GB，另有按量和固定规格付费档，付费需绑定支付方式。数字以 Upstash 当时套餐为准。

## 风险 / 冲突 / 实操注意
REST Token 等同密钥，不要提交到仓库或发到聊天里。免费额度和控制台界面会变。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]限流实现要到模板代码或官方文档里另查，不能认为本篇已经教完。

## 证据位置
专栏引言、建库截图、套餐说明和复制 REST 变量；正文在此结束。


---

## 源文件：01_KNOWLEDGE/summaries/EK2XdrYAVoALd9xPooIcI6WOnwh.md

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


---

## 源文件：01_KNOWLEDGE/summaries/GH5edCpKjoU8R7xzbcIcq7Ojnid.md

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


---

## 源文件：01_KNOWLEDGE/summaries/EyGudtiJmoJwDaxi8AjcszVRnnb.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260423 新手Adsense网站过审求助和Adsterra避雷 ｜ Web.Cafe

- 文档ID: `EyGudtiJmoJwDaxi8AjcszVRnnb`
- URL: https://zcnalei7zaql.feishu.cn/docx/EyGudtiJmoJwDaxi8AjcszVRnnb
- 路径: 出海seo资源分享V1.0/adsense/20260423 新手Adsense网站过审求助和Adsterra避雷 ｜ Web.Cafe
- 正文字符: 1409
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:46:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者催萌芽的求助帖，不是教程。香港个人 AdSense 账户收款已过审，但网站多次过不了，包括他所说月访几十万、运营两三年的正规老站，提示政策违规。新站运营约 5 个月，GSC 最高日点击三万多。截图显示申请次数已达上限，要等到 2026-04-29 才能再试，所有权已验证。他问：账户是否被标记、要不要注销重开；同一网站换新账号审核会不会关联；改了很多次仍显示违规；近期过审是否变难。本篇没有收录他人的解答。

## 方法 / 阈值
无方法，只描述自己的经历和问题。

## 案例
无奈于 3 月初改用有人推荐的 Adsterra，只开 SocialBar，并请客服过滤色情等广告，仍觉得伤体验。作者称排名一夜掉到 50 名之后，GSC 几乎只剩品牌词。收益表图注：2026-03-03 至 09 日曝光约 10.37 万、点击约 3.39 万、CTR 约 31.5%、CPM 约 0.665 美元、收入约 62.74 美元；单日如 3 月 9 日 CTR 约 25%。作者认为主要是美国流量，但 CPM 低得像「第三世界」，非常不值得。

## 风险 / 冲突 / 实操注意
这是单一样本求助，不能推广为「AdSense 普遍过不了」或「Adsterra 一定惩罚」。SocialBar 点击率异常高，可能含误点，对体验和质量评估都不利。用新 AdSense 账号跑同一网站以绕过拒审，有账户关联和政策风险，不作为建议。遇到违规提示应以官方政策说明和账户通知为准。

## 证据位置
四个问题和审核截图，以及 Adsterra 流量下跌与收益表。


---

## 源文件：01_KNOWLEDGE/summaries/H1dodeQPqoLOwWxbjyMc1qAvneg.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260616 adsense 审计 skill | Web.Cafe

- 文档ID: `H1dodeQPqoLOwWxbjyMc1qAvneg`
- URL: https://zcnalei7zaql.feishu.cn/docx/H1dodeQPqoLOwWxbjyMc1qAvneg
- 路径: 出海seo资源分享V1.0/adsense/20260616 adsense 审计 skill | Web.Cafe
- 正文字符: 2884
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:47:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者阿飞 2026-06-16 说早上在群里看到讨论，就做了一个给 Codex/Claude 用的 AdSense 站点审计 skill。本篇飞书正文几乎只有调用提示词，没有附上 skill 本身，也没有列出所谓 ADS-* 要求的完整清单或官方政策原文。群聊截图里有人说按流程改了几十轮、配合 skill 优化后当天过审，此前两次被拒。

## 方法 / 阈值
作者的经验表述是：把 AdSense 官方文档发给模型反复修改、相互审核，内容页面要做深，一般两三次提交会过；不通过就再增加内容深度和更多页面。提示词原则：必须给目标 URL 或本地仓库路径；说明是申请前、拒审后还是修复后复查；要完整清单不要只给摘要；每条 ADS-* 标 Pass / Fail / Unknown / N/A；Fail 和 Unknown 要有证据和修改建议。文中提供了若干调用模板：全站审计、只基于线上页面、仓库加线上、拒审诊断、修复后复审、改成任务清单，以及一条最短提示。

## 案例
除群里「今日通过」的转述外，没有可核对的站点案例。同文件夹《Adsense审核4连过的思考》里，江帅称试过圈友的 Codex 技能但游戏站难以按清单改完，未采用仍过审，说明这类技能不是充分或必要条件。

## 风险 / 冲突 / 实操注意
模型对照官方文档的输出不能代替 AdSense 审核。本篇缺 skill 文件时，所谓 ADS-* 编号无法核验，不能当作官方条款。靠「加内容和加页面」凑过审，有堆薄内容的风险。不能把两三次通过的说法当成成功率。

## 证据位置
群聊截图、用法原则和七类提示词模板。


---

## 源文件：01_KNOWLEDGE/summaries/O1w5dBYnEoHrtgxuCjec2FLxnHg.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20251029 谷歌客户经理关于Adsense的问答 | Web.Cafe

- 文档ID: `O1w5dBYnEoHrtgxuCjec2FLxnHg`
- URL: https://zcnalei7zaql.feishu.cn/docx/O1w5dBYnEoHrtgxuCjec2FLxnHg
- 路径: 出海seo资源分享V1.0/adsense/20251029 谷歌客户经理关于Adsense的问答 | Web.Cafe
- 正文字符: 5745
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:48:38 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
飞书页眉日期是 2025-10-29、作者哥飞，但正文主线是年末审核倒计时、12 月活动和 2024-12-12 的推文，时间线对不上，更像是旧分享被重新入库。主体是他与台湾 AdSense 新客经理 Nika 约 1 小时通话后的转述。他明确写了：这些文字不是对话原文，是按自己的理解重写的。因此不能当成谷歌官方政策原文，也不能当成可公开引用的政策解释。文末他要求不要外传、不要写成对外文章，理由是把 AdSense 政策落成文字可能违反谷歌政策；本摘要只作资料库内部对照，不把它写成操作规程。

## 方法 / 阈值
先交代自己的账号因误填公司收款信息被要求限期核查，年末放假导致审核卡住，系统倒计时要中止服务；后来经朋友转到 Nika，用表单 ID 加急工单后通过。问答要点（皆为转述）：1) 个人账号与企业账号不能互改，要用公司信息收款需新开账号，并避免被系统判成同一人操作多账号。2) 两类账号本质差别主要在收款信息；用 PIN 信验证时个人地址或公司地址都可以；[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]3) 同一网站出现在新旧两个发布商账号下，他称在栏目代理等场景可以，只要不要极端到一个站挂十几个发布商广告；也可把部分网站迁到新的企业账号。4) 同时又写，理论上一个身份只允许一个 AdSense 账号，要注意登录环境和网络，不要在同一浏览器同时登录多个账号，否则可能被提示一人多号。这两条并放，本身有张力。5) 新账号遇突然大流量可能被限制投放，前几天较常见；若新账号、新站、流量又高又不稳定，限制两周或更久也有可能，由算法判断。6) 不被限制的是优质老账号；质量差的老账号同样会被限甚至封。优质老账号给名下新站一个初始信任信号，之后仍会持续评分。7) 解决新号限制，转述是靠长期用高质量流量证明价值；文中还提到可以把新账号报到该经理处以降低限制、恢复填充，并说先拿他将要注册的企业账号试。这是个人协助，不是普通用户可走的官方流程，不作为实践步骤。8) 新账号初期单价往往较低，要用高质量流量逐渐证明。9) 做未被很好满足的搜索需求、把网站做好并长期经营，是他转述中谷歌愿意看到的；不希望新站只为短期变现。10) 对「AdSense 套利」，转述是有人把搜索广告玩坏，已封大量不合规账号，产品侧会更谨慎，更希望广告主、发布商、平台共赢。11) 同一老账号下不同网站单价不同是正常的，取决于人群和流量价值，不是人工定价。12) 审核难易与流量质量、网站质量有关，尤其是新账号的第一个站，人和算法都会看；内容差、几乎没流量或流量质量差更难过。13) H5 游戏站能否开激励广告：要先审站再判断，没有明确允准。

## 案例
加急通过是作者自己的一次信息核查，不是普通过审案例。文前还提醒：群里至少两位朋友收到过类似商标或域名冲突的邮件，他把它当作骗子邮件、可以不理。这类邮件有真有假，既不要随便点不明链接，也不宜一律当作诈骗忽略，需单独辨别。文后另有几条与问答无关的社群碎记：有人做了给搜索结果里近一年新站标颜色的插件；称 Substack Newsletter 里的链接是 dofollow；GSC 的 24 小时数据改按所在时区显示。

## 风险 / 冲突 / 实操注意
转述加内部关系加急，不能当作政策或过审保证。同一站点多账号、账号隔离等说法尤其不能写成「如何开多个互不关联的账号」指南；文中出现的「指纹浏览器」字样没有展开，实践中不采用这类方法。报备到个人客户经理也不能推广。所谓套利被打击，是对短线玩法的警告，不是教如何打擦边。

## 证据位置
通话时长截图、13 个问题的转述、作者自己的免责声明，以及文末与主题无关的几条补充。


---

## 源文件：01_KNOWLEDGE/summaries/S2D7d1d1zokzjyx2A5ucb3J0nu4.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 【哥飞探案】Adsense 广告单价跌了吗？ | Web.Cafe

- 文档ID: `S2D7d1d1zokzjyx2A5ucb3J0nu4`
- URL: https://zcnalei7zaql.feishu.cn/docx/S2D7d1d1zokzjyx2A5ucb3J0nu4
- 路径: 出海seo资源分享V1.0/adsense/20240813 【哥飞探案】Adsense 广告单价跌了吗？ | Web.Cafe
- 正文字符: 2302
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:47:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞回应社群里「AdSense 单价跌了很多」的说法，拿出两位朋友的 AI 工具站截图，并和自己去年那篇分国家收入文里的 AI 图片工具站对比。开头还有一段关于年龄传言的个人说明，与单价判断无关。

## 方法 / 阈值
比较不同站点、不同年份的「网页每千次展示收入」，并提醒要考虑品类差异：广告收入来自广告主预算，声音、视频相关广告主可能更舍得花钱。不能只看国家，也要看做的是哪类 AI 工具。

## 案例
AI 声音站（按每千次展示收入排序）：图注澳大利亚约 12.06 美元（浏览 1503、估算收入约 18.13）、新西兰约 11.83、加拿大约 10.73、美国约 10.37（浏览 8249、收入约 85.51）；正文还写瑞士约 9 美元，新加坡、挪威、丹麦等也在 3 美元以上。AI 视频站（按浏览量排序，图注区间 2024-07-16 至 22 日）：美国约 8.57 美元（浏览 16432、收入约 140.83），泰国、越南、巴西等更低。对比去年 AI 图片站：瑞士约 7.34 美元最高，美国、法国、加拿大约 4 美元出头。作者据此认为，只从发达国家单价看，今年并不比去年低。第二个视频站称 6 月 1 日上线即获得搜索流量，第 3 天申请 AdSense、第 4 天通过；用来反驳「域名要注册满 3 个月才能申请」的口口相传，并称流量够大时谷歌会很快审，流量小时才用规则卡住。他也写这是第一次见到一周内就过审。

## 风险 / 冲突 / 实操注意
三个站品类不同、时间窗口短，截图匿名，不能证明「今年单价普遍更高」或「声音视频一定更赚钱」。一周内过审是单例，既不能当成申请时间表，也不能反过来证明 3 个月规则在别的情况下无效。流量大就一定快过审，同样没有对照样本。

## 证据位置
两张新截图、对去年表格的回顾，以及视频站上线与过审时间的转述。


---

## 源文件：01_KNOWLEDGE/summaries/WJWwdoTljoNt1XxeclDcDReNnFe.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 哥飞解读：Adsense 生态是谷歌的胜利 | Web.Cafe

- 文档ID: `WJWwdoTljoNt1XxeclDcDReNnFe`
- URL: https://zcnalei7zaql.feishu.cn/docx/WJWwdoTljoNt1XxeclDcDReNnFe
- 路径: 出海seo资源分享V1.0/adsense/20240813 哥飞解读：Adsense 生态是谷歌的胜利 | Web.Cafe
- 正文字符: 1370
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:46:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞在文中称当天是谷歌 25 周岁生日，写了一篇关于 AdSense 生态的短评，不是操作教程。谷歌成立于 1998 年 9 月，把 2024-08-13 写成生日可能只是修辞或记错，不必当真。观点是：谷歌要维持搜索，必须解决内容供给；给站长分广告费，才能让人不断建站、更新；搜索广告约 2000 年上线，AdSense 约 2003 年上线后形成多赢：站长做各种需求尤其是少人做的词，靠搜索流量和广告变现，再把蛋糕做大。

## 方法 / 阈值
无操作步骤。文末推广其公众号自 7 月中旬起日更。

## 案例
无具体站点或收入数据。

## 风险 / 冲突 / 实操注意
这是叙事和动机文，历史时间点是粗线条，不能当成经济学证明，也不能推导出现在只要做冷门词就一定能靠广告赚钱。

## 证据位置
从雅虎手工收录到 AdSense 飞轮的几段论述。


---

## 源文件：01_KNOWLEDGE/summaries/QB3OdXt08ouIvXxjEzJcmA6kn8d.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 Adsense账号注册、审核、网站审核的一点经验分享 | Web.Cafe

- 文档ID: `QB3OdXt08ouIvXxjEzJcmA6kn8d`
- URL: https://zcnalei7zaql.feishu.cn/docx/QB3OdXt08ouIvXxjEzJcmA6kn8d
- 路径: 出海seo资源分享V1.0/adsense/20240813 Adsense账号注册、审核、网站审核的一点经验分享 | Web.Cafe
- 正文字符: 7552
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:48:38 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞 2024-08-13 的注册与过审经验文。先说明 AdSense 是网站广告联盟，收入因站而异，离钱近的内容和发达国家流量单价通常更高。一个账号可以添加多个网站，不必为每个站新开账号。界面和门槛以当时后台为准，现在可能已改。

## 方法 / 阈值
需先有 Google 账号。作者不建议新注册的 Gmail 立刻去开 AdSense，可先正常使用半个月到一个月。入口为 adsense.com 或 google.com/adsense。还没有网站时不建议先注册。流量较小的站，他提到还可能要求域名注册超过约 3 个月、并有一定内容；没有站的人可先用 WordPress 写原创博客，一天一到两篇，坚持半个月到一个月再申请。填写顶级域名，不要加协议和路径，不要勾选「目前还没有网站」；国家地区填真实所在地（人在中国就选中国），因为后续要验证地址才能收款。个人信息选个人、按真实中文填写。审核期先放广告代码，设置保持默认即可，审核期间通常不会真正展示广告。关联网站时，作者根据自己的经验认为广告代码和网站根目录 ads.txt 都要做，不是二选一，然后再点已放置代码并申请审核。首次审核往往较长：先由爬虫检查代码和 ads.txt，再观察流量、抓取内容，然后才可能进入人工；流量和内容都很少时，很大概率被要求补内容或等流量。已有账号添加新站：在管理站点里新建网站，同样放代码和 ads.txt。付款方面，文称至少满 100 美元才会付款；在此之前要填真实地址、收美国寄来的 PIN 平信并在后台输入。信可能丢失，可申请重发，最多 3 次，仍收不到再走线上认证，上传身份证件，并建议补一张在填写地址旁地标的本人照片。这与同文件夹 PIN 文里「满 10 美元寄信」不是同一门槛，一个是身份验证触发，一个是付款阈值，不要混为一谈。正文和配图里若出现广告客户端编号，摘要不转抄。

## 案例
中文站秋玉米：作者先说 eCPM 约 0.54 美元，按每 UV 4 个 PV、每 PV 约 1.74 次展示估算，日 1000 UV 则月约 208 美元（约 1500 元人民币）；随后再截图时 eCPM 约 0.58 美元，展示/浏览比也变成约 1.69，说明这两个系数都会变。又假设若有英文站那样最高约 10 美元的 eCPM，收入约能到 18.5 倍、月约 3848 美元，但作者自己说这只是「算算过过瘾」，中文站单价低，所以才强调做海外、尤其是发达国家。关于 3 个月域名：他称那是针对内容少、流量小的站；社群有朋友 7 月注册域名，8 月就过审，不到一个月，原因是已有流量。这与后来《广告单价跌了吗》里「上线第 4 天过审」的例子方向一致，都把流量当作加速条件，但仍是个例。

## 风险 / 冲突 / 实操注意
「先养 Gmail 再申请」、3 个月域名、博客更新频率都是当时经验，不是现行成文门槛。PIN、重寄次数和付款最低额会变，要以官方帮助中心为准。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]把中文站单价乘到 10 美元是假想，不能当收益预期。

## 证据位置
秋玉米估算与截图、注册到申请审核的步骤说明，以及不到一个月过审的社群转述。


---

## 源文件：01_KNOWLEDGE/summaries/I6ZIdsSYYoVe22xzjMVc8BE5nQh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 Adsense如何收取Pin码，如何上传文件进行实名实地认证 | Web.Cafe

- 文档ID: `I6ZIdsSYYoVe22xzjMVc8BE5nQh`
- URL: https://zcnalei7zaql.feishu.cn/docx/I6ZIdsSYYoVe22xzjMVc8BE5nQh
- 路径: 出海seo资源分享V1.0/adsense/20240813 Adsense如何收取Pin码，如何上传文件进行实名实地认证 | Web.Cafe
- 正文字符: 1186
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:46:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞补充 AdSense 收款验证：第一个网站过审后可以放代码；广告费满 10 美元后，谷歌从美国寄平信 PIN 码，填进后台即完成他所说的「实人实地」验证。信件丢失率被认为较高。文首有断句，像是两段话粘在一起。正文让读者收藏「上面的链接」，但本篇抓取正文里并没有给出这个人工审核入口 URL。

## 方法 / 阈值
收不到信时，在后台申请人工审核。作者称一般要连续寄出 3 次都没收到才能进入；每次后台提示已寄出后约两周，看是否能点再次发送，凑满 3 次后再走判断流程，满足条件才出表单。为提高一次通过率，作者建议上传身份证照片，以及在填写地址附近的地标旁自拍，本人和地标名称要同时出现在画面里。

## 案例
作者大学时一次就拿到放到隔壁寝室信箱的信。后来教朋友时有人一直收不到。称有朋友按此昨天提交、今天通过，并附聊天和「被证明身份」界面截图，无更多材料说明。

## 风险 / 冲突 / 实操注意
这是 2024 年左右的经验，谷歌后来可能改为其他身份验证，PIN、10 美元门槛、三次重寄和人工入口都会变，必须以当时 AdSense 帮助中心和后台为准，不要把缺失的链接或本篇步骤当成现行官方流程。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 证据位置
PIN 信说明、三次重寄、材料建议和通过案例。


---

## 源文件：01_KNOWLEDGE/summaries/P5Hcdu7QEosEwCxKC0kctVxynUf.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 我如何通过SEO和Adsense优化，把一个网站广告收入从每月八百多美元提升到每月两千多美元，经验全分享 | Web.Cafe

- 文档ID: `P5Hcdu7QEosEwCxKC0kctVxynUf`
- URL: https://zcnalei7zaql.feishu.cn/docx/P5Hcdu7QEosEwCxKC0kctVxynUf
- 路径: 出海seo资源分享V1.0/adsense/20240813 我如何通过SEO和Adsense优化，把一个网站广告收入从每月八百多美元提升到每月两千多美元，经验全分享 | Web.Cafe
- 正文字符: 7530
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:48:38 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞回顾 2016 年帮一位网友改版站点后，广告收入从 6 月约 874 美元升到 7 月约 1475 美元，再到 11 月约 2100 美元。关键改动集中在 6 月底，主要三件事：重写前后端并提升速度、做站内 SEO、调整广告位。图注写的是各月「期末余额」，作者按当月收入来讲；若截图实际是余额而非当月估算收入，读法会不同，但正文是按月收入叙述的。站点名称被替换为「网站名称」。这是一个提供 Kindle 等格式「免费电子书分享下载」的中文列表站，详情页图书介绍直接复制自京东样式和内容。涉及可能的版权内容分发，只作历史案例阅读，不能作为实践项目。

## 方法 / 阈值
原站问题：打开慢；下载与网页同机，下载拖慢页面；找书不便；列表页和详情页都只有 1 个广告位。技术上是从 GitHub 找来的新手 PHP 社区程序，渲染 HTML 时查库，而且在循环里继续查库。他用 CodeIgniter 重写、重新设计表结构并导入旧数据，约 6 月 25 日上线。对已有收录的站，他强调新版 URL 必须与旧版一致，例如分类 /book/keji.html、详情 /book/view/9.html。站内 SEO：首页标题「网站名称 - 免费电子书分享下载」，描述围绕免费 Kindle 电子书下载；首页 h1 为站点名和口号；详情标题「{书名}-网站名称-通用关键字」，描述「《书名》是{作者}的作品，网站名称为您提供《书名》免费……」；详情 h1 用书名；分类标题「{分类}-网站名称-slogan」，描述「{分类}类……，网站名称为您提供……」，h1 为分类名；新增标签页，标题「标签:{标签}-网站名称-slogan」，作者 7 年后发现当时忘了写描述；作者名当作特殊标签，有作者聚合页；并加了搜索，但 Wayback 只有静态页，没有搜索结果截图。广告上，他在首页、分类、详情、标签等页面都放到 3 个广告位，理由是当时 AdSense 文档推荐的上限。改版后仍保留京东图书介绍板块，只改了样式。

## 案例
上线次日 UV、PV 都比前一天高很多。作者把 UV 上升归因于：搜索已有流量，旧站太慢导致部分人打不开就离开，速度修好后这些访问能留下来。PV 上升还因为新增标签页、搜索页，单用户可点页面变多，PV/UV 提高，广告展示和收入随之上升，所以 7 月大约到了 6 月的两倍。8 月几乎没涨，9、10 月再涨，11 月较大，他归因于新站对搜索更友好、收录增加、体验和速度更好带来排名和搜索流量上升。收入数字图注为：2016-06 约 874.04、07 约 1475.09、08 约 1481.95、09 约 1622.17、10 约 1710.51、11 约 2100.70 美元。

## 风险 / 冲突 / 实操注意
多项改动同时上线，无法分离速度、URL 保持、新列表页和增加广告位各自的贡献；2016 年的中文下载站也不能外推到现在的海外工具站。把页面都放满 3 个广告位，只是作者当时的做法，可能影响体验，也不等于今天的政策允许或收益最优。复制电商详情和提供电子书下载有版权与政策风险，不纳入学习后的实践。文末「看完就会优化自己的网站」过满，只应抽取「已收录站点改版要稳定 URL、先修性能再谈变现」这类可核验的方法，而不是复制这个站的模式。

## 证据位置
2016 年 6 至 11 月收入表、Wayback 旧版与新版布局，以及各类页面的标题、描述和 h1 格式说明。


---

## 源文件：01_KNOWLEDGE/summaries/RnSVdVMNPoC4rNxXcQbcYBqYnzc.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 如何快速估算一个网站的Adsense广告收入？ | Web.Cafe

- 文档ID: `RnSVdVMNPoC4rNxXcQbcYBqYnzc`
- URL: https://zcnalei7zaql.feishu.cn/docx/RnSVdVMNPoC4rNxXcQbcYBqYnzc
- 路径: 出海seo资源分享V1.0/adsense/20240813 如何快速估算一个网站的Adsense广告收入？ | Web.Cafe
- 正文字符: 3052
- 阅读深度: 方法精读
- 阅读时间: 2026-11-15 00:47:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞给出一套用流量和假设单价估算 AdSense 月收入的乘法，便于快速量级判断，不是已核实的报表。指标解释：UV、PV、广告曝光、eCPM（每 1000 次展示收入）。称国内站点 eCPM 很可能不到 1 美元，欧美发达国家可能 3 到 6 美元；谷歌通常建议一个页面最多约 3 个广告位。

## 方法 / 阈值
先设基数：eCPM=1 美元、1 个 UV 只产生 1 个 PV、1 个 PV 只产生 1 次展示，日 UV=1000，则日收入 1 美元、月收入约 30 美元，把 30 美元当基数。再按倍数连乘：UV 相对 1000 的倍数 × eCPM × 每 UV 的 PV × 每 PV 的展示次数。举例：欧美查询工具日 UV 1 万（10 倍）、eCPM 4 美元、每 UV 3 个 PV、每 PV 3 次展示，月收入 30×10×4×3×3=10800 美元。Similarweb 的「访问量」按作者解释：同一用户距上次访问超过 30 分钟会再计一次访问，估算 UV 时要判断是否存在短时间多次访问。

## 案例
以 calculator-online.net 做练习：Similarweb 图注总访问量约 180 万、跳出率约 58.15%、每次访问页数 2.36、平均时长约 1 分 16 秒；流量约 83% 来自自然搜索。作者先举例若每人每天 3 次访问则 UV 约为 2 万，但认为计算工具通常每人每天 1 次访问，故按 180 万/30 估日 UV 约 6 万（60 个 1000）。首页首屏见 3 个广告位，内页广告不一定都在首屏，估每 PV 约 2 次展示；流量主要来自美国、巴西、印尼，估平均 eCPM 约 2.5 美元。计算：30×60×2.5×2.36×2=21240 美元。他又说假设不完全准，实际「不会差特别多」，举例可能到 3 万美元，但没有该站真实收入对照。域名称注册于 2013 年（图注公司成立年份为 2014），用来说明晚入场仍可能有机会，并建议把已成功的在线工具加上 AI 再做一遍。

## 风险 / 冲突 / 实操注意
Similarweb 是估算，UV 换算、eCPM 和每页展示次数都是口头假设，连乘会放大误差，「2 万多到 3 万」没有出处。页面堆 3 个广告位只是作者观察，既可能高估展示，也可能影响体验和广告政策，不能当布局标准。这套公式只能做数量级讨论，不能当建站收益承诺。

## 证据位置
指标与基数公式、查询工具例题，以及 calculator-online.net 的 Similarweb 与页面观察。


---

## 源文件：01_KNOWLEDGE/summaries/CbOGd3tVmo7gUVx7xpUcMeVEnjj.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240813 从一个AI工具站最近7天Adsense不同国家收入数据分析对比告诉你为什么要出海 | Web.Cafe

- 文档ID: `CbOGd3tVmo7gUVx7xpUcMeVEnjj`
- URL: https://zcnalei7zaql.feishu.cn/docx/CbOGd3tVmo7gUVx7xpUcMeVEnjj
- 路径: 出海seo资源分享V1.0/adsense/20240813 从一个AI工具站最近7天Adsense不同国家收入数据分析对比告诉你为什么要出海 | Web.Cafe
- 正文字符: 1136
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:46:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞展示匿名朋友一个 AI 工具站最近 7 天的 AdSense 分国家数据，用来说明收入不只看浏览量，还要看各国单价，并由此论证要面向全球、赚美元。短文，没有展开选词或投放方法。

## 方法 / 阈值
按每千次展示收入从高到低看表，对比高单价国家和高浏览量但低单价的国家。

## 案例
正文：瑞士每千次展示约 7.34 美元最高，美国约 4.34 美元，法国、加拿大也在 4 美元以上，英国、澳大利亚、德国大约 2–3 美元。第二张图注还给出估算收入，如瑞士约 2.13 美元、美国约 55.79–79.79 美元、法国约 7.98 美元、加拿大约 5.00 美元、中国约 32.26 美元但每千次展示约 0.71 美元。第一张图注曾把美国写成「最高」，与正文和后表冲突，以正文排序为准。站点未具名，只有 7 天切片。

## 风险 / 冲突 / 实操注意
单价随广告主、季节和站点内容变化，不能把这一周的数字当成稳定 RPM。中国收入总额仍可能因量大而不低，文中用来对比的是单价。匿名截图无法独立核对。

## 证据位置
两张分国家表和文末结论。


---

## 源文件：01_KNOWLEDGE/summaries/PpHAdpeHjoo5ZRxOZ84cYXmhnTh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260715 AdSense 美国税务信息填写指南 | Web.Cafe

- 文档ID: `PpHAdpeHjoo5ZRxOZ84cYXmhnTh`
- URL: https://zcnalei7zaql.feishu.cn/docx/PpHAdpeHjoo5ZRxOZ84cYXmhnTh
- 路径: 出海seo资源分享V1.0/adsense/20260715 AdSense 美国税务信息填写指南 | Web.Cafe
- 正文字符: 1194
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:46:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。][去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 方法 / 阈值
飞书里写到的唯一步骤：在 AdSense 后台进入收款 → 支付信息 → 管理设置，找到「美国税务信息」再点修改。其余让读者打开 https://mp.weixin.qq.com/s/fg604vVtbmlTdoUt1aPiLQ 。评论区没有实质补充。

## 案例
无具体表单选项或填写示例出现在本篇正文。

## 风险 / 冲突 / 实操注意
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]本篇也不构成税务建议。

## 证据位置
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]


---

## 源文件：01_KNOWLEDGE/summaries/WYnqd2h5KooPyNxj613cU4xqntf.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260716 Adsense审核4连过的思考 | Web.Cafe

- 文档ID: `WYnqd2h5KooPyNxj613cU4xqntf`
- URL: https://zcnalei7zaql.feishu.cn/docx/WYnqd2h5KooPyNxj613cU4xqntf
- 路径: 出海seo资源分享V1.0/adsense/20260716 Adsense审核4连过的思考 | Web.Cafe
- 正文字符: 3098
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:47:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
作者江帅有点忙 2026-07-16 发帖：同一批模板的网站以前申请 AdSense 常被拒，最近连续 4 次通过，总结自己观察到的变化。这是个人复盘，不是官方审核标准。[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 方法 / 阈值
1) 流量：以前几乎只有必应排名，现在谷歌核心词多进前十；他给的经验特征是谷歌日点击大于 100，并附 24 小时 GSC 图注：点击 112、曝光 3555、平均点击率 3.2%、平均排名 9.4。2) 网页性能：用 pagespeed.web.dev 查完再交给 Codex 改；LCP、INP、CLS 也可看必应 Clarity。正文写以前就把 PC 和移动端优化到 90 分以上，但文中一张 Pagespeed 图注是 86/100（来自 92 个页面测量），另一张 Core Web Vitals 报告为未通过（LCP 2.6 秒、INP 200 毫秒、CLS 0.13）。这两张图与「90 分以上」并不一致，作者未解释是哪个地址、哪个阶段。3) 申请方式：以前几个站一起提交，现在一个通过后再申下一个。他推测同时提交会被同一审核员看到同一模板从而拒审，错开则换审核员、降低拒审。这只是推测，没有官方依据。4) 基础仍提哥飞说过的三件套：博客、隐私政策、服务条款。

## 案例
作者是游戏站，试过圈友分享的 Codex 审计技能，按官方手册列出一大堆改项且难以做到，就没按清单改。因为之前被 Adsterra 坑到，仍去申请，结果 4 连过，并称后来再申一个大约 3 天能出结果。截图里部分记录 Ads.txt 为「未找到」或「已授权」，审批状态多为「准备就绪」，更新时间集中在 2026 年 7 月。

## 风险 / 冲突 / 实操注意
日点击、分数和「错开提交」都是单一样本，不能当过审门槛。用时间差避免被看出同一模板，是在猜测审核分配，不能作为建议，更不能用来掩盖低质量批量站。作者写「规矩是规矩，现实有灰度，老老实实守规矩会束缚自己」，这种表述不能当作可以忽略官方政策。实验室分数、字段 CWV 和「90 分」在文中互相打架，引用时要分开看。

## 证据位置
现象截图、三个要素说明、三件套引用，以及技能未用仍过审的自述。


---

## 源文件：01_KNOWLEDGE/summaries/I9msdZsldoq9ZnxkIMKcH1lhnch.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260106 《哥飞实战手册》：海外工具站从0到月入万刀全流程指南 | Web.Cafe

- 文档ID: `I9msdZsldoq9ZnxkIMKcH1lhnch`
- URL: https://zcnalei7zaql.feishu.cn/docx/I9msdZsldoq9ZnxkIMKcH1lhnch
- 路径: 出海seo资源分享V1.0/新手入门/20260106 《哥飞实战手册》：海外工具站从0到月入万刀全流程指南 | Web.Cafe
- 正文字符: 11354
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:22:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 概念
GONG 用 AI 汇总的手册，文首自承「用 AI 总结编写」。核心理念养网站防老、单域名单站单关键词、新词新站。

## 方法
挖词：新词=过去 12 个月才显著起量；KDROI=(Volume×CPC)/KD；避开季节词和强品牌词。上站 SOP：Perplexity「只收集不总结」→用 LLM 先设计 H 结构再出 HTML/CSS/JS→Vercel/CF 部署→GSC+社区引爬。SEO 用 TDH（指出 keywords 元标签已弃用）。外链抄竞品。AdSense 估收入=(PV/1000)×RPM，PIN 信、付款门槛 100 美元。SEM 早期测「100 UV 能否出第一单」，规模化看 LTV>CAC。结语口号「多上站」。

## 阈值 / 主张
优先 KD<29。页面单词 800+、密度 3%–5%（与 SOP 冲突，不宜当硬指标）。新词定义 12 个月，与路线 180 天、2026-11 文 30 天窗口不同。

## 案例
手册内 ChatGPT、Grok 作为新词例子；无完整独立复盘。

## 依赖
pplx.ai、Claude 3.5/GPT-4o（会过时）、Vercel/CF、Semrush/Ahrefs、GSC。

## 风险 / 不宜无依据背书
AI 汇编可能平滑或夸大原话，引用优先回哥飞署名原文。「上线即排名」是宣传口吻。密度规则过时风险高。工具名与版本会过时。

## 证据位置
前言；第一至七章及结语。详见 SPINE 摘要对应节。


---

## 源文件：01_KNOWLEDGE/summaries/Hyyvd5ZW1oCt5OxN9JGcK69inRh.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240729 如何用GPT生成SEO友好的网页Title和Description | Web.Cafe

- 文档ID: `Hyyvd5ZW1oCt5OxN9JGcK69inRh`
- URL: https://zcnalei7zaql.feishu.cn/docx/Hyyvd5ZW1oCt5OxN9JGcK69inRh
- 路径: 出海seo资源分享V1.0/新手入门/20240729 如何用GPT生成SEO友好的网页Title和Description | Web.Cafe
- 正文字符: 4683
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:31:36 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
演示上线前用 GPT 辅助写首页 Title 和 Description：不能空手让模型编，先准备用户真实会搜的词表，再多轮改到长度和用词都符合要求。对象站 chinesenames.ai 被指 UI 尚可，但 Head 里最重要的 Title、Description 都缺失。

## 方法 / 阈值
用 Similarweb 或 Semrush 关键词生成器输入核心词，导出「语句匹配」和「相关关键词」，合并去重后按搜索量排序，只保留前 100 个词（一行一个，不要数据）。把网址、站名、定位和这份词表交给 GPT 写 Title；不满意就指出问题继续改，或自己先写一版让它润色。约束包括标题一般小于 60 字符、开头突出核心功能与「AI」、覆盖核心词、结尾放品牌名、避免用户不会搜的生僻词。Title 定稿后再写 Description，过长就压缩，并检查是否漏了核心词。也可用 Claude。

## 案例
站点定位为帮非中国人起中国名并解释含义。提示词里的品牌多次写成 ChinsesNames.ai / ChinesesNames.ai。迭代中先后丢掉 Generated、缩短长度、拒绝 Interpreter，最终标题为：AI Chinese Names Generator & Meaning Explainer | ChinsesNames.ai。描述定稿为：Discover Chinese names and meanings with our AI Chinese Names Generator at ChinsesNames.ai. Find unique names effortlessly tailored to your preferences.

## 风险 / 冲突 / 实操注意
文中品牌名拼写前后不一致，照抄会把错误写进 Title。词表前 100 和「标题里塞进 AI、核心词、品牌」仍可能偏满，需对照「优化不要太满」和字数限制自己取舍。这是写作流程演示，不是该站后来是否获得流量的证据。

## 证据位置
开篇缺 TDK 的截图；数据准备与提示词；多轮 Title 对话；Description 补上 Chinese 的两轮；文末方法小结。


---

## 源文件：01_KNOWLEDGE/summaries/PQBzd4ZU4ok7IAx83eyc1Na2nOe.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 介绍几个 Ahrefs 家的免费SEO工具 Free SEO Tools（上）

- 文档ID: `PQBzd4ZU4ok7IAx83eyc1Na2nOe`
- URL: https://zcnalei7zaql.feishu.cn/docx/PQBzd4ZU4ok7IAx83eyc1Na2nOe
- 路径: 出海seo资源分享V1.0/新手入门/20240812 介绍几个 Ahrefs 家的免费SEO工具 Free SEO Tools（上）
- 正文字符: 3248
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:29:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
罗列 Ahrefs 14 个免费工具，上篇介绍前一组：Google 关键词生成器、Amazon、Bing、YouTube 关键词工具、关键词难度检查器、反链检查器、网站权威检查器。其余 7 个留到下篇。正文小标题不完整，第一节没有「一」的标题，第三节 Bing 也没有单独标题，演示图和说明有错位。

## 方法 / 阈值
Keyword Generator 输入词根出相关词，前 10 个带 KD；Volume 是近 12 个月月均。Amazon/Bing/YouTube 工具同理换搜索源。难度工具指向另一篇《有了这几个关键字优化难度分析工具…》。反链与权威工具输入域名即可，作者说两者展示的权威数据是同一套。

## 案例
「ai generator」相关词示例（图注写了 3288 个词，并出现 voice/nsfw 等）。Bing 示例词 seo；YouTube 示例 music（music 340 万、study music 84 万等）。qiuyumi.com：正文写 1100 个网站、7500 条外链，配图却是 DR 46、外链 75K（97% dofollow）、来源站 1.1K。ahrefs.com 演示 DR 91、外链 4.1M、来源站 84K。

## 风险 / 冲突 / 实操注意
qiuyumi.com 的 7500 与 75K 互相矛盾，以配图字段为准并应复查工具。演示图有的标成 Amazon 实际像 Google 生成器，引用时不要用错工具名。免费工具额度与界面后来可能已变。

## 证据位置
文首 14 项清单；各工具用途和演示图；文末「剩下 7 个明天再讲」。


---

## 源文件：01_KNOWLEDGE/summaries/WWvTd45uDo0EUyxhbXScbjEOnIb.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（上） | Web.Cafe

- 文档ID: `WWvTd45uDo0EUyxhbXScbjEOnIb`
- URL: https://zcnalei7zaql.feishu.cn/docx/WWvTd45uDo0EUyxhbXScbjEOnIb
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（上） | Web.Cafe
- 正文字符: 5594
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:29:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
带读 SearchEngineJournal「10 个重要元标签」的上篇，先讲 Title、Description、Headings。开篇强调没有单一最重要因素，要做包含外链和站内标签的全面策略。元标签用来说明页面关于什么、如何阅读、以及希望出现在哪些检索里。

## 方法 / 阈值
Title：每页唯一、50–60 字符、重要词靠前但自然；作者习惯在全站标题末尾加网站名和域名。Description：不是排名因素，但常出现在摘要里影响点击；每页独特、约 150–160 字符，用一两句自然话带出关键词，可加行动号召，不要堆词，也不要抄竞争对手。若用户搜的是页内原句，谷歌可能用页面片段替换描述。H1–H6：帮助引擎理解结构和给用户预期，作者建议连非长文页也可以给出目录。谷歌说 Title 与 H1 可以相同也可以不同，写不出差异时允许一样。文末推荐社群产品 AITDK 免费浏览器插件查看这些标签和域名、流量等信息。

## 案例
再次引用那张非官方「2024 排名因素」饼图，称标题关键词占 15%。用「how to build brand awareness」说明标题不必逐字匹配也能排上。checkfiletype.com 的标题只写 File Type Checker，却在 file type detector、file type checker、file extension detector、file extension checker 四个相近查询里都排第一。插件截图里该站 Title 49/60、Description 147/160、缺 canonical，域名 2011-11-08 注册。

## 风险 / 冲突 / 实操注意
15% 标题权重不是谷歌官方数字，与「再聊内链」用的是同一来源，不能当算法事实。AITDK 是社群插件，流量等数据需当第三方估算。

## 证据位置
开篇 SEJ 立场；Title 四点实践与四词同站案例；Description 与 Headings 实践；Title/H1 可否相同；AITDK 截图与下载链接。


---

## 源文件：01_KNOWLEDGE/summaries/Ddhpde8TjoMwzrx3lpPc8RO5n2e.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240716 出海工具网站，从需求挖掘到网站制作全流程，让你一篇文章学会 | Web.Cafe

- 文档ID: `Ddhpde8TjoMwzrx3lpPc8RO5n2e`
- URL: https://zcnalei7zaql.feishu.cn/docx/Ddhpde8TjoMwzrx3lpPc8RO5n2e
- 路径: 出海seo资源分享V1.0/新手入门/20240716 出海工具网站，从需求挖掘到网站制作全流程，让你一篇文章学会 | Web.Cafe
- 正文字符: 13974
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:33:29 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
这是三份「需求挖掘到做站全流程」里日期最早的一份（2024-07-16），标题没有「5000字长文」，原文链接也与 8 月 13 日的进阶版 LKE7、根目录版 YgOad 不同。结构同为前景、挖需求、实战、做站，论点大部分相同：工具站可长期收流但前提是真有用、新手先做短期或 for fun、Similarweb→Semrush→Trends→Ahrefs 复核、低 KD 且 SERP 多为内页则可用独立域名去抢、着色页产品构想、用简单技术或模板做站。已全文对照，不能因为同主题而跳过。

## 方法 / 阈值
与后两份相同的主线：谷歌找到站点后看 Similarweb；Semrush 付费可筛 KD<60，实战又用 Keyword Magic 的 0–29%；Ahrefs 免登录难度工具，所需外链站<100 再尝试；跳过别人的品牌词。实战词与 ai-coloring-pages.com、A4 线稿、公开 AI 生成图、下载分层收费、alt 冲图片搜索等构想也相同。建站仍建议菜鸟教程+ChatGPT，Vue 或原生 JS，或改 Vercel 模板、买 Codecanyon。

## 案例
同样覆盖 ilovepdf、presearch、poxer、Reddit 2000 美元案例、cat coloring pages、Vercel 模板朋友和 225 美元短链系统。本篇独有的一句：作者根据 Similarweb 判断 ilovepdf 在美国几乎没流量，并指出 Ahrefs 的 pdf 美区 SERP 里也没有它。本篇首张 Similarweb 图注写 ilovepdf 营收 2000–5000 万美元、员工 50，与进阶版图注的 200–850 万美元不同，倒是更接近根目录那份。同类列表图注把 23.9M 月访写在 smallpdf 上，和后两份把同一数字写在 ilovepdf 上不一致。cat coloring pages 的一张图注出现搜索量 156,444、排名 33,100，与其他副本不同，这些数字只能当图注，不能混用。

## 风险 / 冲突 / 实操注意
淘宝共享账号、poxer 意图可能误判、「域名带 AI 事半功倍」、手速抢域名、以及三份副本之间的配图数字差异，处理原则与 LKE7/YgOad 摘要相同。本篇是 7 月 16 日较早发表的版本，引用时标明新手入门这一份，不要和 8 月 13 日两份当成同一文件。

## 证据位置
文首 2024-07-16 与不同原文链接；第二节末尾关于 ilovepdf 美国几乎无流量的补充；其余段落与后两份同序；第四节至文末的模板与 Codecanyon 案例。


---

## 源文件：01_KNOWLEDGE/summaries/FVx5d1QLHoJDvjxnuPOc7yg3n8f.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 月访问量八百万的在线自动化工具站如何用内容做SEO获取大量优质免费流量？ | Web.Cafe

- 文档ID: `FVx5d1QLHoJDvjxnuPOc7yg3n8f`
- URL: https://zcnalei7zaql.feishu.cn/docx/FVx5d1QLHoJDvjxnuPOc7yg3n8f
- 路径: 出海seo资源分享V1.0/新手入门/20240812 月访问量八百万的在线自动化工具站如何用内容做SEO获取大量优质免费流量？ | Web.Cafe
- 正文字符: 3131
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:28:46 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
拆 Zapier：工具站也可以靠博客内容拿到大量非品牌搜索流量。对 AI 产品的两条启发是「工具站一定加博客」和「AI 相关词值得做」，后一句是作者当时的判断，需用具体词的 SERP/KD 复核。

## 方法 / 阈值
用 Similarweb 看体量、时长、渠道，再对照 Semrush 的自然/付费词和落地页。观察非品牌词是否指向博客、付费词是否也落在「Best xxx」类文章。

## 案例
数据约在 2023-09：Similarweb 月访 874.8 万、时长 4 分 22 秒、跳出约 50.53%，直接访问 38.47%、自然搜索 48.93%、付费搜索 7.10%；近半年约 826 万至 973 万后回落。Semrush 权威分 73、自然流量 430 万，与 875 万×48.9% 接近。自然词里出现 ai image generator、ai detector，付费里有 ai website builder；非品牌自然和多数付费落地页是博客，品牌词进首页。

## 风险 / 冲突 / 实操注意
Zapier 是大品牌长周期内容机器，不能直接外推到新站。「AI 词优化不难」与其他篇的难度门槛并置。正文写人均 7.2 页，首张图未给出同等确认，引用以渠道和落地页结构为主。

## 证据位置
文首流量与渠道图；Semrush 对照；付费/自然落地页截图；文末两条启发。


---

## 源文件：01_KNOWLEDGE/summaries/QDVSd2NSYoPRDGxoYIacBq12nFd.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 有了这几个关键字优化难度分析工具，妈妈再也不怕我不会判断SEO难度了 | Web.Cafe

- 文档ID: `QDVSd2NSYoPRDGxoYIacBq12nFd`
- URL: https://zcnalei7zaql.feishu.cn/docx/QDVSd2NSYoPRDGxoYIacBq12nFd
- 路径: 出海seo资源分享V1.0/新手入门/20240812 有了这几个关键字优化难度分析工具，妈妈再也不怕我不会判断SEO难度了 | Web.Cafe
- 正文字符: 5299
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:30:00 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
教用多工具判断难度，并强调不要只看分数，要看需要多少个来源域名的外链，还要按国家看搜索量。站长工具偏向百度环境，Ahrefs 才是谷歌侧量化。

## 方法 / 阈值
一、站长工具 kwevaluate：看优化分、百度指数、百度结果数、长尾数等；指数不等于日搜索量，只能比相对大小。二、Ahrefs 免费难度工具：看 KD 和「进入前 10 约需多少个网站的 followed 外链」（按来源域名计，不是一条页脚全站链算几百条）。作者归纳：0–10 约<10 个域名；11–30 约 11–36 个；60 以下几十个域名「可以去做」；超过 65 先不考虑。难度与所需域名数不是线性，越高越陡。三、换国家看量和 KD，难度低还得有量。养成每天看数据的习惯。

## 案例
词例 timestamp。站长工具优化分 91：百度指数等数据外，前 50 结果里权重≥4 的域名有 36 个，是高分主因；百度系 11 个、内页 37、首页结果仅 2。Ahrefs 美国 KD 81，约需 374 个来源域。日本 KD 12，约 13 个域。全球量 182.7K，美国和印度各 14.8K，法国 12.1K，印尼 9.9K，巴西和菲律宾各 8.1K。印度 KD 仍 86；法国 KD 47，作者认为可做法语版；法语词 horodatage 量仅 1.9K 但 KD 28；印尼 KD 40。

## 风险 / 冲突 / 实操注意
同一英文词在站长工具（百度）和 Ahrefs（谷歌、分国家）上的分数不可混用。KD>65 不做、60 以下可做，又与其他篇 0–29 或筛 KD<60 且量≥30000 的口径并存。法国可做是作者判断，还要看语言能力和意图。免费版只能看到部分 SERP。

## 证据位置
第一节 timestamp 站长工具与百度指数/结果数；第二节 Ahrefs 81 分与 374 个域及难度标尺；第三节多国家量级与 horodatage 对照。


---

## 源文件：01_KNOWLEDGE/summaries/Jo9Qd8dDVoBWYWxM1QZcLgF6nkb.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 我如何通过SEO和Adsense优化，把一个网站广告收入从每月八百多美元提升到每月两千多美元，经验全分享 | Web.Cafe

- 文档ID: `Jo9Qd8dDVoBWYWxM1QZcLgF6nkb`
- URL: https://zcnalei7zaql.feishu.cn/docx/Jo9Qd8dDVoBWYWxM1QZcLgF6nkb
- 路径: 出海seo资源分享V1.0/新手入门/20240812 我如何通过SEO和Adsense优化，把一个网站广告收入从每月八百多美元提升到每月两千多美元，经验全分享 | Web.Cafe
- 正文字符: 7812
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:32:39 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
2016 年帮朋友改造一个已有流量的中文电子书列表站：6 月底重写前后端并提速、补站内 SEO、调整 AdSense 布局。截图显示广告收入 6 月 874.04 美元，7 月 1475.09，8 月 1481.95，9 月 1622.17，10 月 1710.51，11 月 2100.70。作者把 7 月翻倍主要归因于打开速度改善后留住了搜索流量，把 8 月后的继续上涨归因于更多页面被收录和体验变好带来的排名提升。这是旧站改造案例，不是新站从零做广告的路径。

## 方法 / 阈值
当时诊断：页面慢（GitHub 上刚学 PHP 的社区程序，渲染时循环查库、无 MVC）、下载与网页同机互相拖累、找书不便、列表和详情都只有一个广告位。用 CodeIgniter 重写并重建表、导入旧数据，约 6 月 25 日上线。已收录站点改版必须保持旧 URL 不变，文中举例分类 /book/keji.html、详情 /book/view/9.html。新版列表改卡片、加封面；所有页放到作者所称的「AdSense 文档推荐上限」3 个广告位；新增标签页、作者页和搜索。TDK 模板：首页「网站名-免费电子书分享下载」且 H1 同步 slogan；详情「{书名}-网站名-通用关键字」，H1 为书名；分类「{分类}-网站名-slogan」，H1 为分类名；标签「标签:{名}-网站名-slogan」。七年后作者发现标签页当时忘了写 description。

## 案例
站点名称在文中被替换。作者说答应帮忙，是因为看到下载/浏览数据和详情里的图书介绍。次日 UV、PV 明显上升，解释为原先打开太慢，部分搜索用户直接关掉；页面类型变多后 PV/UV 也上升，广告展示随之增加。

## 风险 / 冲突 / 实操注意
该站定位是「免费电子书分享下载」，详情介绍还被作者写明是直接复制京东图书文案和样式，涉及版权问题，不能当作实践项目，更不能去复制电商简介。3 个广告位是否仍是现行 AdSense 上限须核对官方说明，广告增多不是收入翻倍的唯一变量。2016 年数据和「看完就会优化自己的网站」都不能直接外推到每天 60 分钟的新站练习。

## 证据位置
文首 6–11 月收入表；改版前 archive 列表/详情与问题清单；保 URL、新版布局与各类 TDK/H1 模板；标签页缺 description 的自我更正；对 7 月与此后增长原因的解释。


---

## 源文件：01_KNOWLEDGE/summaries/JYScdeUvtogu7UxMMxzc4Vu3n3c.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 推荐一款好用且免费的SEO插件，哥飞天天都在用 | Web.Cafe

- 文档ID: `JYScdeUvtogu7UxMMxzc4Vu3n3c`
- URL: https://zcnalei7zaql.feishu.cn/docx/JYScdeUvtogu7UxMMxzc4Vu3n3c
- 路径: 出海seo资源分享V1.0/新手入门/20240812 推荐一款好用且免费的SEO插件，哥飞天天都在用 | Web.Cafe
- 正文字符: 6401
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:32:03 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
哥飞推荐社群成员 @blank 做的免费 Chrome 插件 AITDK SEO Extension，声称自发推荐、未收推广费。需求来自他原先要同时用 Detailed 看 TDK/标题、Similarweb 看流量、再另查域名注册时间。文中版本为 1.4.0（约 80.44KiB，截图显示 2024-02-28 更新）；当时商店页约 1000 用户、10 个 5.0 评价。作者说它已能替代 Detailed 和 Similarweb 插件。元标签系列文末也曾提到同一插件。

## 方法 / 阈值
打开任意页面可看：Title/Description 长度、作者不建议使用的 keywords、URL 与 canonical、域名注册/到期（文称 .ai 注册局可能不返回）、是否有 robots.txt 和 sitemap.xml、是否含 GA 与 AdSense、H1–H6 数量、图片及缺 alt 数量、内外链与 dofollow。另有流量概览（月访、跳出、页数、停留、全球/国家排名、近三月曲线、渠道和地区）、标题列表、图片列表、链接锚文本、OG/Twitter Card、hreflang、结构化数据、Whois 与 DNS。用来检查自己的页或学习大站。国家排名被写成「根据服务器所在国家判断」，这个口径需存疑。

## 案例
monkeytype.com：流量截图月访 1270 万、跳出 68.10%、人均 1.89 页、直接访问约 91.85%；作者认为首页几乎只做品牌词。概览图曾显示 H1 为 0，Headings 页又列出 1 个 H1「monkey see monkeytype」，同一文内数字冲突。pngtree.com 用来演示图片统计（66 张图、11 张唯一、alt 都有但 title 属性全缺）。hix.ai 用来演示 hreflang 与 Organization 结构化数据。DNS 示例显示走 Cloudflare。

## 风险 / 冲突 / 实操注意
流量、排名等是第三方估算，不能当成官方统计。插件功能和商店数据会变，下载应以当时商店页为准；本篇文末只说「欢迎下载」，未在抓取正文里写出安装链接（前序元标签文曾给 aitdk.com 扩展页）。图片 Title 属性缺失被单独统计，重要性低于 alt，不必同等对待。

## 证据位置
开篇无推广费声明与 1.4.0 信息；第一节 13 项概览；二至九节以 monkeytype、pngtree、hix.ai 为示例的功能说明。


---

## 源文件：01_KNOWLEDGE/summaries/NPOFdkkGXo8cbvxqTc5cS3HxnEd.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 如何用AI做SEO之内容自动批量生成，从搜索引擎获取免费流量 | Web.Cafe

- 文档ID: `NPOFdkkGXo8cbvxqTc5cS3HxnEd`
- URL: https://zcnalei7zaql.feishu.cn/docx/NPOFdkkGXo8cbvxqTc5cS3HxnEd
- 路径: 出海seo资源分享V1.0/新手入门/20240812 如何用AI做SEO之内容自动批量生成，从搜索引擎获取免费流量 | Web.Cafe
- 正文字符: 1292
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:28:46 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
短文结论：作者在 2024-08 认为搜索引擎还不能准确识别 AI 正文，所以用 GPT 做 SEO「可行」；要做精准需求文，不要泛娱乐，也不要垃圾文，因为垃圾文转不了顾客。标题写了「自动批量生成」，正文几乎没有批量流程，只给方向和两则朋友案例。

## 方法 / 阈值
按企业服务和产品范围，分析潜在客户会搜的词，用 AI 写能解决痛点的文章，替代过去半月或一月一篇的人工更新。

## 案例
朋友在国外做旅馆，用 GPT 写英文站被谷歌收录并有流量；另一朋友中文站做百度，称每天流量还不错；第三人帮亲戚的城市消杀公司给物业客户写定向文章。均无数据核验。

## 风险 / 冲突 / 实操注意
「搜索引擎无法识别 AI 内容」是当时判断，不能当现在的操作前提，也与后文「不要垃圾页、要有用内容」以及「哥飞网站权重」里停止劣质批量页的主张需要并排看待。实践中不可把批量生成未审核文章当作每日任务。

## 证据位置
开篇两项结论；旅馆/中文站/消杀三个例子；文末强调必须对潜在顾客有用。


---

## 源文件：01_KNOWLEDGE/summaries/OrxBdZcJeoj6w8xowxCcXEzEnXd.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 如何给一个已经上线的网站出SEO改造建议 | Web.Cafe

- 文档ID: `OrxBdZcJeoj6w8xowxCcXEzEnXd`
- URL: https://zcnalei7zaql.feishu.cn/docx/OrxBdZcJeoj6w8xowxCcXEzEnXd
- 路径: 出海seo资源分享V1.0/新手入门/20240812 如何给一个已经上线的网站出SEO改造建议 | Web.Cafe
- 正文字符: 2145
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:28:46 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
针对已上线站点：已有 URL 尽量不要改，以免丢掉收录和外链。改造分两块：在老域名子目录下按用户需求加新页面（工具或内容，相当于「不做新域名的新站」）；以及在 URL 不变前提下改老页面。

## 方法 / 阈值
检查 TDK、树状内链（首页到内页尽量不超过 4 次点击）、sitemap、canonical、每页一个 H1 与合理的 H2/H3/P。首页 title 模板写成「网站名-Slogan-关键词1-2-3…」，并建议首页写 keywords；栏目页和内页的 keywords 可以不写。canonical 示例用了 https://weixin.qq.com。

## 案例
[去敏：涉及联系、授权、支付、推广标识或内部运行信息的句段已略。]

## 风险 / 冲突 / 实操注意
「URL 绝对不能改」说得过死，必要迁移通常应配合 301，本文未谈。首页堆积关键词、又建议写 keywords 元标签，与 5800 字长文「删掉 keywords、优化不要太满」冲突，改造时不要把模板当唯一写法。文中有「H2、H2」笔误。

## 证据位置
开篇不改 URL 的原则；一节加新页；2.1–2.5 的 TDK 模板、内链深度、sitemap、canonical 与标题层级。


---

## 源文件：01_KNOWLEDGE/summaries/A5tvd7xfXowvbexO4rccsza2nke.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 介绍几个 Ahrefs 家的免费SEO工具 Free SEO Tools（下）

- 文档ID: `A5tvd7xfXowvbexO4rccsza2nke`
- URL: https://zcnalei7zaql.feishu.cn/docx/A5tvd7xfXowvbexO4rccsza2nke
- 路径: 出海seo资源分享V1.0/新手入门/20240812 介绍几个 Ahrefs 家的免费SEO工具 Free SEO Tools（下）
- 正文字符: 3948
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:30:00 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
接上篇，介绍剩余 7 个免费工具：坏链检查、流量检查、关键词排名检查、SERP 检查、WordPress 插件、AI 写作工具、SEO 工具栏。结构同样较松，部分工具缺少清晰小标题，排名检查的演示图看起来更像 SERP 检查结果。

## 方法 / 阈值
坏链分出站死链（你链出去的目标失效）和入站死链（别人链向你但你的页失效）。流量工具看自然流量和「流量价值」，作者称当时比 Semrush 显示得更多。排名工具查某站某词在谷歌的名次。SERP 工具给出某词前 10 结果及各页 DR、UR、外链、流量、词数。WP 插件被官方说成对其它 SEO 插件的补充，偏内容审查。AI 写作列出缩略词、改写、摘要、大纲等十几种功能，作者说以后再测，本文无实测。工具栏自行安装。

## 案例
qiuyumi.com 出站死链 8 条、入站 0。producthunt.com 自然流量 110 万、价值约 49.52 万美元，美国约 28%、印度约 24%。ahrefs.com 在 keyword research 上排第 7。ai generator 的前 10 结果带 DR/流量等指标。

## 风险 / 冲突 / 实操注意
流量价值是工具估算。上篇 qiuyumi 外链数字已有矛盾，本篇坏链数据可分开记。免费工具界面与额度后来可能变化。AI 写作列表不能代替内容质量要求。

## 证据位置
文首 7 项清单；坏链与流量、排名/SERP 演示图；WP 插件说明；AI 写作功能列表；文末工具栏一笔带过。


---

## 源文件：01_KNOWLEDGE/summaries/AuUUdOEOBo53SGx7GeScUau6nir.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞评站】AI贴纸生成网站 StickerBaker 的SEO评测报告和改进建议（4000字） | Web.Cafe

- 文档ID: `AuUUdOEOBo53SGx7GeScUau6nir`
- URL: https://zcnalei7zaql.feishu.cn/docx/AuUUdOEOBo53SGx7GeScUau6nir
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞评站】AI贴纸生成网站 StickerBaker 的SEO评测报告和改进建议（4000字） | Web.Cafe
- 正文字符: 11506
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:33:07 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
用 AITDK 插件逐页评 stickerbaker.com（开源 AI 贴纸工具，基于 Replicate 的 fofr/sticker-maker）。页面结构为首页、/sticker/{id}、/stickers、/search 与带 query 的搜索结果。作者认为详情页和搜索结果页可以变成大量长尾入口，但很多内容是前端渲染，爬虫看到的是重复 HTML。文首提到代码开源、部署看「上面那篇」，本篇抓取正文里没有保留那篇的链接。文末说明这是免费简评，付费会更细，并强调 SEO 拼细节。

## 方法 / 阈值
首页：Title 仅 12 字符、Description 21 字符，浪费长度；不写 keywords 是对的；缺 canonical，建议补上；sitemap 对小站不是必须，但「有比没有好」。一页不要两个 H1，H1 应带核心需求词如 Sticker Maker；「Upload」不宜做 H1/H2，建议挂在 Convert photo/face to sticker 下用 H3；Latest 改为 Latest Generated Stickers 并作 H2。图标缺 alt，生成图 alt 可更长并带 Sticker。可控出站用 dofollow 也可以。OG/Twitter 已有。首页优点：首屏就是工具、最新作品使首页常有新内容、动态冒出新贴纸像在「热闹」。无限上拉爬虫做不到，应加可分页的 Discover。详情页：纯数字 ID 易被遍历，建议 /sticker/29961-fairy-unicorn，长提示词不要整段进 URL；SEO 标题可写成 AI Sticker of fairy unicorn，分享用的「I made an…」放到 OG；H1 应是主题词而不是 Similar-ish stickers；相似贴纸有助于密度，但须改后端渲染。搜索首页做 Sticker Search 这个词是对的，品牌写成无空格 StickerSearch（作者称结果页更少），但 Title/H1 仍要兼容有空格写法；现仅一个 H5，应改 H1 并加内容。搜索结果页 Title/Description/H 标签写死且前端渲染，被当作重复页；应后端渲染，例如 H1/Title 用「160 Best Unicorn Stickers」。建议新增：分页 Discover（当前页前后 10 页、首尾页，以及 50/100/200 这类跳级，或学 Toolify 首页底部入口）、专题页（人工或向量聚合）、全部搜索词的列表入口（可配最佳贴纸图）。

## 案例
Trends 里 Sticker Maker 在 2 月下旬有过高峰。photo to sticker 相对 image to sticker 更热，Convert photo to sticker 在他给出的那张图上是 0，但正文仍建议用 Convert 句式。/sticker/29961 示例主题为 fairy unicorn。Google 显示 StickerSearch 约 8.35 万条结果，用来支持无空格品牌名。

## 风险 / 冲突 / 实操注意
「把 Title 用满 60 字符」与「写准确独特标题」可能冲突。为每个用户生成物和每个搜索词大量建页，与《再聊内链》里「不要一条 UGC 就做一个索引页、先按有搜索量的词聚合」存在张力，需用质量门槛约束，否则容易变成薄页面。前端渲染等于重复页的说法需理解为「源码里没有独特内容」，不是所有 CSR 都不可收录。数值 ID 改 slug 时要处理好旧 URL。这是评测建议，不是该站后来涨流量的验证。

## 证据位置
首页 1.1–1.10 与优缺点；详情页 URL/标题/标题层级与 SSR 建议；搜索首页与结果页问题；第五节三类应增页面及 Toolify 底部例子。


---

## 源文件：01_KNOWLEDGE/summaries/Rgeudmd3aoeP6gxZkBCchH0rnFg.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞解读】2024年谷歌算法排名因素变化 | Web.Cafe

- 文档ID: `Rgeudmd3aoeP6gxZkBCchH0rnFg`
- URL: https://zcnalei7zaql.feishu.cn/docx/Rgeudmd3aoeP6gxZkBCchH0rnFg
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞解读】2024年谷歌算法排名因素变化 | Web.Cafe
- 正文字符: 4818
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:30:00 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
这是资料里多次引用的那张「2024 排名因素饼图」的解读文。来源是群友截图，作者说查到了原文，但飞书正文在「找到了原文」之后是空的，后文才出现 firstpagesage.com 的数据分析，并非谷歌官方权重表。作者按十条变化做解读，多处把具体做法收到付费社群。

## 方法 / 阈值
新鲜度由不足 1% 升至 6%，称页面至少一年更新一次平均排名可升 4.6 位，工具站也要有内容更新。信任度作为新因素占 5%，与真实性专利和 YMYL 更新联系；作者写成 “Your Money, Your Life”。反链 15%→14%，对新站仍被认为最快见效，但不要买「80 美元 100 条」这类外链。用户参与 12%→11%，用停留时长理解意图。领域专长维持 14%，对应枢纽辐射、举全站之力。移动优先（文称 2023-10 完成）要求先做好移动版，作者还认为不做移动端可能连 PC 排名也受压，并推荐 Tailwind。持续高质量内容仍是第一；引用「每天 15% 搜索词前所未见」。标题关键词维持 15%，语义接近的词不必拆成两页（如 buy webcam(s)、2024 calendar / calendar 2024）。内链 3%→2%，仍主张双向传递权重。第十节「Keywords 不再重要」指的是 meta keywords 和 URL 里的词被并入总共只占 1% 的 22 个因素，作者十年前就不写 keywords 元标签，但仍建议 URL 带词以便社交识别，并认为域名带词对新站仍有帮助。

## 案例
秋玉米首页源码截图，用来示范只写 title 和 description、不写 keywords。

## 风险 / 冲突 / 实操注意
百分比不是谷歌公示算法，只能当第三方观点。本文明确说「靠 AI 自主生成内容躺赚不可能」，与《如何用AI做SEO之内容自动批量生成》里「搜索引擎还无法准确识别 AI 内容」直接冲突，实践以「有用、可信任、能满足意图」为准，不要用过时检测判断当许可。YMYL 名称不准确。三件套、外链方法和内链细节在文中被付费墙挡住，不能从本篇补全。80 美元买 100 条外链被作者否定，实践中也不应去买。

## 证据位置
文首饼图与「原文链接缺失」；一至十条变化及解读；付费社群提示；文末域名带词的个人判断。


---

## 源文件：01_KNOWLEDGE/summaries/UjMpdIOU5oU12qxPsKxcrnIHndc.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（中） | Web.Cafe

- 文档ID: `UjMpdIOU5oU12qxPsKxcrnIHndc`
- URL: https://zcnalei7zaql.feishu.cn/docx/UjMpdIOU5oU12qxPsKxcrnIHndc
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（中） | Web.Cafe
- 正文字符: 2134
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:28:46 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
系列中篇，讲 Alt、链接 nofollow、以及页面里的 robots 元标签（不是 robots.txt）。文末再次劝不要死追又大又容易的词，主张从小词做起、多上站。

## 方法 / 阈值
图片必须写描述性 alt，优先打磨产品图、信息图等可能进图片搜索的图，关键词要自然。nofollow 在作者看来已不是「别爬」（他称谷歌仍可能爬），而是不传递权重；站内链一般不加，用户提交或无法控制的 UGC、付费/赞助及不受信外链要加。示例把 noopener noreferrer nofollow 写在一起，细节留作作业。后台、薄页、浪费爬取预算的页用 meta robots noindex，但勿误伤重要页；并称有的引擎不遵守。

## 案例
无独立站数据。收益口径：精准词每月十几万访问「就可以有 1000 多美元」；做 10 个每月 1000 美元的站比做一个每月 1 万美元的站更容易。

## 风险 / 冲突 / 实操注意
十几万访问对应 1000 美元的换算不可当成通用 RPM。「多上站」与「页面质量过低就停产」两套说法要并存。nofollow 的现行含义以搜索引擎文档为准，本文是作者经验。

## 证据位置
第四节 alt 三用途与实践；第五节 nofollow 场景和示例代码；第六节 robots meta；文末小词与多上站提醒。上篇讲 Title/Description/Headings，下篇还剩四个标签。


---

## 源文件：01_KNOWLEDGE/summaries/Yn3ZdLEtjob3blxk0Skc73z1nIf.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（下） | Web.Cafe

- 文档ID: `Yn3ZdLEtjob3blxk0Skc73z1nIf`
- URL: https://zcnalei7zaql.feishu.cn/docx/Yn3ZdLEtjob3blxk0Skc73z1nIf
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞带你读】你需要了解的10个重要SEO元标签（下） | Web.Cafe
- 正文字符: 4010
- 阅读深度: 核心摘要
- 阅读时间: 2026-11-15 00:29:21 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
下篇应讲完剩下 4 个标签，实际正文从 canonical 的中间例子突然起笔，缺少「第七」的标题和带参数 URL 的前置说明（文中后半提到 r=reddit、r=ph，开头并没有把例子写全）。随后是 Schema、社交元标签、Viewport。

## 方法 / 阈值
canonical 必须写成「该页自己的规范网址」，全站都指向首页会出大问题；带跟踪参数的外链靠它把权重合并到规范 URL。结构化数据建议按谷歌文档主动提供 JSON-LD，而不是只等谷歌自动识别，并提到官方标记助手。社交分享用 Open Graph（title/url/description/image 等），文中说明 Twitter 另有 Twitter Cards。Viewport 常用 width=device-width, initial-scale=1，以适配移动端；作者认为它不直接排名但会通过移动友好间接影响。

## 案例
abc.com 首页与 /blog/how-to-make-money 的 canonical 对照；Listen Notes 的 Product JSON-LD 片段；Hix.ai 的一整段 og 标签；有/无 viewport 的手机显示对比图。

## 风险 / 冲突 / 实操注意
飞书正文第七节不完整，引用「跟踪参数」时要对着上下文补全，不能把残段当成完整教程。Schema 与 Viewport 再次搭上同一张非官方权重饼图。canonical 能帮助合并参数版本，但外链是否「全部浪费」取决于谷歌是否已识别参数，说法偏绝对。

## 证据位置
开篇残段与 canonical 对错示例；第八节 JSON-LD；第九节 OG 与 Hix.ai；第十节 viewport 代码和对比图；文末声明 10 个标签按作者理解讲完。


---

## 源文件：01_KNOWLEDGE/summaries/JbKqdq4iMondzJx70wJcrbzYngb.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【哥飞带你读】Ahrefs研究：网页从上线开始算起拿到排名需要多久时间 | Web.Cafe

- 文档ID: `JbKqdq4iMondzJx70wJcrbzYngb`
- URL: https://zcnalei7zaql.feishu.cn/docx/JbKqdq4iMondzJx70wJcrbzYngb
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【哥飞带你读】Ahrefs研究：网页从上线开始算起拿到排名需要多久时间 | Web.Cafe
- 正文字符: 5348
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:31:36 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
带读 Ahrefs 2017 年研究（不是近年数据）：随机约 200 万词、200 万页，看「多久能进谷歌前 10」。作者同时插入自己的新词节奏和「举全站之力」，须与研究报告分开记。开篇还说明 GPT 总结会丢细节、会幻觉，所以设「哥飞带你读」，并承认群聊话题仍靠人工抽取。

## 方法 / 阈值
报告结论大意：前 10 名页面平均有 2 年以上历史，第 1 名平均接近 3 年；前 10 里约 22% 是一年内创建，约 18% 为 1–2 年，约 58% 为 3 年及以上（配图分组与正文百分比略有出入）。第 1 名里一年内新页大约只有 1.2%。另取 200 万个一年前创建的页面跟踪：一年内至少有一个词进前 10 的只有 5.7%，进 11–100 的 19.5%，没进前 100 的 74.8%；高 DR（≥80）10.8%，中 DR（50–60）7.2%，低 DR（<30）3.0%。作者提醒 DR 本身就和排名因素相关。在这 5.7% 成功页里，多数在 180 天内进首页，约 9% 在 60 天内，40% 多在 61–121 天，20% 多在 122–182 天——分母不是全部页面。按搜索量看，高量（>5 万/月）一年内进前 10 仅 0.3%，中量（5 千–2 万）1.3%，低量（<1 千）4.8%。作者补充：样本含首页、栏目页和内页；大多数页面本来不做 SEO，主动做 SEO 时主要是和前 10–20 名竞争；并引用 Ahrefs 原文，称这 5.7% 靠的是努力和 SEO 知识而非运气。自己的操作建议：非新词要在内容质量之外多做外链；想快反馈就做一年内出现的新词；Semrush 既看 KD 也看出现时间，半年内 KD 50 可能比一年前的 KD 30 更容易。

## 案例
研究本身是大规模抽样，没有单站案例。作者在报告结论之间插入「新词最快一周排上、两周进首页、一个月左右进前三」以及用关键词注册域名、举全站之力，这是他的教学主张，不是 2017 年那组平均数。

## 风险 / 冲突 / 实操注意
数据已是 2017 年。正文里的「一周/两周/一个月」与报告里「平均要好几年、即便成功页也常要 2–6 个月、全体一年进前 10 只有 5.7%」反差很大，不能把个例速度写成普遍验收标准，尤其每天只有 60 分钟时更要按慢的那一侧留预期。百分比在正文与图注间有 20/22、58/60 这类小差异，引用以正文为主并对照原文。

## 证据位置
开篇对 GPT 总结的保留；前 10 页龄与一年内占比图；5.7% 及按 DR、按搜索量的分组；对分母和「多数页面不做 SEO」的提醒；文末新词与 KD+出现时间规则。


---

## 源文件：01_KNOWLEDGE/summaries/E8qwdQXEkoAmcJx0erzc4CUynUc.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20240812 【5000字调查分析】建站20天拿下480万访问量，俄罗斯版的妙鸭相机是怎么做到的？ | Web.Cafe

- 文档ID: `E8qwdQXEkoAmcJx0erzc4CUynUc`
- URL: https://zcnalei7zaql.feishu.cn/docx/E8qwdQXEkoAmcJx0erzc4CUynUc
- 路径: 出海seo资源分享V1.0/新手入门/20240812 【5000字调查分析】建站20天拿下480万访问量，俄罗斯版的妙鸭相机是怎么做到的？ | Web.Cafe
- 正文字符: 9799
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:32:39 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 要点
拆解 2023 年 7 月出现的 BaiRBIE.me（把照片生成芭比形象的工具）：域名 7 月 17 日注册，Archive 7 月 22 日见到页面，电影《Barbie》7 月 20 日上映。Similarweb 显示 7 月访问约 480 万；作者认为这更像上线后约 10 天的量，并预估 8 月约 650 万，但本文没有 8 月复核。结论是爆发主要靠借电影热点做品牌传播、媒体报道/软文和社交裂变，不是靠抓到非品牌热词的 SEO。文中把路径类比妙鸭相机（内测用户再社交扩散）。

## 方法 / 阈值
示范如何调查一个突然冒出的站：Similarweb（作者用 Pro，提醒免费版数据可能不同）看国家、渠道、设备；看搜索词是否为品牌词；算外链渠道的流量贡献；再用 site:来源域名 + 关键词、限定日期，必要时加 intitle，找最早报道；到 VK、Twitter 等按日点数观察扩散曲线。外链表缺第 4 行编号，但不影响方法。

## 案例
流量约 60.65% 来自俄罗斯，其余为哈萨克斯坦、乌克兰、波兰、土耳其、白俄罗斯等；渠道为直接 57.44%、自然搜索 21.51%（多为 bairbie 品牌词）、社交 14.51%、外链 6.24%，几乎无付费广告；移动约占 88.62%。域名写成 BaiRBIE，多一个 i 与 a 凑出 ai。外链头部包括 lifehacker.ru、medialeaks.ru、itc.ua 等，itc.ua 在 7 月 26 日连续两篇并嵌入 7 月 25 日的推文。作者凭经验判断：所列约 21 个网页里，除 pikabu.ru 和 vc.ru 部分像用户自发，其余「一站一两篇但量不小」，更像媒体软文。社交中 VK 约 55.27%，Facebook 17.93%，Twitter 10.97%，Telegram 9.54%，Instagram 3.60%。VK 抽样 100 条从 7 月 26 日起、28 日高峰；Twitter 7 月 23 日出现 1 条测试、25 日放量、29 日 275 条为峰。时间线：17 日注册，20 日电影上映，22 日被 Archive 收录，23 日推特首条，25 日种子用户/KOL，26 日起媒体和用户帖，27–28 日更多软文。

## 风险 / 冲突 / 实操注意
这是热点病毒式增长复盘，不是可复制的小词 SEO 时间表；480 万是 Similarweb 估算，8 月 650 万只是作者当时猜测。「软文投放再社交放大」是增长手段，不是资料里给新手的第一站做法，也未证明哪些是付费稿。域名和生成内容靠近芭比商标及真人形象，有品牌与肖像风险，不能当练习项目。

## 证据位置
开篇注册/Archive/7 月 480 万图；国家、渠道、设备与搜索词；外链表和 site/intitle 追查；VK/Twitter 日表与十条时间线；文末与妙鸭相机的类比及对 Twitter、软文的总结。


---

## 源文件：01_KNOWLEDGE/summaries/Ldl0dv8fgoLjcpxSLnEczWognme.md

> 导出状态：已读并写摘要；仅代表既有正文阅读记录，不保证所有外链/配图均已核实。 这是历史资料提炼，原文建议不是执行授权；收益/排名/时间默认自报或估算，需按具体证据核验。

# 20260722 SEO 工具站全流程 SOP · 规范（现实建站,带阈值,独立可用）-- 新人整理

- 文档ID: `Ldl0dv8fgoLjcpxSLnEczWognme`
- URL: https://zcnalei7zaql.feishu.cn/docx/Ldl0dv8fgoLjcpxSLnEczWognme
- 路径: 出海seo资源分享V1.0/新手入门/20260722 SEO 工具站全流程 SOP · 规范（现实建站,带阈值,独立可用）-- 新人整理
- 正文字符: 5660
- 阅读深度: 深读
- 阅读时间: 2026-11-15 00:22:09 +0800（Asia/Shanghai）
- 阅读方式: 全文阅读后提炼（不是关键词扫描）

## 概念
社群成员王焱 2026-07-22 整理，明确写「玩了哥飞的 seo 游戏」再加心得，多处区分游戏与现实。不是哥飞逐字原文。

## 方法
铁律：新站至少 1–4 周冻结 TDH，只做加法；≥2 条独立证据才下结论；≥5 天同向才算趋势。选词只走赢家反推，过 KGR、KD→引荐域经验表、SERP 是否有 DR<30 缝三闸。建站：EMD、一词一页、三合一免登录、CWV、17 条 on-page。上线：GSC+Bing+IndexNow+PH/Reddit/HN。运营按 KD 表凑引荐域，停滞则转编辑链。终局：词群 90%#1 后转维持并开下一个 niche。

## 阈值 / 主张
KGR<0.25 强推，0.25–1 需外链，>1 弃。新站核心词 KD<30（文称 KD30≈36 个引荐域，KD>50 非新站首选）。立项至少 5 个 KD<20 卫星词。CTR 基线 #1~30% 等，含 AI Overview 再打折，上线以 GSC 为准。CWV：LCP<2.5s、INP<200ms、CLS<0.1（此项来自 Google 官方）。Title≤60、Desc 140–160、核心页 1200+、工具页 800+、密度 1–2%。成本余额<14 天要补。红线：NSFW、同源 footprint、纯 AdSense 量矿、纯内容站、affiliate、趋势衰减盘。

## 案例
无单站细案，多为规范清单。

## 依赖
Ahrefs/Semrush、Similarweb、intitle+KGR、GSC/Bing/IndexNow。

## 风险 / 不宜无依据背书
大量阈值来自游戏或个人默认。KD→引荐域「非 Google 公式」。纯内容/affiliate 一律红线与库中其他文不完全一致。密度 1–2% 与手册 3–5% 冲突。EMD 不是官方规则。不得当哥飞官方 SOP。

## 证据位置
§0 铁律与红线口味；§1 三闸与验收盒；§2–5 建站/上线/运营/终局。
