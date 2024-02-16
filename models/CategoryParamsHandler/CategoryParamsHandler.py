from openpyxl.worksheet.worksheet import Worksheet

from models.RequiredParam.RequiredParam import RequiredParam
from models.Product.Product import Product
from consts.category_param_ids import category_param_ids

class CategoryParamsHandler:
    def __init__(self):
        self._sheet = None
        self._missing_categories = []

    @property
    def sheet(self):
        return self._sheet
    
    @sheet.setter
    def sheet(self, value: Worksheet):
        if isinstance(value, Worksheet):
            self._sheet = value
        else:
            raise TypeError("Значение sheet должно иметь тип Worksheet")

    def get_category_params(self, product: Product):
        required_param_ids = self._get_required_param_ids(category=product.category)
        required_params = self._create_required_params(required_param_ids=required_param_ids)
        product.required_params = required_params

        return product
    
    def _create_required_params(self, required_param_ids: list[str]):
        required_params = []

        for param_id in required_param_ids:
            col_index = self._find_param_col_index(param_id)

            param_obj = RequiredParam(param_id, col_index)
            
            required_params.append(param_obj)

        return required_params

    def _get_required_param_ids(self, category: str):
        param_ids = []

        try:
            param_ids = category_param_ids[category]
        except:
            raise KeyError(f"Не было найдено нужной категории: {category}")

        return param_ids

    def _find_param_col_index(self, param_id: str):
        # for headings in self._sheet.iter_rows(min_row=1, max_row=1):
        #     for index, cell in enumerate(headings):
        #         if cell.value == param_id:
        #             return index

        for col_index, param_heading in enumerate(self._sheet.iter_cols(min_row=1, max_row=1)):
            cell = param_heading[0]

            if cell.value == param_id:
                return col_index