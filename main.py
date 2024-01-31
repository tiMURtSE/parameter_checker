from models.Excel.Excel import Excel
from models.Product.Product import Product
from models.Param.Param import Param
from models.ConditionalParamChecker.ConditionalParamChecker import ConditionalParamChecker
from models.Fill.Fill import Fill
from models.Statistics.Statistics import Statistics

class Main:
    PRODUCTS_TABLE_START_POS = 3

    def __init__(self):
        self._excel = Excel()
        self._param = Param()
        self._conditional_param_checker = ConditionalParamChecker()
        self._fill = Fill()
        self._statistics = Statistics()

        self._sheet = None

    def run(self):
        self._sheet = self._excel.get_data()
        self._param.sheet = self._sheet

        for row in self._sheet.iter_rows(min_row=self.PRODUCTS_TABLE_START_POS):
            # Создает объект "Товар"
            product = Product(row=row)

            # Возвращает параметры для заполнения, основываясь на категории товара
            product = self._param.get_category_params(product=product)

            # Получает значения параметров
            product.set_param_values()

            # Определяет какие параметры являются необязательными для заполнения и какие параметрмы являются условными
            product = self._conditional_param_checker.check_conditions(product=product)

            # Заливка ячеек
            self._fill.fill_cells(product=product)

            # Добавление данных товара в объект со статистикой
            self._statistics.update_statistics(product=product)

        print(self._statistics.get_result())
        # self._excel.save_workbook()

if __name__ == "__main__":
    app = Main()
    app.run()