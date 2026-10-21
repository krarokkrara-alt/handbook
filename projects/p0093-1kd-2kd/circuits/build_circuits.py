from pathlib import Path
from html import escape
import json
P=Path(__file__).parent
W,H=1800,1250
BLUE='#147aa5'; RED='#c53838'; GREEN='#16805e'; INK='#182b3b'; AMBER='#ae6900'
TH={'01_hydraulic_paths':'P0093: ไล่เส้นทางน้ำมันทั้งแรงดันต่ำ แรงดันสูง และทางกลับ','02_pressure_feedback':'วงป้อนกลับ: คำสั่ง SCV ไม่ได้พิสูจน์ว่าน้ำมันส่งได้จริง','03_sensor_electrical':'เซ็นเซอร์แรงดันราง: แยกไฟอ้างอิง สัญญาณ และขั้วกลับ','04_scv_driver_measurement':'SCV: วัดคร่อมสองขั้วและดูกระแสที่สายเส้นเดียว','05_scv_nc_no':'SCV แบบ NC / NO: สภาพไม่จ่ายไฟต่างกัน','06_limiter_discharge':'แยกวาล์วจำกัดแรงดันกับวาล์วระบายที่สั่งด้วยไฟฟ้า','07_injector_command_return':'หัวฉีด: ตรวจทั้งการสั่งไฟฟ้าและน้ำมันไหลกลับ','08_ground_offset':'ขั้วกลับเซ็นเซอร์ไม่ดี ทำให้ค่าแรงดันที่อ่านคลาดเคลื่อนได้','09_pressure_event_sequence':'อ่านเหตุการณ์ก่อน ECU ตัด ไม่ตัดสินจากแรงดันหลังดับ','10_fuel_balance':'สมดุลในราง: ปริมาณส่งเข้าเทียบกับปริมาณไหลออก'}
class S:
 def __init__(self,n,title,sub):
  self.n=n; self.a=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="context-stroke"/></marker></defs><rect width="1800" height="1250" fill="white"/>'];self.text(60,55,TH[n],32);self.text(60,100,title,26);self.text(60,140,sub,21,'#596a75');self.line([(60,165),(1740,165)],'#cad6dc',2)
 def text(self,x,y,t,size=25,c=INK):self.a.append(f'<text x="{x}" y="{y}" font-family="Arial, Leelawadee UI, sans-serif" font-size="{size}" fill="{c}">{escape(t)}</text>')
 def line(self,p,c=INK,w=4,arrow=False,dash=False):self.a.append(f'<polyline points="'+ ' '.join(f'{x},{y}' for x,y in p)+f'" fill="none" stroke="{c}" stroke-width="{w}"'+(' marker-end="url(#arr)"' if arrow else '')+(' stroke-dasharray="12 8"' if dash else '')+'/>')
 def box(self,x,y,w,h,lines,c=INK):
  self.a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f5f8fa" stroke="{c}" stroke-width="3"/>')
  for i,t in enumerate(lines):self.text(x+18,y+37+i*35,t,25,c)
 def node(self,x,y,label=''):
  self.a.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{INK}"/>')
  if label:self.text(x+12,y-15,label,22)
 def tp(self,x,y,t):
  self.a.append(f'<circle cx="{x}" cy="{y}" r="12" fill="white" stroke="{AMBER}" stroke-width="4"/>');self.text(x+17,y-16,t,23,AMBER)
 def gnd(self,x,y,label=''):
  self.line([(x,y),(x,y+20)]);self.line([(x-24,y+20),(x+24,y+20)]);self.line([(x-16,y+30),(x+16,y+30)]);self.line([(x-8,y+40),(x+8,y+40)])
  if label:self.text(x-45,y+75,label,20)
 def meter(self,x,y,label='V'):
  self.a.append(f'<circle cx="{x}" cy="{y}" r="40" fill="white" stroke="{AMBER}" stroke-width="4"/>');self.text(x-10,y+10,label,27,AMBER)
 def resistor(self,x,y,label):
  self.line([(x,y),(x+25,y)]);self.a.append(f'<rect x="{x+25}" y="{y-15}" width="90" height="30" fill="white" stroke="{INK}" stroke-width="3"/>');self.line([(x+115,y),(x+140,y)]);self.text(x+20,y-28,label,22)
 def cap(self,x,y,label):
  self.line([(x,y),(x,y+35)]);self.line([(x-25,y+35),(x+25,y+35)]);self.line([(x-25,y+50),(x+25,y+50)]);self.line([(x,y+50),(x,y+85)]);self.text(x+37,y+50,label,22)
 def coil(self,x,y,label):
  self.line([(x,y),(x,y+25)]);self.a.append(f'<path d="M{x},{y+25} '+''.join(f'a 25 20 0 0 1 0 40 ' for _ in range(4))+f'" fill="none" stroke="{INK}" stroke-width="4"/>');self.line([(x,y+185),(x,y+210)]);self.text(x+45,y+100,label,25)
 def note(self,lines):
  self.line([(60,1040),(1740,1040)],'#cad6dc',2)
  for i,t in enumerate(lines):self.text(70,1080+i*35,t,23)
 def finish(self):
  scope='ผังวาดใหม่เฉพาะ DR201E / TASA Argentina | MODEL-SPECIFIC REDRAW' if self.n.startswith(('11_','12_')) else 'ภาพหลักการวาดใหม่ ไม่ใช่ผังขา OEM | EDUCATIONAL, NOT OEM PINOUT'
  self.text(60,1220,f'{self.n} | {scope}',19,'#596a75');self.a.append('</svg>');(P/(self.n+'.svg')).write_text('\n'.join(self.a),encoding='utf-8')

