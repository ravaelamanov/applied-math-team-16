class Function:
    def __init__(self, f, a, b, x0):
        self.f = f
        self.a = a
        self.b = b
        self.x0 = x0
    
    def params(self):
        return (self.f, self.a, self.b)
