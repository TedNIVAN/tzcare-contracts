import smartpy as sp

class Tzcare(sp.Contract):
    def __init__(self, initialOwner):
        self.init(owner = initialOwner, user = initialOwner, device_alert = "XXXXXXYYYYYYZZZZ", amount_to_stack = sp.tez(10))

    @sp.entry_point
    def setAlert(self, params):
        sp.verify(sp.amount >= self.data.amount_to_stack)
        self.data.device_alert = params
        self.data.user = sp.sender

    @sp.entry_point
    def unlockAmount(self, params):
        sp.verify(sp.sender == self.data.owner)
        sp.verify(sp.balance >= self.data.amount_to_stack)
        sp.send(params, self.data.amount_to_stack)

# Tests
@sp.add_test(name = "Basic Test")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Alert Test")

    c1 = Tzcare(sp.address("tz1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
    scenario += c1
    scenario.h2("Update Alert")
    scenario += c1.setAlert("AAAAAABBBBBBCCCC").run(amount = sp.tez(10))
    
    scenario.h2("Unlock Amount")
    scenario += c1.unlockAmount(sp.address("tz1YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")).run(sender = sp.address("tz1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
    
