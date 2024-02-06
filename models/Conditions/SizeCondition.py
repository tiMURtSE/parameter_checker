from models.Conditions.Condition import Condition
from models.Product.Product import Product

class SizeCondition(Condition):
    DIAMETER_PARAM_NAME = "Диаметр"
    LENGTH_PARAM_NAME = "Длина"
    WIDTH_PARAM_NAME = "Ширина"

    def check_condition(self, product: Product):
        conditional_param_names = [
            self.DIAMETER_PARAM_NAME,
            self.LENGTH_PARAM_NAME,
            self.WIDTH_PARAM_NAME
        ]
        diameter, length, width = self._find_conditional_params(
            conditional_param_names=conditional_param_names,
            product=product
        )

        if diameter.value:
            width.is_required = False
            length.is_required = False
        elif width.value and length.value:
            diameter.is_required = False

        self._set_conditional_is_true([diameter, length, width])

        return product