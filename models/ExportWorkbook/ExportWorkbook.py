import sys
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import tkinter as tk
from tkinter import filedialog

class ExportWorkbook:
    TEST_FILE_PATH = "C:/Users/user10/Desktop/Stuff/Scripts/variations_3.0/Выгрузка/ss.xlsx"

    def __init__(self):
        self._setup()

    def _setup(self):
        # self._file_path = self._input_file_path()
        self._file_path = self.TEST_FILE_PATH
        self._workbook = openpyxl.load_workbook(self._file_path)
        self._sheet = self._workbook.active

    def get_data(self) -> Worksheet:
        return self._sheet
    
    def save_workbook(self):
        self._workbook.save(self._file_path)

    def _input_file_path(self):
        print("Выберите файл для проверки: ")
        self._remove_extra_window()

        file_path = filedialog.askopenfilename()

        if not file_path:
            print("Файл не был открыт")
            sys.exit()

        return file_path
    
    def _remove_extra_window(self):
        root = tk.Tk()
        root.withdraw()