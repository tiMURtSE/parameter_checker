from models.Excel.Excel import Excel

class Main:
    def __init__(self):
        self._excel = Excel()

        self._sheet = None

    def run(self):
        self._sheet = self._excel.get_data()

        for row in self._sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=2):
            for cell in row:
                print(cell.value)

if __name__ == "__main__":
    app = Main()
    app.run()