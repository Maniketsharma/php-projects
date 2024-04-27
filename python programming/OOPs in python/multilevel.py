class dad:
    basketball=9
class son(dad):
    dance=1
    def isdance(self):
        return f"Yes i can dance{self.dance} no of times"

class Grandson(son):
    dance=6

    def isdance(self):
        return f"yeh jeckson!"\
               f"Yes they can dance mickel jection version {self.dance} no of times"
darry=dad()
larry=son()
harry=Grandson()
print(harry.isdance())
print(harry.basketball)

