import math
from HinhHoc import HinhHoc


class HinhTron(HinhHoc):

    def __init__(self, bankinh: float) -> None:
        self.__banKinh = bankinh
        super().__init__(bankinh)

    def HinhTron(self, banKinh: float):
        pass

    def TinhDienTich(self) -> float:
        return pow(self.__banKinh) * math.pi

    def xuat(self):
        print(self.__banKinh, self.tinhDienTich())

    @property
    def banKinh(self):
        return self._canh


ht = HinhTron(5)
ht.tinhDienTich(7)
# ht.xuat()
