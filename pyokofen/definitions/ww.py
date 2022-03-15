from pyokofen.utils import (
    OkofenDefinition,
    OkofenDefinitionHelperMixin,
    temperature_format,
)


class Ww(OkofenDefinitionHelperMixin, OkofenDefinition):
    def __init__(self, data):
        """domestic hot water data"""
        cls = super()
        cls.__init__("ww")
        cls.set("L_temp_set", temperature_format(data["L_temp_set"]))  # 300
        cls.set("L_ontemp_act", temperature_format(data["L_ontemp_act"]))  # 557
        cls.set("L_offtemp_act", temperature_format(data["L_offtemp_act"]))  # 557
        cls.set("L_pump", data["L_pump"])  # false
        cls.set("L_state", data["L_state"])  # 8200
        cls.set("L_statetext", data["L_statetext"])
        # t hors prog horaire|Demande marche off
        cls.set("time_prg", data["time_prg"])  # 0
        cls.set("sensor_on", data["sensor_on"])  # 0
        cls.set("sensor_off", data["sensor_off"])  # 0
        cls.set("mode_auto", data["mode_auto"])  # 1
        cls.set("mode_dhw", data["mode_dhw"])  # 1
        cls.set("heat_once", data["heat_once"])  # false
        cls.set("temp_min_set", temperature_format(data["temp_min_set"]))  # 350
        cls.set("temp_max_set", temperature_format(data["temp_max_set"]))  # 600
        cls.set("name", data["name"])  #
        cls.set("smartstart", data["smartstart"])  # 0
        cls.set("use_boiler_heat", data["use_boiler_heat"])  # 0
        cls.set("oekomode", data["oekomode"])  # 3
