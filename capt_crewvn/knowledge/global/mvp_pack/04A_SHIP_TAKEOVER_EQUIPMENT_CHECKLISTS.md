# CAPT CREWVN — SHIP TAKEOVER EQUIPMENT / SYSTEM CHECKLISTS

Status: GENERIC CAPT CREWVN FRAMEWORK. Extension of `04_SHIP_TAKEOVER_PROCEDURE.md`.

This file is NOT a company procedure, maker instruction or Class/Flag requirement. Where a company SMS/PMS or maker manual exists, it governs and these checklists must be mapped to it.

## How to use

1. Use with 04 §1 levels, §2 status codes, §5 test preconditions, §6 access restriction, §7 spares, §8 bunkers, §9 defect class.
2. Each line has a TARGET level (the highest level that line asks for). Record the level actually REACHED. A line targeted TESTED but only seen is reported as SEEN + NT, not as satisfactory.
3. No set point, capacity, pressure, time or limit is given here. Every reference value is TBD and must come from the maker manual, approved drawings, trial data, company SMS or applicable regulation (verified current text).
4. Alarm, trip and safety-device tests: only by the approved test method (test button, simulation, test device) and by authorized ship staff. Never by bypassing, jumpering or creating an unsafe condition.
5. Enclosed spaces (holds, tanks, chain locker, void spaces): entry only with permit, ventilation and atmosphere testing per company SMS.
6. Responsible rank shown is typical practice (Capt Crewvn practical experience), not a company assignment. Verify against company SMS.
7. Every defect line → Template 1 (09). Every equipment → Template 2 (09) summary.

Chinese system names (中文) are a Claude draft using pack 02 terms where available; not yet checked against an authoritative Chinese source. Engineer rank convention: owner decision 2026-10-01, Máy hai = Second Engineer = 大管轮.

## Level codes

SEEN = L1 · INSPECTED = L2 · DOC = L3 Document verified · TESTED = L4 Function tested · PERF = L5 Performance verified

## Status codes

S · D · NT · NA · NV · FVR (see 04 §2)

## Common identification block (fill for every checklist)

```
Vessel:                 IMO:
Equipment code (PMS):   TBD
Maker / Model / Serial: TBD
Running hours:          TBD (source: ...)
Location / No. of units:
Date / time:
Inspected by (rank):    Witnessed by (rank / side):
```

## Common closing block (fill for every checklist)

```
Highest level reached:  ☐ SEEN ☐ INSPECTED ☐ DOC ☐ TESTED ☐ PERF
Overall status:         ☐ S ☐ D ☐ NT ☐ NA ☐ NV ☐ FVR
Defect class (04 §9):   ☐ A ☐ B ☐ C ☐ D   Defect report refs:
Access restriction (04 §6): ☐ None ☐ Yes → record
Critical spares checked (04 §7): ☐ Yes ☐ No  Discrepancy refs:
Evidence refs (photo / reading / document):
Required follow-up:
Signed (inspector):        Acknowledged (ship / seller rep):
```

## Index

**DECK (17)**

- D01 Hull external, draft marks and load line marks / Vỏ tàu bên ngoài, thước nước, dấu mạn khô / 船体外部、吃水标志及载重线标志
- D02 Cargo holds / Hầm hàng / 货舱
- D03 Hatch covers and coamings / Nắp hầm hàng và thành quây / 舱盖及舱口围
- D04 Hatch cover hydraulic / drive system / Hệ thống thủy lực / truyền động nắp hầm / 舱盖液压/驱动系统
- D05 Cargo cranes, derricks and grabs / Cẩu hàng, cần cẩu, gàu ngoạm / 货物起重机、吊杆及抓斗
- D06 Windlass, anchors, cables and chain locker / Tời neo, neo, xích neo, hầm xích / 锚机、锚、锚链及锚链舱
- D07 Mooring winches and mooring arrangements / Tời và hệ thống chằng buộc / 系泊绞车及系泊设备
- D08 Tanks, sounding pipes, air pipes, ventilators and closing appliances / Két, ống đo, ống thông hơi, quạt gió và thiết bị đóng kín / 液舱、测深管、空气管、通风筒及关闭装置
- D09 Access: accommodation ladder, gangway and pilot boarding arrangements / Thang mạn, cầu thang lên tàu, thang hoa tiêu / 舷梯、登轮梯及引航员登乘装置
- D10 Lifeboats, rescue boat, davits and winches / Xuồng cứu sinh, xuồng cấp cứu, cần và tời / 救生艇、救助艇、吊艇架及绞车
- D11 Liferafts and personal life-saving appliances / Bè cứu sinh và trang bị cứu sinh cá nhân / 救生筏及个人救生设备
- D12 Fire hydrants, hoses, portable extinguishers and firefighter's outfits / Họng cứu hỏa, vòi, bình chữa cháy xách tay, trang bị lính cứu hỏa / 消防栓、水龙带、手提式灭火器及消防员装备
- D13 Fixed fire-extinguishing system and remote closures / Hệ thống chữa cháy cố định và thiết bị đóng từ xa / 固定式灭火系统及遥控关闭装置
- D14 Bridge navigation equipment, charts and publications / Thiết bị hàng hải buồng lái, hải đồ và ấn phẩm / 驾驶台航行设备、海图及航海出版物
- D15 GMDSS and radio equipment / Thiết bị GMDSS và vô tuyến điện / GMDSS及无线电设备
- D16 Deck pollution prevention: SOPEP equipment, scuppers and garbage / Phòng chống ô nhiễm trên boong: SOPEP, lỗ thoát, rác / 甲板防污染：SOPEP设备、排水孔及垃圾
- D17 Loading computer, stability and cargo documents / Máy tính xếp hàng, ổn định và hồ sơ hàng hóa / 装载计算机、稳性及货物文件

**ENGINE (21)**

