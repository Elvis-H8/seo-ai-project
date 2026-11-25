# 三个候选：研究现状，不是已选项目

记录来源：既有学习页的2026-11-15上午（Asia/Shanghai）研究说明；本次导出成功读取该页，但没有重新访问以下外部页面。下面“当时打开”只是历史观察。月搜索量、KD、商业空间一律未知；公开索引不是指定地区Google前十。PTO只是有条件第一候选，用户尚未选择，可三个都不选。

## A. PTO计提与余额估算
- 用户任务：按自己公司的政策数字，算每发薪周期计提与余额/入职折算。只做算术，不给州法、病假、税务或离职兑付判断。
- 候选词：pto accrual calculator；pto per pay period；prorated pto calculator new hire。
- 需求信号（历史当时打开）：[用户询问在线工具/表格](https://www.reddit.com/r/personalfinance/comments/pjs5x6/pto_accrual_calculator/)；内容说26个发薪周期下如何算一年剩余假。单帖不证明市场规模。
- 竞品（历史当时打开）：[Paycor](https://www.paycor.com/resource-center/tools/pto-calculator/)、[TimeCamp](https://www.timecamp.com/helpers/pto-accrual-calculator/)、[SmartOvertime](https://smartovertime.com/pto-accrual-calculator)、[Spot Check Tools](https://spotchecktools.com/payroll/pto-accrual/)、[OrgaNice](https://organice.app/prorated-pto-calculator/)。部分已有余额、上限、入职折算和本地处理；不是空白市场。
- 最小范围：年度小时数、全年周期数、已完成周期、已用时数→计提率/累计/余额。结转、上限、按天或整月入职折算须先约定顺序，未支持的明确拒绝，不一次做全。
- 黄金例子：年度80小时/26周期=每期约3.076923小时，显示3.08但内部不逐期舍入；13期累计40小时，已用8小时得32小时（无结转/上限情形）。
- 假设差异：清晰口径+可复算明细+无获客表单；竞品可能已覆盖，必须实测。
- 停止：算不准公开例题、无法解释口径，或现有页已完整覆盖且找不到诚实改进。

## B. 字幕时间轴校正
- 任务：字幕恒定偏移做平移；逐渐漂移用两个锚点做线性变换；必要时SRT/VTT转换。只处理有权使用的用户字幕，不抓取他人字幕。
- 词：srt shifter；fix out of sync subtitles srt；subtitle drift fixer。
- 历史工具页观察：[PlainScribe](https://www.plainscribe.com/tools/subtitle-shifter)有本地平移；[The Boring Tools](https://theboringtools.com/subtitle-sync/)和[anysweb](https://anysweb.jp/subtitle-time-rescaler/)已做拉伸/双锚点；[Subconverter](https://subconverter.com/subtitle-fps-drift-fixer-online)页面称最终下载有服务器校验，不能一概称全本地。
- 讨论帖子曾出现500或正文已删，不能当已读用户正文。需求强度主要来自工具供给信号，待补独立任务证据。
- 最小范围可先只做平移+预览+下载；双锚点/帧率模式经验证再加，不做转写、OCR、音频自动对齐和完整ASS样式。
- 黄金例子：1.000→2.000秒偏移+1秒；双锚点t=10→12、t=110→122，变换t'=1.1t+1，t=60→67。负时间如何处理必须写明并测试，不能静默损坏时长。
- 停止：无法证明本地处理、输出损坏或同功能已做完而无具体改进。

## C. RRULE生成、解释与日期预览
- 任务：开发者写重复规则时理解BYDAY/BYSETPOS等，不是替用户创建真实日历事件。
- 词：rrule generator；rrule explainer；last friday of every month rrule。
- 历史已打开提问：[BYDAY与BYSETPOS](https://stackoverflow.com/questions/24943832/rrule-explanaiton-using-byday-and-bysetpos)、[每月第二个周一/三/五](https://stackoverflow.com/questions/55516245/rrule-to-get-the-2nd-monday-wednesday-and-friday-of-the-month-for-every-month)。浏览量只是当时页面显示，不换算搜索量。
- 规范入口：[RFC5545](https://www.rfc-editor.org/rfc/rfc5545)。竞品：[kloq](https://www.kloq.dev/tools/rrule-builder)、[Edge Tools](https://app.edgetools.io/rrule)、[Jagodana](https://www.jagodana.com/work/rrule-generator)已支持生成/解释/预览，差异待证。
- 最小范围：明确DTSTART、选定频率/间隔/星期、COUNT或UNTIL，展示下N次；拒绝COUNT与UNTIL并存。先支持可测子集，时区/DST/复杂组合不作未测试保证。
- 黄金测试：固定无DST时区，DTSTART=2026-01-05 09:00，每周一COUNT=3→1月5/12/19；BYDAY=2MO,2WE,2FR与BYDAY=MO,WE,FR;BYSETPOS=2含义不同，不可混用。
- 停止：RFC例子对不上或无法解释时区边界；竞品完整满足同一任务而无法说明新增价值。

## 当前比较
A适合练清楚公式，但政策误解风险更高；B容易用自有样例验收，但既有工具很完整；C适合开发者，但规则准确性门槛高。先比任务证据、实测缺口、准确可验收与兴趣，别比编造的流量。
下一步：见DAY_01。任何推荐都须接受反证，最终由Elvis选择。
