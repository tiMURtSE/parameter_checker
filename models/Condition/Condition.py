class Condition:
    DIAM = "pi:20"
    DL = "pi:17"
    SHIR = "pi:19"

    def __init__(self):
        pass

    def check_size_conditions(self, required_params):
        diametr = self._find_param(param_name=self.DIAM, required_params=required_params)
        shirina = self._find_param(param_name=self.SHIR, required_params=required_params)
        dlina = self._find_param(param_name=self.DL, required_params=required_params)

        if diametr.value:
            shirina.is_required = False
            dlina.is_required = False
        elif shirina.value and dlina.value:
            diametr.is_required = False

        diametr.is_conditional = True
        shirina.is_conditional = True
        dlina.is_conditional = True

        return required_params
    
    def _find_param(self, param_name: str, required_params: list):
        target_param = [param for param in required_params if param.name == param_name]

        return target_param[0]