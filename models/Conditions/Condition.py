from consts.params import params
from models.Product.Product import Product
from models.RequiredParam.RequiredParam import RequiredParam

class Condition:
    def _find_conditional_params(self, conditional_param_names: list[str], product: Product):
        conditional_params: list[RequiredParam] = []

        for name in conditional_param_names:
            param_id = params[name]
            param = product.get_required_param(param_id=param_id)

            if param is None:
                print(product.required_params)
                raise KeyError(f"У товара нет нужного условного параметра (хотя должно быть): {name}")

            conditional_params.append(param)

        return conditional_params

    def _set_conditional_is_true(self, conditional_params: list[RequiredParam]):
        for param in conditional_params:
            param.is_conditional = True

        return param