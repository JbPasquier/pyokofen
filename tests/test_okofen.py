import os
import unittest
import pyokofen


class TestOkofen(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        okofen = pyokofen.Okofen()
        self.okofen = okofen

    async def test_setting_manual_datas(self):
        # Load sample datas
        self.assertTrue(
            await self.okofen.update_datas(
                open(
                    os.path.join(os.path.dirname(__file__), "fixtures/all.json"), "r"
                ).read()
            )
        )
        # Check if sample ambient temp is properly loaded
        self.assertEqual(self.okofen.get("system", "L_ambient"), 7.7)

    """TODO: Some real testing"""


"""Disabled test, require a local okofen boiler with no usb stick on :-)"""
# class TestOkofenStep3(unittest.IsolatedAsyncioTestCase):
#     async def asyncSetUp(self):
#         okofen = pyokofen.Okofen()
#         self.okofen = okofen

#     async def test_sync_datas(self):
#         self.assertTrue(await self.okofen.credentials("192.168.0.240", "4321", "PASS"))
#         self.assertEqual(self.okofen.get("system", "L_usb_stick"), "false")