s=S('01_hydraulic_paths','P0093: follow fuel, not just the code','HYDRAULIC CIRCUIT | blue = low pressure / red = high pressure / green = return')
s.box(70,310,190,120,['FUEL TANK','pickup / vent'],BLUE);s.box(340,310,210,120,['FILTER','primer / seals'],BLUE);s.box(650,280,240,180,['SUPPLY PUMP','feed stage','SCV + plungers'],BLUE);s.box(1010,300,260,130,['COMMON RAIL','pressure storage'],RED);s.box(1400,300,280,130,['INJECTOR x 4','fuel to cylinder'],RED)
for a,b,c in [(260,340,BLUE),(550,650,BLUE),(890,1010,RED),(1270,1400,RED)]:s.line([(a,370),(b,370)],c,6,True)
s.line([(1540,430),(1540,820),(170,820),(170,430)],GREEN,5,True);s.text(600,865,'Injector control / leak-off return',25,GREEN)
s.box(1010,570,400,125,['RAIL RETURN DEVICE','limiter OR discharge valve'],GREEN);s.line([(1140,430),(1140,570)],RED,5,True);s.line([(1210,695),(1210,820)],GREEN,5,True);s.node(1210,820)
s.line([(770,460),(770,700),(770,820)],GREEN,5,True);s.node(770,820);s.text(380,740,'Pump overflow / case return',24,GREEN)
s.tp(600,370,'A');s.tp(950,370,'B');s.tp(1340,370,'C');s.tp(1500,820,'D')
s.note(['A: restriction / air ingress can reduce pump filling without leaving an external wet leak.','B / C: inspect high-pressure connections only with the approved depressurisation procedure.','D: return flow is normal; excessive loss must be tested by the correct component procedure.']);s.finish()

s=S('02_pressure_feedback','Pressure control: one command, several possible causes','CONTROL LOOP | command is not proof of fuel delivery; measured pressure is not independent proof')
s.box(70,230,270,140,['TARGET PRESSURE','speed / load / temp']);s.box(440,230,290,140,['ECU CONTROLLER','error = target - actual']);s.box(850,230,270,140,['SCV DRIVER','current / duty']);s.box(1270,230,400,140,['PUMP + RAIL','delivery versus outflow'])
for a,b in [(340,440),(730,850),(1120,1270)]:s.line([(a,300),(b,300)],INK,4,True)
s.box(1210,590,460,150,['RAIL PRESSURE SENSOR','reference + signal + return'],BLUE);s.line([(1470,370),(1470,590)],BLUE,4,True);s.line([(1210,665),(580,665),(580,370)],BLUE,4,True);s.text(770,640,'ACTUAL FEEDBACK',25,BLUE)
s.box(80,590,350,230,['INDEPENDENT CHECKS','fuel supply / return','sensor wiring / ground','driver current / voltage'],AMBER)
s.line([(1670,300),(1720,300),(1720,850),(1140,850)],RED,4,True);s.text(850,900,'Outflow = injection + control return + leakage + rail relief',24,RED)
s.note(['Actual pressure low + corrective command: check fuel balance AND credibility of the feedback.','SCV current present does not prove the valve moves or the pump displaces enough fuel.','Do not infer SCV direction from a scanner duty label; confirm valve type and PID definition.']);s.finish()