- E01 Main engine / Máy chính / 主机
- E02 Turbochargers, scavenge air and exhaust system / Tua bin tăng áp, khí quét và hệ thống khí xả / 废气涡轮增压器、扫气及排气系统
- E03 Shafting, stern tube, thrust bearing and propeller / Hệ trục, ống bao trục, ổ chặn, chân vịt / 轴系、艉轴管、推力轴承及螺旋桨
- E04 Diesel generators / Máy phát điện diesel / 柴油发电机组
- E05 Boilers and exhaust gas economizer / Nồi hơi và nồi hơi khí xả / 锅炉及废气经济器
- E06 Air compressors and air receivers / Máy nén khí và chai gió / 空气压缩机及空气瓶
- E07 Fuel oil system / Hệ thống nhiên liệu / 燃油系统
- E08 Fuel oil and lube oil purifiers / Máy lọc dầu đốt và dầu nhờn / 燃油及滑油分油机
- E09 Lube oil systems / Hệ thống dầu nhờn / 滑油系统
- E10 Cooling water systems (sea water, fresh water, central cooling) / Hệ thống nước làm mát / 冷却水系统（海水、淡水、中央冷却）
- E11 Fresh water generator and domestic water / Máy sinh hoạt nước ngọt và nước sinh hoạt / 造水机及生活用水
- E12 Steering gear / Máy lái / 舵机
- E13 Bilge system and bilge pumps / Hệ thống và bơm la canh / 舱底水系统及舱底泵
- E14 Ballast pumps and engine-room ballast system / Bơm và hệ thống ballast buồng máy / 压载泵及机舱压载系统
- E15 Ballast water management system (BWMS) / Hệ thống xử lý nước dằn (BWMS) / 压载水管理系统（BWMS）
- E16 Oily water separator, oil content meter, bilge and sludge tanks / Máy phân ly nước dầu, thiết bị đo hàm lượng dầu, két la canh và cặn / 油水分离器、油分浓度计、舱底水舱及油渣舱
- E17 Incinerator and sewage treatment plant / Lò đốt rác và hệ thống xử lý nước thải / 焚烧炉及生活污水处理装置
- E18 Fire pumps and emergency fire pump / Bơm cứu hỏa và bơm cứu hỏa sự cố / 消防泵及应急消防泵
- E19 Engine room fire safety arrangements / Bố trí an toàn cháy buồng máy / 机舱防火安全布置
- E20 Refrigeration and air-conditioning plant / Hệ thống lạnh và điều hòa / 冷藏及空调装置
- E21 Tank soundings and ROB measurement for oils / Đo két và tính ROB dầu / 油舱测深及存油量（ROB）计量

**ETO / ELECTRICAL (11)**

- T01 Main switchboard and generator protection / Bảng điện chính và bảo vệ máy phát / 主配电板及发电机保护
- T02 Emergency generator and emergency switchboard / Máy phát sự cố và bảng điện sự cố / 应急发电机及应急配电板
- T03 Batteries, UPS and emergency lighting / Ắc quy, UPS và đèn sự cố / 蓄电池、UPS及应急照明
- T04 Alarm monitoring system / UMS / Hệ thống giám sát báo động / UMS / 报警监测系统/无人机舱（UMS）
- T05 Main engine remote control and safety system / Hệ thống điều khiển từ xa và an toàn máy chính / 主机遥控及安全系统
- T06 Fire detection, general alarm and public address / Báo cháy, báo động chung và truyền thanh / 火灾探测、通用报警及广播系统
- T07 Electric motors, starters and insulation / Động cơ điện, khởi động từ và cách điện / 电动机、启动器及绝缘
- T08 Internal communication / Thông tin nội bộ / 船内通信
- T09 Deck machinery electrical drives / Truyền động điện máy boong / 甲板机械电力驱动
- T10 Navigation lights, signals and searchlights / Đèn hành trình, tín hiệu và đèn pha / 航行灯、信号灯及探照灯
- T11 Remote valve control, tank gauging and level / water ingress alarms / Điều khiển van từ xa, đo két và báo động mức nước / 遥控阀、液位遥测及液位/进水报警


---

# DECK


## D01 — Hull external, draft marks and load line marks
### Vỏ tàu bên ngoài, thước nước, dấu mạn khô | 船体外部、吃水标志及载重线标志

Typical responsible rank: Chief Officer (verify against company SMS)

**Safety before inspection / test:**
- Inspect from quay, boat or launch only under company procedure for overside work.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D01.1 | Last dry-docking / hull survey record and Class hull items reviewed | DOC | | | | |
| D01.2 | Recorded hull damage, temporary repairs or doublers reviewed | DOC | | | | |
| D01.3 | Draft marks forward / midship / aft legible both sides | SEEN | | | | |
| D01.4 | Load line marks and deck line legible both sides | SEEN | | | | |
| D01.5 | Visible shell plating condition: indentations, cracks, heavy corrosion, coating breakdown | SEEN | | | | |
| D01.6 | Fresh localized painting or welding on shell recorded with location | SEEN | | | | |
| D01.7 | Overboard discharges and sea-chest gratings visible above waterline | SEEN | | | | |
| D01.8 | Name, port of registry and IMO number markings present | INSPECTED | | | | |
| D01.9 | Draft readings taken and compared with loading computer / cargo documents | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Draft F / M / A port & stbd (m) | | TBD | |
| Sea condition at reading | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Doublers or inserts not in repair history
- Rust streaks from shell at specific frames
- Paint fresh only around one area

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D02 — Cargo holds
### Hầm hàng | 货舱

Typical responsible rank: Chief Officer (verify against company SMS)

**Safety before inspection / test:**
- Enclosed-space entry only with permit, ventilation and atmosphere testing per company SMS.
- Use safe access only; do not climb damaged ladders.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D02.1 | Hold survey / thickness measurement records and Class notations reviewed | DOC | | | | |
| D02.2 | Previous cargoes and hold cleaning records reviewed | DOC | | | | |
| D02.3 | Frames, brackets, side shell, hopper and topside tank plating: deformation, cracks, corrosion | SEEN | | | | |
| D02.4 | Tank top condition: indentations, grab damage, pitting | SEEN | | | | |
| D02.5 | Bulkheads, stools and corrugations condition | SEEN | | | | |
| D02.6 | Access ladders, platforms and handrails secured and not wasted | INSPECTED | | | | |
| D02.7 | Bilge wells: strum boxes / covers present and clean | INSPECTED | | | | |
| D02.8 | Hold lighting, ventilation openings and fixtures | INSPECTED | | | | |
| D02.9 | Hold bilge suction tested by pumping out where authorized | TESTED | | | | |
| D02.10 | Water ingress / bilge level alarms tested by approved method where fitted (see T11) | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Coating condition per hold (description) | | TBD | |
| Measured thickness where survey available (ref. report) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Fresh welding on frames
- Cargo residue hiding tank top
- Wet patches or rust streaks under hatch coaming

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D03 — Hatch covers and coamings
### Nắp hầm hàng và thành quây | 舱盖及舱口围

Typical responsible rank: Chief Officer (verify against company SMS)

**Safety before inspection / test:**
- Keep clear of moving panels and hydraulic lines during opening/closing.
- Do not remain under open panels.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D03.1 | Maker manual, maintenance and hose-test / ultrasonic test records reviewed | DOC | | | | |
| D03.2 | Panels: plating, stiffeners, top plating deformation, corrosion | SEEN | | | | |
| D03.3 | Rubber packing: continuity, hardening, permanent set, missing sections | INSPECTED | | | | |
| D03.4 | Compression bars, cleats, wedges, cross-joint seals | INSPECTED | | | | |
| D03.5 | Coamings, coaming top plate and drain channels / non-return valves | INSPECTED | | | | |
| D03.6 | Wheels, rails, stoppers and securing devices | INSPECTED | | | | |
| D03.7 | Opening and closing operated in normal sequence | TESTED | | | | |
| D03.8 | Weathertightness verified by hose test or ultrasonic test (method per company/maker) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Operating time open/close per hatch (observed) | | TBD | |
| Weathertightness test result per hatch (ref. report) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- New packing on one cover only
- Silicone or tape on cross-joints
- Rust stains inside coaming below joints

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D04 — Hatch cover hydraulic / drive system
### Hệ thống thủy lực / truyền động nắp hầm | 舱盖液压/驱动系统

