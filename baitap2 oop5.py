class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban):
        if he_so_luong <= 0:
            raise ValueError("Hệ số lương phải > 0")

        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self):
        return self.he_so_luong * self.luong_co_ban

    def hien_thi(self):
        print(f"Mã NV: {self.ma_nv}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Hệ số lương: {self.he_so_luong}")
        print(f"Lương: {self.tinh_luong()}")

class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi,
                 he_so_luong, luong_co_ban, thoi_han_hd, phu_cap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_co_ban)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap = phu_cap

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap

    def hien_thi(self):
        super().hien_thi()
        print(f"Thời hạn HĐ: {self.thoi_han_hd}")
        print(f"Phụ cấp: {self.phu_cap}")

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi,
                 he_so_luong, luong_co_ban, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_co_ban)
        self.vi_tri = vi_tri

    def hien_thi(self):
        super().hien_thi()
        print(f"Vị trí: {self.vi_tri}")

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi,
                 he_so_luong, luong_co_ban, ngay_bat_dau, phu_cap_quan_ly):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh,
                         dia_chi, he_so_luong, luong_co_ban)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap_quan_ly = phu_cap_quan_ly

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap_quan_ly

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngày bắt đầu: {self.ngay_bat_dau}")
        print(f"Phụ cấp QL: {self.phu_cap_quan_ly}")
        
ctv = CongTacVien("CT01", "Nguyễn Văn A", 2000, "Nam", "Hà Nội",
                  2.0, 1500000, "6 tháng", 500000)

nv = NhanVienChinhThuc("NV01", "Trần Thị B", 1995, "Nữ", "HCM",
                        2.5, 1500000, "Kế toán")

tp = TruongPhong("TP01", "Lê Văn C", 1985, "Nam", "Đà Nẵng",
                  3.0, 1500000, "01/01/2020", 2000000)

print("=== Cộng tác viên ===")
ctv.hien_thi()

print("\n=== Nhân viên chính thức ===")
nv.hien_thi()

print("\n=== Trưởng phòng ===")
tp.hien_thi()








