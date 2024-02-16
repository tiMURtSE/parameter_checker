from models.ExportWorkbook.ExportWorkbook import ExportWorkbook
from models.Product.Product import Product
from models.CategoryParamsHandler.CategoryParamsHandler import CategoryParamsHandler
from models.ConditionalParamChecker.ConditionalParamChecker import ConditionalParamChecker
from models.Fill.Fill import Fill
from models.Statistics.Statistics import Statistics
from models.ResultWorkbook.ResultWorkbook import ResultWorkbook
from models.ProgressBar.ProgressBar import ProgressBar

class Main:
    PRODUCTS_TABLE_START_POS = 3

    def __init__(self):
        self._export_workbook = ExportWorkbook()
        self._category_params_handler = CategoryParamsHandler()
        self._conditional_param_checker = ConditionalParamChecker()
        self._fill = Fill()
        self._statistics = Statistics()
        self._result_workbook = ResultWorkbook()
        self._progress_bar = ProgressBar()

    def run(self):
        sheet = self._export_workbook.get_data()
        self._category_params_handler.sheet = sheet

        for index, row in enumerate(sheet.iter_rows(min_row=self.PRODUCTS_TABLE_START_POS)):
            product = Product(row=row)
            product = self._category_params_handler.get_category_params(product=product)
            product = self._conditional_param_checker.check_conditions(product=product)

            self._fill.fill_cells(product=product)
            self._statistics.update_statistics(product=product)
            self._progress_bar.show_progress_bar(number_of_completed_rows=index + 1, total_rows=sheet.max_row - 2)

        self._result_workbook.write_result(self._statistics.get_result())
        self._export_workbook.save_workbook()

if __name__ == "__main__":
    app = Main()
    app.run()