from models.Product.Product import Product
from models.Conditions.Condition import Condition

class ShapeCondition(Condition):
    SHAPE_PARAM_NAME = "Форма"
    SHAPE_OF_LAMPSHADE_PARAM_NAME = "Форма плафона"

    def check_condition(self, product: Product):
        conditional_param_names = [self.SHAPE_PARAM_NAME, self.SHAPE_OF_LAMPSHADE_PARAM_NAME]
        shape, shape_of_lampshade = self._find_conditional_params(
            conditional_param_names=conditional_param_names,
            product=product
        )
        
        if shape.value:
            shape_of_lampshade.is_required = False
        elif shape_of_lampshade.value:
            shape.is_required = False

        self._set_conditional_is_true(conditional_params=[shape, shape_of_lampshade])

        return product