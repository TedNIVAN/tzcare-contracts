import smartpy as sp

class Tzcare(sp.Contract):
    def __init__(self):
        self.init(device_alert = "XXXXXXYYYYYYZZZZ")

    @sp.entry_point
    def setAlert(self, params):
        self.data.device_alert = params

# Tests
@sp.add_test(name = "Basic Test")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Alert Test")

    c1 = Tzcare()
    scenario += c1
    scenario.h2("Set Alert")
    scenario += c1.setAlert("AAAAAABBBBBBCCCC")