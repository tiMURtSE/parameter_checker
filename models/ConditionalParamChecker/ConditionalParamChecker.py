from consts.common_category_conditions import common_category_conditions
from models.Product.Product import Product

class ConditionalParamChecker:
    def check_conditions(self, product: Product):
        try:
            conditions = common_category_conditions[product.category]
        except:
            raise KeyError(f"Не было найдено категории {product.category}")

        for condition in conditions:
            condition.check_condition(product=product)

        return product