from models.Product.Product import Product

class Statistics:
    def __init__(self):
        self.total_products = 0
        self.incomplete_products = 0
        self.unfilled_required_params = {}

    def update_statistics(self, product: Product):
        self.total_products += 1
        self.incomplete_products = self.incomplete_products + 1 if product._is_incomplete() else self.incomplete_products
        self._set_unfilled_required_params(product=product)

    def get_result(self):
        result = {
            "total_products": self.total_products,
            "total_incomplete_products": self.incomplete_products,
            "unfilled_required_params": self.unfilled_required_params,
        }

        return result

    def _set_unfilled_required_params(self, product: Product):
        for param in product.required_params:
            if param.is_required_parameter_unfilled():
                param_name = param.get_param_name()
                
                if param_name in self.unfilled_required_params.keys():
                    self.unfilled_required_params[param_name] += 1
                else:
                    self.unfilled_required_params[param_name] = 1