s=S('03_sensor_electrical','Rail sensor: separate reference, signal and sensor return','3-NET PRINCIPLE | DR201E p.05-73 example; RM1151E p.05-490 differs | verify vehicle EWD')
s.box(90,240,400,620,['ENGINE ECU','regulated reference','analogue input / ADC','sensor-return circuit']);s.box(1240,270,450,520,['RAIL PRESSURE SENSOR','pressure -> voltage','internal electronics'])
for y,t in [(430,'REFERENCE'),(590,'SIGNAL'),(750,'SENSOR RETURN')]:
 if y==590:
  s.line([(490,y),(700,y)]);s.line([(840,y),(1240,y)])
 else:s.line([(490,y),(1240,y)],BLUE,4)
 s.node(650,y);s.tp(950,y,t)
s.resistor(700,590,'harness resistance')
s.line([(1050,590),(1120,590),(1120,735)],AMBER,3);s.line([(1120,765),(1120,910),(1050,910)],AMBER,3);s.line([(970,910),(900,910),(900,750)],AMBER,3);s.meter(1010,910);s.text(530,990,'DMM: signal-to-sensor-return; separate leads, no jumper',23,AMBER)
s.node(1050,590);s.node(900,750)
s.a.append('<path d="M1120,735 Q1150,750 1120,765" fill="none" stroke="#ae6900" stroke-width="3"/>')
s.note(['Measure reference-to-return and signal-to-return at the same operating condition.','A reference short may affect other sensors on the same supply; verify shared nets in the EWD.','Three functional nets shown, not a universal wire count: RM1151E uses a different sensor circuit.']);s.finish()

s=S('04_scv_driver_measurement','SCV: test the complete current path','ELECTRICAL PRINCIPLE | driver topology omitted deliberately; neither coil terminal assumed chassis ground')
s.box(90,250,480,600,['ECU CURRENT DRIVER','power stage + protection','current control / monitoring','Output A','Output B']);s.coil(1260,400,'SCV solenoid');s.line([(570,450),(980,450),(980,400),(1260,400)]);s.line([(1260,610),(1260,730),(570,730)])
s.tp(850,450,'A');s.tp(850,730,'B');s.box(670,180,560,100,['DIFFERENTIAL PROBE: V(A) - V(B)'],AMBER);s.line([(850,450),(850,320),(900,280)],AMBER,3,dash=True);s.line([(850,730),(720,730),(720,320),(760,280)],AMBER,3,dash=True)
s.a.append('<ellipse cx="1090" cy="450" rx="27" ry="42" fill="none" stroke="#ae6900" stroke-width="5"/>');s.text(1040,350,'CURRENT CLAMP',24,AMBER);s.line([(1090,365),(1090,405)],AMBER,3,True);s.text(1060,860,'Clamp ONE conductor',25,AMBER)
s.note(['Voltage switching + no current: open coil, open harness, poor terminal, or test setup error.','Current rises + pressure response absent: valve movement and hydraulic delivery still need testing.','Use an isolated / differential setup of suitable rating; a grounded scope clip can short a driver output.']);s.finish()

s=S('05_scv_nc_no','Two SCV rest states: never use one unplug rule for both','MECHANICAL / HYDRAULIC PRINCIPLE | type is defined with the solenoid DE-ENERGISED')
for x,title,closed in [(100,'NORMALLY CLOSED (NC)',True),(940,'NORMALLY OPEN (NO)',False)]:
 s.box(x,240,710,600,[title],BLUE);s.line([(x+70,490),(x+640,490)],BLUE,7,True)
 if closed:s.a.append(f'<rect x="{x+310}" y="420" width="70" height="140" fill="#c53838"/>');s.text(x+130,640,'Spring holds passage CLOSED',28,RED);s.text(x+95,720,'No electrical command: intake restricted',24)
 else:s.a.append(f'<rect x="{x+310}" y="340" width="70" height="100" fill="#16805e"/>');s.text(x+130,640,'Spring holds passage OPEN',28,GREEN);s.text(x+80,720,'No electrical command: intake can be high',24)
