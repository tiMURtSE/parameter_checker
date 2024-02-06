from openpyxl.cell.cell import Cell

from typing import List
from models.RequiredParam.RequiredParam import RequiredParam

class Product:
    ID_COLUMN_INDEX = 0
    CATEGORY_COLUMN_INDEX = 5

    def __init__(self, row: tuple[Cell]):
        self._row = row

        self._category = self._get_category()
        self._cell = None
        self._value = None

        self._required_params: List[RequiredParam] = []

    @property
    def category(self):
        return self._category
    
    @property
    def required_params(self):
        return self._required_params
    
    @required_params.setter
    def required_params(self, value):
        if value:
            self._required_params = value
        else:
            print(f"Для категории {self._category} не было найдено обязательных параметров")

    def set_param_values(self):
        for param in self._required_params:
            index = param.col_index
            cell = self._row[index]
            value = self._remove_whitespaces(cell.value)

            param.cell = cell
            param.value = value

    def get_required_param(self, param_id: str):
        for param in self._required_params:
            if param.id == param_id:
                return param

    def _get_category(self):
        category = self._row[self.CATEGORY_COLUMN_INDEX].value
        formatted_category = category.lower().strip()

        return formatted_category

    def _remove_whitespaces(self, value):
        if isinstance(value, str):
            return value.strip()
        
        return value