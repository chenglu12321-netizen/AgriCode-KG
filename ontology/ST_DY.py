
class Entity:
    '''
    所有实体的基类。
    '''
    def __init__(self, name: str):
        self.name = name

class Crop(Entity):
    '''
    农作物是一个宽泛的概念，农业上经大片田地栽培获得的粮食类、经济类植物统称为农作物。
    '''
    pass

class FieldCrop(Crop):
    '''
    大田作物，俗称 “庄稼”，指大片田地种植，可直供粮、油、衣物原料的植物，含粮、油等作物 。
    '''
    pass


class Vegetable(Crop):
    '''
    是指可作副食品的草本植物及少数可作副食品德木本植物和菌类。
    在本规范中，蔬菜具体分类及代码遵循《SB/T 10029-2012 新鲜蔬菜分类与代码》。
    '''
    pass

class Fruit(Crop):
    '''
    水果指的是植物的果实，一般由植物的精卵子或者性器官发育而来。
   对于水果的界定通常具有主观色彩，因此本规范将遵循《SB/T 11024-2013 新鲜水果分类与代码》对其进行严格划分。
    '''
    pass

class part(Entity):
    '''
    部位指的是农作物体内的各个具体部分或器官，这些部位在植物的生长、繁殖和发育过程中扮演着重要角色。
    '''
    pass

class Pesticide(Entity):
    '''
    农药是指保障、促进植物和农作物的成长所施用的杀虫、杀菌等的一类药物。
    '''
    pass

#杀虫剂
class Insecticide(Pesticide):
    '''
    杀虫剂是指用以防治害虫的化学制剂。
    '''
    pass

#杀螨剂
class Acaricide(Pesticide):
    '''
    杀螨剂用于防治植食性害螨的药剂称为杀螨剂。
    '''
    pass

#灭鼠剂
class Rodenticide(Pesticide):
    '''
        灭鼠剂泛指防治啮齿类动物的化学制剂。
    '''
    pass

class Fungicide(Pesticide):
    '''
    杀菌剂指能有效地控制或杀死微生物（细菌、真菌和藻类）的化学制剂。
    '''
    pass

class Herbicide(Pesticide):
    '''
    除草剂指可使杂草彻底地或选择地发生枯死的药剂，又称除莠剂， 用以消灭或抑制植物生长的一类物质。
    '''
    pass

class Synergist(Pesticide):
    '''
    增效剂指本身不具备某种特定活性或活性较低，但在与具备此种活性的物质混用时，能大幅度提高活性物质的性能的一类物质。
    '''
    pass

class PlantGrowthRegulator(Pesticide):
    '''
    植物生长调节剂泛指一类与植物激素具有相似生理和生物学效应的物质。
    '''
    pass

class Fertilizer(Entity):
    '''
    肥料：能供给作物生长发育所需养分，改善土壤性状，提高作物产量和品质的物质。
    只含有一种可标明含量的营养元素的化肥称为单元肥料，如氮肥、磷肥、钾肥以及微量元素肥料等。
    含有氮、磷、钾三种营养元素中的两种或三种且可标明其含量的化肥，称为复合肥料。
    '''
    pass

class PotassiumFertilizer(Fertilizer):
    '''
    钾肥是指以氮（K）为主要成分，施于土壤可提供植物氮素营养的单元肥料。
    '''
    pass

class NitrogenFertilizer(Fertilizer):
    '''
    氮肥是指以氮（N）为主要成分，施于土壤可提供植物氮素营养的单元肥料。
    '''
    pass

class PotassiumFertilizer(Fertilizer):
    '''
    磷肥是指以磷（P）为主要成分，施于土壤可提供植物磷素营养的单元肥料。
    '''
    pass


class SulfurFertilizer(Fertilizer):
    '''
    硫肥是指以硫（S）为主要成分，施于土壤可提供植物硫素营养的单元肥料。
    '''

    pass


class CalciumFertilizer(Fertilizer):
    '''
    钙肥是指以钙（Ca）为主要成分，施于土壤可提供植物钙素营养的单元肥料。
    '''
    pass

class MagnesiumFertilizer(Fertilizer):
    '''
    镁肥是指以镁（Mg）为主要成分，施于土壤可提供植物镁素营养的单元肥料。
    '''
    pass


class CompoundFertilizer(Fertilizer):
    '''
    复合肥是指含有氮、磷、钾三种营养元素中的两种或三种且可标明其含量的化肥，称为复合肥料。
    '''
    pass

