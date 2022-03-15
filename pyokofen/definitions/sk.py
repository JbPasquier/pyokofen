from pyokofen.utils import (
    OkofenDefinition,
    OkofenDefinitionHelperMixin,
    temperature_format,
)


class Sk(OkofenDefinitionHelperMixin, OkofenDefinition):
    def __init__(self, data):
        """solar circuit data"""
        cls = super()
        cls.__init__("sk")
        cls.set("L_koll_temp", temperature_format(data["L_koll_temp"]))  # 405
        cls.set("L_spu", temperature_format(data["L_spu"]))  # 352
        cls.set("L_pump", data["L_pump"])  # 0
        cls.set("L_state", data["L_state"])  # 65536
        cls.set("L_statetext", data["L_statetext"])  # Tmin PanSol pas atteinte
        cls.set("mode", data["mode"])  # 1
        cls.set("cooling", data["cooling"])  # 0
        cls.set("spu_max", temperature_format(data["spu_max"]))  # 800
        cls.set("name", data["name"])  #
