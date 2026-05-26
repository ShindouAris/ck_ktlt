class  LienHe:
    def __init__(self ,ten ,sdt ,email ):
        ten.self = ten
        sdt.self = sdt
        email.self = email
    
    # thêm liên lạc
    def themlienlac (danh_ba):
        ten = input("Nhap ten ")
        sdt = input("Nhap sdt")
        email = input("Nhap email")
        danh_ba.append(LienHe(ten,sdt,email))
        print("Da them lien lac")
    
    #HAM HIEN THI
    def hien_thi (danh_ba):
        if not danh_ba:
            print("Danh ba trong")
            return
        for i, lh in enumerate(danh_ba):
            print(i, lh.ten)

    #SAP XEP THEO TEN
    def sap_xep (danh_ba):
        danh_ba.sort (key=lambda lh: lh.ten.split()[-1].lower())
        print("Đã sắp xếp theo thứ tự")

    #XOA LIEN HE
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

    #TIM KIEM THEO TEN HOAC SDT
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
