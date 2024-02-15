from models.Conditions.SizeCondition import SizeCondition
from models.Conditions.BaseCondition import BaseCondition
from models.Conditions.ShapeCondition import ShapeCondition

light_category_conditions = {
    "люстры": [
        SizeCondition(),
        BaseCondition(),
        ShapeCondition(),
    ],
    "подвесные светильники": [
        SizeCondition(),
        BaseCondition(),
        ShapeCondition(),
    ],
    "потолочные светильники": [
        SizeCondition(),
        BaseCondition(),
        ShapeCondition(),
    ],
    "настенные свтельники": [
        SizeCondition(),
        BaseCondition(),
        ShapeCondition(),
    ],
    "трековые светильники": [
        SizeCondition(),
        BaseCondition(),
    ],
    "шинопроводы": [
        SizeCondition(),
    ],
    "точечные светильники": [
        SizeCondition(),
        BaseCondition(),
    ],
    "настольные лампы": [
        SizeCondition(),
        ShapeCondition(),
        BaseCondition(),
    ],
    "торшеры": [
        SizeCondition(),
    ],
    "детские светильники": [
        SizeCondition(),
        BaseCondition(),
        ShapeCondition(),
    ],
    "светильники в ванную комнату": [
        SizeCondition(),
        BaseCondition(),
    ],
    "уличные светильники": [
        SizeCondition(),
        BaseCondition(),
    ],
    "светодиодная лента": [
        SizeCondition(),
        BaseCondition(),
    ],
    "профили для светодиодной ленты": [
        SizeCondition(),
    ],
    "блоки питания для светодиодных лент": [
        SizeCondition(),
    ],
}