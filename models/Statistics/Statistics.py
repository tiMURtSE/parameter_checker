class Statistics:
    def __init__(self):
        self.total_products = 0
        self.total_required_params = 0
        self.total_conditional_params = 0
        self.missing_categories = []

    def update_statistics(self, product):
        self.total_products += 1
        self.total_required_params += len(product.required_params)
        self.total_conditional_params += len(product.required_conditional_params)
        self.missing_categories.extend(product.missing_categories)

    def get_summary(self):
        summary = {
            "Total Products": self.total_products,
            "Total Required Params": self.total_required_params,
            "Total Conditional Params": self.total_conditional_params,
            "Missing Categories": self.missing_categories
        }
        return summary
