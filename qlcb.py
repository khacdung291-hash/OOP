class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi(self):
        print(f"Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, "
              f"Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}")


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def hien_thi(self):
        super().hien_thi()
        print(f"Bậc: {self.bac}")


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngành đào tạo: {self.nganh_dao_tao}")


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi(self):
        super().hien_thi()
        print(f"Công việc: {self.cong_viec}")


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
            cb.hien_thi()
            print("-" * 30)


def main():
    ql = QLCB()

    while True:
        print("\n--- QUẢN LÝ CÁN BỘ ---")
        print("1. Thêm cán bộ")
        print("2. Tìm kiếm theo tên")
        print("3. Hiển thị danh sách")
        print("4. Thoát")

        chon = input("Chọn: ")

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
            if not kq:
                print("Không tìm thấy!")
            else:
                for cb in kq:
                    cb.hien_thi()
                    print("-" * 30)

        elif chon == "3":
            ql.hien_thi_ds()

        elif chon == "4":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()







