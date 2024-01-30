from consts.category_conditional_params import CATEGORY_CONDITIONAL_PARAMS
from models.Condition.Condition import Condition
from models.Product.Product import Product

class ConditionalParamChecker:
    def __init__(self):
        self._condition = Condition()

    def check_conditions(self, product: Product):
        category = product.category
        required_params = product.required_params

        formatted_category = category.lower().strip()
        conditions = CATEGORY_CONDITIONAL_PARAMS[formatted_category]

        for condition in conditions:
            if condition == "размер":
                required_params = self._condition.check_size_condition(required_params=required_params)
            elif condition == "цоколь":
                required_params = self._condition.check_base_condition(required_params=required_params)
            elif condition == "внешний вид":
                required_params = self._condition.check_appearance_condition(required_params=required_params)

        product.required_params = required_params

        return product