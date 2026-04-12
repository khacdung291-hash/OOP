from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self.gia = gia  

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe("Giá phải >= 0")
        self._gia = value

    @abstractmethod
    def hien_thi(self):
        pass

    def __str__(self):
        return f"{self._ma_hang} - {self._ten_hang} - {self._gia}"

    def __eq__(self, other):
        return self._ma_hang == other._ma_hang

    def __lt__(self, other):
        return self._gia < other._gia

    def __hash__(self):
        return hash(self._ma_hang)

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def hien_thi(self):
        print(self)
        print(f"Bảo hành: {self.tg_baohanh}")
        print(f"Điện áp: {self.dien_ap}")
        print(f"Công suất: {self.cong_suat}")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def hien_thi(self):
        print(self)
        print(f"Nguyên liệu: {self.loai_nguyenlieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def hien_thi(self):
        print(self)
        print(f"Ngày SX: {self.ngay_sx}")
        print(f"Hạn dùng: {self.ngay_hethan}")

ds = []

try:
    ds.append(HangDienMay("DM01", "Tủ lạnh", "Samsung", 10000000, "24 tháng", "220V", "150W"))
    ds.append(HangSanhSu("SS01", "Bát sứ", "Minh Long", 50000, "Sứ cao cấp"))
    ds.append(HangThucPham("TP01", "Sữa", "Vinamilk", 30000, "01/01/2024", "01/06/2024"))

    print("=== DANH SÁCH HÀNG HÓA ===")
    for sp in ds:
        sp.hien_thi()
        print("------")

    print("\n=== SẮP XẾP THEO GIÁ ===")
    for sp in sorted(ds):
        print(sp)

    print("\n=== TEST SET ===")
    s = set(ds)
    for sp in s:
        print(sp)

except GiaKhongHopLe as e:
    print("Lỗi:", e)







