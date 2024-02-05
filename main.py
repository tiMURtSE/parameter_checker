from models.ExportWorkbook.ExportWorkbook import ExportWorkbook
from models.Product.Product import Product
from models.Param.Param import Param
from models.ConditionalParamChecker.ConditionalParamChecker import ConditionalParamChecker
from models.Fill.Fill import Fill
from models.Statistics.Statistics import Statistics
from models.ResultWorkbook.ResultWorkbook import ResultWorkbook

class Main:
    PRODUCTS_TABLE_START_POS = 3

    def __init__(self):
        self._export_workbook = ExportWorkbook()
        self._param = Param()
        self._conditional_param_checker = ConditionalParamChecker()
        self._fill = Fill()
        self._statistics = Statistics()
        self._result_workbook = ResultWorkbook()

        self._sheet = None

    def run(self):
        self._sheet = self._export_workbook.get_data()
        self._param.sheet = self._sheet

        for index, row in enumerate(self._sheet.iter_rows(min_row=self.PRODUCTS_TABLE_START_POS)):
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

            # Лог
            print(f"Номер строки: {index + 1}")
            print([param.__dict__ for param in product.required_params])

        print(self._statistics.get_result())
        # self._result_workbook.write_result(self._statistics.get_result())
        # self._export_workbook.save_workbook()

if __name__ == "__main__":
    app = Main()
    app.run()