s.note(['DENSO HP3 / HP4 families include NC and NO applications. Identify the fitted pump / SCV first.','DENSO 00400706E (2009), section 2.2, describes NC SCV for its listed 1KD / 2KD applications.','This comparison explains rest state; it is NOT an instruction to unplug an SCV on a running engine.']);s.finish()

s=S('06_limiter_discharge','Rail return devices: mechanical relief is not commanded discharge','HYDRAULIC + ELECTRICAL PRINCIPLE | select the variant from the actual rail / vehicle documentation')
s.box(100,230,690,600,['VARIANT A: PRESSURE LIMITER'],GREEN);s.box(980,230,690,600,['VARIANT B: DISCHARGE VALVE'],GREEN)
for x in [150,1030]:
 s.line([(x+70,400),(x+500,400)],RED,6);s.text(x+70,360,'RAIL',26,RED);s.line([(x+290,400),(x+290,490)],RED,6);s.box(x+180,490,230,110,['RAIL DEVICE'],GREEN);s.line([(x+290,600),(x+290,730)],GREEN,5,True);s.text(x+100,780,'RETURN TO TANK',25,GREEN)
s.text(180,910,'Spring / hydraulic force opens relief',25);s.box(980,860,320,110,['ECU -> EDU','electrical actuation']);s.line([(1300,915),(1570,915),(1570,545),(1440,545)],INK,4,True)
s.note(['A mechanically opened limiter may be a consequence of preceding overpressure, not the initial cause.','A commanded discharge valve adds wiring / EDU / command checks to the hydraulic return investigation.','DENSO 00400706E section 3.1 documents a variant change; confirm applicability, not engine name alone.']);s.finish()

s=S('07_injector_command_return','Injection has an electrical path AND a fuel control path','COMBINED PRINCIPLE | current confirmation is not a measurement of nozzle delivery or return leakage')
s.box(80,250,300,180,['ENGINE ECU','injection request','timing / duration']);s.box(590,250,370,230,['EDU','boost + current drive','diagnostic feedback']);s.box(1260,250,400,230,['INJECTOR SOLENOID','control valve movement']);s.line([(380,320),(590,320)],INK,4,True);s.line([(590,400),(380,400)],BLUE,4,True);s.text(390,450,'feedback',22,BLUE)
s.line([(960,315),(1260,315)],INK,5,True);s.line([(1260,420),(960,420)],INK,5);s.text(980,255,'two-terminal drive',23)
s.box(1080,650,610,220,['RAIL -> CONTROL CHAMBER','control valve -> return','needle lift -> nozzle -> cylinder'],RED);s.line([(1460,480),(1460,650)],INK,3,True,dash=True);s.box(80,650,690,220,['TWO DIFFERENT QUESTIONS','Is electrical actuation correct?','Is fuel delivery / internal leakage correct?'],AMBER)
s.note(['P0093 with P0200: follow the applicable EDU / injector electrical diagnosis before assuming fuel leakage.','Normal correction values or current pulses do not by themselves rule out excessive injector return.','Never apply battery voltage directly to an injector; drive and test equipment must match the injector type.']);s.finish()

s=S('08_ground_offset','A poor sensor return can make pressure look different','ELECTRICAL ERROR MODEL | Vread = Vsignal-to-local-return + Vreturn-offset')
s.box(100,240,370,590,['ECU','ADC reads relative','to ECU return']);s.box(1260,240,420,590,['SENSOR','local pressure signal','local sensor return'])
s.line([(470,400),(1260,400)],INK,4);s.text(720,360,'SIGNAL',27);s.line([(470,700),(750,700)]);s.resistor(750,700,'BAD TERMINAL / R');s.line([(890,700),(1260,700)]);s.tp(690,700,'ECU side');s.tp(1050,700,'sensor side')
s.line([(690,700),(690,920),(830,920)],AMBER,3);s.line([(910,920),(1050,920),(1050,700)],AMBER,3);s.meter(870,920);s.text(700,1000,'DMM: return-to-return voltage drop',25,AMBER);s.text(570,520,'Sensor return is a circuit conductor,',27);s.text(570,565,'not automatically the same as chassis.',27)
s.note(['The direction and magnitude of error depend on the circuit and fault; use measured voltages.','Check voltage drop while the fault occurs; a static continuity test may miss intermittent resistance.','Do not bridge the sensor return to chassis as a repair. Restore the documented wiring / terminals.']);s.finish()

