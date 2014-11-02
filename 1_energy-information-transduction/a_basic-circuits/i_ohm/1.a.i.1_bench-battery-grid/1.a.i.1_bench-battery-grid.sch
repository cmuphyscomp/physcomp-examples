<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="7.1.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="no" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="supply2">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
Please keep in mind, that these devices are necessary for the
automatic wiring of the supply signals.&lt;p&gt;
The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="+09V">
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="94"/>
<wire x1="0" y1="0.635" x2="0" y2="1.905" width="0.1524" layer="94"/>
<circle x="0" y="1.27" radius="1.27" width="0.254" layer="94"/>
<text x="-1.905" y="3.175" size="1.778" layer="96">&gt;VALUE</text>
<pin name="+9V" x="0" y="-2.54" visible="off" length="short" direction="sup" rot="R90"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="+9V" prefix="SUPPLY">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="+09V" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="special">
<description>&lt;b&gt;Special Devices&lt;/b&gt;&lt;p&gt;
7-segment displays, switches, heatsinks, crystals, transformers, etc.&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="LDH-5R">
<description>&lt;B&gt;LED HOLDER&lt;/B&gt;</description>
<wire x1="-1.27" y1="4.445" x2="0.635" y2="4.445" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="5.207" x2="-0.635" y2="3.683" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="3.683" x2="0.635" y2="4.445" width="0.1524" layer="21"/>
<wire x1="0.635" y1="4.445" x2="1.27" y2="4.445" width="0.1524" layer="21"/>
<wire x1="0.635" y1="4.445" x2="-0.635" y2="5.207" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="5.842" x2="0.127" y2="6.604" width="0.1524" layer="21"/>
<wire x1="0" y1="5.461" x2="0.762" y2="6.223" width="0.1524" layer="21"/>
<wire x1="-0.254" y1="6.477" x2="0" y2="6.223" width="0.1524" layer="21"/>
<wire x1="0" y1="6.223" x2="0.127" y2="6.604" width="0.1524" layer="21"/>
<wire x1="0.127" y1="6.604" x2="-0.254" y2="6.477" width="0.1524" layer="21"/>
<wire x1="0.762" y1="6.223" x2="0.381" y2="6.096" width="0.1524" layer="21"/>
<wire x1="0.381" y1="6.096" x2="0.635" y2="5.842" width="0.1524" layer="21"/>
<wire x1="0.635" y1="5.842" x2="0.762" y2="6.223" width="0.1524" layer="21"/>
<wire x1="0.508" y1="6.096" x2="0.635" y2="5.969" width="0.1524" layer="21"/>
<wire x1="-0.127" y1="6.477" x2="0" y2="6.35" width="0.1524" layer="21"/>
<wire x1="0.635" y1="3.683" x2="0.635" y2="5.207" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="1.524" x2="-2.54" y2="6.604" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="6.604" x2="2.54" y2="6.604" width="0.1524" layer="21" curve="-180"/>
<wire x1="2.54" y1="1.524" x2="2.54" y2="6.604" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="1.524" x2="-2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="3.81" y1="1.524" x2="3.81" y2="0" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="1.524" x2="-3.81" y2="0" width="0.1524" layer="21"/>
<wire x1="2.54" y1="1.524" x2="3.81" y2="1.524" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.524" x2="1.905" y2="-6.096" width="0.1524" layer="51"/>
<wire x1="-1.905" y1="1.524" x2="-1.905" y2="-6.096" width="0.1524" layer="51"/>
<wire x1="1.27" y1="4.445" x2="1.27" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="4.445" x2="-1.27" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-6.096" x2="3.302" y2="-6.096" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="1.524" x2="-1.27" y2="1.524" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="1.524" x2="1.27" y2="1.524" width="0.1524" layer="21"/>
<wire x1="1.27" y1="1.524" x2="2.54" y2="1.524" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0" x2="3.302" y2="0" width="0.0508" layer="21"/>
<wire x1="3.81" y1="0" x2="3.81" y2="-6.096" width="0.1524" layer="21"/>
<wire x1="3.302" y1="-6.096" x2="3.302" y2="0" width="0.0508" layer="21"/>
<wire x1="3.302" y1="-6.096" x2="3.81" y2="-6.096" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0" x2="-4.318" y2="0" width="0.0508" layer="21"/>
<wire x1="-3.81" y1="0" x2="-3.81" y2="-6.096" width="0.1524" layer="21"/>
<wire x1="-4.318" y1="-6.096" x2="-4.318" y2="0" width="0.0508" layer="21"/>
<wire x1="-4.318" y1="-6.096" x2="-3.81" y2="-6.096" width="0.0508" layer="21"/>
<circle x="2.54" y="0" radius="0.635" width="0.1524" layer="21"/>
<circle x="-2.54" y="0" radius="0.635" width="0.1524" layer="21"/>
<pad name="1" x="-1.27" y="-5.08" drill="0.8128" shape="long" rot="R90"/>
<pad name="2" x="1.27" y="-5.08" drill="0.8128" shape="long" rot="R90"/>
<text x="-4.318" y="-7.747" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-4.318" y="-9.271" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
<hole x="2.54" y="0" drill="1.2192"/>
<hole x="-2.54" y="0" drill="1.2192"/>
</package>
<package name="BATTERY">
<description>&lt;B&gt;BATTERY&lt;/B&gt;&lt;p&gt;
22 mm</description>
<wire x1="0.635" y1="2.54" x2="0.635" y2="0" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0" x2="-0.635" y2="0" width="0.1524" layer="21"/>
<wire x1="0.635" y1="0" x2="2.54" y2="0" width="0.1524" layer="21"/>
<wire x1="0.635" y1="0" x2="0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-3.175" x2="2.54" y2="-3.175" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-2.54" x2="1.905" y2="-3.81" width="0.1524" layer="21"/>
<circle x="0" y="0" radius="11.43" width="0.1524" layer="21"/>
<circle x="0" y="0" radius="10.2362" width="0.1524" layer="21"/>
<pad name="-" x="-5.715" y="0" drill="1.016" shape="long"/>
<pad name="+" x="9.525" y="-5.08" drill="1.016" shape="long"/>
<pad name="+@1" x="9.525" y="5.08" drill="1.016" shape="long"/>
<text x="-4.1656" y="6.35" size="1.778" layer="25" ratio="10">&gt;NAME</text>
<text x="-4.445" y="3.81" size="1.778" layer="27" ratio="10">&gt;VALUE</text>
<rectangle x1="-0.635" y1="-1.27" x2="0" y2="1.27" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="LAMP">
<wire x1="4.064" y1="2.286" x2="4.064" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="4.064" y1="-2.54" x2="2.54" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="-1.524" y1="-2.54" x2="-1.524" y2="2.286" width="0.4064" layer="94"/>
<wire x1="0" y1="1.27" x2="0" y2="-2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="-1.524" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="2.54" y1="1.27" x2="2.54" y2="-2.54" width="0.254" layer="94"/>
<wire x1="2.54" y1="-2.54" x2="0" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="0" y1="1.27" x2="1.2959" y2="2.5651" width="0.254" layer="94" curve="-92.32742" cap="flat"/>
<wire x1="1.2954" y1="2.54" x2="2.5654" y2="1.27" width="0.254" layer="94" curve="-90" cap="flat"/>
<wire x1="-1.524" y1="2.286" x2="1.2957" y2="5.1055" width="0.4064" layer="94" curve="-91.045739" cap="flat"/>
<wire x1="1.2954" y1="5.08" x2="4.0894" y2="2.286" width="0.4064" layer="94" curve="-90" cap="flat"/>
<text x="-2.54" y="-2.54" size="1.778" layer="95" rot="R90">&gt;NAME</text>
<text x="6.985" y="-2.54" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<pin name="1" x="0" y="-5.08" visible="off" length="short" direction="pas" swaplevel="1" rot="R90"/>
<pin name="2" x="2.54" y="-5.08" visible="off" length="short" direction="pas" swaplevel="1" rot="R90"/>
</symbol>
<symbol name="BATTERY">
<wire x1="-1.27" y1="3.81" x2="-1.27" y2="-3.81" width="0.4064" layer="94"/>
<wire x1="0" y1="1.27" x2="0" y2="-1.27" width="0.4064" layer="94"/>
<wire x1="1.27" y1="3.81" x2="1.27" y2="-3.81" width="0.4064" layer="94"/>
<wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.4064" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.524" y2="0" width="0.1524" layer="94"/>
<text x="-3.81" y="5.08" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-6.35" size="1.778" layer="96">&gt;VALUE</text>
<pin name="-" x="5.08" y="0" visible="off" length="short" direction="pwr" rot="R180"/>
<pin name="+" x="-5.08" y="0" visible="off" length="short" direction="pwr"/>
<pin name="+@1" x="-2.54" y="0" visible="off" length="short" direction="pwr" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="LAMP" prefix="LMP" uservalue="yes">
<description>&lt;B&gt;LED HOLDER&lt;/B&gt;</description>
<gates>
<gate name="G$1" symbol="LAMP" x="0" y="0"/>
</gates>
<devices>
<device name="" package="LDH-5R">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BATTERY" prefix="BAT" uservalue="yes">
<description>&lt;B&gt;BATTERY&lt;/B&gt;</description>
<gates>
<gate name="G$1" symbol="BATTERY" x="0" y="0"/>
</gates>
<devices>
<device name="" package="BATTERY">
<connects>
<connect gate="G$1" pin="+" pad="+"/>
<connect gate="G$1" pin="+@1" pad="+@1"/>
<connect gate="G$1" pin="-" pad="-"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="supply1">
<description>&lt;b&gt;Supply Symbols&lt;/b&gt;&lt;p&gt;
 GND, VCC, 0V, +5V, -5V, etc.&lt;p&gt;
 Please keep in mind, that these devices are necessary for the
 automatic wiring of the supply signals.&lt;p&gt;
 The pin name defined in the symbol is identical to the net which is to be wired automatically.&lt;p&gt;
 In this library the device names are the same as the pin names of the symbols, therefore the correct signal names appear next to the supply symbols in the schematic.&lt;p&gt;
 &lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
