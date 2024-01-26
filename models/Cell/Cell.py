from openpyxl.cell.cell import Cell

class Cell:
    def __init__(self, param: str, cell: Cell):
        self._param = param

        self.cell = cell
        self.value = cell.value
        self.is_required = True

        self.is_conditional = False

    @property
    def cell(self):
        return self.cell

    @property
    def value(self):
        return self.value
    
    @property
    def is_required(self):
        return self.is_required