#从下面的文本中提取关系
class MicronutrientFertilizer(Fertilizer):
    '''
    微量元素肥通常简称为微肥，是指含有微量营养元素的肥料，微量元素具体包括硼、锌、钼、铁、锰、铜等。
    '''
    pass

class Disease(Entity):
    '''
    病害是由细菌、真菌、病毒等引起植物发育不良、枯萎或死亡统称为病害。
    '''
    pass

class FungalDisease(Disease):
    '''
    真菌病害是由真菌病菌侵染所致的一类病害。
    '''
    pass
class BacterialDisease(Disease):
    '''
    细菌病害是由细菌病菌侵染所致的一类病害。
    '''
    pass

class ViralDisease(Disease):
    '''
    病毒病害是由植物病毒寄生引起的一类病害。
    '''
    pass

class NematodeDisease(Disease):
    '''
    线虫病害是由植物寄生线虫侵袭和寄生引起的一类植物病害。
    '''
    pass
class InsectPest(Entity):
    '''
    对植物生长造成影响的害虫。
    '''
    pass

class InsectaPest(InsectPest):
    '''
    昆虫纲虫害：节肢动物门昆虫纲动物侵害植物所引发的一类虫害。
    '''
    pass

class ArachnidaPest(InsectPest):
    '''
    蛛形纲虫害：节肢动物门蛛形纲动物侵害植物所引发的一类虫害。
    '''
    pass

class Symptom(Entity):
    '''
    症状：泛指由病害、虫害、营养不足、不良环境导致的植物生理、组织结构和形态上所发生的病变特征。
    '''
    pass

class NaturalEnvironment(Entity):
    '''
    自然环境：在农田中，由水土、风、光、地域等自然事物所形成的环境。
    '''
    pass

class SoilTemperature(NaturalEnvironment):
    '''
    土壤温度只标注温度值、温度范围或具有描述温度含义的词语。
    当描述性词语既包括温度含义，又包括湿度含义时，统一标为“土壤温度”。
    '''
    pass

class SoilMoisture(NaturalEnvironment):
    '''
    土壤湿度只标注湿度值、湿度范围或具有描述湿度含义的词语。
    '''
    pass

class SoilSalinity(NaturalEnvironment):
    '''
    土壤盐分只标注土壤含盐量、盐度范围或描述盐分程度的词语。
    '''
    pass

class SoilpH(NaturalEnvironment):
    '''
    土壤酸碱度只标注PH值、酸碱范围或描述酸碱程度的词语。
    '''
    pass

class SoilNutrientElements(NaturalEnvironment):
    '''
    土壤营养只标注氮、磷、钾、微量元素等词语。
    '''
    pass

class SoilType(NaturalEnvironment):
    '''
    土壤类型仅标注粘土、壤土、冲积壤土、砂壤土等具体的专业术语或带有简短限定词的专业术语。
    '''
    pass

class AirTemperature(NaturalEnvironment):
    '''
    空气温度：只标注温度值、温度范围或具有描述温度含义的词语。当描述性词语既包括温度含义，又包括湿度含义时，统一标为“空气温度”。
    '''
    pass

class AirHumidity(NaturalEnvironment):
    '''
    空气湿度：只标注湿度值、湿度范围或具有描述湿度含义的词语。
    '''

    pass

class AirCO2Concentration(NaturalEnvironment):
    '''
    空气二氧化碳浓度只标注浓度值、浓度范围或具有二氧化碳描述的词语。
    '''

    pass

class AirNH3Concentration(NaturalEnvironment):
    '''
    空气 NH₃ 浓度只标注浓度值、浓度范围或具有空气NH₃ 浓度描述的词语。
    '''

    pass

class WindSpeed(NaturalEnvironment):
    '''
    风只标注风速值、风速值范围以及描述风速的相关词语。
    '''
    pass

class Sunshine(NaturalEnvironment):
    '''
    阳光只标注光照强度值、强度范围以及描述光照的相关词语。
    '''

    pass

class Water(NaturalEnvironment):
    '''
    水只标注需水量、需水范围以及描述水的相关词语。
    '''

    pass

class TerrainInformation(NaturalEnvironment):
    '''
    地形只标注农田所在区域的地理高度、坡度以及描述地貌形态特征的相关词语。
    '''

    pass
class Growthperiodr(Entity):
    '''
   生长周期是指生物体从出生、发育、成熟到衰老、死亡的整个过程所经历的时间和各个阶段。
    '''
    pass




