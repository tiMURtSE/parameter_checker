from models.Conditions.SizeCondition import SizeCondition
from models.Conditions.BaseCondition import BaseCondition
from models.Conditions.ShapeCondition import ShapeCondition

# CATEGORY_CONDITIONAL_PARAMS = {
#     "люстры": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "подвесные светильники": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "потолочные светильники": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "настенные свтельники": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "трековые светильники": [
#         "размер",
#         "цоколь",
#     ],
#     "шинопроводы": [
#         "размер",
#     ],
#     "точечные светильники": [
#         "размер",
#         "цоколь",
#     ],
#     "настольные лампы": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "торшеры": [
#         "размер",
#     ],
#     "детские светильники": [
#         "размер",
#         "форма",
#         "цоколь",
#     ],
#     "светильники в ванную комнату": [
#         "размер"
#         "цоколь",
#     ],
#     "уличные светильники": [
#         "размер",
#         "цоколь",
#     ],
#     "светодиодная лента": [
#         "размер",
#         "цоколь",
#     ],
#     "профили для светодиодной ленты": [
#         "размер",
#     ],
#     "блоки питания для светодиодных лент": [
#         "размер",
#     ],
# }

CATEGORY_CONDITIONAL_PARAMS = {
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