Typical responsible rank: Chief Officer / Engineer in charge (verify against company SMS)

**Safety before inspection / test:**
- Verify isolation before touching hydraulic components.
- Pressurized hydraulic oil: no hands near leaks under pressure.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D04.1 | Hydraulic oil analysis / change history reviewed | DOC | | | | |
| D04.2 | Power pack: oil level, leakage, filter indicators, motor condition | INSPECTED | | | | |
| D04.3 | Hoses and pipes: chafing, ageing, leaks, temporary clamps | INSPECTED | | | | |
| D04.4 | Cylinders: rod condition, seal leakage | INSPECTED | | | | |
| D04.5 | Pumps started; each hatch operated | TESTED | | | | |
| D04.6 | Local and remote controls / emergency stop tested | TESTED | | | | |
| D04.7 | System pressure during operation compared with maker value (maker value: TBD per manual) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Working pressure (bar) | | TBD | |
| Oil temperature | | TBD | |
| Motor current (A) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Oil-soaked rags around fittings
- Drip trays recently emptied
- Hoses of different age on same unit

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D05 — Cargo cranes, derricks and grabs
### Cẩu hàng, cần cẩu, gàu ngoạm | 货物起重机、吊杆及抓斗

Typical responsible rank: Chief Officer / ETO / Engineer in charge (verify against company SMS)

**Safety before inspection / test:**
- Lifting tests only within certified SWL and under company procedure.
- No one under suspended load.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D05.1 | Cargo gear register / certificates and periodic test records reviewed | DOC | | | | |
| D05.2 | Wire rope certificates and renewal history reviewed | DOC | | | | |
| D05.3 | Structure, pedestal, jib, slewing ring area: cracks, corrosion | SEEN | | | | |
| D05.4 | Wires: broken strands, kinks, corrosion, lubrication, end terminations | INSPECTED | | | | |
| D05.5 | Sheaves, hooks, swivels, SWL markings | INSPECTED | | | | |
| D05.6 | Limit switches and cut-outs present and undamaged | INSPECTED | | | | |
| D05.7 | Hoist, luff, slew operated through range | TESTED | | | | |
| D05.8 | Limit switches / emergency stop tested in operation | TESTED | | | | |
| D05.9 | Grab opening/closing tested where fitted | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Hoist / luff / slew motor current (A) | | TBD | |
| Hydraulic pressure where applicable | | TBD | |
| Brake slip observed (Y/N) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Limit switch tied or taped
- Fresh grease only on visible sheaves
- Unusual noise at slewing ring

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D06 — Windlass, anchors, cables and chain locker
### Tời neo, neo, xích neo, hầm xích | 锚机、锚、锚链及锚链舱

Typical responsible rank: Chief Officer / Bosun (verify against company SMS)

