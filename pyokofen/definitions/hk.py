from pyokofen.utils import (
    OkofenDefinition,
    OkofenDefinitionHelperMixin,
    temperature_format,
)


class Hk(OkofenDefinitionHelperMixin, OkofenDefinition):
    def __init__(self, data):
        """heating circuit data"""
        cls = super()
        cls.__init__("hk")
        cls.set("L_roomtemp_act", temperature_format(data["L_roomtemp_act"]))  # 188
        cls.set("L_roomtemp_set", temperature_format(data["L_roomtemp_set"]))  # 80
        cls.set("L_flowtemp_act", temperature_format(data["L_flowtemp_act"]))  # 355
        cls.set("L_flowtemp_set", temperature_format(data["L_flowtemp_set"]))  # 80
        cls.set("L_comfort", data["L_comfort"])  # 0
        cls.set("L_state", data["L_state"])  # 264224
        cls.set("L_statetext", data["L_statetext"])
        # Mode confort actif|T ambiante atteinte|Beau temps - abaissement T?C amb en cours
        cls.set("L_pump", data["L_pump"])  # false
        cls.set("remote_override", data["remote_override"])  # 0
        cls.set("mode_auto", data["mode_auto"])  # 1
        cls.set("time_prg", data["time_prg"])  # 0
        cls.set("temp_setback", data["temp_setback"])  # 175
        cls.set("temp_heat", data["temp_heat"])  # 190
        cls.set("temp_vacation", data["temp_vacation"])  # 160
        cls.set("name", data["name"])  #
        cls.set("oekomode", data["oekomode"])  # 3
        cls.set("autocomfort", data["autocomfort"])  # -1
        cls.set("autocomfort_sunset", data["autocomfort_sunset"])  # 0
        cls.set("autocomfort_sunrise", data["autocomfort_sunrise"])  #