s=S('09_pressure_event_sequence','Read the seconds before fail-safe, not only the stalled engine','HYPOTHETICAL NC APPLICATION | synthetic current trace; not universal NO / NC behaviour or OEM values')
for y,label in [(270,'TARGET'),(460,'ACTUAL'),(650,'SCV CURRENT'),(840,'INJECTION')]:s.text(65,y+20,label,24);s.line([(350,y+80),(1700,y+80)],'#b5c4cc',2);s.line([(350,y-70),(350,y+80)],'#b5c4cc',2)
s.line([(350,270),(750,270),(850,220),(1700,220)],BLUE,5);s.line([(350,460),(750,460),(850,425),(1000,450),(1120,490),(1370,510),(1440,530),(1700,530)],RED,5)
s.line([(350,650),(750,650),(850,620),(1100,580),(1370,580),(1440,690),(1700,690)],GREEN,5)
for x in range(390,1390,70):s.line([(x,880),(x,810),(x+20,810),(x+20,880)],INK,3)
s.line([(1400,880),(1700,880)],INK,3);s.line([(1400,180),(1400,950)],AMBER,3,dash=True);s.text(1230,1005,'FAIL-SAFE / CUT-OFF',24,AMBER)
s.note(['Example: target rises, actual fails to follow, correction rises, then injection is disabled.','Near-zero pressure AFTER cut-off does not identify the original failed component.','Synchronise rail target / actual, SCV command / current, RPM, voltage and DTC timing.']);s.finish()

s=S('10_fuel_balance','The rail is a pressure accumulator: draw the balance','HYDRAULIC MODEL | conceptual mass balance, not an ECU algorithm or a calibration threshold')
s.box(600,320,580,310,['COMMON RAIL','effective storage / compliance','net inflow changes pressure'],RED);s.line([(150,460),(600,460)],RED,7,True);s.text(95,390,'PUMP DELIVERY',28,RED);s.line([(1180,380),(1660,380)],RED,6,True);s.text(1250,330,'INJECTED FUEL',26,RED);s.line([(1180,500),(1660,500)],GREEN,6,True);s.text(1250,455,'CONTROL / LEAK-OFF',26,GREEN);s.line([(900,630),(900,850),(1650,850)],GREEN,6,True);s.text(1060,810,'RAIL RELIEF / DISCHARGE',26,GREEN)
s.text(80,980,'Pressure may fall because supply falls OR outflow rises OR feedback is misleading.',29)
s.note(['A suction restriction, air ingress or weak pump lowers delivered volume; it is not external rail leakage.','Injector return / rail relief can lose pressure internally without a wet high-pressure pipe.','A P0093 code directs diagnosis; it does not determine which branch of this balance failed.']);s.finish()

