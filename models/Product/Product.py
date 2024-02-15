from openpyxl.cell.cell import Cell

from typing import List
from models.RequiredParam.RequiredParam import RequiredParam

class Product:
    ID_COLUMN_INDEX = 0
    CATEGORY_COLUMN_INDEX = 5

    def __init__(self, row: tuple[Cell]):
        self._row = row

        self._category = self._get_category()

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
            print(index)
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
    






# [{'id': 'pl:42', 'col_index': 63, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pt:16', 'col_index': 85, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pf:121', 'col_index': 90, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:2', 'col_index': 17, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:74', 'col_index': 59, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:69', 'col_index': 60, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:207', 'col_index':f:121', 'col_index': 90, 'cell':  46, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:257', 'col_index': 68, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:259', 'col_index': 70, 'cee': None, 'is_required': True, 'ill': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:131', 'col_index': 33, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:87', 'col_index': 120, 'cell': Nononal': False}, {'id': 'pl:257', 'e, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:128', 'col_index': 36, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pl:208', 'col_index': 45, 'cell': None, 'valux': 33, 'cell': None, 'value': Noe': None, 'is_required': True, 'is_conditional': False}, {'id': 'pf:122', 'col_index': 88, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}, {'id': 'pi:18', 'col_index': None, 'cell': None, 'value': Nonrequired': True, 'is_conditional'e, 'is_required': True, 'is_conditional': False}, {'id': 'pf:118', 'col_index': 92, 'cell': None, 'value': None, 'is_required': True, 'is_conditional': False}]    