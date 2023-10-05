from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime):
        self.__maSo = maSo  
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi


    def __str__(self):
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"


    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")



class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSinhVienTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv(self, mssv:int):
        for i in range (len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1


    def XoaSvTheoMssv(self, maso:int) -> bool:
        vt = self.timSinhVienTheoMssv(maso)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.ten == 'Nam']

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngay <= '15/06/2000']
    
    def sapxepTheoTenTD(self,ten: str):
        tangdan = self.dssv.sort(key=lambda self: self.__ten, reverse=False)
        return tangdan
    def sapxepTheoTenGD(self, ten: str):
        giamdan = self.dssv.sort(key=lambda self:self.__ten, reverse=True)
        return giamdan

ds=DanhSachSv()

f = open('D://Python//Ex Python//Lab2//Bài 2//dssv.txt', 'r')
for x in f:
    print(x)
data = f.read()
f.close()
ten = data.split()



ketqua = ds.sapxepTheoTenTD(ten)
print('Danh sách sắp xếp',ketqua)



