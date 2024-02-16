from openpyxl.cell.cell import Cell

from consts.params import params

class RequiredParam:
    def __init__(self, id: str, col_index: int):
        self.id = id
        self.col_index = col_index
        self._cell = None
        self._value = None
        
        self.is_required = True
        self.is_conditional = False

    @property
    def cell(self):
        return self._cell
    
    @cell.setter
    def cell(self, value: Cell):
        self._cell = value

    @property
    def value(self):
        value = self._remove_whitespaces(self._cell.value)

        return value

    def is_required_parameter_filled(self):
        return self.is_required and self.value
    
    def is_required_parameter_unfilled(self):
        return self.is_required and not self.value
    
    def get_param_name(self):
        for param_name, param_id in params.items():
            if self.id == param_id:
                return param_name
            
    def set_cell(self, row: tuple[Cell]):
        cell = row[self.col_index]

        self.cell = cell

    def _remove_whitespaces(self, value):
        if isinstance(value, str):
            return value.strip()
        
        return value