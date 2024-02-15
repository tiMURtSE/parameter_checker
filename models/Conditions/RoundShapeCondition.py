from models.Product.Product import Product
from models.Conditions.Condition import Condition

class RoundShapeCondition(Condition):
    WIDTH_PARAM_NAME = "Ширина (см)"
    DEPTH_PARAM_NAME = "Глубина (см)"
    DIAMETER_PARAM_NAME = "Диаметр (см) (см)"

    def check_condition(self, product: Product):
        conditional_param_names = [
            self.WIDTH_PARAM_NAME,
            self.DEPTH_PARAM_NAME,
            self.DIAMETER_PARAM_NAME
        ]

        width, depth, diameter = self._find_conditional_params(
            conditional_param_names=conditional_param_names, product=product
        )

        if diameter.value:
            width.is_required = False
            depth.is_required = False
        elif width.value and depth.value:
            diameter.is_required = False

        self._set_conditional_is_true(conditional_params=[width, depth, diameter])

        return product