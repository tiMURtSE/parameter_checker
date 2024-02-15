from models.Product.Product import Product
from models.Conditions.Condition import Condition

class TableLegsColorCondition(Condition):
    TABLE_LEGS_COLOR_PARAM_NAME = "Цвет ножек"
    BASE_TYPE_PARAM_NAME = "Тип опоры"

    def check_condition(self, product: Product):
        conditional_param_names = [
            self.TABLE_LEGS_COLOR_PARAM_NAME,
            self.BASE_TYPE_PARAM_NAME,
        ]

        table_legs_color, base_type = self._find_conditional_params(
            conditional_param_names=conditional_param_names, product=product
        )

        if base_type.value != "на ножках":
            table_legs_color.is_required = False

        self._set_conditional_is_true(conditional_params=[table_legs_color])

        return product