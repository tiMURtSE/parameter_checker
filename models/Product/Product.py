from openpyxl.cell.cell import Cell

from typing import List
from models.RequiredParam.RequiredParam import RequiredParam

class Product:
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
    def required_params(self, value: List[RequiredParam]):
        self._required_params = value
        self._set_required_param_values()

    def _set_required_param_values(self):
        for param in self._required_params:
            param.set_cell(row=self._row)

    def get_required_param(self, param_id: str):
        for param in self._required_params:
            if param.id == param_id:
                return param
            
    def _is_incomplete(self):
        for param in self._required_params:
            if param.is_required_parameter_unfilled():
                return True
            
        return False 

    def _get_category(self):
        category = self._row[self.CATEGORY_COLUMN_INDEX].value
        formatted_category = category.lower().strip()

        return formatted_category