class shape():
    
    def __init__(self) -> None:
        pass
    def area(self):
        return 0

class square(shape):
    
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length * self.length


a = int(input())
s = square(x)
print(s.area())

print(square().area())