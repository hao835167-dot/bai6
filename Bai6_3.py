print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Sử dụng
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
