from consts.params import PARAMS
from models.Product.Product import Product
from models.RequiredParam.RequiredParam import RequiredParam

class Condition:
    def _find_conditional_params(self, conditional_param_names: list[str], product: Product):
        params = []

        for name in conditional_param_names:
            param_id = PARAMS[name]
            param = product.get_required_param(param_id=param_id)

            if param is None:
                raise KeyError("У товара нет нужного условного параметра (хотя должно быть)")

            params.append(param)

        return params

    def _set_conditional_is_true(self, params: list[RequiredParam]):
        for param in params:
            param.is_conditional = True

        return param