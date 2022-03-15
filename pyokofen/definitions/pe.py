from pyokofen.utils import (
    OkofenDefinition,
    OkofenDefinitionHelperMixin,
    temperature_format,
)


class Pe(OkofenDefinitionHelperMixin, OkofenDefinition):
    def __init__(self, data):
        """pellematic data"""
        cls = super()
        cls.__init__("pe")
        cls.set("L_temp_act", temperature_format(data["L_temp_act"]))  # 521
        cls.set("L_temp_set", temperature_format(data["L_temp_set"]))  # 80
        cls.set("L_frt_temp_act", temperature_format(data["L_frt_temp_act"]))  # 917
        cls.set("L_frt_temp_set", temperature_format(data["L_frt_temp_set"]))  # 80
        cls.set("L_ext_temp", data["L_ext_temp"])  # -32768
        cls.set("L_br", data["L_br"])  # false
        cls.set("L_ak", data["L_ak"])  # false
        cls.set("L_not", data["L_not"])  # true
        cls.set("L_stb", data["L_stb"])  # true
        cls.set("L_modulation", data["L_modulation"])  # 0
        cls.set("L_uw_speed", data["L_uw_speed"])  # 0
        cls.set("L_state", data["L_state"])  # 5
        cls.set("L_statetext", data["L_statetext"])  # Mise ? l'arr?t
        cls.set("L_type", data["L_type"])  # 7
        cls.set("L_starts", data["L_starts"])  # 3153
        cls.set("L_runtime", data["L_runtime"])  # 2310
        cls.set("L_avg_runtime", data["L_avg_runtime"])  # 43
        cls.set("L_uw_release", data["L_uw_release"])  # 350
        cls.set("L_uw", data["L_uw"])  # 0
        cls.set("L_storage_fill", data["L_storage_fill"])  # 0
        cls.set("L_storage_min", data["L_storage_min"])  # 400
        cls.set("L_storage_max", data["L_storage_max"])  # 6000
        cls.set("L_storage_popper", data["L_storage_popper"])  # 0
        cls.set("storage_fill_today", data["storage_fill_today"])  # 0
        cls.set("storage_fill_yesterday", data["storage_fill_yesterday"])  # 0
        cls.set("mode", data["mode"])  # 1