TH['11_dr201e_rail_connections']='ตัวอย่างเฉพาะ DR201E: สายเซ็นเซอร์รางถึง ECM'
s=S('11_dr201e_rail_connections','DR201E / Hilux TASA made for Argentina: verified circuit connections','MODEL-SPECIFIC EXAMPLE | source Toyota DR201E p.05-73 / 05-75 | confirm applicability before use')
s.box(70,270,390,590,['F9: RAIL SENSOR','VC: terminal 3','PR: terminal 2','E2: terminal 1']);s.box(1310,270,420,590,['ECM: E8 CONNECTOR','VC: terminal 18','PCR1: terminal 26','E2: terminal 28'])
s.line([(460,470),(700,470)]);s.box(700,430,280,80,['J6 junction E -> E']);s.line([(980,470),(1310,470)],BLUE,4);s.text(490,420,'F9-3 / VC',24,BLUE);s.text(1040,420,'E8-18 / VC',24,BLUE)
s.line([(460,620),(1310,620)],INK,4);s.text(490,585,'F9-2 / PR',24);s.text(1030,585,'E8-26 / PCR1',24)
s.line([(460,770),(700,770)],GREEN,4);s.box(700,730,330,80,['J7(B) -> J/C -> J8(B)']);s.line([(1030,770),(1310,770)],GREEN,4);s.text(490,720,'F9-1 / E2',24,GREEN);s.text(1090,720,'E8-28 / E2',24,GREEN)
s.text(100,950,'Functional connection map only: connector face orientation and wire colours are not reproduced.',25)
s.note(['ผังต่อสายวาดใหม่จากคู่มือ DR201E หน้า 05–73 ไม่ใช่ผังสากลของ 1KD / 2KD ทุกปี','ชื่อขั้ว F9 / E8 เป็นรหัสเอกสารนี้ ก่อนใช้จริงต้องยืนยันรุ่น ECU และมุมมองขั้วปลั๊ก','RM1151E มีวงจรเซ็นเซอร์หลายสายต่างออกไป ห้ามนำเลขขาภาพนี้ข้ามเอกสาร']);s.finish()

TH['12_dr201e_scv_connections']='ตัวอย่างเฉพาะ DR201E: วงจร SCV สองขั้ว PCV+ / PCV–'
s=S('12_dr201e_scv_connections','DR201E / Hilux TASA made for Argentina: SCV coil circuit','MODEL-SPECIFIC EXAMPLE | source Toyota DR201E p.05-80 / 05-82 | no assumed chassis-ground terminal')
s.box(80,260,400,620,['ECM / connector E8','driver topology not shown']);s.box(1210,260,480,620,['SCV / connector S8']);s.coil(1410,450,'coil')
s.line([(480,450),(1410,450)]);s.line([(1410,660),(1410,750),(480,750)]);s.node(1410,450);s.text(520,400,'E8-2: PCV+  <->  S8-1',29);s.text(520,700,'E8-1: PCV-  <->  S8-2',29);s.tp(910,450,'PCV+');s.tp(910,750,'PCV-')
s.text(90,960,'PLUS / MINUS are circuit names; do not connect a scope ground clip to either output by assumption.',25)
s.note(['ผังวงขดลวดวาดใหม่ตาม DR201E หน้า 05–80 เฉพาะ application ของเอกสารนี้','ตรวจสายและขดลวดโดยแยกการทดสอบแบบดับเครื่องออกจากการวัดคลื่นขณะทำงาน','วัดแรงดันคร่อม PCV+ / PCV– ด้วยอุปกรณ์เหมาะสม ไม่สมมติว่า PCV– เป็นกราวด์ตัวถัง']);s.finish()
TH['13_overshoot_then_drop']='แรงดันตกอาจเริ่มจากแรงดันสูง: อ่าน P1229 ร่วมกับ P0093'
s=S('13_overshoot_then_drop','Possible sequence: overfeed -> overshoot -> relief opens -> pressure falls','DIAGNOSTIC WORKFLOW EXAMPLE | limiter configuration only; a causal hypothesis to prove, not every P0093')
for x,lines,col in [(60,['1. ส่งน้ำมันมากเกิน','SCV / control issue'],INK),(510,['2. แรงดันสูงเกิน','pressure overshoot'],RED),(960,['3. limiter เปิด','flow to return'],GREEN),(1410,['4. แรงดันตก','P0093 may follow'],AMBER)]:s.box(x,260,330,150,lines,col)
for a,b in [(390,510),(840,960),(1290,1410)]:s.line([(a,335),(b,335)],INK,4,True)
s.text(90,520,'ตัวอย่างกราฟสังเคราะห์ — ไม่มีค่าความดันหรือเวลา OEM',28)
s.line([(170,860),(1650,860)],INK,3,True);s.line([(170,860),(170,580)],INK,3,True);s.text(75,610,'pressure',22);s.text(1560,910,'time',24)
s.line([(170,740),(1650,740)],BLUE,3,dash=True);s.text(1450,715,'target (example)',22,BLUE)
s.line([(170,755),(420,755),(620,705),(800,625),(950,620),(1070,780),(1240,820),(1650,820)],RED,5)
s.line([(990,560),(990,930)],GREEN,3,dash=True);s.text(790,970,'ตรวจว่า limiter เปิดหลังช่วงแรงดันสูงจริงหรือไม่',26,GREEN)
s.note(['Toyota RM1151E หน้า 05–501 เตือนเส้นทาง P1229 ร่วม: แรงดันสูงเปิด limiter แล้วพบ P0093 ได้','อย่าเปลี่ยน limiter จากค่าแรงดันต่ำปลายเหตุอย่างเดียว ตรวจข้อมูลก่อนและหลังเหตุการณ์','ถ้าเป็นวาล์วระบายสั่งไฟฟ้า ให้ใช้ผัง variant นั้นและตรวจคำสั่ง ECU / EDU เพิ่ม']);s.finish()