</packages>
<symbols>
<symbol name="GND">
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="-2.54" size="1.778" layer="96">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GND" prefix="GND">
<description>&lt;b&gt;SUPPLY SYMBOL&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="voltmeter">
<packages>
<package name="VOLTMETER">
<circle x="0" y="0" radius="3.5921" width="0.127" layer="21"/>
<text x="0" y="0" size="2.1844" layer="21" align="center">V</text>
<pad name="P$1" x="-3.81" y="0" drill="0.8" shape="square"/>
<pad name="P$2" x="3.81" y="0" drill="0.8" shape="square"/>
</package>
</packages>
<symbols>
<symbol name="VOLTMETER">
<circle x="0" y="0" radius="7.184203125" width="0.254" layer="94"/>
<text x="0" y="0" size="5.08" layer="94" align="center">V</text>
<pin name="VIN" x="-7.62" y="0" length="middle" rot="R180"/>
<pin name="GND" x="7.62" y="0" length="middle"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="VOLTMETER">
<gates>
<gate name="G$1" symbol="VOLTMETER" x="0" y="0"/>
</gates>
<devices>
<device name="" package="VOLTMETER">
<connects>
<connect gate="G$1" pin="GND" pad="P$1"/>
<connect gate="G$1" pin="VIN" pad="P$2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="SUPPLY1" library="supply2" deviceset="+9V" device=""/>
<part name="LMP1" library="special" deviceset="LAMP" device=""/>
<part name="SUPPLY2" library="supply2" deviceset="+9V" device="" value="+120V"/>
<part name="BAT1" library="special" deviceset="BATTERY" device="" value="+9V"/>
<part name="GND1" library="supply1" deviceset="GND" device=""/>
<part name="GND2" library="supply1" deviceset="GND" device=""/>
<part name="U$1" library="voltmeter" deviceset="VOLTMETER" device=""/>
<part name="U$2" library="voltmeter" deviceset="VOLTMETER" device=""/>
<part name="U$3" library="voltmeter" deviceset="VOLTMETER" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="SUPPLY1" gate="G$1" x="-22.86" y="63.5"/>
<instance part="LMP1" gate="G$1" x="63.5" y="71.12"/>
<instance part="SUPPLY2" gate="G$1" x="15.24" y="63.5"/>
<instance part="BAT1" gate="G$1" x="66.04" y="50.8"/>
<instance part="GND1" gate="1" x="2.54" y="38.1"/>
<instance part="GND2" gate="1" x="40.64" y="38.1"/>
<instance part="U$1" gate="G$1" x="66.04" y="30.48"/>
<instance part="U$2" gate="G$1" x="27.94" y="50.8"/>
<instance part="U$3" gate="G$1" x="-10.16" y="50.8"/>
</instances>
<busses>
</busses>
<nets>
<net name="+9V" class="0">
<segment>
<pinref part="SUPPLY1" gate="G$1" pin="+9V"/>
<wire x1="-22.86" y1="60.96" x2="-22.86" y2="50.8" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="SUPPLY2" gate="G$1" pin="+9V"/>
<wire x1="15.24" y1="60.96" x2="15.24" y2="50.8" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="GND1" gate="1" pin="GND"/>
<wire x1="2.54" y1="50.8" x2="2.54" y2="40.64" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="GND2" gate="1" pin="GND"/>
<wire x1="40.64" y1="50.8" x2="40.64" y2="40.64" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="BAT1" gate="G$1" pin="+"/>
<wire x1="60.96" y1="50.8" x2="60.96" y2="66.04" width="0.1524" layer="91"/>
<pinref part="LMP1" gate="G$1" pin="1"/>
<wire x1="60.96" y1="66.04" x2="63.5" y2="66.04" width="0.1524" layer="91"/>
<wire x1="53.34" y1="30.48" x2="53.34" y2="50.8" width="0.1524" layer="91"/>
<wire x1="53.34" y1="50.8" x2="60.96" y2="50.8" width="0.1524" layer="91"/>
<junction x="60.96" y="50.8"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="BAT1" gate="G$1" pin="-"/>
<wire x1="71.12" y1="50.8" x2="71.12" y2="66.04" width="0.1524" layer="91"/>
<pinref part="LMP1" gate="G$1" pin="2"/>
<wire x1="71.12" y1="66.04" x2="66.04" y2="66.04" width="0.1524" layer="91"/>
<wire x1="78.74" y1="30.48" x2="78.74" y2="50.8" width="0.1524" layer="91"/>
<wire x1="78.74" y1="50.8" x2="71.12" y2="50.8" width="0.1524" layer="91"/>
<junction x="71.12" y="50.8"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
