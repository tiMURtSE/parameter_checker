from consts.params import PARAMS

class RequiredParam:
    def __init__(self, id: str, col_index: int):
        self.id = id
        self.col_index = col_index
        self.cell = None
        self.value = None
        
        self.is_required = True
        self.is_conditional = False
        print(self.__dict__)

    def is_required_parameter_filled(self):
        return self.is_required and self.value
    
    def is_required_parameter_unfilled(self):
        return self.is_required and not self.value
    
    def get_param_name(self):
        for param_name, param_id in PARAMS.items():
            if self.id == param_id:
                return param_name
