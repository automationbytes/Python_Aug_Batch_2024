

class dad:
    def party(self):
        print("Dad's party method")

    def gift(self):
        print("Dad's gift method")


class mom:
    def function(self):
        print("Mom's function method")

    def gift(self):
        print("Mom's gift method")

class child(dad,mom): #Method Resoln Order (MRO)
    def ahgah(self):
        pass

c = child()
c.function()
c.party()
c.gift()