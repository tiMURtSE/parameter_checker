from consts.params import PARAMS
from models.Product.Product import Product
from models.RequiredParam.RequiredParam import RequiredParam

class Condition:
    def __init__(self):
        pass

    def _find_conditional_params(self, conditional_param_names: list[str], product: Product):
        params = []

        for name in conditional_param_names:
            param_id = PARAMS[name]
            param = product.get_required_param(param_id=param_id)

            if param is None:
                raise KeyError("У товара нет нужного условного параметра (хотя должно быть)")

            params.append(param)

        return params

    def set_conditional_is_true(self, params: list[RequiredParam]):
        for param in params:
            param.is_conditional = True

        return param
    
class SizeCondition(Condition):
    DIAMETER_PARAM_NAME = "Диаметр"
    LENGTH_PARAM_NAME = "Длина"
    WIDTH_PARAM_NAME = "Ширина"

    def check_condition(self, product: Product):
        conditional_param_names = [self.DIAMETER_PARAM_NAME, self.LENGTH_PARAM_NAME, self.WIDTH_PARAM_NAME]
        diameter, length, width = self._find_conditional_params(conditional_param_names=conditional_param_names, product=product)

        if diameter.value:
            width.is_required = False
            length.is_required = False
        elif width.value and length.value:
            diameter.is_required = False

        self.set_conditional_is_true([diameter, length, width])

        return product

# СТРАТЕГИЯ №2
class BaseCondition(Condition):
    def __init__(self):
        pass

    def check_condition(self, product):
        base = self._find_param(param_id=PARAMS["Цоколь"], required_params=product.required_params)
        total_LED_power = self._find_param(param_id=PARAMS["Суммарная мощность LED"], required_params=product.required_params)
        color_temperature = self._find_param(param_id=PARAMS["Цветовая температура"], required_params=product.required_params)
        glow_color = self._find_param(param_id=PARAMS["Цвет свечения"], required_params=product.required_params)
        luminous_flux = self._find_param(param_id=PARAMS["Световой поток, Lm"], required_params=product.required_params)

        if base.value != "LED":
            total_LED_power.is_required = False
            color_temperature.is_required = False
            glow_color.is_required = False
            luminous_flux.is_required = False

        total_LED_power.is_conditional = True
        color_temperature.is_conditional = True
        glow_color.is_conditional = True
        luminous_flux.is_conditional = True

        return product
