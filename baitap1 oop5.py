class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def hien_thi(self):
        print(f"Mã: {self.ma_hang}")
        print(f"Tên: {self.ten_hang}")
        print(f"Nhà SX: {self.nha_sx}")
        print(f"Giá: {self.gia}")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def hien_thi(self):
        super().hien_thi()
        print(f"Bảo hành: {self.tg_baohanh}")
        print(f"Điện áp: {self.dien_ap}")
        print(f"Công suất: {self.cong_suat}")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def hien_thi(self):
        super().hien_thi()
        print(f"Nguyên liệu: {self.loai_nguyenlieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngày SX: {self.ngay_sx}")
        print(f"Hạn dùng: {self.ngay_hethan}")

dien_may = HangDienMay("DM01", "Tủ lạnh", "Samsung", 10000000, "24 tháng", "220V", "150W")
sanh_su = HangSanhSu("SS01", "Bát sứ", "Minh Long", 50000, "Sứ cao cấp")
thuc_pham = HangThucPham("TP01", "Sữa", "Vinamilk", 30000, "01/01/2024", "01/06/2024")

print("=== Hàng điện máy ===")
dien_may.hien_thi()

print("\n=== Hàng sành sứ ===")
sanh_su.hien_thi()

print("\n=== Hàng thực phẩm ===")
thuc_pham.hien_thi()








