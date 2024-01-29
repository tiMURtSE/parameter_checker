from models.Excel.Excel import Excel
from models.Product.Product import Product
from models.Param.Param import Param

class Main:
    PRODUCTS_TABLE_START_POS = 3

    def __init__(self):
        self._excel = Excel()
        self._param = Param()

        self._sheet = None

    def run(self):
        self._sheet = self._excel.get_data()
        self._param.sheet = self._sheet

        for row in self._sheet.iter_rows(min_row=self.PRODUCTS_TABLE_START_POS):
            product = Product(row=row)
            required_params = self._param.get_category_params(product.category)
            product.required_params = required_params

            print([param.__dict__ for param in product.required_params])

if __name__ == "__main__":
    app = Main()
    app.run()