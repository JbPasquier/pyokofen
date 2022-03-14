"""JSON to python API for Okofen boilers"""
import requests
import json
import pyokofen.definitions


class Okofen:
    def __init__(self) -> None:
        """Initialize."""
        return None

    async def credentials(self, ip, port, password) -> None:
        self.ip = ip
        self.port = port
        self.password = password

    async def get_data(self) -> bool:
        response = requests.get(
            "http://" + self.ip + ":" + self.port + "/" + self.password + "/all?"
        )
        if response.status_code == 200:
            return await self.set_data(response.text)

        return False

    async def set_data(self, data) -> bool:
        try:
            self.data = json.loads(data)
        except ValueError:
            return False
        return await self.handle_data()

    async def handle_data(self) -> bool:
        try:
            if self.data["system"]:
                self.system = pyokofen.definitions.System(self.data["system"])

            """TODO: weather"""
            if self.data["weather"]:
                self.weather = pyokofen.definitions.Weather(self.data["weather"])

            """TODO: forecast"""
            if self.data["forecast"]:
                self.forecast = pyokofen.definitions.Forecast(self.data["forecast"])

            """TODO: powermeter"""
            if self.data["power"]:
                self.power = pyokofen.definitions.Power(self.data["power"])

            """TODO: stirling"""
            if self.data["stirling"]:
                self.stirling = pyokofen.definitions.Stirling(self.data["stirling"])

            self.hk = []
            for i in range(7):
                if self.data["hk" + i]:
                    self.hk.append(pyokofen.definitions.Hk(self.data["hk" + i]))

            """TODO: Third party sensors"""
            self.thirdparty = []
            for i in range(11):
                if self.data["thirdparty" + i]:
                    self.thirdparty.append(
                        pyokofen.definitions.Thirdparty(self.data["thirdparty" + i])
                    )

            """TODO: accu"""
            self.pu = []
            for i in range(4):
                if self.data["pu" + i]:
                    self.pu.append(pyokofen.definitions.Pu(self.data["pu" + i]))

            self.ww = []
            for i in range(4):
                if self.data["ww" + i]:
                    self.ww.append(pyokofen.definitions.Ww(self.data["ww" + i]))

            self.sk = []
            for i in range(7):
                if self.data["sk" + i]:
                    self.sk.append(pyokofen.definitions.Sk(self.data["sk" + i]))

            """TODO: Solar gain"""
            self.se = []
            for i in range(4):
                if self.data["se" + i]:
                    self.se.append(pyokofen.definitions.Se(self.data["se" + i]))

            """TODO: circulation pump"""
            self.circ = []
            for i in range(4):
                if self.data["circ" + i]:
                    self.circ.append(pyokofen.definitions.Circ(self.data["circ" + i]))

            self.pe = []
            for i in range(5):
                if self.data["pe" + i]:
                    self.pe.append(pyokofen.definitions.Pe(self.data["pe" + i]))

            """TODO: 5k stirling"""
            self.st5k = []
            for i in range(5):
                if self.data["st5k" + i]:
                    self.st5k.append(pyokofen.definitions.St5k(self.data["st5k" + i]))

            return True
        except:
            return False
