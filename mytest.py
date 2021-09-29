class First:
    a = 10
    b = 20
    def pra(self):
        print(self.a)

    def prb(self):
        print(self.b)

    def prs(self):
        print(self.a + self.b)

    def __init__(self, a = a, b = b):
        self.a = a
        self.b = b
class Last(First):
    def prs(self):
        print(self.a - self.b)