TH['14_suction_measurement']='ด้านดูด: จุดวัดอยู่ตรงไหน เปลี่ยนความหมายของค่าแรงดัน'
s=S('14_suction_measurement','Suction-side diagnosis: compare location, load and flow conditions','HYDRAULIC MEASUREMENT PRINCIPLE | for a verified vacuum-fed supply; no restriction / vacuum pass limits')
s.box(80,350,240,150,['ถังน้ำมัน','pickup / vent'],BLUE);s.box(750,350,260,150,['กรองน้ำมัน','FILTER'],BLUE);s.box(1450,350,270,150,['ปั๊มส่งเข้าราง','SUPPLY PUMP'],BLUE)
s.line([(320,425),(750,425)],BLUE,6,True);s.line([(1010,425),(1450,425)],BLUE,6,True)
for x,lab in [(560,'A: ก่อนกรอง'),(1210,'B: หลังกรอง')]:
 s.node(x,425);s.line([(x,425),(x,300)],BLUE,4);s.a.append(f'<circle cx="{x}" cy="{250}" r="50" fill="white" stroke="{BLUE}" stroke-width="4"/>');s.text(x-10,260,'P',28,BLUE);s.text(x-100,195,lab,25,BLUE)
s.box(170,650,1460,280,['บันทึกตำแหน่ง A / B, รอบเครื่อง, โหลด, อุณหภูมิ และค่าแบบ gauge หรือ absolute ให้ครบ','เทียบก่อน–หลังกรองภายใต้สภาวะเดียวกัน: ความต่างความดันต้องตีความร่วมกับการไหล','อากาศเข้าด้านดูดอาจไม่มีน้ำมันเปียกภายนอก ตรวจท่อ ข้อต่อ ซีลกรอง และ primer','adapter / sight section ต้องรองรับดีเซลและสุญญากาศ ไม่สร้างจุดรั่วเพิ่ม'],INK)
s.note(['ภาพนี้เป็นการวัดด้านแรงดันต่ำ ไม่ต่อเกจชนิดนี้เข้าท่อ common rail แรงดันสูง','ใช้วิธีและเกณฑ์ของรุ่นจริง ห้ามสร้างค่า vacuum สากล และไม่ปิดท่อดูดเพื่อเร่งให้เครื่องดับ','Pico AGT-833 เป็นแหล่งหลักการ vacuum-fed supply; ภาพนี้ไม่คัดลอกชุดทดสอบเฉพาะเครื่องมือ']);s.finish()

