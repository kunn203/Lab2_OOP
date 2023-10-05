from datetime import datetime

from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(1144141, "Trần Văn A",
                       datetime.strptime("13/2/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1356641, "Trần Văn Bướm",
                       datetime.strptime("14/2/2002", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(3365941, "Doãn Hải My", datetime.strptime(
    "3/6/2000", "%d/%m/%Y"), "Cao đẳng", 2)
sv4 = SinhVienPhiCQ(5656566, "Đoàn Văn Hậu", datetime.strptime(
    "20/5/1997", "%d/%m/%Y"), "Cao đẳng", 2)
sv5 = SinhVienPhiCQ(6565656, "Nguyễn Thanh Tùng", datetime.strptime(
    "17/6/1998", "%d/%m/%Y"), "Trung cấp", 2.5)
sv6 = SinhVienChinhQuy(6566656, "Nguyễn Văn Tràm",
                       datetime.strptime("9/9/2001", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiCQ(5896565, "Bùi Xuân Huẩn", datetime.strptime(
    "13/8/2002", "%d/%m/%Y"), "Trung cấp", 2.5)
sv8 = SinhVienChinhQuy(6595898, "Phan Thành Trung",
                       datetime.strptime("9/10/2002", "%d/%m/%Y"), 70)

dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()

# vt = dssv.timSVTheoMs(1144141)
# print(f"Sinh viên ở vị trí thứ {vt+1} trong danh sách")

# kq = dssv.timSvTheoLoai("chinhquy")
# print("Danh sách sinh viên theo loại:")
# for sv in kq:
#     print(sv)

diemRl = dssv.TimSVCoDiemRenLuyen80()
print("---------------")
for sv in diemRl:
    print(sv)

print("Danh sách sinh viên là cao đẳng có ngày sinh trước 15/8/1999")
sinhtruoc = dssv.TimSVsinhtrcngay()
for sv in sinhtruoc:
    print(sv)
