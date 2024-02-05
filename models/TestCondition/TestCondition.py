from consts.params import PARAMS

# class Context:
#     def __init__(self, strategy):
#         self._strategy = strategy

#     def set_strategy(self, strategy):
#         self._strategy = strategy

#     def perform_check(self, product):
#         product = self._strategy.check_condition(product)

#         return product

class Strategy:
    def __init__(self):
        pass

    def check_condition(self, product):
        pass

    def _find_param(self, param_id: str, required_params: list):
        target_param = [param for param in required_params if param.id == param_id]

        return target_param[0]
    
    def _find_params(self, conditional_param_names, product):
        params = []

        for name in conditional_param_names:
            param_id = PARAMS[name]
            param = self._find_param(param_id=param_id, required_params=product.required_params)

            params.append(param)

        return params

    def set_conditional_is_true(self, params):
        for param in params:
            param.is_conditional = True

        return param
    
# СТРАТЕГИЯ №1
class SizeStrategy(Strategy):
    def __init__(self):
        pass

    def check_condition(self, product):
        conditional_param_names = ["Диаметр", "Длина", "Ширина"]
        diameter, length, width = self._find_params(conditional_param_names, product)

        if diameter.value:
            width.is_required = False
            length.is_required = False
        elif width.value and length.value:
            diameter.is_required = False

        diameter.is_conditional = True
        width.is_conditional = True
        length.is_conditional = True

        self.set_conditional_is_true([diameter, length, width])

        return product

# СТРАТЕГИЯ №2
class BaseCondition(Strategy):
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