TH['15_return_test_conditions']='ทดสอบน้ำมันกลับ: เทียบได้เมื่อเงื่อนไขเหมือนกัน'
s=S('15_return_test_conditions','Injector return assessment: preserve the correct return-system conditions','TEST-PLANNING WORKFLOW | select approved method for the injector / return-pressure configuration first')
s.box(80,230,1630,130,['เริ่มจากยืนยันชนิดหัวฉีด + part number + ข้อกำหนดแรงดันทางกลับ','เลือกวิธีผู้ผลิต / ชุด adapter ที่ตรงระบบ ก่อนถอดท่อน้ำมันกลับ'],AMBER)
s.box(80,450,490,410,['สิ่งที่ต้องบันทึกร่วม','เวลาเก็บ / ปริมาตรหรือ pressure','อุณหภูมิน้ำมัน / รอบ / โหลด','rail target และ actual','แรงดันทางกลับ / เครื่องมือ'],INK)
s.box(700,450,470,410,['การเปรียบเทียบ','เปรียบเทียบรายสูบและยอดรวม','มองความต่างภายใต้เงื่อนไขเดียว','ค่าชดเชยไม่ใช่ค่า leak-off','ไม่มี mL กลางสำหรับทุกชุด'],GREEN)
s.box(1300,450,410,410,['หลักฐานหลังแก้','ทดสอบซ้ำด้วยเงื่อนไขเดิม','ตรวจการรั่วและ rail tracking','ทำ coding / learning','เฉพาะที่คู่มือกำหนด'],BLUE)
s.line([(570,650),(700,650)],INK,4,True);s.line([(1170,650),(1300,650)],INK,4,True)
s.text(100,970,'ไม่อุดทางกลับ ไม่ตัดแรงดันทางกลับจำเป็น และไม่ใช้วิธี solenoid แทน piezo โดยอัตโนมัติ',27,RED)
s.note(['Pico AGT-786 จำกัดวิธีของตนไว้กับ solenoid / low-return-pressure system; ไม่ใช่สเปก Toyota ทุกคัน','ปริมาณกลับและ balance ขึ้นกับ rail pressure และสภาพระบบรวม จึงต้องเก็บบริบทขณะเกิดอาการ','ภาพเป็นแผนเลือกวิธีตรวจ ไม่ใช่คำสั่งต่อชุดทดสอบที่อนุญาตกับรถทุกแบบ']);s.finish()

TH['16_p0093_evidence_workflow']='P0093: ผังเลือกทางตรวจและพิสูจน์ผลหลังแก้ไข'
s=S('16_p0093_evidence_workflow','Evidence-led workflow: establish variant -> capture event -> test -> repair -> verify','DIAGNOSTIC WORKFLOW | editorial synthesis; follow the vehicle repair manual when it specifies a different path')
s.box(60,210,460,130,['1. ยืนยันรถและระบบ','VIN / ECU / pump / rail variant']);s.box(670,210,470,130,['2. เก็บก่อนลบโค้ด','freeze frame / DTC / pre-event']);s.box(1290,210,450,130,['3. รหัสร่วมและความปลอดภัย','P0200? P1229? รั่วภายนอก?'])
for a,b in [(520,670),(1140,1290)]:s.line([(a,275),(b,275)],INK,4,True)
s.line([(1515,340),(1515,410),(900,410),(900,470)],INK,4,True)
s.box(670,470,470,140,['4. แยกเหตุการณ์แรงดัน','ค่าที่อ่านเชื่อถือได้หรือไม่?'],AMBER)
s.box(60,690,460,150,['สัญญาณยังไม่น่าเชื่อถือ','reference / return / harness','แก้หลักฐานไฟฟ้าที่พบ'],BLUE);s.box(670,690,470,150,['แรงดันตกจริง: เข้า / ออก','supply / SCV / return / relief','ทดสอบเจาะจงตาม variant'],GREEN);s.box(1290,690,450,150,['มี overshoot ก่อนตก','ตรวจ overfeed / limiter','และวาล์วระบายตามระบบ'],RED)
s.line([(670,540),(290,540),(290,690)],BLUE,4,True);s.line([(900,610),(900,690)],GREEN,4,True);s.line([(1140,540),(1515,540),(1515,690)],RED,4,True)
s.line([(290,840),(290,920),(1515,920),(1515,840)],INK,3);s.line([(900,840),(900,950)],INK,4,True);s.node(900,920);s.box(460,950,900,70,['5. แก้ตามหลักฐาน -> ทดสอบซ้ำเงื่อนไขเดิม -> บันทึกผลยืนยัน'],INK)
s.note(['P0200 ร่วม: ใช้ทางตรวจวงจร EDU / หัวฉีดตามคู่มือ ไม่ข้ามไปเปลี่ยนปั๊ม','การอ่าน current / sensor ใช้เป็นหลักฐานประกอบ ไม่ใช่ข้อสรุปชิ้นส่วนเสียโดยลำพัง','ทดสอบซ้ำขณะร้อน / โหลดที่เคยเกิดอาการอย่างปลอดภัย ก่อนปิดงานด้วยการลบโค้ด']);s.finish()
print('created',len(list(P.glob('*.svg'))),'SVG diagrams')
