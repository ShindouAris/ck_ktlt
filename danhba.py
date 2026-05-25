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
