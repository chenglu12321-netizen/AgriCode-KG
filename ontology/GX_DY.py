from ST_DY import *
# 导致，抗性，危害，诱发，防治，促进，抑制，缓解，恶化，表征
class Relation:
    """
    所有关系的基类。
    """
    def __init__(self, head_entity: Entity, tail_entity: Entity):
        self.head_entity =head_entity
        self.tail_entity =tail_entity

class PartRelation(Relation):
    '''
    部位关系，表示尾实体作为头实体的具体物理构成部分（如叶片、根、茎、叶鞘、心叶等）。在该关系中，头实体特指农作物本体，尾实体指的是对应农作物具体的器官或组织结构。
    '''
    def __init__(self, head_entity: Crop, tail_entity: Crop):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)


class CauseRelation(Relation):
    '''
    "导致"表示某个因素引发了农作物出现特定的症状、疾病或损害。这个因素可以是病害、虫害、不适宜的自然环境，或者不当使用的农药等。
    '''
    def __init__(self, head_entity: Disease|InsectPest|NaturalEnvironment, tail_entity: Symptom):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)


class ResistanceRelation(Relation):
    """
    "抗性"表示农作物对某些有害因素（如病害、虫害、不适宜的自然环境或农药等）具有抵抗或耐受的能力。
    """
    def __init__(self, head_entity: Crop, tail_entity: Disease|InsectPest):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)


class HazardRelation(Relation):
    """
    "危害"指某一因素（如病虫害、环境胁迫等）对农作物或其特定部位造成不利影响，导致其生长受抑制、产量或品质下降，甚至死亡。这种危害可针对农作物的整体、局部器官（如根、茎、叶等），或特定生长阶段（如苗期、开花期等）。
    """
    def __init__(self, head_entity:  Disease|InsectPest|Fertilizer, tail_entity:Crop|Growthperiodr ):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)



class InduceRelation(Relation):
    '''
    "诱发"表示某种因素或事件在特定条件下引起或激发了农作物出现新的病害、虫害或其他负面影响。
    '''
    def __init__(self, head_entity: InsectPest|NaturalEnvironment, tail_entity:Disease|InsectPest):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class ControlRelation(Relation):
    '''
    "防治"指通过采取措施预防或控制农作物的病害、虫害，以减少其对作物的危害。防治手段包括使用农药、肥料、物理方法和生物控制等，旨在减少病虫害的发生、传播，确保作物的健康生长。
    '''
    def __init__(self, head_entity: InsectPest|Pesticide|Fertilizer, tail_entity:Disease|InsectPest):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class PromotionRelation(Relation):
    '''
    "促进"表示某个因素通过提供适宜的条件或支持作用，有助于农作物的生长、发育、繁殖或健康。这个因素可能是自然环境、农药、肥料等，它们为作物提供了所需的资源，进而提高作物的生长势头、产量或品质。
    '''
    def __init__(self, head_entity: NaturalEnvironment|Pesticide|Fertilizer, tail_entity:Crop):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class InhibitionRelation(Relation):
    '''
    "抑制"表示某个因素限制农作物的生长、发育、繁殖或健康，导致作物的生长受到影响，产量或品质下降。
    '''
    def __init__(self, head_entity: NaturalEnvironment, tail_entity:Crop):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class AlleviationRelation(Relation):
    '''
    "缓解"表示通过改善环境条件或其他方式，减轻病害、虫害或症状的严重程度，帮助农作物恢复健康或减少损害。
    '''
    def __init__(self, head_entity: NaturalEnvironment, tail_entity:Disease|InsectPest|Symptom):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class WorseningRelation(Relation):
    '''
    "恶化"表示某个因素通过不适当的使用或不利条件，使病害、虫害或症状加重，导致农作物遭受更多损害。
    '''
    def __init__(self, head_entity: Pesticide|Fertilizer, tail_entity:Disease|InsectPest):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)

class Growthcycle(Relation):
        '''
        生长周期关系，尾实体表示农作物生长过程中的某一阶段。
        '''
        def __init__(self, head_entity: Crop, tail_entity:Crop):
            super().__init__(
                head_entity = head_entity,
                tail_entity = tail_entity)











#----------------------下面剔除


class Manifestation(Relation):
    '''
    “Manifestation”（表现）关系用于描述农作物或其部位在病虫害等生物胁迫下表现出的可见异常症状，反映其整体或局部的健康状况：
    1. 农作物整体表现出系统性症状；
    2. 农作物部位表现出局部异常特征。
    '''

    def __init__(self, head_entity: Crop, tail_entity: Symptom):
        super().__init__(
            head_entity=head_entity,
            tail_entity=tail_entity)

class RepresentationRelation(Relation):
    '''
    "表征"表示某种症状作为病害或虫害的外部特征，反映了病害或虫害的存在和影响。
    '''
    def __init__(self, head_entity: Symptom, tail_entity:Disease|InsectPest):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)
class Category(Relation):
    '''
    类别关系
    '''
    def __init__(self, head_entity: Crop, tail_entity:Crop):
        super().__init__(
            head_entity = head_entity,
            tail_entity = tail_entity)
