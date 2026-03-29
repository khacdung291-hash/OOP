class NhanVien:
    LUONG_MAX = 50000000  

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong
    def getTenNhanVien(self):
        return self.__tenNhanVien

    def setTenNhanVien(self, ten):
        self.__tenNhanVien = ten

    def getLuongCoBan(self):
        return self.__luongCoBan

    def setLuongCoBan(self, luong):
        self.__luongCoBan = luong

    def getHeSoLuong(self):
        return self.__heSoLuong

    def setHeSoLuong(self, heso):
        self.__heSoLuong = heso
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong
    def inTTin(self):
        print(f"Tên: {self.__tenNhanVien}")
        print(f"Lương cơ bản: {self.__luongCoBan}")
        print(f"Hệ số lương: {self.__heSoLuong}")
        print(f"Lương: {self.tinhLuong()}")
    def tangLuong(self, giaTri):
        heSoMoi = self.__heSoLuong + giaTri
        luongMoi = self.__luongCoBan * heSoMoi

        if luongMoi > NhanVien.LUONG_MAX:
            print("Không thể tăng lương, vượt quá mức tối đa!")
            return False
        else:
            self.__heSoLuong = heSoMoi
            return True
#exam
nv = NhanVien("Nguyen Van A", 5000000, 2.0)
nv.inTTin()

print("\nTăng lương:")
if nv.tangLuong(1.5):
    print("Tăng lương thành công!")
else:
    print("Tăng lương thất bại!")

nv.inTTin()