import math
class PhanSo:
    def __init__(self, tuso = 1, mauso = 1) -> None:
        self.tu = tuso
        self.mau = mauso

    def __str__(self) -> str:
        return (f'{self.tu}/{self.mau}')
    
    def __add__(self, other):
        ps = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu * other.mau + self.mau * other.tu
        ps.mau = self.mau * other.mau
        return ps.Rutgon()
    
    def __sub__(self, other):
        ps = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu * other.mau - self.mau * other.tu
        ps.mau = self.mau * other.mau
        return ps.Rutgon()
    
    def __mul__(self, other):
        ps = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu * other.tu
        ps.mau = self.mau * other.mau
        return ps.Rutgon()
    
    def __truediv__(self, other):
        ps = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu * other.mau
        ps.mau = self.mau * other.tu
        return ps.Rutgon()

    def Rutgon(self):
        ps = PhanSo()
        ucln = math.gcd(self.tu, self.mau)
        ps.tu = self.tu // ucln
        ps.mau = self.mau // ucln
        return ps
    
    def tinhGiaTri(self):
        return self.tu/self.mau

    def laPhanSoAm(self):
        return self.tu * self.mau < 0

    def coMauNhoHon(self, other):
        return self.mau < other.mau

    def coMauNhoHonHoacBang(self, other):
        return self.mau <= other.mau

    def coTuNhoHon(self, other):
        return self.tu < other.tu
    def __eq__(self, other) -> bool:
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu == other.tu
        return self.tu * other.mau == self.mau * other.tu

    def __lt__(self, other):
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu < other.tu
        return self.tu * other.mau < self.mau * other.tu

    def __gt__(self, other):
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu > other.tu
        return self.tu * other.mau > self.mau * other.tu