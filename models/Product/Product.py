from openpyxl.cell.cell import Cell

class Product:
    ID_COLUMN_INDEX = 0
    CATEGORY_COLUMN_INDEX = 5

    def __init__(self, row: tuple[Cell]):
        self._row = row

        self._id = self._row[self.ID_COLUMN_INDEX].value
        self._category = self._row[self.CATEGORY_COLUMN_INDEX].value

        self._required_params = []

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