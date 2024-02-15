from models.Conditions.RoundShapeCondition import RoundShapeCondition
from models.Conditions.TableLegsColorCondition import TableLegsColorCondition

furniture_category_conditions = {
    "детская мебель": [],
    "диваны": [],
    "кровати": [],
    "банкетки": [],
    "кресла": [],
    "пуфы": [],
    "стулья": [],
    "табуреты": [],
    "столы и консоли": [
        RoundShapeCondition(),
        TableLegsColorCondition(),
    ],
    "тумбочки": [],
    "шкафы": [],
    "комоды": [],
    "обувницы": [],
    "полки": [],
    "подставки": [],
    "уличная и садовая мебель": [],
    "комплекты мебели": [],
    "бескаркасная мебель": [],
    "хранение вещей": [],
}