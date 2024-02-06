from consts.category_conditional_params import CATEGORY_CONDITIONAL_PARAMS
from models.Condition.Condition import Condition
from models.Product.Product import Product

class ConditionalParamChecker:
    def __init__(self):
        self._condition = Condition()

    def check_conditions(self, product: Product):
        try:
            conditions = CATEGORY_CONDITIONAL_PARAMS[product.category]
        except:
            raise KeyError(f"Не было найдено категории {product.category}")

        for condition in conditions:
            condition.check_condition(product=product)

        return product