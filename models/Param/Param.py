from models.RequiredParam.RequiredParam import RequiredParam
from consts.category_params import CATEGORY_PARAMS
from local_types import RequiredParamType

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

    def get_category_params(self, category: str) -> RequiredParamType:
        required_param_names = self._get_required_param_names(category=category)
        required_params = self._create_required_params(required_param_names=required_param_names)

        return required_params
    
    def _create_required_params(self, required_param_names: list[str]):
        required_params = []

        for param_name in required_param_names:
            col_index = self._find_param_col_index(param_name)

            param_obj = RequiredParam(param_name, col_index)

            required_params.append(param_obj)

        return required_params

    def _get_required_param_names(self, category: str):
        names = []

        try:
            formatted_category = category.lower().strip()
            names = CATEGORY_PARAMS[formatted_category]
        except:
            self._missing_categories.append(category)

        return names

    def _find_param_col_index(self, param_name: str):
        for headings in self._sheet.iter_rows(min_row=1, max_row=1):
            for index, cell in enumerate(headings):
                if cell.value == param_name:
                    return index