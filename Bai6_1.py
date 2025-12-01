print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius ** 2 * 3.14

# Sử dụng
aCircle = Circle(2)
print(aCircle.area())
