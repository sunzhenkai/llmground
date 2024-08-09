#!/bin/python3
from typing import Dict, Any, Optional, List

from langchain.chains.base import Chain
from langchain_core.callbacks import CallbackManagerForChainRun, AsyncCallbackManagerForChainRun
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import BasePromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from llms.ollama_llms import OllamaWrapper
from pydantic.v1 import BaseModel

CITIES = '安阳,玉溪,吕梁,七台河,山南,兰州,梧州,忻州,乌鲁木齐市,双鸭山,阿克苏,阿勒泰,茂名,宜宾,顺义,新乡,西城,克拉玛依,甘孜,海东,朝阳,中卫,武威,宝鸡,高雄,台中,嘉定,达州,珠海,雅安,三亚,昆明,肇庆,毕节,秦皇岛,辽阳,延庆,白城,驻马店,宁河,广安,彭水,固原,长春,绥化,西安,张家界,潍坊,承德,晋中,眉山,玉树,天门,恩施,宝山,城口,平顶山,贺州,丽水,合川,奉节,滨海新区,和平,白沙,嘉峪关,五指山,果洛,黔东南,铜仁,东莞,周口,常德,呼伦贝尔,徐汇区,鹰潭,白山,长宁,平谷,渭南,万州,湛江,崇左,绵阳,淮南,大渡口,常州,宣城,本溪,普陀,重庆,淮北,太原,琼海,怀化,张家口,东营,衡阳,河池,房山,神农架,盐城,六盘水,日喀则,甘南,昭通,柳州,德阳,定西,邯郸,湖州,荃湾,延安,辽源,德州,渝北,泰州,台北,武隆,博尔塔拉,荣昌,郑州,自贡,铜陵,衡水,开州,黔江,锦州,伊犁,阿里,武汉,乌海,阿坝,北海,酒泉,石景山,聊城,清远,包头,福州,池州,商丘,怒江,江北,乌鲁木齐,丽江,奉贤,贵州,烟台,铁岭,保定,佳木斯,莆田,广元,海西,静海,鹤岗,四平,宜昌,九龙坡,兴安盟,红河,氹仔岛,深圳,贵阳,津南,门头沟,南平,济南,昌都,万宁,云浮,浦东新区,河东,嘉兴,焦作,攀枝花,连云港,东沙,东丽,青浦,秀山,金昌,宝坻,通辽,济宁,邵阳,海淀,上海,梁平,儋州,岳阳,孝感,鄂尔多斯,临夏,克州,天水,巫山,东方,哈密,益阳,徐州,盘锦,吐鲁番,乐山,璧山,日照,宿迁,大理,晋城,黄石,巴彦淖尔,钦州,定安,大足,丹东,潮州,陵水,巴音郭楞,延边,安顺,西宁,沙坪坝,江津,湘潭,汕头,呼和浩特,咸阳,德宏,鄂州,许昌,亳州,北京,黄山,云阳,南京,阿拉善盟,防城港,林芝,娄底,普洱,吴忠,景德镇,通化,商洛,无锡,仙桃,渝中,泸州,合肥,石家庄,和田,阜新,成都,长沙,台州,牡丹江,萍乡,汕尾,云南,朔州,滨州,安康,南岸,上饶,潜江,通州,河北,衢州,锡林郭勒,宁德,内蒙古,百色,临沧,运城,黄浦,酉阳,长治,伊春,泉州,忠县,枣庄,北碚,三沙,阳泉,河源,白银,大兴安岭,杭州,松原,武清,庆阳,扬州,涪陵,芜湖,大同,信阳,保亭,垫江,黔南,拉萨,新疆,齐齐哈尔,淮安,荆门,虹口,资阳,绍兴,邢台,三门峡,遵义,西双版纳,静安,海南,九江,东城,镇江,来宾,阜阳,南通,洛阳,南充,苏州,乌兰察布,大庆,玉林,广州,西青,海北,长寿,吉林,九龙,泰安,马鞍山,漳州,梅州,张掖,温州,淄博,襄阳,昌吉,永州,巴南,龙岩,宿州,湘西,石河子,阳江,佛山,十堰,吉安,崇明,金山,湖南,沧州,铜梁,威海,澳门,滁州,南宁,宁波,宜春,江门,南昌,厦门,唐山,蚌埠,赤峰,揭阳,保山,密云,北辰,塔城,黄冈,大连,綦江,大兴,凉山,银川,临高,济源,永川,安庆,甘肃,咸宁,南阳,南开,葫芦岛,抚州,韶关,巫溪,河西,随州,海口,桂林,六安,路环岛,松江,鸡西,红桥,鞍山,青岛,迪庆,鹤壁,香港,漯河,南川,株洲,榆林,临沂,石嘴山,文昌,丰都,遂宁,黄南,潼南,石柱,新余,怀柔,抚顺,五家渠,濮阳,昌江,三明,惠州,内江,曲靖,中山,杨浦,琼中,沈阳,铜川,荆州,汉中,营口,舟山,黔西南,巴中,喀什,蓟州,天津,昌平,平凉,丰台,阿拉尔,金华,廊坊,菏泽,黑河,临汾,乐东,陇南,文山,贵港,那曲,赣州,郴州,闵行,新界,澄迈,哈尔滨,开封,楚雄,屯昌'

class WeatherAssistantChain(Chain):
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", f"""你是一个贴心的中文天气助手， 简明扼要地提醒用户需要关注的天气信息，以下是中国的城市列表 {CITIES}， 请使用中文回答"""),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ]
    )
    output_key: str = 'text'

    class InputSchema(BaseModel):
        input: str

    @property
    def input_keys(self) -> List[str]:
        return self.prompt.input_variables

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _call(self, inputs: Dict[str, Any], run_manager: Optional[CallbackManagerForChainRun] = None) -> Dict[str, Any]:
        prompt_value = self.prompt.format_prompt(**inputs)
        response = self.llm.generate_prompt([prompt_value], callbacks=run_manager.get_child() if run_manager else None)
        return {self.output_key: response.generations[0][0].text}

    def _acall(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        raise NotImplementedError()


class OllamaWeatherAssistantChain:
    def __init__(self, *args, **kwargs):
        self.llm = OllamaWrapper(*args, **kwargs)
        self.chain = WeatherAssistantChain(llm=self.llm.llm)
