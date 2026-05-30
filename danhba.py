import locale
# Hàm này đổi locale hiện tại của chương trình
# locale.LC_COLLATE là quy tắc so sánh và sắp xếp chuỗi
# 'Vietnamese_Vietnam.1258': Đây là tên locale trên Windows.
# ChatGPT giải thích kĩ dòng này làm ơn
locale.setlocale(locale.LC_COLLATE, 'Vietnamese_Vietnam.1258')
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern_phone = r'^\+?\d+$'

class LienHe:
    def __init__(self, ten, sdt, email):
        self.ten = ten # string
        self.sdt = sdt # string (Lưu số 0 vào đầu, nếu dùng int sẽ mất tiêu
        self.email = email # string

class DanhBa:
    def __init__(self):
        self._danh_ba = []
        self._so_dien_thoai = set() # dùng set để kiểm tra số điện thoại, chống lặp, hay còn nói là unique đi số điện thoại

    def _kiem_tra_ten(self, name):
        """
            Kiểm tra xem coi tên nhập vào có kí tự lạ không
            Chặn '-' trong tên, vì nó dùng để phân biệt trong function xoá liên hệ
        """

        if "-" in name:
            return False
        if not name:
            return False
        if "," in name:
            return False
        return True

    # THEM LIEN LAC
    def them_lien_lac(self, name, phone_num: str, email):
        """Thêm liên lạc vào mảng (danh sách) _danh_ba"""

        if not self._kiem_tra_ten(name):
            # Kiểm tra xem tên có hợp lệ không, nếu không thì trả false kèm lý do từ chối luôn
            return False, "Tên bạn nhập vào không hợp lệ"

        if phone_num in self._so_dien_thoai:
            return False, "Số điện thoại này đã tồn tại rồi"

        if email and not re.fullmatch(pattern, email): # Regex để Kiểm tra xem email có hợp lệ không
            return False, "Email bạn nhập vào không hợp lệ"

        if phone_num and not re.fullmatch(pattern_phone, phone_num.strip()): # Kiểm tra xem số điện thoại có hợp lệ không, xoá space và leading bằng .strip()
            return False, "Số điện thoại không hợp lệ"

        # Hợp lệ thì thêm nó vào cuối danh sách

        self._danh_ba.append(LienHe(name, phone_num.strip(), email))

        self._so_dien_thoai.add(phone_num)

        return True, "Thêm Liên hệ thành công"

    # HIEN THI
    def lay_danh_sach(self) -> list[LienHe]:
        """Trả về mảng danh bạ chứa các liên hệ"""
        return self._danh_ba

    # SAP XEP
    def sap_xep(self):
        """Sắp xếp danh bạ theo Tên cuối của Liên hệ đó"""
        # Hàm .sort để sắp xếp lại danh sách
        # key -> lấy cái gì để đem đi so sánh
        # lambda lh: -> hàm ngắn, nó tương tự như def lay_ten_cuoi(lh):
        # locale.strxfrm() là hàm để biến string thành “key” dùng cho sorting theo ngôn ngữ địa phương
        # lh.ten -> Lấy tên đầy đủ
        # .split -> Tách nó ra theo khoảng trắng
        # [-1] -> lấy phần tử cuối cùng của danh sách đã tách từ hàm split
        # .lower() -> Chuyển thành chữ thường để tránh cho việc N < a
        self._danh_ba.sort(key=lambda lh: locale.strxfrm(lh.ten.split()[-1].lower()))
        # Sort xong thì trả về true để biết rằng đã sort xong
        return True

    # TIM KIEM
    def tim_kiem(self, name):
        """Hàm tìm kiếm, vâng, cơ chế đơn giàn, tìm theo tên bằng cách duyệt danh sách"""
        found = []
        for lh in self._danh_ba:
            # Duyệt mảng danh bạ
            if name.lower() in lh.ten.lower():
                # Kiểm tra tên được cho vào hàm <name> có nằm trong liên hệ đang so sánh hiên tại <lh> không
                # Nếu có, thêm liên hệ đó vào danh sách
                found.append(lh)

        return found # Trả về kết quả đã tìm dưới dạng danh sách, [] (danh sách rỗng) nếu không tìm thấy ai hết

    # XOA LIEN HE
    def xoa_lien_he(self, lienhe):
        """Hàm này xoá liên hệ, xong trả về trạng thái <False / True> và Reason"""
        # Bốc số điện thoại ra từ chuỗi gửi vào hàm "<Tên> <Số điện thoại> <Email>
        # .split để chẻ một chuỗi thành danh sách, gặp dấu cách thỉ cắt ra -> ["<tên>", "<Số điện thoại>", "<Email>"]
        # Sau đó lấy phần tử thứ 1 (Danh sách trong python bắt đầu từ số 0
        sdt = lienhe.split(" - ")[1]

        if not self._danh_ba:
            # Nếu cái danh sách danh bạ trống thì trả về trạng thái False, kèm lý do "Danh bạ trống"
            return False, "Danh bạ trống"

        for lh in self._danh_ba:
            # Duyệt qua mảng danh bạ
            if sdt == lh.sdt:
                # Nếu sdt trùng với lh đang so sánh hiện tại
                self._danh_ba.remove(lh) # Xoá liên hệ này khỏi danh sách
                self._so_dien_thoai.remove(lh.sdt) # Xoá số này khỏi danh sách số điện thoại

                return True, "Xoá thành công" # Trả về trạng thái True (Xoá thành công) và message (lý do)

        return False, f"Không tìm thấy liên hệ với sdt {sdt}" # Duyệt hết mảng rồi mà không thấy thì trả False kèm lý do

    # GHI FILE
    def ghi_file(self):
        with open("danhba.txt", "w", encoding="utf-8") as f:

            for lh in self._danh_ba:
                f.write(lh.ten + "," + lh.sdt + "," + lh.email + "\n")

        return True

    # DOC FILE
    def doc_file(self):
        try:
            with open("danhba.txt", "r", encoding="utf-8") as f:

                for line in f:
                    ten, sdt, email = line.strip().split(",")

                    if sdt in self._so_dien_thoai: # Kiểm tra xem sdt này có trong ds số chưa
                        print(f"Lỗi: Số điện thoại này đã có trong danh bạ, bỏ qua")
                        continue # Skip luôn khối đằng sau và nhảy đến item tiếp theo

                    self._danh_ba.append(LienHe(ten, sdt, email))
                    self._so_dien_thoai.add(sdt)

            return True
        except FileNotFoundError:
            return False
        except Exception:
            print("File lưu dữ liệu bị hỏng, bỏ qua")
            return False