**Safety before inspection / test:**
- Chain locker is an enclosed space: permit and atmosphere testing before entry.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D06.1 | Anchor / cable certificates and cable renewal or gauging records reviewed | DOC | | | | |
| D06.2 | Windlass: brake linings, gear, foundations, bolts | INSPECTED | | | | |
| D06.3 | Chain stoppers / compressors and securing | INSPECTED | | | | |
| D06.4 | Anchors and visible cable: wear, missing studs, shackles marked | INSPECTED | | | | |
| D06.5 | Hawse pipe, spurling pipe covers | INSPECTED | | | | |
| D06.6 | Chain locker: bitter end, drainage, condition | INSPECTED | | | | |
| D06.7 | Windlass run in both directions, clutch engaged/disengaged | TESTED | | | | |
| D06.8 | Brake holding observed during operation | TESTED | | | | |
| D06.9 | Chain locker bilge / drainage tested where fitted | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Motor current / hydraulic pressure | | TBD | |
| Cable wear measurements where taken (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- New paint on cable marking only
- Brake band adjustment at end of travel
- Water in chain locker

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D07 — Mooring winches and mooring arrangements
### Tời và hệ thống chằng buộc | 系泊绞车及系泊设备

Typical responsible rank: Chief Officer / 2/O / Bosun (verify against company SMS)

**Safety before inspection / test:**
- Snap-back zones: keep clear during any line test.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D07.1 | Mooring line certificates, mooring plan and brake test records reviewed | DOC | | | | |
| D07.2 | Winch brakes, drums, foundations | INSPECTED | | | | |
| D07.3 | Mooring lines / wires: condition, certificates matched to lines | INSPECTED | | | | |
| D07.4 | Fairleads, rollers, bollards, chocks: free turning, wear, cracks | INSPECTED | | | | |
| D07.5 | Each winch run in both directions | TESTED | | | | |
| D07.6 | Brake holding capacity verified by brake test (method and value per maker/company: TBD) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Motor current / hydraulic pressure | | TBD | |
| Brake test result (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Seized rollers
- Lines without traceable certificate
- Grooved fairleads

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D08 — Tanks, sounding pipes, air pipes, ventilators and closing appliances
### Két, ống đo, ống thông hơi, quạt gió và thiết bị đóng kín | 液舱、测深管、空气管、通风筒及关闭装置

Typical responsible rank: Chief Officer (verify against company SMS)

**Safety before inspection / test:**
- Ballast and void tanks are enclosed spaces: permit and atmosphere testing before entry.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D08.1 | Ballast tank inspection / coating records reviewed | DOC | | | | |
| D08.2 | Air pipe heads: floats/discs, gauze screens, closing devices, markings | INSPECTED | | | | |
| D08.3 | Ventilators: closing flaps, gaskets, operating handles | INSPECTED | | | | |
| D08.4 | Sounding pipes: caps, threads, markings | INSPECTED | | | | |
| D08.5 | Weathertight doors and manhole covers: gaskets, dogs | INSPECTED | | | | |
| D08.6 | Closing devices operated | TESTED | | | | |
| D08.7 | Tank internal inspection where accessible and authorized | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Coating condition per tank (description) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Air pipe float seized or missing
- Painted-over closing devices
- Tank never inspected per records

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D09 — Access: accommodation ladder, gangway and pilot boarding arrangements
### Thang mạn, cầu thang lên tàu, thang hoa tiêu | 舷梯、登轮梯及引航员登乘装置

Typical responsible rank: Chief Officer / 2/O (verify against company SMS)

**Safety before inspection / test:**
- Test ladders and winches under supervision; nobody on the ladder during load or winch tests.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D09.1 | Maintenance and load test records, pilot ladder certificate and service history reviewed | DOC | | | | |
| D09.2 | Accommodation ladder structure, treads, stanchions, rope, safety net | INSPECTED | | | | |
| D09.3 | Davits / winch, wires, sheaves, limit switches | INSPECTED | | | | |
| D09.4 | Pilot ladder: steps, side ropes, spreaders, securing points, markings | INSPECTED | | | | |
| D09.5 | Pilot boarding area: lighting, lifebuoy, stanchions, handholds | INSPECTED | | | | |
| D09.6 | Accommodation ladder lowered and recovered | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Winch current / pressure | | TBD | |
| Wire condition (description) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Pilot ladder without traceable history
- Shackle pins not secured

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D10 — Lifeboats, rescue boat, davits and winches
### Xuồng cứu sinh, xuồng cấp cứu, cần và tời | 救生艇、救助艇、吊艇架及绞车

Typical responsible rank: 2/O or designated officer / Engineer for engines (verify against company SMS)

**Safety before inspection / test:**
- Lowering and release tests only by crew under company procedure and maker instructions.
- Inspector does not operate release gear.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D10.1 | Servicing records by service provider, inspection and drill records reviewed | DOC | | | | |
| D10.2 | Boat hull, fittings, inventory against list | INSPECTED | | | | |
| D10.3 | On-load / off-load release gear condition and markings | INSPECTED | | | | |
| D10.4 | Davit structure, wires, sheaves, brake, limit switches | INSPECTED | | | | |
| D10.5 | Lifeboat / rescue boat engine started (ahead/astern) per routine | TESTED | | | | |
| D10.6 | Boat lowered and recovered where authorized | TESTED | | | | |
| D10.7 | Davit winch motor operated | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Engine running observation | | TBD | |
| Inventory shortages (list) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Service record overdue
- Release gear painted over
- Engine starts only after repeated attempts

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D11 — Liferafts and personal life-saving appliances
### Bè cứu sinh và trang bị cứu sinh cá nhân | 救生筏及个人救生设备

Typical responsible rank: 2/O (verify against company SMS)

**Safety before inspection / test:**
- No inflation tests onboard; servicing is by approved station.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D11.1 | Liferaft and HRU service dates, certificates reviewed | DOC | | | | |
| D11.2 | Liferaft stowage, painter, HRU fitted correctly | INSPECTED | | | | |
| D11.3 | Lifebuoys: lights, smoke signals, lines, markings, count vs plan | INSPECTED | | | | |
| D11.4 | Lifejackets: count vs plan, lights, whistles, condition | INSPECTED | | | | |
| D11.5 | Immersion suits / thermal protective aids: count, condition, service record | INSPECTED | | | | |
| D11.6 | Pyrotechnics: count and expiry dates | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Quantities found vs required by plan (list) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Expired pyrotechnics
- HRU wrongly rigged
- Quantities differ from muster/fire plan

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D12 — Fire hydrants, hoses, portable extinguishers and firefighter's outfits
### Họng cứu hỏa, vòi, bình chữa cháy xách tay, trang bị lính cứu hỏa | 消防栓、水龙带、手提式灭火器及消防员装备

Typical responsible rank: Officer in charge of FFA (per company SMS) (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D12.1 | Fire control plan and FFA maintenance records reviewed | DOC | | | | |
| D12.2 | Hydrants: valves free, handwheels, spindles | INSPECTED | | | | |
| D12.3 | Hoses and nozzles: count vs fire plan, condition, couplings | INSPECTED | | | | |
| D12.4 | Portable extinguishers: count, location vs plan, service dates | INSPECTED | | | | |
| D12.5 | Firefighter's outfits and breathing apparatus: count, cylinder pressures, service | INSPECTED | | | | |
| D12.6 | EEBDs: count, location, service | INSPECTED | | | | |
| D12.7 | Fire main pressurized and hydrants tested on deck (see E18) | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Pressure at hydrants during test | | TBD | |
| BA cylinder pressures | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Hoses missing at stations
- BA cylinders below full
- Valve spindles seized

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D13 — Fixed fire-extinguishing system and remote closures
### Hệ thống chữa cháy cố định và thiết bị đóng từ xa | 固定式灭火系统及遥控关闭装置

Typical responsible rank: Chief Engineer / Chief Officer (per SMS) (verify against company SMS)

**Safety before inspection / test:**
- NEVER release fixed system for test. Inspection is visual/document only.
- Release cabinets must not be opened without authorization.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D13.1 | Service provider records (cylinder weighing / level checks, hose tests) reviewed | DOC | | | | |
| D13.2 | Cylinder room: cylinders secured, manifold, pilot lines, safety pins status | INSPECTED | | | | |
| D13.3 | Release station: instructions posted, keys, alarms | INSPECTED | | | | |
| D13.4 | Fire dampers and ventilation closures: markings, operation handles | INSPECTED | | | | |
| D13.5 | Fire dampers operated where authorized | TESTED | | | | |
| D13.6 | Pre-discharge alarm tested by approved method without release (where possible) | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Quantity per service report (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Service record overdue
- Pilot line disconnected
- Dampers seized open

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D14 — Bridge navigation equipment, charts and publications
### Thiết bị hàng hải buồng lái, hải đồ và ấn phẩm | 驾驶台航行设备、海图及航海出版物

Typical responsible rank: Master / 2/O (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D14.1 | Equipment list, annual / service reports and error logs reviewed | DOC | | | | |
| D14.2 | ECDIS / chart and publication update status reviewed | DOC | | | | |
| D14.3 | Radars / ARPA: performance, heading and speed inputs | TESTED | | | | |
| D14.4 | ECDIS: sensor inputs, alarms, backup arrangement | TESTED | | | | |
| D14.5 | Gyro compass and repeaters; magnetic compass and deviation record | TESTED | | | | |
| D14.6 | Autopilot and changeover to hand steering | TESTED | | | | |
| D14.7 | AIS, echo sounder, speed log, GNSS | TESTED | | | | |
| D14.8 | BNWAS and VDR status indication | TESTED | | | | |
| D14.9 | Daylight signalling lamp, sound signals, flags | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Gyro error (deg) | | TBD | |
| Compass deviation (ref. card) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Persistent alarms acknowledged without action
- Sensor fault on ECDIS ignored
- Equipment switched off 'because faulty'

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D15 — GMDSS and radio equipment
### Thiết bị GMDSS và vô tuyến điện | GMDSS及无线电设备

Typical responsible rank: Master / designated GMDSS operator (verify against company SMS)

**Safety before inspection / test:**
- No live distress transmission for testing. Test only per equipment test mode.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D15.1 | Radio log, shore-based maintenance / survey reports reviewed | DOC | | | | |
| D15.2 | MF/HF and VHF DSC routine tests | TESTED | | | | |
| D15.3 | Inmarsat / satellite terminal test | TESTED | | | | |
| D15.4 | EPIRB and SART: expiry dates, HRU, battery dates | INSPECTED | | | | |
| D15.5 | Portable VHF (GMDSS) batteries and test | TESTED | | | | |
| D15.6 | Reserve source of energy / radio batteries changeover | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Battery voltage on load where measured | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Expired EPIRB battery or HRU
- Radio log not maintained

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D16 — Deck pollution prevention: SOPEP equipment, scuppers and garbage
### Phòng chống ô nhiễm trên boong: SOPEP, lỗ thoát, rác | 甲板防污染：SOPEP设备、排水孔及垃圾

Typical responsible rank: Chief Officer (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D16.1 | Garbage record book and garbage management plan reviewed | DOC | | | | |
| D16.2 | SOPEP locker inventory vs list | INSPECTED | | | | |
| D16.3 | Scupper plugs available and fitting | INSPECTED | | | | |
| D16.4 | Save-alls / drip trays around deck machinery and vents | INSPECTED | | | | |
| D16.5 | Garbage segregation and storage | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Inventory shortages (list) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Oil stains at scuppers
- Empty SOPEP locker

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## D17 — Loading computer, stability and cargo documents
### Máy tính xếp hàng, ổn định và hồ sơ hàng hóa | 装载计算机、稳性及货物文件

Typical responsible rank: Chief Officer (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| D17.1 | Approved stability booklet, loading manual onboard | DOC | | | | |
| D17.2 | Loading computer approval and periodic test record reviewed | DOC | | | | |
| D17.3 | Loading computer test condition run and compared with approved test condition | TESTED | | | | |
| D17.4 | Grain / cargo securing / other cargo-specific documents as applicable | DOC | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Test condition result (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Software version differs from approval
- No record of periodic test

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


---

# ENGINE


## E01 — Main engine
### Máy chính | 主机

Typical responsible rank: Chief Engineer / 2/E (verify against company SMS)

**Safety before inspection / test:**
- Testing only by ship's engineers with Master and bridge informed.
- No crankcase opening on running or recently stopped engine.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E01.1 | Running hours, overhaul history and PMS status reviewed | DOC | | | | |
| E01.2 | Performance records (indicator/PMI), LO analysis reviewed | DOC | | | | |
| E01.3 | Class items / machinery survey status reviewed | DOC | | | | |
| E01.4 | Leakage: fuel, LO, cooling water, exhaust gas | SEEN | | | | |
| E01.5 | Abnormal sound, vibration, smoke at funnel | SEEN | | | | |
| E01.6 | Crankcase inspection records / photos; crankcase opened only if stopped and authorized | INSPECTED | | | | |
| E01.7 | Holding-down bolts, chocks, foundation where accessible | INSPECTED | | | | |
| E01.8 | Start from control room and local station where authorized | TESTED | | | | |
| E01.9 | Ahead / astern operation | TESTED | | | | |
| E01.10 | Load readings compared with shop trial / sea trial / maker values (reference: TBD) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| RPM | | TBD | |
| Load indicator / fuel rack | | TBD | |
| Exhaust temperatures per cylinder | | TBD | |
| Cooling water / LO pressures and temps | | TBD | |
| Scavenge air pressure / temp | | TBD | |
| Turbocharger RPM | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Exhaust temperatures uneven between cylinders
- Repeated slowdown entries in alarm log
- Fresh paint on crankcase doors

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E02 — Turbochargers, scavenge air and exhaust system
### Tua bin tăng áp, khí quét và hệ thống khí xả | 废气涡轮增压器、扫气及排气系统

Typical responsible rank: 2/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E02.1 | Turbocharger overhaul history and running hours reviewed | DOC | | | | |
| E02.2 | Scavenge space inspection records reviewed | DOC | | | | |
| E02.3 | Abnormal noise / vibration of turbochargers | SEEN | | | | |
| E02.4 | Air coolers: drain, differential pressure readings | INSPECTED | | | | |
| E02.5 | Exhaust piping insulation and lagging condition | INSPECTED | | | | |
| E02.6 | Water washing / cleaning equipment condition and use records | TESTED | | | | |
| E02.7 | Turbocharger performance compared with reference (TBD per maker/trial data) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| TC RPM | | TBD | |
| Air cooler diff. pressure | | TBD | |
| Exhaust temp before/after TC | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Oil wet scavenge spaces in photos
- Missing lagging near fuel lines

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E03 — Shafting, stern tube, thrust bearing and propeller
### Hệ trục, ống bao trục, ổ chặn, chân vịt | 轴系、艉轴管、推力轴承及螺旋桨

Typical responsible rank: Chief Engineer (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E03.1 | Last shaft withdrawal / stern tube survey and bearing wear-down records reviewed | DOC | | | | |
| E03.2 | Stern tube oil consumption / analysis records reviewed | DOC | | | | |
| E03.3 | Intermediate bearings: oil level, temperature, condition | INSPECTED | | | | |
| E03.4 | Stern tube seal: leakage, oil header tank level | INSPECTED | | | | |
| E03.5 | Thrust bearing: temperature, leakage | INSPECTED | | | | |
| E03.6 | Shaft observed in operation | TESTED | | | | |
| E03.7 | Propeller condition from dry-dock records or underwater survey photos | SEEN | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Bearing temperatures | | TBD | |
| Stern tube oil consumption | | TBD | |
| Wear-down reading (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Frequent stern tube oil top-up
- Water in stern tube oil analysis

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E04 — Diesel generators
### Máy phát điện diesel | 柴油发电机组

Typical responsible rank: 2/E / 3/E with ETO (verify against company SMS)

**Safety before inspection / test:**
- Load changes only under the engineer in charge; avoid blackout risk.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E04.1 | Running hours and overhaul history per unit | DOC | | | | |
| E04.2 | LO analysis and alarm history | DOC | | | | |
| E04.3 | Leakage, sound, vibration per unit | SEEN | | | | |
| E04.4 | Fuel injection pipes, shielding, hot surfaces insulation | INSPECTED | | | | |
| E04.5 | Each generator started, synchronized and loaded (see T01) | TESTED | | | | |
| E04.6 | Standby generator auto start tested by approved method | TESTED | | | | |
| E04.7 | Load sharing and readings compared between units | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| kW / A / V / Hz | | TBD | |
| Exhaust temperatures | | TBD | |
| LO pressure and temp | | TBD | |
| Cooling water temps | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- One unit never run ('standby')
- Unequal load sharing
- Missing hot surface insulation

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E05 — Boilers and exhaust gas economizer
### Nồi hơi và nồi hơi khí xả | 锅炉及废气经济器

Typical responsible rank: 2/E (verify against company SMS)

**Safety before inspection / test:**
- Safety valves and firing controls: no adjustment or test outside maker / company procedure.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E05.1 | Boiler survey and water treatment records reviewed | DOC | | | | |
| E05.2 | Gauge glasses, burner, refractory where visible | INSPECTED | | | | |
| E05.3 | Insulation and leakage | INSPECTED | | | | |
| E05.4 | Burner firing sequence observed | TESTED | | | | |
| E05.5 | Low water level / flame failure safety devices tested by approved method | TESTED | | | | |
| E05.6 | Safety valve setting records reviewed | DOC | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Steam pressure | | TBD | |
| Water analysis results (ref.) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Gauge glass blocked
- Chemical dosing not recorded

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E06 — Air compressors and air receivers
### Máy nén khí và chai gió | 空气压缩机及空气瓶

Typical responsible rank: 3/E or 4/E (per SMS) (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E06.1 | Running hours, overhaul history | DOC | | | | |
| E06.2 | Compressors: leaks, belts / couplings, guards | INSPECTED | | | | |
| E06.3 | Receivers: drains, safety valves, pressure gauges, inspection records | INSPECTED | | | | |
| E06.4 | Compressors started; auto start/stop operation observed | TESTED | | | | |
| E06.5 | Filling time compared with reference (reference: TBD per maker/trial) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Discharge pressure / temps per stage | | TBD | |
| Receiver pressure | | TBD | |
| Filling time | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Excessive water at drains
- Compressor that 'does not need testing'

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E07 — Fuel oil system
### Hệ thống nhiên liệu | 燃油系统

Typical responsible rank: Chief Engineer / 3/E (verify against company SMS)

**Safety before inspection / test:**
- No hot work or open flame near fuel systems.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E07.1 | Fuel oil tanks list, bunker records, oil record book reviewed | DOC | | | | |
| E07.2 | Transfer pumps, filters, heaters | INSPECTED | | | | |
| E07.3 | Quick-closing valves: markings, wires / air lines, reset | INSPECTED | | | | |
| E07.4 | Quick-closing valves remote operation tested where authorized and safe | TESTED | | | | |
| E07.5 | Fuel line shielding and drip trays, leak detection | INSPECTED | | | | |
| E07.6 | Tank sounding pipes, self-closing cocks | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Fuel temperature / viscosity where fitted | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Tied open self-closing cocks
- Quick-closing valve wire disconnected
- Fuel in drip trays

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E08 — Fuel oil and lube oil purifiers
### Máy lọc dầu đốt và dầu nhờn | 燃油及滑油分油机

Typical responsible rank: 3/E (verify against company SMS)

**Safety before inspection / test:**
- Do not open bowl while running or before full stop.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E08.1 | Overhaul history, running hours | DOC | | | | |
| E08.2 | Sound and vibration compared between units | SEEN | | | | |
| E08.3 | Leakage, sludge discharge, heaters | INSPECTED | | | | |
| E08.4 | Start, separation, sludge discharge cycle observed | TESTED | | | | |
| E08.5 | Alarms (e.g. water/oil detection where fitted) tested by approved method | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Throughput | | TBD | |
| Oil temperature | | TBD | |
| Motor current | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- One purifier always stopped
- Unusual noise during run-up

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E09 — Lube oil systems
### Hệ thống dầu nhờn | 滑油系统

Typical responsible rank: 2/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E09.1 | LO analysis results and consumption records | DOC | | | | |
| E09.2 | Pumps, coolers, filters, sump / tank levels | INSPECTED | | | | |
| E09.3 | Standby pump auto changeover tested by approved method | TESTED | | | | |
| E09.4 | Pressures and temperatures compared with maker values (TBD) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| LO pressure / temp | | TBD | |
| Filter diff. pressure | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- High consumption not explained
- Water in LO analysis

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E10 — Cooling water systems (sea water, fresh water, central cooling)
### Hệ thống nước làm mát | 冷却水系统（海水、淡水、中央冷却）

Typical responsible rank: 3/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E10.1 | Cooler cleaning records, water treatment records | DOC | | | | |
| E10.2 | Pumps, coolers, sea chests, strainers, valves | INSPECTED | | | | |
| E10.3 | Piping: doublers, clamps, cement boxes, temporary repairs | INSPECTED | | | | |
| E10.4 | Standby pumps run and auto changeover tested by approved method | TESTED | | | | |
| E10.5 | Temperatures across coolers compared with reference (TBD) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Pressures / temperatures in/out | | TBD | |
| Expansion tank level | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Cement boxes or clamps on sea water lines
- Frequent expansion tank top-ups

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E11 — Fresh water generator and domestic water
### Máy sinh hoạt nước ngọt và nước sinh hoạt | 造水机及生活用水

Typical responsible rank: 3/E / 4/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E11.1 | Running records, water treatment / testing records | DOC | | | | |
| E11.2 | Evaporator, ejector, salinometer, pumps | INSPECTED | | | | |
| E11.3 | Plant run and output observed | TESTED | | | | |
| E11.4 | Salinometer alarm / dump valve tested by approved method | TESTED | | | | |
| E11.5 | Hydrophore, UV / sterilizer where fitted | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Output (t/day) | | TBD | |
| Salinity reading | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Salinometer bypassed

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E12 — Steering gear
### Máy lái | 舵机

Typical responsible rank: Chief Engineer / 2/E with bridge (verify against company SMS)

**Safety before inspection / test:**
- Steering tests coordinated with bridge; nobody near tiller/rams during test.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E12.1 | Steering gear test records and drill records reviewed | DOC | | | | |
| E12.2 | Hydraulic units, oil level, leakage, rams/actuator, rudder carrier | INSPECTED | | | | |
| E12.3 | Changeover instructions and block diagram posted | INSPECTED | | | | |
| E12.4 | Each pump run; hard over to hard over | TESTED | | | | |
| E12.5 | Local / emergency steering and communication with bridge tested | TESTED | | | | |
| E12.6 | Alarms tested by approved method | TESTED | | | | |
| E12.7 | Hard-over timing measured (required value per applicable requirement: verify) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Hard-over time (s) | | TBD | |
| Hydraulic pressure | | TBD | |
| Motor current | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Oil leakage at rams
- Emergency steering drill not recorded

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E13 — Bilge system and bilge pumps
### Hệ thống và bơm la canh | 舱底水系统及舱底泵

Typical responsible rank: 2/E / 3/E (verify against company SMS)

**Safety before inspection / test:**
- Trace before testing; no overboard discharge of oily bilge.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E13.1 | Bilge system drawing vs actual piping (trace where authorized) | DOC | | | | |
| E13.2 | Pumps, valves, strainers, non-return valves | INSPECTED | | | | |
| E13.3 | Bilge wells: level, oil presence, alarms | INSPECTED | | | | |
| E13.4 | Bilge suction from each well tested where authorized | TESTED | | | | |
| E13.5 | Emergency bilge suction valve operable | TESTED | | | | |
| E13.6 | Bilge level alarms tested by approved method | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Pump suction / discharge pressure | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Flexible hoses on bilge lines
- Blank flanges with fresh paint
- Pipe not matching drawing

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E14 — Ballast pumps and engine-room ballast system
### Bơm và hệ thống ballast buồng máy | 压载泵及机舱压载系统

Typical responsible rank: Chief Officer / 3/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E14.1 | Ballast water record book reviewed | DOC | | | | |
| E14.2 | Pumps, eductors, valves, remote valve actuators | INSPECTED | | | | |
| E14.3 | Pumps run; valves operated locally and remotely (see T11) | TESTED | | | | |
| E14.4 | Pump performance observed vs maker data (TBD) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Suction / discharge pressure | | TBD | |
| Motor current | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Valves only operable locally
- Indicator positions not matching valve

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E15 — Ballast water management system (BWMS)
### Hệ thống xử lý nước dằn (BWMS) | 压载水管理系统（BWMS）

Typical responsible rank: Chief Officer / Chief Engineer / ETO (verify against company SMS)

**Safety before inspection / test:**
- Operate only per maker and approved BWM plan.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E15.1 | Type approval documents, BWM plan, operating logs, maintenance records | DOC | | | | |
| E15.2 | Alarm / fault log and bypass records reviewed | DOC | | | | |
| E15.3 | Filters, UV / electrolysis units, sensors | INSPECTED | | | | |
| E15.4 | System operated in ballasting or test mode | TESTED | | | | |
| E15.5 | Spare consumables (lamps, sensors, chemicals) vs maker list | DOC | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Operating parameters per maker display | | TBD | |
| Fault count from log | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Frequent bypass entries
- System shown 'out of order' for long periods

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E16 — Oily water separator, oil content meter, bilge and sludge tanks
### Máy phân ly nước dầu, thiết bị đo hàm lượng dầu, két la canh và cặn | 油水分离器、油分浓度计、舱底水舱及油渣舱

Typical responsible rank: Chief Engineer (verify against company SMS)

**Safety before inspection / test:**
- Never adjust or bypass oil content meter. No overboard discharge during inspection unless lawful and authorized.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E16.1 | Oil record book and sludge / bilge tank sounding records reviewed | DOC | | | | |
| E16.2 | OWS / OCM type approval and calibration records | DOC | | | | |
| E16.3 | Piping traced from bilge holding tank to overboard valve | INSPECTED | | | | |
| E16.4 | Overboard valve sealing / locking arrangement per company procedure | INSPECTED | | | | |
| E16.5 | OWS operated in recirculation / test mode where available | TESTED | | | | |
| E16.6 | OCM alarm and automatic stopping device tested by approved method | TESTED | | | | |
| E16.7 | Sludge tank and sludge pump / shore connection | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| OCM reading | | TBD | |
| Tank soundings | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Flexible hose near OWS
- Clean OWS that has run many hours
- Tank levels not matching ORB

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E17 — Incinerator and sewage treatment plant
### Lò đốt rác và hệ thống xử lý nước thải | 焚烧炉及生活污水处理装置

Typical responsible rank: 3/E / 4/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E17.1 | Operation and maintenance records | DOC | | | | |
| E17.2 | Incinerator: refractory, burner, safety devices | INSPECTED | | | | |
| E17.3 | Incinerator start / flame failure sequence observed | TESTED | | | | |
| E17.4 | Sewage plant: blowers, pumps, chlorination where fitted | INSPECTED | | | | |
| E17.5 | Sewage plant running observed | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Combustion temperature where displayed | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Incinerator never used per records

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E18 — Fire pumps and emergency fire pump
### Bơm cứu hỏa và bơm cứu hỏa sự cố | 消防泵及应急消防泵

Typical responsible rank: 2/E / 3/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E18.1 | Test and maintenance records | DOC | | | | |
| E18.2 | Pumps, isolation valves, priming arrangement | INSPECTED | | | | |
| E18.3 | Main fire pumps started locally and remotely | TESTED | | | | |
| E18.4 | Emergency fire pump started from its own position and outside machinery space | TESTED | | | | |
| E18.5 | Pressure at highest / remotest hydrants (required pressure per applicable requirement: verify) | PERF | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Discharge pressure | | TBD | |
| Hydrant pressure at test points | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Emergency fire pump fails to prime
- Isolation valve seized

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E19 — Engine room fire safety arrangements
### Bố trí an toàn cháy buồng máy | 机舱防火安全布置

Typical responsible rank: Chief Engineer (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E19.1 | Remote stops for fans and fuel pumps: markings, protection | INSPECTED | | | | |
| E19.2 | Remote stops tested where authorized | TESTED | | | | |
| E19.3 | Fire dampers and skylights closing | INSPECTED | | | | |
| E19.4 | Escape routes clear, signage, lighting | INSPECTED | | | | |
| E19.5 | Housekeeping: oil in bilges, oily rags, insulation soaked | INSPECTED | | | | |

**Sea Eye — signs that need verification (not proof of defect):**
- Oil-soaked insulation
- Blocked escape trunk

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E20 — Refrigeration and air-conditioning plant
### Hệ thống lạnh và điều hòa | 冷藏及空调装置

Typical responsible rank: 3/E / 4/E (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E20.1 | Maintenance and refrigerant records | DOC | | | | |
| E20.2 | Compressors, condensers, leakage signs | INSPECTED | | | | |
| E20.3 | Plant running; room temperatures | TESTED | | | | |
| E20.4 | Alarm (e.g. person trapped alarm where fitted) tested | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Compressor pressures | | TBD | |
| Room temperatures | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Frequent refrigerant top-up

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## E21 — Tank soundings and ROB measurement for oils
### Đo két và tính ROB dầu | 油舱测深及存油量（ROB）计量

Typical responsible rank: Chief Engineer / 3/E (verify against company SMS)

**Safety before inspection / test:**
- Measure by traceable method only; see 04 §8.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| E21.1 | Tank tables and calibration reviewed | DOC | | | | |
| E21.2 | Soundings / ullages taken jointly where takeover requires | TESTED | | | | |
| E21.3 | Temperature and density basis recorded; calculation traced | PERF | | | | |
| E21.4 | Compared with ROB records and ORB | DOC | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Sounding / ullage per tank | | TBD | |
| Temperature | | TBD | |
| Density basis | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Tables missing for some tanks
- Difference explained only verbally

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


---

# ETO / ELECTRICAL


## T01 — Main switchboard and generator protection
### Bảng điện chính và bảo vệ máy phát | 主配电板及发电机保护

Typical responsible rank: ETO / Chief Engineer (verify against company SMS)

**Safety before inspection / test:**
- Live switchboard work only under electrical safety procedure; no opening of panels for inspection without permission.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T01.1 | Single-line diagram, protection settings record, maintenance history | DOC | | | | |
| T01.2 | Panels: indications, lamps, labels, cleanliness, thermography report where available | INSPECTED | | | | |
| T01.3 | Synchronizing (auto / manual) observed | TESTED | | | | |
| T01.4 | Preferential trip / load shedding tested only by approved method | TESTED | | | | |
| T01.5 | Insulation monitoring / earth fault indication | TESTED | | | | |
| T01.6 | Protection relay test records reviewed | DOC | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Bus voltage / frequency | | TBD | |
| Insulation reading main / 230 V | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Earth fault indicated and accepted as normal
- Bridged or removed protection

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T02 — Emergency generator and emergency switchboard
### Máy phát sự cố và bảng điện sự cố | 应急发电机及应急配电板

Typical responsible rank: ETO / 2/E (verify against company SMS)

**Safety before inspection / test:**
- Blackout test only if planned and authorized by Master / Chief Engineer.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T02.1 | Test records and maintenance history | DOC | | | | |
| T02.2 | Fuel tank level, starting means (batteries / hydraulic / air), room ventilation | INSPECTED | | | | |
| T02.3 | Started manually and by auto start (approved method) | TESTED | | | | |
| T02.4 | Loading to emergency switchboard observed | TESTED | | | | |
| T02.5 | Second means of starting available | INSPECTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Start time | | TBD | |
| Voltage / frequency | | TBD | |
| Load | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Started with assistance only
- Fuel tank low

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T03 — Batteries, UPS and emergency lighting
### Ắc quy, UPS và đèn sự cố | 蓄电池、UPS及应急照明

Typical responsible rank: ETO (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T03.1 | Battery maintenance / replacement records | DOC | | | | |
| T03.2 | Battery room: ventilation, electrolyte / condition, terminals | INSPECTED | | | | |
| T03.3 | Emergency lighting tested | TESTED | | | | |
| T03.4 | UPS / transitional source changeover tested by approved method | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Battery voltages | | TBD | |
| UPS autonomy where indicated | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Swollen batteries
- Lighting failed in escape routes

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T04 — Alarm monitoring system / UMS
### Hệ thống giám sát báo động / UMS | 报警监测系统/无人机舱（UMS）

Typical responsible rank: ETO / Chief Engineer (verify against company SMS)

**Safety before inspection / test:**
- Alarm tests by approved method only; do not create unsafe conditions.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T04.1 | Alarm list and sensor calibration records | DOC | | | | |
| T04.2 | Alarm history: repeated, inhibited or blocked channels | DOC | | | | |
| T04.3 | Sensors, cables, terminals for disconnection or jumpers | INSPECTED | | | | |
| T04.4 | Sample alarms tested (sensor simulation per maker) | TESTED | | | | |
| T04.5 | Extension alarms to accommodation / bridge and dead-man alarm | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Number of inhibited channels | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Many inhibited channels
- Jumpers in terminal boxes

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T05 — Main engine remote control and safety system
### Hệ thống điều khiển từ xa và an toàn máy chính | 主机遥控及安全系统

Typical responsible rank: Chief Engineer / ETO (verify against company SMS)

**Safety before inspection / test:**
- Shutdown / slowdown tested only by simulation per maker procedure.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T05.1 | Settings documentation and test records | DOC | | | | |
| T05.2 | Control transfer bridge / ECR / local | TESTED | | | | |
| T05.3 | Emergency stop from each position where authorized | TESTED | | | | |
| T05.4 | Shutdown / slowdown functions tested by simulation | TESTED | | | | |
| T05.5 | Override records reviewed | DOC | | | | |

**Sea Eye — signs that need verification (not proof of defect):**
- Override switch in use
- Shutdown functions not tested per records

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T06 — Fire detection, general alarm and public address
### Báo cháy, báo động chung và truyền thanh | 火灾探测、通用报警及广播系统

Typical responsible rank: ETO / designated officer (verify against company SMS)

**Safety before inspection / test:**
- Inform bridge and crew before tests; use approved test equipment.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T06.1 | Detector test records and loop drawings | DOC | | | | |
| T06.2 | Fault / disabled zones log | DOC | | | | |
| T06.3 | Sample detectors tested per zone | TESTED | | | | |
| T06.4 | Manual call points tested | TESTED | | | | |
| T06.5 | General alarm and PA audible in all spaces | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Zones disabled (list) | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Detectors covered or removed
- Zones disabled long-term

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T07 — Electric motors, starters and insulation
### Động cơ điện, khởi động từ và cách điện | 电动机、启动器及绝缘

Typical responsible rank: ETO (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T07.1 | Insulation resistance records for critical motors | DOC | | | | |
| T07.2 | Starters: contactors, overloads, labelling | INSPECTED | | | | |
| T07.3 | Motors: noise, vibration, temperature | SEEN | | | | |
| T07.4 | Insulation measurement on selected motors (isolated) | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Insulation resistance (MΩ) | | TBD | |
| Current | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Overloads bypassed
- Burnt contactor marks

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T08 — Internal communication
### Thông tin nội bộ | 船内通信

Typical responsible rank: ETO / 2/O (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T08.1 | Sound-powered telephones bridge ↔ steering gear ↔ ECR ↔ emergency stations | TESTED | | | | |
| T08.2 | Talk-back and telephones | TESTED | | | | |
| T08.3 | Portable radios | TESTED | | | | |

**Sea Eye — signs that need verification (not proof of defect):**
- Steering gear phone inaudible

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T09 — Deck machinery electrical drives
### Truyền động điện máy boong | 甲板机械电力驱动

Typical responsible rank: ETO (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T09.1 | Maintenance history for crane / winch electrical systems | DOC | | | | |
| T09.2 | Control panels, VFDs, slip rings, cable reels | INSPECTED | | | | |
| T09.3 | Limit switches and emergency stops tested with D05 / D06 / D07 | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Motor current | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Water ingress in junction boxes

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T10 — Navigation lights, signals and searchlights
### Đèn hành trình, tín hiệu và đèn pha | 航行灯、信号灯及探照灯

Typical responsible rank: ETO / 2/O (verify against company SMS)

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T10.1 | Navigation lights tested (main and secondary) | TESTED | | | | |
| T10.2 | Failure alarm panel tested | TESTED | | | | |
| T10.3 | Signal lights, NUC, searchlights tested | TESTED | | | | |

**Sea Eye — signs that need verification (not proof of defect):**
- Secondary lights inoperative

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.


## T11 — Remote valve control, tank gauging and level / water ingress alarms
### Điều khiển van từ xa, đo két và báo động mức nước | 遥控阀、液位遥测及液位/进水报警

Typical responsible rank: ETO / Chief Officer (verify against company SMS)

**Safety before inspection / test:**
- Test alarms by approved method; not by flooding spaces.

| # | Check item | Target | Reached | Status | Evidence ref | Remarks |
|---|---|---|---|---|---|---|
| T11.1 | System documentation and test records | DOC | | | | |
| T11.2 | Remote valves operated and indicators compared with actual position | TESTED | | | | |
| T11.3 | Tank gauging compared with manual sounding | TESTED | | | | |
| T11.4 | Level / water ingress alarms tested where fitted | TESTED | | | | |

**Readings to record** (reference values: TBD per maker manual / trial data / company PMS):

| Parameter | Reading | Reference (source) | Remarks |
|---|---|---|---|
| Gauge vs sounding difference | | TBD | |

**Sea Eye — signs that need verification (not proof of defect):**
- Gauges known 'not reliable'
- Alarms muted

Record as: OBSERVATION → POSSIBLE SIGNIFICANCE → VERIFICATION REQUIRED.

