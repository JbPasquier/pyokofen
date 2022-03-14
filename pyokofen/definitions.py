import pyokofen.utils


class System:
    def __init__(self, data):
        """System global variables"""
        self.L_ambient = pyokofen.utils.temperature_format(data["L_ambient"])  # 77


class Hk:
    def __init__(self, data):
        """heating circuit data"""
        self.L_roomtemp_act = pyokofen.utils.temperature_format(
            data["L_roomtemp_act"]
        )  # 188
        self.L_roomtemp_set = pyokofen.utils.temperature_format(
            data["L_roomtemp_set"]
        )  # 80
        self.L_flowtemp_act = pyokofen.utils.temperature_format(
            data["L_flowtemp_act"]
        )  # 355
        self.L_flowtemp_set = pyokofen.utils.temperature_format(
            data["L_flowtemp_set"]
        )  # 80
        self.L_comfort = data["L_comfort"]  # 0
        self.L_state = data["L_state"]  # 264224
        self.L_statetext = data[
            "L_statetext"
        ]  # Mode confort actif|T ambiante atteinte|Beau temps - abaissement T?C amb en cours
        self.L_pump = data["L_pump"]  # false
        self.remote_override = data["remote_override"]  # 0
        self.mode_auto = data["mode_auto"]  # 1
        self.time_prg = data["time_prg"]  # 0
        self.temp_setback = data["temp_setback"]  # 175
        self.temp_heat = data["temp_heat"]  # 190
        self.temp_vacation = data["temp_vacation"]  # 160
        self.name = data["name"]  #
        self.oekomode = data["oekomode"]  # 3
        self.autocomfort = data["autocomfort"]  # -1
        self.autocomfort_sunset = data["autocomfort_sunset"]  # 0
        self.autocomfort_sunrise = data["autocomfort_sunrise"]  #


class Ww:
    def __init__(self, data):
        """domestic hot water data"""
        self.L_temp_set = pyokofen.utils.temperature_format(data["L_temp_set"])  # 300
        self.L_ontemp_act = pyokofen.utils.temperature_format(
            data["L_ontemp_act"]
        )  # 557
        self.L_offtemp_act = pyokofen.utils.temperature_format(
            data["L_offtemp_act"]
        )  # 557
        self.L_pump = data["L_pump"]  # false
        self.L_state = data["L_state"]  # 8200
        self.L_statetext = data["L_statetext"]  # t hors prog horaire|Demande marche off
        self.time_prg = data["time_prg"]  # 0
        self.sensor_on = data["sensor_on"]  # 0
        self.sensor_off = data["sensor_off"]  # 0
        self.mode_auto = data["mode_auto"]  # 1
        self.mode_dhw = data["mode_dhw"]  # 1
        self.heat_once = data["heat_once"]  # false
        self.temp_min_set = pyokofen.utils.temperature_format(
            data["temp_min_set"]
        )  # 350
        self.temp_max_set = pyokofen.utils.temperature_format(
            data["temp_max_set"]
        )  # 600
        self.name = data["name"]  #
        self.smartstart = data["smartstart"]  # 0
        self.use_boiler_heat = data["use_boiler_heat"]  # 0
        self.oekomode = data["oekomode"]  # 3


class Sk:
    def __init__(self, data):
        """solar circuit data"""
        self.L_koll_temp = pyokofen.utils.temperature_format(data["L_koll_temp"])  # 405
        self.L_spu = pyokofen.utils.temperature_format(data["L_spu"])  # 352
        self.L_pump = data["L_pump"]  # 0
        self.L_state = data["L_state"]  # 65536
        self.L_statetext = data["L_statetext"]  # Tmin PanSol pas atteinte
        self.mode = data["mode"]  # 1
        self.cooling = data["cooling"]  # 0
        self.spu_max = pyokofen.utils.temperature_format(data["spu_max"])  # 800
        self.name = data["name"]  #


class Pe:
    def __init__(self, data):
        """pellematic data"""
        self.L_temp_act = pyokofen.utils.temperature_format(data["L_temp_act"])  # 521
        self.L_temp_set = pyokofen.utils.temperature_format(data["L_temp_set"])  # 80
        self.L_ext_temp = data["L_ext_temp"]  # -32768
        self.L_frt_temp_act = pyokofen.utils.temperature_format(
            data["L_frt_temp_act"]
        )  # 917
        self.L_frt_temp_set = pyokofen.utils.temperature_format(
            data["L_frt_temp_set"]
        )  # 80
        self.L_br = data["L_br"]  # false
        self.L_ak = data["L_ak"]  # false
        self.L_not = data["L_not"]  # true
        self.L_stb = data["L_stb"]  # true
        self.L_modulation = data["L_modulation"]  # 0
        self.L_uw_speed = data["L_uw_speed"]  # 0
        self.L_state = data["L_state"]  # 5
        self.L_statetext = data["L_statetext"]  # Mise ? l'arr?t
        self.L_type = data["L_type"]  # 7
        self.L_starts = data["L_starts"]  # 3153
        self.L_runtime = data["L_runtime"]  # 2310
        self.L_avg_runtime = data["L_avg_runtime"]  # 43
        self.L_uw_release = data["L_uw_release"]  # 350
        self.L_uw = data["L_uw"]  # 0
        self.L_storage_fill = data["L_storage_fill"]  # 0
        self.L_storage_min = data["L_storage_min"]  # 400
        self.L_storage_max = data["L_storage_max"]  # 6000
        self.L_storage_popper = data["L_storage_popper"]  # 0
        self.storage_fill_today = data["storage_fill_today"]  # 0
        self.storage_fill_yesterday = data["storage_fill_yesterday"]  # 0
        self.mode = data["mode"]  # 1
