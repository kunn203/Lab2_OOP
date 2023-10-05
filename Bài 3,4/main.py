from phan_so import PhanSo
from ds_phan_so import DanhSachPhanSo

ds = DanhSachPhanSo()
ds.docTuFile("dsps.txt")
print("Danh sách phân số đọc từ tập tin: ")
ds.xuat()

print("*"*50)
print("Danh sách phân số âm: ")
kq = ds.layDsPsAm()
kq.xuat()

print("*"*50)
print("Danh sách phân số dương nhỏ nhất ")
ps = ds.timDSPhanSoDuongNhoNhat()
ps.xuat()

print("*"*50)
print("Số lượng phân số âm của danh sách là: ", ds.demPhanSoAm())

print("*"*50)
print("Tổng các phân số âm trong danh sách là: ", ds.tinhTongPsAm())

print("*"*50)
x = PhanSo(5,6)
ds.xoaPhanSoDungIn(x)
print(f"Danh sách phân số sau khi xóa phân số {x}: ")
ds.xuat()

print("*"*50)
print('Danh sách phân số sau khi xóa phân số 2/5')
ds.xoaPhanSo(PhanSo(2/5))
ds.xuat()

print("*"*50)
print("Danh sách phân số sau khi sắp xếp tăng theo mẫu: ")
ds.sapXepTangTheoMauChonTT()
ds.xuat()