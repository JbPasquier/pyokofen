import os
import unittest


class TestOkofen(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        import pyokofen

        okofen = pyokofen.Okofen()
        await okofen.set_data(
            open(os.path.join(os.path.dirname(__file__), "fixtures/all"), "r").read()
        )
        self.okofen = okofen

    async def test_get_data(self):
        self.assertEqual(self.okofen.system.L_ambient, 7.7)

    """TODO: Some real testing"""
