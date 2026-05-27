class  LienHe:
    def __init__(self ,ten ,sdt ,email ):
        self.ten = ten
        self.sdt = sdt
        self.email = email
    
    # thêm liên lạc (Thế, Đạt)
    def themlienlac (danh_ba):
        ten = input("Nhap ten ")
        sdt = input("Nhap sdt")
        email = input("Nhap email")
        danh_ba.append(LienHe(ten,sdt,email))
        print("Da them lien lac")
    
    #HAM HIEN THI (Thế, Đạt)
    def hien_thi (danh_ba):
        if not danh_ba:
            print("Danh ba trong")
            return
        for i, lh in enumerate(danh_ba):
            print(i, lh.ten)

    #SAP XEP THEO TEN (Thế, Đạt)
    def sap_xep (danh_ba):
        danh_ba.sort (key=lambda lh: lh.ten.split()[-1].lower())
        print("Đã sắp xếp theo thứ tự")

    #XOA LIEN HE (An)
    def xoa_lien_he(danh_ba):
        if not danh_ba:
            print("Danh ba rong")
            return
    tu_khoa = input("Nhap ten hoac sdt can xoa: ").lower()
    for lh in danh_ba:
        if tu_khoa == lh.ten.lower() or tu_khoa == lh.sdt:
            danh_ba.remove(lh)
            print("Da xoa lien he")
            return
    print("Khong tim thay lien he")

    #TIM KIEM THEO TEN HOAC SDT (An)
    def tim_kiem(danh_ba):
    if not danh_ba:
        print("Danh ba rong")
        return
    tu_khoa = input("Nhap ten hoac sdt can tim: ").lower()
    tim_thay = False
    for lh in danh_ba:
        if tu_khoa in lh.ten.lower() or tu_khoa in lh.sdt:
            print("Ten:", lh.ten)
            print("SDT:", lh.sdt)
            print("Email:", lh.email)
            print("-------------------")
            tim_thay = True
    if not tim_thay:
        print("Khong tim thay lien he")
        
 # GHI FILE (Hải)
    def ghi_file(danh_ba):
        f = open("danhba.txt", "w", encoding="utf-8")

        for lh in danh_ba:
            f.write(lh.ten + "," + lh.sdt + "," + lh.email + "\n")

        f.close()

        print("Da ghi vao file")

    # DOC FILE
    def doc_file(danh_ba):
        try:
            f = open("danhba.txt", "r", encoding="utf-8")

            for line in f:
                ten, sdt, email = line.strip().split(",")

                danh_ba.append(LienHe(ten, sdt, email))

            f.close()

        except:
            print("Chua co file danh ba")



# CHUONG TRINH CHINH (Hải)
danh_ba = []

# doc file khi mo chuong trinh (Hải)
LienHe.doc_file(danh_ba)

while True:

    print("\n===== MENU =====")
    print("1. Them lien lac")
    print("2. Hien thi danh ba")
    print("3. Tim kiem")
    print("4. Xoa lien he")
    print("5. Sap xep")
    print("6. Luu vao file")
    print("0. Thoat")

    chon = input("Nhap lua chon: ")

    if chon == "1":
        LienHe.themlienlac(danh_ba)

    elif chon == "2":
        LienHe.hien_thi(danh_ba)

    elif chon == "3":
        LienHe.tim_kiem(danh_ba)

    elif chon == "4":
        LienHe.xoa_lien_he(danh_ba)

    elif chon == "5":
        LienHe.sap_xep(danh_ba)

    elif chon == "6":
        LienHe.ghi_file(danh_ba)

    elif chon == "0":
        LienHe.ghi_file(danh_ba)

        break

    else:
        print("Lua chon khong hop le")
