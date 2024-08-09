from unittest import TestCase

from chains.weather_assistant import OllamaWeatherAssistantChain


class TestOllamaWeatherAssistantChain(TestCase):
    def test_init(self):
        chain = OllamaWeatherAssistantChain()
        print(chain.chain.invoke("我在北京"))

    def test_cities(self):
        cts = '北京/北京,北京/东城,北京/西城,北京/朝阳,北京/丰台,北京/石景山,北京/海淀,北京/门头沟,北京/房山,北京/通州,北京/顺义,北京/昌平,北京/大兴,北京/怀柔,北京/平谷,北京/密云,北京/延庆,天津/天津,天津/和平,天津/河东,天津/河西,天津/南开,天津/河北,天津/红桥,天津/东丽,天津/西青,天津/津南,天津/北辰,天津/武清,天津/宝坻,天津/滨海新区,天津/宁河,天津/静海,天津/蓟州,河北/石家庄/石家庄,河北/石家庄/长安,河北/石家庄/桥西,河北/石家庄/新华,河北/石家庄/井陉,河北/石家庄/裕华,河北/石家庄/藁城,河北/石家庄/鹿泉,河北/石家庄/栾城,河北/石家庄/井陉,河北/石家庄/正定,河北/石家庄/行唐,河北/石家庄/灵寿,河北/石家庄/高邑,河北/石家庄/深泽,河北/石家庄/赞皇,河北/石家庄/无极,河北/石家庄/平山,河北/石家庄/元氏,河北/石家庄/赵县,河北/石家庄/辛集,河北/石家庄/晋州,河北/石家庄/新乐,河北/唐山/唐山,河北/唐山/路南,河北/唐山/路北,河北/唐山/古冶,河北/唐山/开平,河北/唐山/丰南,河北/唐山/丰润,河北/唐山/曹妃甸,河北/唐山/滦南,河北/唐山/乐亭,河北/唐山/迁西,河北/唐山/玉田,河北/唐山/遵化,河北/唐山/迁安,河北/唐山/滦州,河北/秦皇岛/秦皇岛,河北/秦皇岛/海港,河北/秦皇岛/山海关,河北/秦皇岛/北戴河,河北/秦皇岛/抚宁,河北/秦皇岛/青龙,河北/秦皇岛/昌黎,河北/秦皇岛/卢龙,河北/邯郸/邯郸,河北/邯郸/邯山,河北/邯郸/丛台,河北/邯郸/复兴,河北/邯郸/峰峰,河北/邯郸/肥乡,河北/邯郸/永年,河北/邯郸/临漳,河北/邯郸/成安,河北/邯郸/大名,河北/邯郸/涉县,河北/邯郸/磁县,河北/邯郸/邱县,河北/邯郸/鸡泽,河北/邯郸/广平,河北/邯郸/馆陶,河北/邯郸/魏县,河北/邯郸/曲周,河北/邯郸/武安,河北/邢台,河北/邢台/桥东,河北/邢台/桥西,河北/邢台/邢台,河北/邢台/临城,河北/邢台/内丘,河北/邢台/柏乡,河北/邢台/隆尧,河北/邢台/任县,河北/邢台/南和,河北/邢台/宁晋,河北/邢台/巨鹿,河北/邢台/新河,河北/邢台/广宗,河北/邢台/平乡,河北/邢台/威县,河北/邢台/清河,河北/邢台/临西,河北/邢台/南宫,河北/邢台/沙河,河北/保定/保定,河北/保定/竞秀,河北/保定/莲池,河北/保定/满城,河北/保定/清苑,河北/保定/徐水,河北/保定/涞水,河北/保定/阜平,河北/保定/定兴,河北/保定/唐县,河北/保定/高阳,河北/保定/容城,河北/保定/涞源,河北/保定/望都,河北/保定/安新,河北/保定/易县,河北/保定/曲阳,河北/保定/蠡县,河北/保定/顺平,河北/保定/博野,河北/保定/雄县,河北/保定/涿州,河北/保定/定州,河北/保定/安国,河北/保定/高碑店,河北/张家口/张家口,河北/张家口/桥东,河北/张家口/桥西,河北/张家口/宣化,河北/张家口/下花园,河北/张家口/万全,河北/张家口/崇礼,河北/张家口/张北,河北/张家口/康保,河北/张家口/沽源,河北/张家口/尚义,河北/张家口/蔚县,河北/张家口/阳原,河北/张家口/怀安,河北/张家口/怀来,河北/张家口/涿鹿,河北/张家口/赤城,河北/承德/承德,河北/承德/双桥,河北/承德/双滦,河北/承德/鹰手营,河北/承德/承德县,河北/承德/兴隆,河北/承德/滦平,河北/承德/隆化,河北/承德/丰宁,河北/承德/宽城,河北/承德/围场,河北/承德/平泉,河北/沧州/沧州,河北/沧州/新华,河北/沧州/运河,河北/沧州/沧县,河北/沧州/青县,河北/沧州/东光,河北/沧州/海兴,河北/沧州/盐山,河北/沧州/肃宁,河北/沧州/南皮,河北/沧州/吴桥,河北/沧州/献县,河北/沧州/孟村,河北/沧州/泊头,河北/沧州/任丘,河北/沧州/黄骅,河北/沧州/河间,河北/廊坊/廊坊,河北/廊坊/安次,河北/廊坊/广阳,河北/廊坊/固安,河北/廊坊/永清,河北/廊坊/香河,河北/廊坊/大城,河北/廊坊/文安,河北/廊坊/大厂,河北/廊坊/霸州,河北/廊坊/三河,河北/衡水/衡水,河北/衡水/桃城,河北/衡水/冀州,河北/衡水/枣强,河北/衡水/武邑,河北/衡水/武强,河北/衡水/饶阳,河北/衡水/安平,河北/衡水/故城,河北/衡水/景县,河北/衡水/阜城,河北/衡水/深州,山西/太原/太原,山西/太原/小店区,山西/太原/迎泽,山西/太原/杏花岭,山西/太原/尖草坪区,山西/太原/万柏林,山西/太原/晋源,山西/太原/清徐,山西/太原/阳曲,山西/太原/娄烦,山西/太原/古交,山西/大同/大同,山西/大同/新荣,山西/大同/平城,山西/大同/云冈,山西/大同/云州,山西/大同/阳高,山西/大同/天镇,山西/大同/广灵,山西/大同/灵丘,山西/大同/浑源,山西/大同/左云,山西/阳泉,山西/阳泉/阳泉,山西/阳泉/矿区,山西/阳泉/郊区,山西/阳泉/平定,山西/阳泉/盂县,山西/长治/长治,山西/长治/潞州,山西/长治/上党,山西/长治/屯留,山西/长治/潞城,山西/长治/襄垣,山西/长治/平顺,山西/长治/黎城,山西/长治/壶关,山西/长治/长子,山西/长治/武乡,山西/长治/沁县,山西/长治/沁源,山西/晋城,山西/晋城/晋城,山西/晋城/沁水,山西/晋城/阳城,山西/晋城/陵川,山西/晋城/泽州,山西/晋城/高平,山西/朔州/朔州,山西/朔州/朔城,山西/朔州/平鲁,山西/朔州/山阴,山西/朔州/应县,山西/朔州/右玉,山西/朔州/怀仁,山西/晋中/晋中,山西/晋中/榆次,山西/晋中/榆社,山西/晋中/左权,山西/晋中/和顺,山西/晋中/昔阳,山西/晋中/寿阳,山西/晋中/太谷,山西/晋中/祁县,山西/晋中/平遥,山西/晋中/灵石,山西/晋中/介休,山西/运城/运城,山西/运城/盐湖,山西/运城/临猗,山西/运城/万荣,山西/运城/闻喜,山西/运城/稷山,山西/运城/新绛,山西/运城/绛县,山西/运城/垣曲,山西/运城/夏县,山西/运城/平陆,山西/运城/芮城,山西/运城/永济,山西/运城/河津,山西/忻州/忻州,山西/忻州/忻府,山西/忻州/定襄,山西/忻州/五台县,山西/忻州/代县,山西/忻州/繁峙,山西/忻州/宁武,山西/忻州/静乐,山西/忻州/神池,山西/忻州/五寨,山西/忻州/岢岚,山西/忻州/河曲,山西/忻州/保德,山西/忻州/偏关,山西/忻州/原平,山西/临汾/临汾,山西/临汾/尧都,山西/临汾/曲沃,山西/临汾/翼城,山西/临汾/襄汾,山西/临汾/洪洞,山西/临汾/古县,山西/临汾/安泽,山西/临汾/浮山,山西/临汾/吉县,山西/临汾/乡宁,山西/临汾/大宁,山西/临汾/隰县,山西/临汾/永和,山西/临汾/蒲县,山西/临汾/汾西,山西/临汾/侯马,山西/临汾/霍州,山西/吕梁/吕梁,山西/吕梁/离石,山西/吕梁/文水,山西/吕梁/交城,山西/吕梁/兴县,山西/吕梁/临县,山西/吕梁/柳林,山西/吕梁/石楼,山西/吕梁/岚县,山西/吕梁/方山,山西/吕梁/中阳,山西/吕梁/交口,山西/吕梁/孝义,山西/吕梁/汾阳,内蒙古/呼和浩特/呼和浩特,内蒙古/呼和浩特/新城,内蒙古/呼和浩特/回民,内蒙古/呼和浩特/玉泉,内蒙古/呼和浩特/赛罕,内蒙古/呼和浩特/土左旗,内蒙古/呼和浩特/托县,内蒙古/呼和浩特/和林,内蒙古/呼和浩特/清水河,内蒙古/呼和浩特/武川,内蒙古/包头/包头,内蒙古/包头/东河,内蒙古/包头/昆都仑,内蒙古/包头/青山,内蒙古/包头/石拐,内蒙古/包头/白云鄂博,内蒙古/包头/九原,内蒙古/包头/土右旗,内蒙古/包头/固阳,内蒙古/包头/达茂旗,内蒙古/乌海/乌海,内蒙古/乌海/海勃湾,内蒙古/乌海/海南,内蒙古/乌海/乌达,内蒙古/赤峰/赤峰,内蒙古/赤峰/红山,内蒙古/赤峰/元宝山,内蒙古/赤峰/松山,内蒙古/赤峰/阿鲁旗,内蒙古/赤峰/巴林左旗,内蒙古/赤峰/巴林右旗,内蒙古/赤峰/林西,内蒙古/赤峰/克什克腾,内蒙古/赤峰/翁牛特,内蒙古/赤峰/喀喇沁,内蒙古/赤峰/宁城,内蒙古/赤峰/敖汉,内蒙古/通辽/通辽,内蒙古/通辽/科尔沁,内蒙古/通辽/科左中旗,内蒙古/通辽/科左后旗,内蒙古/通辽/开鲁,内蒙古/通辽/库伦,内蒙古/通辽/奈曼,内蒙古/通辽/扎鲁特,内蒙古/通辽/霍林郭勒,内蒙古/鄂尔多斯/鄂尔多斯,内蒙古/鄂尔多斯/东胜,内蒙古/鄂尔多斯/康巴什,内蒙古/鄂尔多斯/达拉特,内蒙古/鄂尔多斯/准格尔,内蒙古/鄂尔多斯/鄂前旗,内蒙古/鄂尔多斯/鄂托克,内蒙古/鄂尔多斯/杭锦旗,内蒙古/鄂尔多斯/乌审旗,内蒙古/鄂尔多斯/伊金霍洛,内蒙古/内蒙古/呼伦贝尔,内蒙古/呼伦贝尔/海拉尔,内蒙古/呼伦贝尔/扎赉诺尔,内蒙古/呼伦贝尔/阿荣旗,内蒙古/呼伦贝尔/莫力达瓦,内蒙古/呼伦贝尔/鄂伦春旗,内蒙古/呼伦贝尔/鄂温克旗,内蒙古/呼伦贝尔/陈旗,内蒙古/呼伦贝尔/新左旗,内蒙古/呼伦贝尔/新右旗,内蒙古/呼伦贝尔/满洲里,内蒙古/呼伦贝尔/牙克石,内蒙古/呼伦贝尔/扎兰屯,内蒙古/呼伦贝尔/额尔古纳,内蒙古/呼伦贝尔/根河,内蒙古/内蒙古/巴彦淖尔,内蒙古/巴彦淖尔/临河,内蒙古/巴彦淖尔/五原,内蒙古/巴彦淖尔/磴口,内蒙古/巴彦淖尔/乌前旗,内蒙古/巴彦淖尔/乌中旗,内蒙古/巴彦淖尔/乌后旗,内蒙古/巴彦淖尔/杭锦后旗,内蒙古/内蒙古/乌兰察布,内蒙古/乌兰察布/集宁,内蒙古/乌兰察布/卓资,内蒙古/乌兰察布/化德,内蒙古/乌兰察布/商都,内蒙古/乌兰察布/兴和,内蒙古/乌兰察布/凉城,内蒙古/乌兰察布/察右前旗,内蒙古/乌兰察布/察右中旗,内蒙古/乌兰察布/察右后旗,内蒙古/乌兰察布/四子王旗,内蒙古/乌兰察布/丰镇,内蒙古/兴安盟/兴安,内蒙古/兴安盟/乌兰浩特,内蒙古/兴安盟/阿尔山,内蒙古/兴安盟/科右前旗,内蒙古/兴安盟/科右中旗,内蒙古/兴安盟/扎赉特,内蒙古/兴安盟/突泉,内蒙古/内蒙古/锡林郭勒,内蒙古/锡林郭勒/二连浩特,内蒙古/锡林郭勒/锡林浩特,内蒙古/锡林郭勒/阿巴嘎,内蒙古/锡林郭勒/苏左旗,内蒙古/锡林郭勒/苏右旗,内蒙古/锡林郭勒/东乌旗,内蒙古/锡林郭勒/西乌旗,内蒙古/锡林郭勒/太仆寺,内蒙古/锡林郭勒/镶黄旗,内蒙古/锡林郭勒/正镶白旗,内蒙古/锡林郭勒/正蓝旗,内蒙古/锡林郭勒/多伦,内蒙古/阿拉善盟/阿拉善,内蒙古/阿拉善盟/阿左旗,内蒙古/阿拉善盟/阿右旗,内蒙古/阿拉善盟/额济纳,辽宁/沈阳/沈阳,辽宁/沈阳/和平,辽宁/沈阳/沈河,辽宁/沈阳/大东,辽宁/沈阳/皇姑,辽宁/沈阳/铁西,辽宁/沈阳/苏家屯,辽宁/沈阳/浑南,辽宁/沈阳/沈北新区,辽宁/沈阳/于洪,辽宁/沈阳/辽中,辽宁/沈阳/康平,辽宁/沈阳/法库,辽宁/沈阳/新民,辽宁/大连/大连,辽宁/大连/中山,辽宁/大连/西岗,辽宁/大连/沙河口,辽宁/大连/甘井子,辽宁/大连/旅顺,辽宁/大连/金州,辽宁/大连/普兰店,辽宁/大连/长海,辽宁/大连/瓦房店,辽宁/大连/庄河,辽宁/鞍山/鞍山,辽宁/鞍山/铁东,辽宁/鞍山/铁西,辽宁/鞍山/立山,辽宁/鞍山/千山,辽宁/鞍山/台安,辽宁/鞍山/岫岩,辽宁/鞍山/海城,辽宁/抚顺,辽宁/抚顺/新抚,辽宁/抚顺/东洲,辽宁/抚顺/望花,辽宁/抚顺/顺城,辽宁/抚顺/抚顺,辽宁/抚顺/新宾,辽宁/抚顺/清原,辽宁/本溪/本溪,辽宁/本溪/平山,辽宁/本溪/溪湖,辽宁/本溪/明山,辽宁/本溪/南芬,辽宁/本溪/本溪县,辽宁/本溪/桓仁,辽宁/丹东/丹东,辽宁/丹东/元宝,辽宁/丹东/振兴,辽宁/丹东/振安,辽宁/丹东/宽甸,辽宁/丹东/东港,辽宁/丹东/凤城,辽宁/锦州/锦州,辽宁/锦州/古塔,辽宁/锦州/凌河,辽宁/锦州/太和,辽宁/锦州/黑山,辽宁/锦州/义县,辽宁/锦州/凌海,辽宁/锦州/北镇,辽宁/营口/营口,辽宁/营口/站前,辽宁/营口/西市,辽宁/营口/鲅鱼圈,辽宁/营口/老边,辽宁/营口/盖州,辽宁/营口/大石桥,辽宁/阜新,辽宁/阜新/海州,辽宁/阜新/新邱,辽宁/阜新/太平,辽宁/阜新/清河门,辽宁/阜新/细河,辽宁/阜新/阜新,辽宁/阜新/彰武,辽宁/辽阳/辽阳,辽宁/辽阳/白塔,辽宁/辽阳/文圣,辽宁/辽阳/宏伟,辽宁/辽阳/弓长岭,辽宁/辽阳/太子河,辽宁/辽阳/辽阳县,辽宁/辽阳/灯塔,辽宁/盘锦/盘锦,辽宁/盘锦/双台子,辽宁/盘锦/兴隆台,辽宁/盘锦/大洼,辽宁/盘锦/盘山,辽宁/铁岭,辽宁/铁岭/银州,辽宁/铁岭/清河,辽宁/铁岭/铁岭,辽宁/铁岭/西丰,辽宁/铁岭/昌图,辽宁/铁岭/调兵山,辽宁/铁岭/开原,辽宁/朝阳,辽宁/朝阳/双塔,辽宁/朝阳/龙城,辽宁/朝阳/朝阳,辽宁/朝阳/建平县,辽宁/朝阳/喀左,辽宁/朝阳/北票,辽宁/朝阳/凌源,辽宁/葫芦岛/葫芦岛,辽宁/葫芦岛/连山,辽宁/葫芦岛/龙港,辽宁/葫芦岛/南票,辽宁/葫芦岛/绥中,辽宁/葫芦岛/建昌,辽宁/葫芦岛/兴城,吉林/长春/长春,吉林/长春/南关,吉林/长春/宽城,吉林/长春/朝阳,吉林/长春/二道,吉林/长春/绿园,吉林/长春/双阳,吉林/长春/九台,吉林/长春/农安,吉林/长春/榆树,吉林/长春/德惠,吉林/吉林/吉林,吉林/吉林/昌邑,吉林/吉林/龙潭,吉林/吉林/船营,吉林/吉林/丰满,吉林/吉林/永吉,吉林/吉林/蛟河,吉林/吉林/桦甸,吉林/吉林/舒兰,吉林/吉林/磐石,吉林/四平/四平,吉林/四平/铁西,吉林/四平/铁东,吉林/四平/梨树,吉林/四平/伊通,吉林/四平/公主岭,吉林/四平/双辽,吉林/辽源/辽源,吉林/辽源/龙山,吉林/辽源/西安,吉林/辽源/东丰,吉林/辽源/东辽,吉林/通化/通化,吉林/通化/东昌,吉林/通化/二道江,吉林/通化/通化县,吉林/通化/辉南,吉林/通化/柳河,吉林/通化/梅河口,吉林/通化/集安,吉林/白山/白山,吉林/白山/浑江,吉林/白山/江源,吉林/白山/抚松,吉林/白山/靖宇,吉林/白山/长白,吉林/白山/临江,吉林/松原/松原,吉林/松原/宁江,吉林/松原/前郭,吉林/松原/长岭,吉林/松原/乾安,吉林/松原/扶余,吉林/白城/白城,吉林/白城/洮北,吉林/白城/镇赉,吉林/白城/通榆,吉林/白城/洮南,吉林/白城/大安,吉林/吉林/延边,吉林/延边/延吉,吉林/延边/图们,吉林/延边/敦化,吉林/延边/珲春,吉林/延边/龙井,吉林/延边/和龙,吉林/延边/汪清,吉林/延边/安图,黑龙江/哈尔滨/哈尔滨,黑龙江/哈尔滨/道里,黑龙江/哈尔滨/南岗,黑龙江/哈尔滨/道外,黑龙江/哈尔滨/平房,黑龙江/哈尔滨/松北,黑龙江/哈尔滨/香坊,黑龙江/哈尔滨/呼兰,黑龙江/哈尔滨/阿城,黑龙江/哈尔滨/双城,黑龙江/哈尔滨/依兰,黑龙江/哈尔滨/方正,黑龙江/哈尔滨/宾县,黑龙江/哈尔滨/巴彦,黑龙江/哈尔滨/木兰,黑龙江/哈尔滨/通河,黑龙江/哈尔滨/延寿,黑龙江/哈尔滨/尚志,黑龙江/哈尔滨/五常,黑龙江/齐齐哈尔/齐齐哈尔,黑龙江/齐齐哈尔/龙沙,黑龙江/齐齐哈尔/建华,黑龙江/齐齐哈尔/铁锋,黑龙江/齐齐哈尔/昂昂溪,黑龙江/齐齐哈尔/富拉尔基,黑龙江/齐齐哈尔/碾子山,黑龙江/齐齐哈尔/梅里斯,黑龙江/齐齐哈尔/龙江,黑龙江/齐齐哈尔/依安,黑龙江/齐齐哈尔/泰来,黑龙江/齐齐哈尔/甘南,黑龙江/齐齐哈尔/富裕,黑龙江/齐齐哈尔/克山,黑龙江/齐齐哈尔/克东,黑龙江/齐齐哈尔/拜泉,黑龙江/齐齐哈尔/讷河,黑龙江/鸡西/鸡西,黑龙江/鸡西/鸡冠,黑龙江/鸡西/恒山,黑龙江/鸡西/滴道,黑龙江/鸡西/梨树,黑龙江/鸡西/城子河,黑龙江/鸡西/麻山,黑龙江/鸡西/鸡东,黑龙江/鸡西/虎林,黑龙江/鸡西/密山,黑龙江/鹤岗/鹤岗,黑龙江/鹤岗/向阳,黑龙江/鹤岗/工农,黑龙江/鹤岗/南山,黑龙江/鹤岗/兴安,黑龙江/鹤岗/东山,黑龙江/鹤岗/兴山,黑龙江/鹤岗/萝北,黑龙江/鹤岗/绥滨,黑龙江/双鸭山/双鸭山,黑龙江/双鸭山/尖山,黑龙江/双鸭山/岭东,黑龙江/双鸭山/四方台,黑龙江/双鸭山/宝山,黑龙江/双鸭山/集贤,黑龙江/双鸭山/友谊,黑龙江/双鸭山/宝清,黑龙江/双鸭山/饶河,黑龙江/大庆/大庆,黑龙江/大庆/萨尔图,黑龙江/大庆/龙凤,黑龙江/大庆/让胡路,黑龙江/大庆/红岗,黑龙江/大庆/大同,黑龙江/大庆/肇州,黑龙江/大庆/肇源,黑龙江/大庆/林甸,黑龙江/大庆/杜尔伯特,黑龙江/伊春,黑龙江/伊春/伊春,黑龙江/伊春/南岔,黑龙江/伊春/友好,黑龙江/伊春/西林,黑龙江/伊春/翠峦,黑龙江/伊春/新青,黑龙江/伊春/美溪,黑龙江/伊春/金山屯,黑龙江/伊春/五营,黑龙江/伊春/乌马河,黑龙江/伊春/汤旺河,黑龙江/伊春/带岭,黑龙江/伊春/乌伊岭,黑龙江/伊春/红星,黑龙江/伊春/上甘岭,黑龙江/伊春/嘉荫,黑龙江/伊春/铁力,黑龙江/佳木斯/佳木斯,黑龙江/佳木斯/向阳,黑龙江/佳木斯/前进,黑龙江/佳木斯/东风,黑龙江/佳木斯/郊区,黑龙江/佳木斯/桦南,黑龙江/佳木斯/桦川,黑龙江/佳木斯/汤原,黑龙江/佳木斯/同江,黑龙江/佳木斯/富锦,黑龙江/佳木斯/抚远,黑龙江/七台河/七台河,黑龙江/七台河/新兴,黑龙江/七台河/桃山,黑龙江/七台河/茄子河,黑龙江/七台河/勃利,黑龙江/牡丹江/牡丹江,黑龙江/牡丹江/东安,黑龙江/牡丹江/阳明,黑龙江/牡丹江/爱民,黑龙江/牡丹江/西安,黑龙江/牡丹江/林口,黑龙江/牡丹江/绥芬河,黑龙江/牡丹江/海林,黑龙江/牡丹江/宁安,黑龙江/牡丹江/穆棱,黑龙江/牡丹江/东宁,黑龙江/黑河/黑河,黑龙江/黑河/爱辉,黑龙江/黑河/嫩江,黑龙江/黑河/逊克,黑龙江/黑河/孙吴,黑龙江/黑河/北安,黑龙江/黑河/五大连池,黑龙江/绥化/绥化,黑龙江/绥化/北林,黑龙江/绥化/望奎,黑龙江/绥化/兰西,黑龙江/绥化/青冈,黑龙江/绥化/庆安,黑龙江/绥化/明水,黑龙江/绥化/绥棱,黑龙江/绥化/安达,黑龙江/绥化/肇东,黑龙江/绥化/海伦,黑龙江/大兴安岭/大兴安岭,黑龙江/大兴安岭/漠河,黑龙江/大兴安岭/加格达奇,黑龙江/大兴安岭/呼玛,黑龙江/大兴安岭/塔河,上海/上海,上海/黄浦,上海/徐汇区,上海/长宁,上海/静安,上海/普陀,上海/虹口,上海/杨浦,上海/闵行,上海/宝山,上海/嘉定,上海/浦东新区,上海/金山,上海/松江,上海/青浦,上海/奉贤,上海/崇明,江苏/南京/南京,江苏/南京/玄武,江苏/南京/秦淮,江苏/南京/建邺,江苏/南京/鼓楼,江苏/南京/浦口,江苏/南京/栖霞,江苏/南京/雨花台,江苏/南京/江宁,江苏/南京/六合,江苏/南京/溧水,江苏/南京/高淳,江苏/无锡/无锡,江苏/无锡/锡山,江苏/无锡/惠山,江苏/无锡/滨湖,江苏/无锡/梁溪,江苏/无锡/新吴,江苏/无锡/江阴,江苏/无锡/宜兴,江苏/徐州/徐州,江苏/徐州/鼓楼,江苏/徐州/云龙,江苏/徐州/贾汪,江苏/徐州/泉山,江苏/徐州/铜山,江苏/徐州/丰县,江苏/徐州/沛县,江苏/徐州/睢宁,江苏/徐州/新沂,江苏/徐州/邳州,江苏/常州/常州,江苏/常州/天宁,江苏/常州/钟楼,江苏/常州/新北,江苏/常州/武进,江苏/常州/金坛,江苏/常州/溧阳,江苏/苏州/苏州,江苏/苏州/虎丘,江苏/苏州/吴中,江苏/苏州/相城,江苏/苏州/姑苏,江苏/苏州/吴江,江苏/苏州/常熟,江苏/苏州/张家港,江苏/苏州/昆山,江苏/苏州/太仓,江苏/南通/南通,江苏/南通/崇川,江苏/南通/港闸,江苏/南通/通州,江苏/南通/如东,江苏/南通/启东,江苏/南通/如皋,江苏/南通/海门,江苏/南通/海安,江苏/连云港/连云港,江苏/连云港/连云,江苏/连云港/海州,江苏/连云港/赣榆,江苏/连云港/东海,江苏/连云港/灌云,江苏/连云港/灌南,江苏/淮安/淮安,江苏/淮安/淮安区,江苏/淮安/淮阴区,江苏/淮安/清江浦,江苏/淮安/洪泽,江苏/淮安/涟水,江苏/淮安/盱眙,江苏/淮安/金湖,江苏/盐城/盐城,江苏/盐城/亭湖,江苏/盐城/盐都,江苏/盐城/大丰,江苏/盐城/响水,江苏/盐城/滨海,江苏/盐城/阜宁,江苏/盐城/射阳,江苏/盐城/建湖,江苏/盐城/东台,江苏/扬州/扬州,江苏/扬州/广陵,江苏/扬州/邗江,江苏/扬州/江都,江苏/扬州/宝应,江苏/扬州/仪征,江苏/扬州/高邮,江苏/镇江/镇江,江苏/镇江/京口,江苏/镇江/润州,江苏/镇江/丹徒,江苏/镇江/丹阳,江苏/镇江/扬中,江苏/镇江/句容,江苏/泰州/泰州,江苏/泰州/海陵,江苏/泰州/高港,江苏/泰州/姜堰,江苏/泰州/兴化,江苏/泰州/靖江,江苏/泰州/泰兴,江苏/宿迁/宿迁,江苏/宿迁/宿城,江苏/宿迁/宿豫,江苏/宿迁/沭阳,江苏/宿迁/泗阳,江苏/宿迁/泗洪,浙江/杭州/杭州,浙江/杭州/上城,浙江/杭州/下城,浙江/杭州/江干,浙江/杭州/拱墅,浙江/杭州/西湖,浙江/杭州/滨江,浙江/杭州/萧山,浙江/杭州/余杭,浙江/杭州/富阳,浙江/杭州/临安,浙江/杭州/桐庐,浙江/杭州/淳安,浙江/杭州/建德,浙江/宁波/宁波,浙江/宁波/海曙,浙江/宁波/江北,浙江/宁波/北仑,浙江/宁波/镇海,浙江/宁波/鄞州,浙江/宁波/奉化,浙江/宁波/象山,浙江/宁波/宁海,浙江/宁波/余姚,浙江/宁波/慈溪,浙江/温州/温州,浙江/温州/鹿城,浙江/温州/龙湾,浙江/温州/瓯海,浙江/温州/洞头,浙江/温州/永嘉,浙江/温州/平阳,浙江/温州/苍南,浙江/温州/文成,浙江/温州/泰顺,浙江/温州/瑞安,浙江/温州/乐清,浙江/嘉兴/嘉兴,浙江/嘉兴/南湖,浙江/嘉兴/秀洲,浙江/嘉兴/嘉善,浙江/嘉兴/海盐,浙江/嘉兴/海宁,浙江/嘉兴/平湖,浙江/嘉兴/桐乡,浙江/湖州/湖州,浙江/湖州/吴兴,浙江/湖州/南浔,浙江/湖州/德清,浙江/湖州/长兴,浙江/湖州/安吉,浙江/绍兴/绍兴,浙江/绍兴/越城,浙江/绍兴/柯桥,浙江/绍兴/上虞,浙江/绍兴/新昌,浙江/绍兴/诸暨,浙江/绍兴/嵊州,浙江/金华/金华,浙江/金华/婺城,浙江/金华/金东,浙江/金华/武义,浙江/金华/浦江,浙江/金华/磐安,浙江/金华/兰溪,浙江/金华/义乌,浙江/金华/东阳,浙江/金华/永康,浙江/衢州/衢州,浙江/衢州/柯城,浙江/衢州/衢江,浙江/衢州/常山,浙江/衢州/开化,浙江/衢州/龙游,浙江/衢州/江山,浙江/舟山/舟山,浙江/舟山/定海,浙江/舟山/普陀,浙江/舟山/岱山,浙江/舟山/嵊泗,浙江/台州/台州,浙江/台州/椒江,浙江/台州/黄岩,浙江/台州/路桥,浙江/台州/三门,浙江/台州/天台,浙江/台州/仙居,浙江/台州/温岭,浙江/台州/临海,浙江/台州/玉环,浙江/丽水/丽水,浙江/丽水/莲都,浙江/丽水/青田,浙江/丽水/缙云,浙江/丽水/遂昌,浙江/丽水/松阳,浙江/丽水/云和,浙江/丽水/庆元,浙江/丽水/景宁,浙江/丽水/龙泉,安徽/合肥/合肥,安徽/合肥/瑶海,安徽/合肥/庐阳,安徽/合肥/蜀山,安徽/合肥/包河,安徽/合肥/长丰,安徽/合肥/肥东,安徽/合肥/肥西,安徽/合肥/庐江,安徽/合肥/巢湖,安徽/芜湖/芜湖,安徽/芜湖/镜湖,安徽/芜湖/弋江,安徽/芜湖/鸠江,安徽/芜湖/三山,安徽/芜湖/芜湖县,安徽/芜湖/繁昌,安徽/芜湖/南陵,安徽/芜湖/无为,安徽/蚌埠/蚌埠,安徽/蚌埠/龙子湖,安徽/蚌埠/蚌山,安徽/蚌埠/禹会,安徽/蚌埠/淮上,安徽/蚌埠/怀远,安徽/蚌埠/五河,安徽/蚌埠/固镇,安徽/淮南/淮南,安徽/淮南/大通,安徽/淮南/田家庵,安徽/淮南/谢家集,安徽/淮南/八公山,安徽/淮南/潘集,安徽/淮南/凤台,安徽/淮南/寿县,安徽/马鞍山/马鞍山,安徽/马鞍山/花山,安徽/马鞍山/雨山,安徽/马鞍山/博望,安徽/马鞍山/当涂,安徽/马鞍山/含山,安徽/马鞍山/和县,安徽/淮北/淮北,安徽/淮北/杜集,安徽/淮北/相山,安徽/淮北/烈山,安徽/淮北/濉溪,安徽/铜陵/铜陵,安徽/铜陵/铜官,安徽/铜陵/义安,安徽/铜陵/郊区,安徽/铜陵/枞阳,安徽/安庆/安庆,安徽/安庆/迎江,安徽/安庆/大观,安徽/安庆/宜秀,安徽/安庆/怀宁,安徽/安庆/潜山,安徽/安庆/太湖,安徽/安庆/宿松,安徽/安庆/望江,安徽/安庆/岳西,安徽/安庆/桐城,安徽/黄山/黄山,安徽/黄山/屯溪,安徽/黄山/黄山区,安徽/黄山/徽州,安徽/黄山/歙县,安徽/黄山/休宁,安徽/黄山/黟县,安徽/黄山/祁门,安徽/滁州/滁州,安徽/滁州/琅琊,安徽/滁州/南谯,安徽/滁州/来安,安徽/滁州/全椒,安徽/滁州/定远,安徽/滁州/凤阳,安徽/滁州/天长,安徽/滁州/明光,安徽/阜阳/阜阳,安徽/阜阳/颍州,安徽/阜阳/颍东,安徽/阜阳/颍泉,安徽/阜阳/临泉,安徽/阜阳/太和,安徽/阜阳/阜南,安徽/阜阳/颍上,安徽/阜阳/界首,安徽/宿州/宿州,安徽/宿州/埇桥,安徽/宿州/砀山,安徽/宿州/萧县,安徽/宿州/灵璧,安徽/宿州/泗县,安徽/六安/六安,安徽/六安/金安,安徽/六安/裕安,安徽/六安/叶集,安徽/六安/霍邱,安徽/六安/舒城,安徽/六安/金寨,安徽/六安/霍山,安徽/亳州/亳州,安徽/亳州/谯城,安徽/亳州/涡阳,安徽/亳州/蒙城,安徽/亳州/利辛,安徽/池州/池州,安徽/池州/贵池,安徽/池州/东至,安徽/池州/石台,安徽/池州/青阳,安徽/宣城/宣城,安徽/宣城/宣州,安徽/宣城/郎溪,安徽/宣城/广德,安徽/宣城/泾县,安徽/宣城/绩溪,安徽/宣城/旌德,安徽/宣城/宁国,福建/福州/福州,福建/福州/鼓楼,福建/福州/台江,福建/福州/仓山,福建/福州/马尾,福建/福州/晋安,福建/福州/长乐,福建/福州/闽侯,福建/福州/连江,福建/福州/罗源,福建/福州/闽清,福建/福州/永泰,福建/福州/平潭,福建/福州/福清,福建/厦门/厦门,福建/厦门/思明,福建/厦门/海沧,福建/厦门/湖里,福建/厦门/集美,福建/厦门/同安,福建/厦门/翔安,福建/莆田/莆田,福建/莆田/城厢,福建/莆田/涵江,福建/莆田/荔城,福建/莆田/秀屿,福建/莆田/仙游,福建/三明/三明,福建/三明/梅列,福建/三明/三元,福建/三明/明溪,福建/三明/清流,福建/三明/宁化,福建/三明/大田,福建/三明/尤溪,福建/三明/沙县,福建/三明/将乐,福建/三明/泰宁,福建/三明/建宁,福建/三明/永安,福建/泉州/泉州,福建/泉州/鲤城,福建/泉州/丰泽,福建/泉州/洛江,福建/泉州/泉港,福建/泉州/惠安,福建/泉州/安溪,福建/泉州/永春,福建/泉州/德化,福建/泉州/金门,福建/泉州/石狮,福建/泉州/晋江,福建/泉州/南安,福建/漳州/漳州,福建/漳州/芗城,福建/漳州/龙文,福建/漳州/云霄,福建/漳州/漳浦,福建/漳州/诏安,福建/漳州/长泰,福建/漳州/东山,福建/漳州/南靖,福建/漳州/平和,福建/漳州/华安,福建/漳州/龙海,福建/南平/南平,福建/南平/延平,福建/南平/建阳,福建/南平/顺昌,福建/南平/浦城,福建/南平/光泽,福建/南平/松溪,福建/南平/政和,福建/南平/邵武,福建/南平/武夷山,福建/南平/建瓯,福建/龙岩/龙岩,福建/龙岩/新罗,福建/龙岩/永定,福建/龙岩/长汀,福建/龙岩/上杭,福建/龙岩/武平,福建/龙岩/连城,福建/龙岩/漳平,福建/宁德/宁德,福建/宁德/蕉城,福建/宁德/霞浦,福建/宁德/古田,福建/宁德/屏南,福建/宁德/寿宁,福建/宁德/周宁,福建/宁德/柘荣,福建/宁德/福安,福建/宁德/福鼎,江西/南昌/南昌,江西/南昌/东湖,江西/南昌/西湖,江西/南昌/青云谱,江西/南昌/湾里,江西/南昌/青山湖,江西/南昌/新建,江西/南昌/南昌县,江西/南昌/安义,江西/南昌/进贤,江西/景德镇/景德镇,江西/景德镇/昌江,江西/景德镇/珠山,江西/景德镇/浮梁,江西/景德镇/乐平,江西/萍乡/萍乡,江西/萍乡/安源,江西/萍乡/湘东,江西/萍乡/莲花,江西/萍乡/上栗,江西/萍乡/芦溪,江西/九江/九江,江西/九江/濂溪,江西/九江/浔阳,江西/九江/柴桑,江西/九江/武宁,江西/九江/修水,江西/九江/永修,江西/九江/德安,江西/九江/都昌,江西/九江/湖口,江西/九江/彭泽,江西/九江/瑞昌,江西/九江/共青城,江西/九江/庐山,江西/新余/新余,江西/新余/渝水,江西/新余/分宜,江西/鹰潭/鹰潭,江西/鹰潭/月湖,江西/鹰潭/余江,江西/鹰潭/贵溪,江西/赣州/赣州,江西/赣州/章贡,江西/赣州/南康,江西/赣州/赣县,江西/赣州/信丰,江西/赣州/大余,江西/赣州/上犹,江西/赣州/崇义,江西/赣州/安远,江西/赣州/龙南,江西/赣州/定南,江西/赣州/全南,江西/赣州/宁都,江西/赣州/于都,江西/赣州/兴国,江西/赣州/会昌,江西/赣州/寻乌,江西/赣州/石城,江西/赣州/瑞金,江西/吉安/吉安,江西/吉安/吉州,江西/吉安/青原,江西/吉安/吉安县,江西/吉安/吉水,江西/吉安/峡江,江西/吉安/新干,江西/吉安/永丰,江西/吉安/泰和,江西/吉安/遂川,江西/吉安/万安,江西/吉安/安福,江西/吉安/永新,江西/吉安/井冈山,江西/宜春/宜春,江西/宜春/袁州,江西/宜春/奉新,江西/宜春/万载,江西/宜春/上高,江西/宜春/宜丰,江西/宜春/靖安,江西/宜春/铜鼓,江西/宜春/丰城,江西/宜春/樟树,江西/宜春/高安,江西/抚州/抚州,江西/抚州/临川,江西/抚州/东乡,江西/抚州/南城,江西/抚州/黎川,江西/抚州/南丰,江西/抚州/崇仁,江西/抚州/乐安,江西/抚州/宜黄,江西/抚州/金溪,江西/抚州/资溪,江西/抚州/广昌,江西/上饶/上饶,江西/上饶/信州,江西/上饶/广丰,江西/上饶/上饶县,江西/上饶/玉山,江西/上饶/铅山,江西/上饶/横峰,江西/上饶/弋阳,江西/上饶/余干,江西/上饶/鄱阳,江西/上饶/万年,江西/上饶/婺源,江西/上饶/德兴,山东/济南/济南,山东/济南/历下,山东/济南/市中,山东/济南/槐荫,山东/济南/天桥,山东/济南/历城,山东/济南/长清,山东/济南/章丘,山东/济南/济阳,山东/济南/莱芜,山东/济南/钢城,山东/济南/平阴,山东/济南/商河,山东/青岛/青岛,山东/青岛/市南,山东/青岛/市北,山东/青岛/黄岛,山东/青岛/崂山,山东/青岛/李沧,山东/青岛/城阳,山东/青岛/即墨,山东/青岛/胶州,山东/青岛/平度,山东/青岛/莱西,山东/淄博/淄博,山东/淄博/淄川,山东/淄博/张店,山东/淄博/博山,山东/淄博/临淄,山东/淄博/周村,山东/淄博/桓台,山东/淄博/高青,山东/淄博/沂源,山东/枣庄/枣庄,山东/枣庄/市中,山东/枣庄/薛城,山东/枣庄/峄城,山东/枣庄/台儿庄,山东/枣庄/山亭,山东/枣庄/滕州,山东/东营,山东/东营/东营,山东/东营/河口,山东/东营/垦利,山东/东营/利津,山东/东营/广饶,山东/烟台/烟台,山东/烟台/芝罘,山东/烟台/福山,山东/烟台/牟平,山东/烟台/莱山,山东/烟台/长岛,山东/烟台/龙口,山东/烟台/莱阳,山东/烟台/莱州,山东/烟台/蓬莱,山东/烟台/招远,山东/烟台/栖霞,山东/烟台/海阳,山东/潍坊/潍坊,山东/潍坊/潍城,山东/潍坊/寒亭,山东/潍坊/坊子,山东/潍坊/奎文,山东/潍坊/临朐,山东/潍坊/昌乐,山东/潍坊/青州,山东/潍坊/诸城,山东/潍坊/寿光,山东/潍坊/安丘,山东/潍坊/高密,山东/潍坊/昌邑,山东/济宁/济宁,山东/济宁/任城,山东/济宁/兖州,山东/济宁/微山,山东/济宁/鱼台,山东/济宁/金乡,山东/济宁/嘉祥,山东/济宁/汶上,山东/济宁/泗水,山东/济宁/梁山,山东/济宁/曲阜,山东/济宁/邹城,山东/泰安/泰安,山东/泰安/泰山,山东/泰安/岱岳,山东/泰安/宁阳,山东/泰安/东平,山东/泰安/新泰,山东/泰安/肥城,山东/威海/威海,山东/威海/环翠,山东/威海/文登,山东/威海/荣成,山东/威海/乳山,山东/日照/日照,山东/日照/东港,山东/日照/岚山,山东/日照/五莲,山东/日照/莒县,山东/临沂/临沂,山东/临沂/兰山,山东/临沂/罗庄,山东/临沂/河东,山东/临沂/沂南,山东/临沂/郯城,山东/临沂/沂水,山东/临沂/兰陵,山东/临沂/费县,山东/临沂/平邑,山东/临沂/莒南,山东/临沂/蒙阴,山东/临沂/临沭,山东/德州/德州,山东/德州/德城,山东/德州/陵城,山东/德州/宁津,山东/德州/庆云,山东/德州/临邑,山东/德州/齐河,山东/德州/平原,山东/德州/夏津,山东/德州/武城,山东/德州/乐陵,山东/德州/禹城,山东/聊城/聊城,山东/聊城/东昌府,山东/聊城/阳谷,山东/聊城/莘县,山东/聊城/茌平,山东/聊城/东阿,山东/聊城/冠县,山东/聊城/高唐,山东/聊城/临清,山东/滨州/滨州,山东/滨州/滨城,山东/滨州/沾化,山东/滨州/惠民,山东/滨州/阳信,山东/滨州/无棣,山东/滨州/博兴,山东/滨州/邹平,山东/菏泽/菏泽,山东/菏泽/牡丹,山东/菏泽/定陶,山东/菏泽/曹县,山东/菏泽/单县,山东/菏泽/成武,山东/菏泽/巨野,山东/菏泽/郓城,山东/菏泽/鄄城,山东/菏泽/东明,河南/郑州/郑州,河南/郑州/中原,河南/郑州/二七,河南/郑州/管城,河南/郑州/金水,河南/郑州/上街,河南/郑州/惠济,河南/郑州/中牟,河南/郑州/巩义,河南/郑州/荥阳,河南/郑州/新密,河南/郑州/新郑,河南/郑州/登封,河南/开封/开封,河南/开封/龙亭,河南/开封/顺河,河南/开封/鼓楼,河南/开封/禹王台,河南/开封/祥符,河南/开封/杞县,河南/开封/通许,河南/开封/尉氏,河南/开封/兰考,河南/洛阳/洛阳,河南/洛阳/老城,河南/洛阳/西工,河南/洛阳/瀍河,河南/洛阳/涧西,河南/洛阳/吉利,河南/洛阳/洛龙,河南/洛阳/孟津,河南/洛阳/新安,河南/洛阳/栾川,河南/洛阳/嵩县,河南/洛阳/汝阳,河南/洛阳/宜阳,河南/洛阳/洛宁,河南/洛阳/伊川,河南/洛阳/偃师,河南/平顶山/平顶山,河南/平顶山/新华,河南/平顶山/卫东,河南/平顶山/石龙,河南/平顶山/湛河,河南/平顶山/宝丰,河南/平顶山/叶县,河南/平顶山/鲁山,河南/平顶山/郏县,河南/平顶山/舞钢,河南/平顶山/汝州,河南/安阳/文峰,河南/安阳,河南/安阳/北关,河南/安阳/殷都,河南/安阳/龙安,河南/安阳/安阳,河南/安阳/汤阴,河南/安阳/滑县,河南/安阳/内黄,河南/安阳/林州,河南/鹤壁/鹤壁,河南/鹤壁/鹤山,河南/鹤壁/山城,河南/鹤壁/淇滨,河南/鹤壁/浚县,河南/鹤壁/淇县,河南/新乡,河南/新乡/红旗,河南/新乡/卫滨,河南/新乡/凤泉,河南/新乡/牧野,河南/新乡/新乡,河南/新乡/获嘉,河南/新乡/原阳,河南/新乡/延津,河南/新乡/封丘,河南/新乡/长垣,河南/新乡/卫辉,河南/新乡/辉县,河南/焦作/焦作,河南/焦作/解放,河南/焦作/中站,河南/焦作/马村,河南/焦作/山阳,河南/焦作/修武,河南/焦作/博爱,河南/焦作/武陟,河南/焦作/温县,河南/焦作/沁阳,河南/焦作/孟州,河南/濮阳,河南/濮阳/华龙,河南/濮阳/清丰,河南/濮阳/南乐,河南/濮阳/范县,河南/濮阳/台前,河南/濮阳/濮阳,河南/许昌/许昌,河南/许昌/魏都,河南/许昌/建安,河南/许昌/鄢陵,河南/许昌/襄城,河南/许昌/禹州,河南/许昌/长葛,河南/漯河/漯河,河南/漯河/源汇,河南/漯河/郾城,河南/漯河/召陵,河南/漯河/舞阳,河南/漯河/临颍,河南/三门峡/三门峡,河南/三门峡/湖滨,河南/三门峡/陕州,河南/三门峡/渑池,河南/三门峡/卢氏,河南/三门峡/义马,河南/三门峡/灵宝,河南/南阳/南阳,河南/南阳/宛城,河南/南阳/卧龙,河南/南阳/南召,河南/南阳/方城,河南/南阳/西峡,河南/南阳/镇平,河南/南阳/内乡,河南/南阳/淅川,河南/南阳/社旗,河南/南阳/唐河,河南/南阳/新野,河南/南阳/桐柏,河南/南阳/邓州,河南/商丘/商丘,河南/商丘/梁园,河南/商丘/睢阳,河南/商丘/民权,河南/商丘/睢县,河南/商丘/宁陵,河南/商丘/柘城,河南/商丘/虞城,河南/商丘/夏邑,河南/商丘/永城,河南/信阳/信阳,河南/信阳/浉河,河南/信阳/平桥,河南/信阳/罗山,河南/信阳/光山,河南/信阳/新县,河南/信阳/商城,河南/信阳/固始,河南/信阳/潢川,河南/信阳/淮滨,河南/信阳/息县,河南/周口/周口,河南/周口/川汇,河南/周口/扶沟,河南/周口/西华,河南/周口/商水,河南/周口/沈丘,河南/周口/郸城,河南/周口/淮阳,河南/周口/太康,河南/周口/鹿邑,河南/周口/项城,河南/驻马店/驻马店,河南/驻马店/驿城,河南/驻马店/西平,河南/驻马店/上蔡,河南/驻马店/平舆,河南/驻马店/正阳,河南/驻马店/确山,河南/驻马店/泌阳,河南/驻马店/汝南,河南/驻马店/遂平,河南/驻马店/新蔡,河南/济源/济源,湖北/武汉/武汉,湖北/武汉/江岸,湖北/武汉/江汉,湖北/武汉/硚口,湖北/武汉/汉阳,湖北/武汉/武昌,湖北/武汉/青山,湖北/武汉/洪山,湖北/武汉/东西湖,湖北/武汉/汉南,湖北/武汉/蔡甸,湖北/武汉/江夏,湖北/武汉/黄陂,湖北/武汉/新洲,湖北/黄石/黄石,湖北/黄石/黄石港,湖北/黄石/西塞山,湖北/黄石/下陆,湖北/黄石/铁山,湖北/黄石/阳新,湖北/黄石/大冶,湖北/十堰/十堰,湖北/十堰/茅箭,湖北/十堰/张湾,湖北/十堰/郧阳,湖北/十堰/郧西,湖北/十堰/竹山,湖北/十堰/竹溪,湖北/十堰/房县,湖北/十堰/丹江口,湖北/宜昌/宜昌,湖北/宜昌/西陵,湖北/宜昌/伍家岗,湖北/宜昌/点军,湖北/宜昌/猇亭,湖北/宜昌/夷陵,湖北/宜昌/远安,湖北/宜昌/兴山,湖北/宜昌/秭归,湖北/宜昌/长阳,湖北/宜昌/五峰,湖北/宜昌/宜都,湖北/宜昌/当阳,湖北/宜昌/枝江,湖北/襄阳/襄阳,湖北/襄阳/襄城,湖北/襄阳/樊城,湖北/襄阳/襄州,湖北/襄阳/南漳,湖北/襄阳/谷城,湖北/襄阳/保康,湖北/襄阳/老河口,湖北/襄阳/枣阳,湖北/襄阳/宜城,湖北/鄂州/鄂州,湖北/鄂州/梁子湖,湖北/鄂州/华容,湖北/鄂州/鄂城,湖北/荆门/荆门,湖北/荆门/东宝,湖北/荆门/掇刀,湖北/荆门/沙洋,湖北/荆门/钟祥,湖北/荆门/京山,湖北/孝感/孝感,湖北/孝感/孝南,湖北/孝感/孝昌,湖北/孝感/大悟,湖北/孝感/云梦,湖北/孝感/应城,湖北/孝感/安陆,湖北/孝感/汉川,湖北/荆州,湖北/荆州/沙市,湖北/荆州/荆州,湖北/荆州/公安,湖北/荆州/监利,湖北/荆州/江陵,湖北/荆州/石首,湖北/荆州/洪湖,湖北/荆州/松滋,湖北/黄冈/黄冈,湖北/黄冈/黄州,湖北/黄冈/团风,湖北/黄冈/红安,湖北/黄冈/罗田,湖北/黄冈/英山,湖北/黄冈/浠水,湖北/黄冈/蕲春,湖北/黄冈/黄梅,湖北/黄冈/麻城,湖北/黄冈/武穴,湖北/咸宁/咸宁,湖北/咸宁/咸安,湖北/咸宁/嘉鱼,湖北/咸宁/通城,湖北/咸宁/崇阳,湖北/咸宁/通山,湖北/咸宁/赤壁,湖北/随州/随州,湖北/随州/曾都,湖北/随州/随县,湖北/随州/广水,湖北/恩施,湖北/恩施/恩施,湖北/恩施/利川,湖北/恩施/建始,湖北/恩施/巴东,湖北/恩施/宣恩,湖北/恩施/咸丰,湖北/恩施/来凤,湖北/恩施/鹤峰,湖北/仙桃/仙桃,湖北/潜江/潜江,湖北/天门/天门,湖北/神农架/神农架,湖南/长沙/长沙,湖南/长沙/芙蓉,湖南/长沙/天心,湖南/长沙/岳麓,湖南/长沙/开福,湖南/长沙/雨花,湖南/长沙/望城,湖南/长沙/长沙县,湖南/长沙/浏阳,湖南/长沙/宁乡,湖南/株洲/株洲,湖南/株洲/荷塘,湖南/株洲/芦淞,湖南/株洲/石峰,湖南/株洲/天元,湖南/株洲/渌口,湖南/株洲/攸县,湖南/株洲/茶陵,湖南/株洲/炎陵,湖南/株洲/醴陵,湖南/湘潭,湖南/湘潭/雨湖,湖南/湘潭/岳塘,湖南/湘潭/湘潭,湖南/湘潭/湘乡,湖南/湘潭/韶山,湖南/衡阳/衡阳,湖南/衡阳/珠晖,湖南/衡阳/雁峰,湖南/衡阳/石鼓,湖南/衡阳/蒸湘,湖南/衡阳/南岳,湖南/衡阳/衡阳县,湖南/衡阳/衡南,湖南/衡阳/衡山,湖南/衡阳/衡东,湖南/衡阳/祁东,湖南/衡阳/耒阳,湖南/衡阳/常宁,湖南/邵阳/邵阳,湖南/邵阳/双清,湖南/邵阳/大祥,湖南/邵阳/北塔,湖南/邵阳/邵东,湖南/邵阳/新邵,湖南/邵阳/邵阳县,湖南/邵阳/隆回,湖南/邵阳/洞口,湖南/邵阳/绥宁,湖南/邵阳/新宁,湖南/邵阳/城步,湖南/邵阳/武冈,湖南/岳阳,湖南/岳阳/岳阳楼,湖南/岳阳/云溪,湖南/岳阳/君山,湖南/岳阳/岳阳,湖南/岳阳/华容,湖南/岳阳/湘阴,湖南/岳阳/平江,湖南/岳阳/汨罗,湖南/岳阳/临湘,湖南/常德/常德,湖南/常德/武陵,湖南/常德/鼎城,湖南/常德/安乡,湖南/常德/汉寿,湖南/常德/澧县,湖南/常德/临澧,湖南/常德/桃源,湖南/常德/石门,湖南/常德/津市,湖南/张家界/张家界,湖南/张家界/永定,湖南/张家界/武陵源,湖南/张家界/慈利,湖南/张家界/桑植,湖南/益阳/益阳,湖南/益阳/资阳,湖南/益阳/赫山区,湖南/益阳/南县,湖南/益阳/桃江,湖南/益阳/安化,湖南/益阳/沅江,湖南/郴州/郴州,湖南/郴州/北湖,湖南/郴州/苏仙,湖南/郴州/桂阳,湖南/郴州/宜章,湖南/郴州/永兴,湖南/郴州/嘉禾,湖南/郴州/临武,湖南/郴州/汝城,湖南/郴州/桂东,湖南/郴州/安仁,湖南/郴州/资兴,湖南/永州/永州,湖南/永州/零陵,湖南/永州/冷水滩,湖南/永州/祁阳,湖南/永州/东安,湖南/永州/双牌,湖南/永州/道县,湖南/永州/江永,湖南/永州/宁远,湖南/永州/蓝山,湖南/永州/新田,湖南/永州/江华,湖南/怀化/怀化,湖南/怀化/鹤城,湖南/怀化/中方,湖南/怀化/沅陵,湖南/怀化/辰溪,湖南/怀化/溆浦,湖南/怀化/会同,湖南/怀化/麻阳,湖南/怀化/新晃,湖南/怀化/芷江,湖南/怀化/靖州,湖南/怀化/通道,湖南/怀化/洪江,湖南/娄底/娄底,湖南/娄底/娄星,湖南/娄底/双峰,湖南/娄底/新化,湖南/娄底/冷水江,湖南/娄底/涟源,湖南/湖南/湘西,湖南/湘西/吉首,湖南/湘西/泸溪,湖南/湘西/凤凰,湖南/湘西/花垣,湖南/湘西/保靖,湖南/湘西/古丈,湖南/湘西/永顺,湖南/湘西/龙山,广东/广州/广州,广东/广州/荔湾,广东/广州/越秀,广东/广州/海珠,广东/广州/天河,广东/广州/白云,广东/广州/黄埔,广东/广州/番禺,广东/广州/花都,广东/广州/南沙,广东/广州/从化,广东/广州/增城,广东/韶关/韶关,广东/韶关/武江,广东/韶关/浈江,广东/韶关/曲江,广东/韶关/始兴,广东/韶关/仁化,广东/韶关/翁源,广东/韶关/乳源,广东/韶关/新丰,广东/韶关/乐昌,广东/韶关/南雄,广东/深圳/深圳,广东/深圳/罗湖,广东/深圳/福田,广东/深圳/南山,广东/深圳/宝安,广东/深圳/龙岗,广东/深圳/盐田,广东/深圳/龙华,广东/深圳/坪山,广东/深圳/光明,广东/珠海/珠海,广东/珠海/香洲,广东/珠海/斗门,广东/珠海/金湾,广东/汕头/汕头,广东/汕头/龙湖,广东/汕头/金平,广东/汕头/濠江,广东/汕头/潮阳,广东/汕头/潮南,广东/汕头/澄海,广东/汕头/南澳,广东/佛山/佛山,广东/佛山/禅城,广东/佛山/南海,广东/佛山/顺德,广东/佛山/三水,广东/佛山/高明,广东/江门/江门,广东/江门/蓬江,广东/江门/江海,广东/江门/新会,广东/江门/台山,广东/江门/开平,广东/江门/鹤山,广东/江门/恩平,广东/湛江/湛江,广东/湛江/赤坎,广东/湛江/霞山,广东/湛江/坡头,广东/湛江/麻章,广东/湛江/遂溪,广东/湛江/徐闻,广东/湛江/廉江,广东/湛江/雷州,广东/湛江/吴川,广东/茂名/茂名,广东/茂名/茂南,广东/茂名/电白,广东/茂名/高州,广东/茂名/化州,广东/茂名/信宜,广东/肇庆/肇庆,广东/肇庆/端州,广东/肇庆/鼎湖,广东/肇庆/高要,广东/肇庆/广宁,广东/肇庆/怀集,广东/肇庆/封开,广东/肇庆/德庆,广东/肇庆/四会,广东/惠州/惠州,广东/惠州/惠城,广东/惠州/惠阳,广东/惠州/博罗,广东/惠州/惠东,广东/惠州/龙门,广东/梅州/梅州,广东/梅州/梅江,广东/梅州/梅县,广东/梅州/大埔,广东/梅州/丰顺,广东/梅州/五华,广东/梅州/平远,广东/梅州/蕉岭,广东/梅州/兴宁,广东/汕尾,广东/汕尾/海丰,广东/汕尾/陆河,广东/汕尾/陆丰,广东/河源/河源,广东/河源/源城,广东/河源/紫金,广东/河源/龙川,广东/河源/连平,广东/河源/和平,广东/河源/东源,广东/阳江/阳江,广东/阳江/江城,广东/阳江/阳东,广东/阳江/阳西,广东/阳江/阳春,广东/清远/清远,广东/清远/清城,广东/清远/清新,广东/清远/佛冈,广东/清远/阳山,广东/清远/连山,广东/清远/连南,广东/清远/英德,广东/清远/连州,广东/东莞/东莞,广东/中山/中山,广东/东沙/东沙,广东/潮州/潮州,广东/潮州/湘桥,广东/潮州/潮安,广东/潮州/饶平,广东/揭阳/揭阳,广东/揭阳/榕城,广东/揭阳/揭东,广东/揭阳/揭西,广东/揭阳/惠来,广东/揭阳/普宁,广东/云浮/云浮,广东/云浮/云城,广东/云浮/云安,广东/云浮/新兴,广东/云浮/郁南,广东/云浮/罗定,广西/南宁/南宁,广西/南宁/兴宁,广西/南宁/青秀,广西/南宁/江南,广西/南宁/西乡塘,广西/南宁/良庆,广西/南宁/邕宁,广西/南宁/武鸣,广西/南宁/隆安,广西/南宁/马山,广西/南宁/上林,广西/南宁/宾阳,广西/南宁/横县,广西/柳州/柳州,广西/柳州/城中,广西/柳州/鱼峰,广西/柳州/柳南,广西/柳州/柳北,广西/柳州/柳江,广西/柳州/柳城,广西/柳州/鹿寨,广西/柳州/融安,广西/柳州/融水,广西/柳州/三江,广西/桂林/桂林,广西/桂林/秀峰,广西/桂林/叠彩,广西/桂林/象山,广西/桂林/七星,广西/桂林/雁山,广西/桂林/临桂,广西/桂林/阳朔,广西/桂林/灵川,广西/桂林/全州,广西/桂林/兴安,广西/桂林/永福,广西/桂林/灌阳,广西/桂林/龙胜,广西/桂林/资源,广西/桂林/平乐,广西/桂林/恭城,广西/桂林/荔浦,广西/梧州/梧州,广西/梧州/万秀,广西/梧州/长洲,广西/梧州/龙圩,广西/梧州/苍梧,广西/梧州/藤县,广西/梧州/蒙山,广西/梧州/岑溪,广西/北海/北海,广西/北海/海城,广西/北海/银海,广西/北海/铁山港,广西/北海/合浦,广西/防城港/防城港,广西/防城港/港口,广西/防城港/防城,广西/防城港/上思,广西/防城港/东兴,广西/钦州/钦州,广西/钦州/钦南,广西/钦州/钦北,广西/钦州/灵山,广西/钦州/浦北,广西/贵港/贵港,广西/贵港/港北,广西/贵港/港南,广西/贵港/覃塘,广西/贵港/平南,广西/贵港/桂平,广西/玉林/玉林,广西/玉林/玉州,广西/玉林/福绵,广西/玉林/容县,广西/玉林/陆川,广西/玉林/博白,广西/玉林/兴业,广西/玉林/北流,广西/百色/百色,广西/百色/右江,广西/百色/田阳,广西/百色/田东,广西/百色/平果,广西/百色/德保,广西/百色/那坡,广西/百色/凌云,广西/百色/乐业,广西/百色/田林,广西/百色/西林,广西/百色/隆林,广西/百色/靖西,广西/贺州/贺州,广西/贺州/八步,广西/贺州/平桂,广西/贺州/昭平,广西/贺州/钟山,广西/贺州/富川,广西/河池/河池,广西/河池/金城江,广西/河池/宜州,广西/河池/南丹,广西/河池/天峨,广西/河池/凤山,广西/河池/东兰,广西/河池/罗城,广西/河池/环江,广西/河池/巴马,广西/河池/都安,广西/河池/大化,广西/来宾/来宾,广西/来宾/兴宾,广西/来宾/忻城,广西/来宾/象州,广西/来宾/武宣,广西/来宾/金秀,广西/来宾/合山,广西/崇左/崇左,广西/崇左/江州,广西/崇左/扶绥,广西/崇左/宁明,广西/崇左/龙州,广西/崇左/大新,广西/崇左/天等,广西/崇左/凭祥,海南/海口/海口,海南/海口/秀英,海南/海口/龙华,海南/海口/琼山,海南/海口/美兰,海南/三亚/三亚,海南/三亚/海棠,海南/三亚/吉阳,海南/三亚/天涯,海南/三亚/崖州,海南/三沙/三沙,海南/三沙/西沙,海南/三沙/南沙,海南/三沙/中沙,海南/儋州/儋州,海南/五指山/五指山,海南/琼海/琼海,海南/文昌/文昌,海南/万宁/万宁,海南/东方/东方,海南/定安/定安,海南/屯昌/屯昌,海南/澄迈/澄迈,海南/临高/临高,海南/白沙/白沙,海南/昌江/昌江,海南/乐东/乐东,海南/陵水/陵水,海南/保亭/保亭,海南/琼中/琼中,重庆/万州,重庆/涪陵,重庆/渝中,重庆/大渡口,重庆/江北,重庆/沙坪坝,重庆/九龙坡,重庆/南岸,重庆/北碚,重庆/綦江,重庆/大足,重庆/渝北,重庆/巴南,重庆/黔江,重庆/长寿,重庆/江津,重庆/合川,重庆/永川,重庆/南川,重庆/璧山,重庆/铜梁,重庆/潼南,重庆/荣昌,重庆/开州,重庆/梁平,重庆/武隆,重庆/重庆,重庆/城口,重庆/丰都,重庆/垫江,重庆/忠县,重庆/云阳,重庆/奉节,重庆/巫山,重庆/巫溪,重庆/石柱,重庆/秀山,重庆/酉阳,重庆/彭水,四川/成都/成都,四川/成都/锦江,四川/成都/青羊,四川/成都/金牛,四川/成都/武侯,四川/成都/成华,四川/成都/龙泉驿,四川/成都/青白江区,四川/成都/新都,四川/成都/温江,四川/成都/双流,四川/成都/郫都,四川/成都/金堂,四川/成都/大邑,四川/成都/蒲江,四川/成都/新津,四川/成都/都江堰,四川/成都/彭州,四川/成都/邛崃,四川/成都/崇州,四川/成都/简阳,四川/自贡/自贡,四川/自贡/自流井,四川/自贡/贡井,四川/自贡/大安,四川/自贡/沿滩,四川/自贡/荣县,四川/自贡/富顺,四川/攀枝花/攀枝花,四川/攀枝花/东区,四川/攀枝花/西区,四川/攀枝花/仁和,四川/攀枝花/米易,四川/攀枝花/盐边,四川/泸州/泸州,四川/泸州/江阳,四川/泸州/纳溪,四川/泸州/龙马潭,四川/泸州/泸县,四川/泸州/合江,四川/泸州/叙永,四川/泸州/古蔺,四川/德阳/德阳,四川/德阳/旌阳,四川/德阳/罗江,四川/德阳/中江,四川/德阳/广汉,四川/德阳/什邡,四川/德阳/绵竹,四川/绵阳/绵阳,四川/绵阳/涪城,四川/绵阳/游仙,四川/绵阳/安州,四川/绵阳/三台,四川/绵阳/盐亭,四川/绵阳/梓潼,四川/绵阳/北川,四川/绵阳/平武,四川/绵阳/江油,四川/广元/广元,四川/广元/利州,四川/广元/昭化,四川/广元/朝天,四川/广元/旺苍,四川/广元/青川,四川/广元/剑阁,四川/广元/苍溪,四川/遂宁/遂宁,四川/遂宁/船山,四川/遂宁/安居,四川/遂宁/蓬溪,四川/遂宁/射洪,四川/遂宁/大英,四川/内江/内江,四川/内江/市中,四川/内江/东兴,四川/内江/威远,四川/内江/资中,四川/内江/隆昌,四川/乐山/乐山,四川/乐山/市中,四川/乐山/沙湾,四川/乐山/五通桥,四川/乐山/金口河,四川/乐山/犍为,四川/乐山/井研,四川/乐山/夹江,四川/乐山/沐川,四川/乐山/峨边,四川/乐山/马边,四川/乐山/峨眉山,四川/南充/南充,四川/南充/顺庆,四川/南充/高坪,四川/南充/嘉陵,四川/南充/南部,四川/南充/营山,四川/南充/蓬安,四川/南充/仪陇,四川/南充/西充,四川/南充/阆中,四川/眉山/眉山,四川/眉山/东坡,四川/眉山/彭山,四川/眉山/仁寿,四川/眉山/洪雅,四川/眉山/丹棱,四川/眉山/青神,四川/宜宾/宜宾,四川/宜宾/翠屏,四川/宜宾/南溪,四川/宜宾/叙州,四川/宜宾/江安,四川/宜宾/长宁,四川/宜宾/高县,四川/宜宾/珙县,四川/宜宾/筠连,四川/宜宾/兴文,四川/宜宾/屏山,四川/广安,四川/广安/广安,四川/广安/前锋,四川/广安/岳池,四川/广安/武胜,四川/广安/邻水,四川/广安/华蓥,四川/达州/达州,四川/达州/通川,四川/达州/达川,四川/达州/宣汉,四川/达州/开江,四川/达州/大竹,四川/达州/渠县,四川/达州/万源,四川/雅安/雅安,四川/雅安/雨城,四川/雅安/名山,四川/雅安/荥经,四川/雅安/汉源,四川/雅安/石棉,四川/雅安/天全,四川/雅安/芦山,四川/雅安/宝兴,四川/巴中/巴中,四川/巴中/巴州,四川/巴中/恩阳,四川/巴中/通江,四川/巴中/南江,四川/巴中/平昌,四川/资阳/资阳,四川/资阳/雁江,四川/资阳/安岳,四川/资阳/乐至,四川/阿坝,四川/阿坝/马尔康,四川/阿坝/汶川,四川/阿坝/理县,四川/阿坝/茂县,四川/阿坝/松潘,四川/阿坝/九寨沟,四川/阿坝/金川,四川/阿坝/小金,四川/阿坝/黑水,四川/阿坝/壤塘,四川/阿坝/阿坝,四川/阿坝/若尔盖,四川/阿坝/红原,四川/甘孜,四川/甘孜/康定,四川/甘孜/泸定,四川/甘孜/丹巴,四川/甘孜/九龙,四川/甘孜/雅江,四川/甘孜/道孚,四川/甘孜/炉霍,四川/甘孜/甘孜,四川/甘孜/新龙,四川/甘孜/德格,四川/甘孜/白玉,四川/甘孜/石渠,四川/甘孜/色达,四川/甘孜/理塘,四川/甘孜/巴塘,四川/甘孜/乡城,四川/甘孜/稻城,四川/甘孜/得荣,四川/凉山/凉山,四川/凉山/西昌,四川/凉山/木里,四川/凉山/盐源,四川/凉山/德昌,四川/凉山/会理,四川/凉山/会东,四川/凉山/宁南,四川/凉山/普格,四川/凉山/布拖,四川/凉山/金阳,四川/凉山/昭觉,四川/凉山/喜德,四川/凉山/冕宁,四川/凉山/越西,四川/凉山/甘洛,四川/凉山/美姑,四川/凉山/雷波,贵州/贵阳/贵阳,贵州/贵阳/南明,贵州/贵阳/云岩,贵州/贵阳/花溪,贵州/贵阳/乌当,贵州/贵阳/白云,贵州/贵阳/观山湖,贵州/贵阳/开阳,贵州/贵阳/息烽,贵州/贵阳/修文,贵州/贵阳/清镇,贵州/贵州/六盘水,贵州/六盘水/钟山,贵州/六盘水/六枝,贵州/六盘水/水城,贵州省/六盘水/盘州,贵州/遵义/遵义,贵州/遵义/红花岗,贵州/遵义/汇川,贵州/遵义/播州,贵州/遵义/桐梓,贵州/遵义/绥阳,贵州/遵义/正安,贵州/遵义/道真,贵州/遵义/务川,贵州/遵义/凤冈,贵州/遵义/湄潭,贵州/遵义/余庆,贵州/遵义/习水,贵州/遵义/赤水,贵州/遵义/仁怀,贵州/安顺/安顺,贵州/安顺/西秀,贵州/安顺/平坝,贵州/安顺/普定,贵州/安顺/镇宁,贵州/安顺/关岭,贵州/安顺/紫云,贵州/毕节/毕节,贵州/毕节/七星关,贵州/毕节/大方,贵州/毕节/黔西,贵州/毕节/金沙,贵州/毕节/织金,贵州/毕节/纳雍,贵州/毕节/威宁,贵州/毕节/赫章,贵州/铜仁/铜仁,贵州/铜仁/碧江,贵州/铜仁/万山,贵州/铜仁/江口,贵州/铜仁/玉屏,贵州/铜仁/石阡,贵州/铜仁/思南,贵州/铜仁/印江,贵州/铜仁/德江,贵州/铜仁/沿河,贵州/铜仁/松桃,贵州/贵州/黔西南,贵州/黔西南/兴义,贵州/黔西南/兴仁,贵州/黔西南/普安,贵州/黔西南/晴隆,贵州/黔西南/贞丰,贵州/黔西南/望谟,贵州/黔西南/册亨,贵州/黔西南/安龙,贵州/贵州/黔东南,贵州/黔东南/凯里,贵州/黔东南/黄平,贵州/黔东南/施秉,贵州/黔东南/三穗,贵州/黔东南/镇远,贵州/黔东南/岑巩,贵州/黔东南/天柱,贵州/黔东南/锦屏,贵州/黔东南/剑河,贵州/黔东南/台江,贵州/黔东南/黎平,贵州/黔东南/榕江,贵州/黔东南/从江,贵州/黔东南/雷山,贵州/黔东南/麻江,贵州/黔东南/丹寨,贵州/贵州/黔南,贵州/黔南/都匀,贵州/黔南/福泉,贵州/黔南/荔波,贵州/黔南/贵定,贵州/黔南/瓮安,贵州/黔南/独山,贵州/黔南/平塘,贵州/黔南/罗甸,贵州/黔南/长顺,贵州/黔南/龙里,贵州/黔南/惠水,贵州/黔南/三都,云南/昆明/昆明,云南/昆明/五华,云南/昆明/盘龙,云南/昆明/官渡,云南/昆明/西山,云南/昆明/东川,云南/昆明/呈贡,云南/昆明/晋宁,云南/昆明/富民,云南/昆明/宜良,云南/昆明/石林,云南/昆明/嵩明,云南/昆明/禄劝,云南/昆明/寻甸,云南/昆明/安宁,云南/曲靖/曲靖,云南/曲靖/麒麟,云南/曲靖/沾益,云南/曲靖/马龙,云南/曲靖/陆良,云南/曲靖/师宗,云南/曲靖/罗平,云南/曲靖/富源,云南/曲靖/会泽,云南/曲靖/宣威,云南/玉溪/玉溪,云南/玉溪/红塔,云南/玉溪/江川,云南/玉溪/澄江,云南/玉溪/通海,云南/玉溪/华宁,云南/玉溪/易门,云南/玉溪/峨山,云南/玉溪/新平,云南/玉溪/元江,云南/保山/保山,云南/保山/隆阳,云南/保山/施甸,云南/保山/龙陵,云南/保山/昌宁,云南/保山/腾冲,云南/昭通/昭通,云南/昭通/昭阳,云南/昭通/鲁甸,云南/昭通/巧家,云南/昭通/盐津,云南/昭通/大关,云南/昭通/永善,云南/昭通/绥江,云南/昭通/镇雄,云南/昭通/彝良,云南/昭通/威信,云南/昭通/水富,云南/丽江/丽江,云南/丽江/古城,云南/丽江/玉龙,云南/丽江/永胜,云南/丽江/华坪,云南/丽江/宁蒗,云南/普洱/普洱,云南/普洱/思茅,云南/普洱/宁洱,云南/普洱/墨江,云南/普洱/景东,云南/普洱/景谷,云南/普洱/镇沅,云南/普洱/江城,云南/普洱/孟连,云南/普洱/澜沧,云南/普洱/西盟,云南/临沧/临沧,云南/临沧/临翔,云南/临沧/凤庆,云南/临沧/云县,云南/临沧/永德,云南/临沧/镇康,云南/临沧/双江,云南/临沧/耿马,云南/临沧/沧源,云南/楚雄,云南/楚雄/楚雄,云南/楚雄/双柏,云南/楚雄/牟定,云南/楚雄/南华,云南/楚雄/姚安,云南/楚雄/大姚,云南/楚雄/永仁,云南/楚雄/元谋,云南/楚雄/武定,云南/楚雄/禄丰,云南/红河,云南/红河/个旧,云南/红河/开远,云南/红河/蒙自,云南/红河/弥勒,云南/红河/屏边,云南/红河/建水,云南/红河/石屏,云南/红河/泸西,云南/红河/元阳,云南/红河/红河,云南/红河/金平,云南/红河/绿春,云南/红河/河口,云南/文山,云南/文山/文山,云南/文山/砚山,云南/文山/西畴,云南/文山/麻栗坡,云南/文山/马关,云南/文山/丘北,云南/文山/广南,云南/文山/富宁,云南/云南/西双版纳,云南/西双版纳/景洪,云南/西双版纳/勐海,云南/西双版纳/勐腊,云南/大理,云南/大理/大理,云南/大理/漾濞,云南/大理/祥云,云南/大理/宾川,云南/大理/弥渡,云南/大理/南涧,云南/大理/巍山,云南/大理/永平,云南/大理/云龙,云南/大理/洱源,云南/大理/剑川,云南/大理/鹤庆,云南/德宏/德宏,云南/德宏/瑞丽,云南/德宏/芒市,云南/德宏/梁河,云南/德宏/盈江,云南/德宏/陇川,云南/怒江/怒江,云南/怒江/泸水,云南/怒江/福贡,云南/怒江/贡山,云南/怒江/兰坪,云南/云南/迪庆,云南/迪庆/香格里拉,云南/迪庆/德钦,云南/迪庆/维西,西藏/拉萨/拉萨,西藏/拉萨/城关,西藏/拉萨/堆龙德庆,西藏/拉萨/达孜,西藏/拉萨/林周,西藏/拉萨/当雄,西藏/拉萨/尼木,西藏/拉萨/曲水,西藏/拉萨/墨竹工卡,西藏/日喀则/日喀则,西藏/日喀则/桑珠孜,西藏/日喀则/南木林,西藏/日喀则/江孜,西藏/日喀则/定日,西藏/日喀则/萨迦,西藏/日喀则/拉孜,西藏/日喀则/昂仁,西藏/日喀则/谢通门,西藏/日喀则/白朗,西藏/日喀则/仁布,西藏/日喀则/康马,西藏/日喀则/定结,西藏/日喀则/仲巴,西藏/日喀则/亚东,西藏/日喀则/吉隆,西藏/日喀则/聂拉木,西藏/日喀则/萨嘎,西藏/日喀则/岗巴,西藏/昌都/昌都,西藏/昌都/卡若,西藏/昌都/江达,西藏/昌都/贡觉,西藏/昌都/类乌齐,西藏/昌都/丁青,西藏/昌都/察雅,西藏/昌都/八宿,西藏/昌都/左贡,西藏/昌都/芒康,西藏/昌都/洛隆,西藏/昌都/边坝,西藏/林芝/林芝,西藏/林芝/巴宜,西藏/林芝/工布江达,西藏/林芝/米林,西藏/林芝/墨脱,西藏/林芝/波密,西藏/林芝/察隅,西藏/林芝/朗县,西藏/山南/山南,西藏/山南/乃东,西藏/山南/札囊,西藏/山南/贡嘎,西藏/山南/桑日,西藏/山南/琼结,西藏/山南/曲松,西藏/山南/措美,西藏/山南/洛扎,西藏/山南/加查,西藏/山南/隆子,西藏/山南/错那,西藏/山南/浪卡子,西藏/那曲/那曲,西藏/那曲/色尼,西藏/那曲/嘉黎,西藏/那曲/比如,西藏/那曲/聂荣,西藏/那曲/安多,西藏/那曲/申扎,西藏/那曲/索县,西藏/那曲/班戈,西藏/那曲/巴青,西藏/那曲/尼玛,西藏/那曲/双湖,西藏/阿里/阿里,西藏/阿里/普兰,西藏/阿里/札达,西藏/阿里/噶尔,西藏/阿里/日土,西藏/阿里/革吉,西藏/阿里/改则,西藏/阿里/措勤,陕西/西安/西安,陕西/西安/新城,陕西/西安/碑林,陕西/西安/莲湖,陕西/西安/灞桥,陕西/西安/未央,陕西/西安/雁塔,陕西/西安/阎良,陕西/西安/临潼,陕西/西安/长安,陕西/西安/高陵,陕西/西安/鄠邑,陕西/西安/蓝田,陕西/西安/周至,陕西/铜川/铜川,陕西/铜川/王益,陕西/铜川/印台,陕西/铜川/耀州,陕西/铜川/宜君,陕西/宝鸡/宝鸡,陕西/宝鸡/渭滨,陕西/宝鸡/金台,陕西/宝鸡/陈仓,陕西/宝鸡/凤翔,陕西/宝鸡/岐山,陕西/宝鸡/扶风,陕西/宝鸡/眉县,陕西/宝鸡/陇县,陕西/宝鸡/千阳,陕西/宝鸡/麟游,陕西/宝鸡/凤县,陕西/宝鸡/太白,陕西/咸阳/咸阳,陕西/咸阳/秦都,陕西/咸阳/杨陵,陕西/咸阳/渭城,陕西/咸阳/三原,陕西/咸阳/泾阳,陕西/咸阳/乾县,陕西/咸阳/礼泉,陕西/咸阳/永寿,陕西/咸阳/长武,陕西/咸阳/旬邑,陕西/咸阳/淳化,陕西/咸阳/武功,陕西/咸阳/兴平,陕西/咸阳/彬州,陕西/渭南/渭南,陕西/渭南/临渭,陕西/渭南/华州,陕西/渭南/潼关,陕西/渭南/大荔,陕西/渭南/合阳,陕西/渭南/澄城,陕西/渭南/蒲城,陕西/渭南/白水,陕西/渭南/富平,陕西/渭南/韩城,陕西/渭南/华阴,陕西/延安/延安,陕西/延安/宝塔,陕西/延安/安塞,陕西/延安/延长,陕西/延安/延川,陕西/延安/子长,陕西/延安/志丹,陕西/延安/吴起,陕西/延安/甘泉,陕西/延安/富县,陕西/延安/洛川,陕西/延安/宜川,陕西/延安/黄龙,陕西/延安/黄陵,陕西/汉中/汉中,陕西/汉中/汉台,陕西/汉中/南郑,陕西/汉中/城固,陕西/汉中/洋县,陕西/汉中/西乡,陕西/汉中/勉县,陕西/汉中/宁强,陕西/汉中/略阳,陕西/汉中/镇巴,陕西/汉中/留坝,陕西/汉中/佛坪,陕西/榆林/榆林,陕西/榆林/榆阳,陕西/榆林/横山,陕西/榆林/府谷,陕西/榆林/靖边,陕西/榆林/定边,陕西/榆林/绥德,陕西/榆林/米脂,陕西/榆林/佳县,陕西/榆林/吴堡,陕西/榆林/清涧,陕西/榆林/子洲,陕西/榆林/神木,陕西/安康/安康,陕西/安康/汉滨,陕西/安康/汉阴,陕西/安康/石泉,陕西/安康/宁陕,陕西/安康/紫阳,陕西/安康/岚皋,陕西/安康/平利,陕西/安康/镇坪,陕西/安康/旬阳,陕西/安康/白河,陕西/商洛/商洛,陕西/商洛/商州,陕西/商洛/洛南,陕西/商洛/丹凤,陕西/商洛/商南,陕西/商洛/山阳,陕西/商洛/镇安,陕西/商洛/柞水,甘肃/兰州/兰州,甘肃/兰州/城关,甘肃/兰州/七里河,甘肃/兰州/西固,甘肃/兰州/安宁,甘肃/兰州/红古,甘肃/兰州/永登,甘肃/兰州/皋兰,甘肃/兰州/榆中,甘肃/嘉峪关/嘉峪关,甘肃/金昌/金昌,甘肃/金昌/金川,甘肃/金昌/永昌,甘肃/白银,甘肃/白银/白银,甘肃/白银/平川,甘肃/白银/靖远,甘肃/白银/会宁,甘肃/白银/景泰,甘肃/天水/天水,甘肃/天水/秦州,甘肃/天水/麦积,甘肃/天水/清水,甘肃/天水/秦安,甘肃/天水/甘谷,甘肃/天水/武山,甘肃/天水/张家川,甘肃/武威/武威,甘肃/武威/凉州,甘肃/武威/民勤,甘肃/武威/古浪,甘肃/武威/天祝,甘肃/张掖/张掖,甘肃/张掖/甘州,甘肃/张掖/肃南,甘肃/张掖/民乐,甘肃/张掖/临泽,甘肃/张掖/高台,甘肃/张掖/山丹,甘肃/平凉/平凉,甘肃/平凉/崆峒,甘肃/平凉/泾川,甘肃/平凉/灵台,甘肃/平凉/崇信,甘肃/平凉/庄浪,甘肃/平凉/静宁,甘肃/平凉/华亭,甘肃/酒泉/酒泉,甘肃/酒泉/肃州,甘肃/酒泉/金塔,甘肃/酒泉/瓜州,甘肃/酒泉/肃北,甘肃/酒泉/阿克塞,甘肃/酒泉/玉门,甘肃/酒泉/敦煌,甘肃/庆阳/庆阳,甘肃/庆阳/西峰,甘肃/庆阳/庆城,甘肃/庆阳/环县,甘肃/庆阳/华池,甘肃/庆阳/合水,甘肃/庆阳/正宁,甘肃/庆阳/宁县,甘肃/庆阳/镇原,甘肃/定西/定西,甘肃/定西/安定,甘肃/定西/通渭,甘肃/定西/陇西,甘肃/定西/渭源,甘肃/定西/临洮,甘肃/定西/漳县,甘肃/定西/岷县,甘肃/甘肃/陇南,甘肃/陇南/武都,甘肃/陇南/成县,甘肃/陇南/文县,甘肃/陇南/宕昌,甘肃/陇南/康县,甘肃/陇南/西和,甘肃/陇南/礼县,甘肃/陇南/徽县,甘肃/陇南/两当,甘肃/临夏,甘肃/临夏/临夏,甘肃/临夏/康乐,甘肃/临夏/永靖,甘肃/临夏/广河,甘肃/临夏/和政,甘肃/临夏/东乡,甘肃/临夏/积石山,甘肃/甘肃/甘南,甘肃/甘南/合作,甘肃/甘南/临潭,甘肃/甘南/卓尼,甘肃/甘南/舟曲,甘肃/甘南/迭部,甘肃/甘南/玛曲,甘肃/甘南/碌曲,甘肃/甘南/夏河,青海/西宁/西宁,青海/西宁/城东,青海/西宁/城中,青海/西宁/城西,青海/西宁/城北,青海/西宁/大通,青海/西宁/湟中,青海/西宁/湟源,青海/海东/海东,青海/海东/乐都,青海/海东/平安,青海/海东/民和,青海/海东/互助,青海/海东/化隆,青海/海东/循化,青海/海北/海北,青海/海北/门源,青海/海北/祁连,青海/海北/海晏,青海/海北/刚察,青海/黄南/黄南,青海/黄南/同仁,青海/黄南/尖扎,青海/黄南/泽库,青海/黄南/河南,青海/海南/海南,青海/海南/共和,青海/海南/同德,青海/海南/贵德,青海/海南/兴海,青海/海南/贵南,青海/果洛/果洛,青海/果洛/玛沁,青海/果洛/班玛,青海/果洛/甘德,青海/果洛/达日,青海/果洛/久治,青海/果洛/玛多,青海/玉树,青海/玉树/玉树,青海/玉树/杂多,青海/玉树/称多,青海/玉树/治多,青海/玉树/囊谦,青海/玉树/曲麻莱,青海/海西/海西,青海/海西/格尔木,青海/海西/德令哈,青海/海西/茫崖,青海/海西/乌兰,青海省/海西/都兰,青海/海西/天峻,宁夏/银川/银川,宁夏/银川/兴庆,宁夏/银川/西夏,宁夏/银川/金凤,宁夏/银川/永宁,宁夏/银川/贺兰,宁夏/银川/灵武,宁夏/石嘴山/石嘴山,宁夏/石嘴山/大武口,宁夏/石嘴山/惠农,宁夏/石嘴山/平罗,宁夏/吴忠/吴忠,宁夏/吴忠/利通,宁夏/吴忠/红寺堡,宁夏/吴忠/盐池,宁夏/吴忠/同心,宁夏/吴忠/青铜峡,宁夏/固原/固原,宁夏/固原/原州,宁夏/固原/西吉,宁夏/固原/隆德,宁夏/固原/泾源,宁夏/固原/彭阳,宁夏/中卫/中卫,宁夏/中卫/沙坡头,宁夏/中卫/中宁,宁夏/中卫/海原,新疆/乌鲁木齐/乌鲁木齐,新疆/乌鲁木齐/天池,新疆/乌鲁木齐/沙依巴克,新疆/乌鲁木齐/新市,新疆/乌鲁木齐/水磨沟,新疆/乌鲁木齐/头屯河,新疆/乌鲁木齐/达坂城,新疆/乌鲁木齐/米东,新疆/乌鲁木齐市/乌鲁木齐县,新疆/克拉玛依,新疆/克拉玛依/独山子,新疆/克拉玛依/克拉玛依,新疆/克拉玛依/白碱滩,新疆/克拉玛依/乌尔禾,新疆/吐鲁番/吐鲁番,新疆/吐鲁番/高昌,新疆/吐鲁番/鄯善,新疆/吐鲁番/托克逊,新疆/哈密/哈密,新疆/哈密/伊州,新疆/哈密/巴里坤,新疆/哈密/伊吾,新疆/昌吉,新疆/昌吉/昌吉,新疆/昌吉/阜康,新疆/昌吉/呼图壁,新疆/昌吉/玛纳斯,新疆/昌吉/奇台,新疆/昌吉/吉木萨尔,新疆/昌吉/木垒,新疆/新疆/博尔塔拉,新疆/博尔塔拉/博乐,新疆/博尔塔拉/阿拉山口,新疆/博尔塔拉/精河,新疆/博尔塔拉/温泉,新疆/新疆/巴音郭楞,新疆/巴音郭楞/库尔勒,新疆/巴音郭楞/轮台,新疆/巴音郭楞/尉犁,新疆/巴音郭楞/若羌,新疆/巴音郭楞/且末,新疆/巴音郭楞/焉耆,新疆/巴音郭楞/和静,新疆/巴音郭楞/和硕,新疆/巴音郭楞/博湖,新疆/阿克苏,新疆/阿克苏/阿克苏,新疆/阿克苏/温宿,新疆/阿克苏/库车,新疆/阿克苏/沙雅,新疆/阿克苏/新和,新疆/阿克苏/拜城,新疆/阿克苏/乌什,新疆/阿克苏/阿瓦提,新疆/阿克苏/柯坪,新疆/新疆/克州,新疆/克州/阿图什,新疆/克州/阿克陶,新疆/克州/阿合奇,新疆/克州/乌恰,新疆/喀什,新疆/喀什/喀什,新疆/喀什/疏附,新疆/喀什/疏勒,新疆/喀什/英吉沙,新疆/喀什/泽普,新疆/喀什/莎车,新疆/喀什/叶城,新疆/喀什/麦盖提,新疆/喀什/岳普湖,新疆/喀什/伽师,新疆/喀什/巴楚,新疆/喀什/塔什库尔干,新疆/和田,新疆/和田/和田,新疆/和田/墨玉,新疆/和田/皮山,新疆/和田/洛浦,新疆/和田/策勒,新疆/和田/于田,新疆/和田/民丰,新疆/新疆/伊犁,新疆/伊犁/伊宁,新疆/伊犁/奎屯,新疆/伊犁/霍尔果斯,新疆/伊犁/伊宁县,新疆/伊犁/察布查尔,新疆/伊犁/霍城,新疆/伊犁/巩留,新疆/伊犁/新源,新疆/伊犁/昭苏,新疆/伊犁/特克斯,新疆/伊犁/尼勒克,新疆/塔城,新疆/塔城/塔城,新疆/塔城/乌苏,新疆/塔城/额敏,新疆/塔城/沙湾,新疆/塔城/托里,新疆/塔城/裕民,新疆/塔城/和布克赛尔,新疆/阿勒泰,新疆/阿勒泰/阿勒泰,新疆/阿勒泰/布尔津,新疆/阿勒泰/富蕴,新疆/阿勒泰/福海,新疆/阿勒泰/哈巴河,新疆/阿勒泰/青河,新疆/阿勒泰/吉木乃,新疆/石河子/石河子,新疆/阿拉尔/阿拉尔,新疆/新疆/图木舒克,新疆/五家渠/五家渠,新疆/新疆/北屯,新疆/新疆/铁门关,新疆/新疆/双河,新疆/新疆/可克达拉,新疆/新疆/昆玉,台湾/高雄/恒春,台湾/高雄/台南,台湾/高雄,台湾/高雄/屏东,台湾/高雄/马公,台湾/高雄/嘉义,台湾/高雄/云林,台湾/台中/鹿谷乡,台湾/台中/彰化,台湾/台中/南投,台湾/台中,台湾/台中/苗栗,台湾/台中/台东,台湾/台中/埔里,台湾/台中/花莲,台湾/台北/新竹,台湾/台北/大溪,台湾/台北/桃园,台湾/台北,台湾/台北/宜兰,台湾/台北/基隆,香港,九龙,荃湾,新界,澳门,路环岛,氹仔岛'
        l = set()
        for i in cts.split(','):
            tl = i.split('/')
            if len(tl) == 1:
                l.add(tl[-1])
            elif len(tl) >= 2:
                l.add(tl[1])
        print(','.join(l))
