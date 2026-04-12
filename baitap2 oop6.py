from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception): pass
class BacKhongHopLe(Exception): pass

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten = ho_ten
        self.tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    @property
    def ho_ten(self):
        return self._ho_ten

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if value < 18 or value > 65:
            raise TuoiKhongHopLe("Tuổi phải từ 18-65")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self._ho_ten} - {self._tuoi} - {self._gioi_tinh} - {self._dia_chi}"

    def __eq__(self, other):
        return self._ho_ten == other._ho_ten and self._tuoi == other._tuoi

    def __lt__(self, other):
        return self._ho_ten < other._ho_ten

    def __hash__(self):
        return hash((self._ho_ten, self._tuoi))

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if value < 1 or value > 10:
            raise BacKhongHopLe("Bậc phải từ 1-10")
        self._bac = value

    def mo_ta(self):
        return f"{self} - Bậc: {self._bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def mo_ta(self):
        return f"{self} - Ngành: {self.nganh}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"{self} - Công việc: {self.cong_viec}"

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them_can_bo(self, can_bo):
        self.danh_sach.append(can_bo)

    def tim_kiem(self, ten):
        return [cb for cb in self.danh_sach if ten.lower() in cb.ho_ten.lower()]

    def hien_thi_ds(self):
        if not self.danh_sach:
            print("Danh sách rỗng!")
        for cb in self.danh_sach:
            print(cb.mo_ta())
            print("-" * 30)

    def luu_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for cb in self.danh_sach:
                f.write(cb.mo_ta() + "\n")
                    #Main
def main():
    ql = QLCB()

    while True:
        print("\n--- QUẢN LÝ CÁN BỘ ---")
        print("1. Thêm cán bộ")
        print("2. Tìm kiếm theo tên")
        print("3. Hiển thị danh sách")
        print("4. Sắp xếp theo tên")
        print("5. Thoát")

        chon = input("Chọn: ")

        try:
            if chon == "1":
                loai = input("Loại (congnhan/kysu/nhanvien): ")
                ho_ten = input("Họ tên: ")
                tuoi = int(input("Tuổi: "))
                gioi_tinh = input("Giới tính: ")
                dia_chi = input("Địa chỉ: ")

                if loai == "congnhan":
                    bac = int(input("Bậc (1-10): "))
                    cb = CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)

                elif loai == "kysu":
                    nganh = input("Ngành đào tạo: ")
                    cb = KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)

                elif loai == "nhanvien":
                    cv = input("Công việc: ")
                    cb = NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cv)

                else:
                    print("Loại không hợp lệ!")
                    continue

                ql.them_can_bo(cb)
                print("Đã thêm!")

            elif chon == "2":
                ten = input("Nhập tên cần tìm: ")
                kq = ql.tim_kiem(ten)
                for cb in kq:
                    print(cb.mo_ta())

            elif chon == "3":
                ql.hien_thi_ds()

            elif chon == "4":
                for cb in sorted(ql.danh_sach):
                    print(cb.mo_ta())

            elif chon == "5":
                print("Thoát!")
                break

            else:
                print("Không hợp lệ!")

        except (TuoiKhongHopLe, BacKhongHopLe) as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()






