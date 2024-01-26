from models.Excel.Excel import Excel
from models.Product.Product import Product

class Main:
    PRODUCTS_TABLE_START_POS = 3

    def __init__(self):
        self._excel = Excel()
        self._sheet = None

    def run(self):
        self._sheet = self._excel.get_data()

        for row in self._sheet.iter_rows(min_row=self.PRODUCTS_TABLE_START_POS):
            product = Product(row=row)


if __name__ == "__main__":
    app = Main()
    app.run()