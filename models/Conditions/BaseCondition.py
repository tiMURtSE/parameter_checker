from consts.params import PARAMS
from models.Product.Product import Product
from models.Conditions.Condition import Condition

class BaseCondition(Condition):
    BASE_PARAM_NAME = "Цоколь"
    TOTAL_LED_POWER_PARAM_NAME = "Суммарная мощность LED"
    COLOR_TEMPERATURE_PARAM_NAME = "Цветовая температура"
    GLOW_COLOR_PARAM_NAME = "Цвет свечения"
    LUMINOUS_FLUX_PARAM_NAME = "Световой поток, Lm"

    def check_condition(self, product: Product):
        conditional_param_names = [
            self.BASE_PARAM_NAME,
            self.TOTAL_LED_POWER_PARAM_NAME,
            self.COLOR_TEMPERATURE_PARAM_NAME,
            self.GLOW_COLOR_PARAM_NAME,
            self.LUMINOUS_FLUX_PARAM_NAME
        ]
        base, *dependent_params = self._find_conditional_params(
            conditional_param_names=conditional_param_names,
            product=product
        )
        
        if base.value != "LED":
            for param in dependent_params:
                param.is_required = False

        self._set_conditional_is_true(dependent_params)

        return product