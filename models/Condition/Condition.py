from consts.params import PARAMS

class Condition:

    def __init__(self):
        pass

    def check_size_condition(self, required_params):
        diametr = self._find_param(param_id=PARAMS["Диаметр"], required_params=required_params)
        shirina = self._find_param(param_id=PARAMS["Длина"], required_params=required_params)
        dlina = self._find_param(param_id=PARAMS["Ширина"], required_params=required_params)

        if diametr.value:
            shirina.is_required = False
            dlina.is_required = False
        elif shirina.value and dlina.value:
            diametr.is_required = False

        diametr.is_conditional = True
        shirina.is_conditional = True
        dlina.is_conditional = True

        return required_params
    
    def check_base_condition(self, required_params):
        base = self._find_param(param_id=PARAMS["Цоколь"], required_params=required_params)
        total_LED_power = self._find_param(param_id=PARAMS["Суммарная мощность LED"], required_params=required_params)
        color_temperature = self._find_param(param_id=PARAMS["Цветовая температура"], required_params=required_params)
        glow_color = self._find_param(param_id=PARAMS["Цвет свечения"], required_params=required_params)
        luminous_flux = self._find_param(param_id=PARAMS["Световой поток, Lm"], required_params=required_params)

        if base.value != "LED":
            total_LED_power.is_required = False
            color_temperature.is_required = False
            glow_color.is_required = False
            luminous_flux.is_required = False

        total_LED_power.is_conditional = True
        color_temperature.is_conditional = True
        glow_color.is_conditional = True
        luminous_flux.is_conditional = True

        return required_params
    
    def check_shape_condition(self, required_params):
        shape = self._find_param(param_id=PARAMS["Форма"], required_params=required_params)
        shape_of_lampshade = self._find_param(param_id=PARAMS["Форма плафона"], required_params=required_params)

        if shape.value:
            shape_of_lampshade.is_required = False
        elif shape_of_lampshade.value:
            shape.is_required = False

        shape.is_conditional = True
        shape_of_lampshade.is_conditional = True

        return required_params
    
    def _find_param(self, param_id: str, required_params: list):
        target_param = [param for param in required_params if param.id == param_id]

        return target_param[0]