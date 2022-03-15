from pyokofen.utils import (
    OkofenDefinition,
    OkofenDefinitionHelperMixin,
    temperature_format,
)


class System(OkofenDefinitionHelperMixin, OkofenDefinition):
    def __init__(self, data):
        """System global variables"""
        cls = super()
        cls.__init__("system")
        cls.set("L_ambient", temperature_format(data["L_ambient"]))  # 77
        cls.set("L_errors", data["L_errors"])  # 0
        cls.set("L_usb_stick", data["L_usb_stick"])  # false
