import sys
import openpyxl
import tkinter as tk
from tkinter import filedialog

from local_types import ResultType

class ResultWorkbook:
    def __init__(self):
        self._workbook = None
        self._sheet = None
        self._directory_path = None

    def write_result(self, result: ResultType):
        self._directory_path = self._input_result_directory_path()
        self._create_workbook()
        self._write_total_products_info(result)

        self._save_workbook()

    def _create_workbook(self):
        self._workbook = openpyxl.Workbook()
        self._sheet = self._workbook.active

    def _input_result_directory_path(self):
        print("Выберите папку для вывода результатов: ")
        self._remove_extra_window()

        directory_path = filedialog.askdirectory()

        if not directory_path:
            print("Папка не была выбрана")
            sys.exit()

        return directory_path
    
    def _remove_extra_window(self):
        root = tk.Tk()
        root.withdraw()

    def _save_workbook(self):
        self._workbook.save(self._directory_path + "/" + "Result.xlsx")

    def _write_total_products_info(self, result: ResultType):
        total_products = result["total_products"]
        total_incomplete_products = result["total_incomplete_products"]

        self._sheet["A1"].value = f"У {total_incomplete_products} из {total_products} товаров не заполнены обязательные параметры"