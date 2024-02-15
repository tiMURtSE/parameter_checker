from models.RequiredParam.RequiredParam import RequiredParam
from consts.category_param_ids import category_param_ids
from models.Product.Product import Product

class Param:

    def __init__(self):
        self._missing_categories = []
        self._sheet = None

    @property
    def sheet(self):
        return self._sheet
    
    @sheet.setter
    def sheet(self, value):
        try:
            self._sheet = value
        except:
            raise ValueError("Sheet не должно быть пустым значением")

    def get_category_params(self, product: Product):
        required_param_ids = self._get_required_param_ids(category=product.category)
        product.required_params = self._create_required_params(required_param_ids=required_param_ids)

        return product
    
    def _create_required_params(self, required_param_ids: list[str]):
        required_params = []

        for param_id in required_param_ids:
            col_index = self._find_param_col_index(param_id)

            param_obj = RequiredParam(param_id, col_index)
            
            required_params.append(param_obj)

        return required_params

    def _get_required_param_ids(self, category: str):
        ids = []

        try:
            ids = category_param_ids[category]
        except:
            self._missing_categories.append(category)

        return ids

    def _find_param_col_index(self, param_id: str):
        for headings in self._sheet.iter_rows(min_row=1, max_row=1):
            for index, cell in enumerate(headings):
                if cell.value == param_id:
                    return index