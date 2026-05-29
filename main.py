import time

from rich import table # Hiển thị
from rich.console import Console # Hiển thị
from rich.prompt import Prompt, Confirm # Thư viện Nhập liệu
import inquirer # Thư viện lựa chọn

from danhba import DanhBa

class CauHoi(Prompt):
    validate_error_message = "Lựa chọn không phù hợp, hãy chọn lại"
class Input(Prompt):
    validate_error_message = "Dữ liệu bạn nhập không hợp lệ, hãy thử lại"

def setup_table():
    bangLienHe = table.Table(header_style="bold cyan", border_style="blue")
    bangLienHe.add_column("Tên", style="white")
    bangLienHe.add_column("Số điện thoại", style="yellow")
    bangLienHe.add_column("Email", style="green")
    return bangLienHe

def main():
    console = Console()
    danhba = DanhBa()
    danhba.doc_file()

    while True:
        # Xoá console
        console.clear()
        console.print("Danh bạ promax 67", style="bold bright_white blue")
        # Lấy danh sách liên hệ ra
        lienhe = danhba.lay_danh_sach()
        # Thiết lập bảng để hiển thị danh sách liên hệ
        bangLH = setup_table()
        # Duyệt qua toàn bộ danh bạ và thêm vào bảng
        for lh in lienhe:
            bangLH.add_row(lh.ten, lh.sdt, lh.email)
        # In nó ra
        console.print(bangLH)

        # Tương tác
        questions = [
            inquirer.List(
                "action",
                message="Bạn cần gì?",
                choices=["Thêm liên lạc", "Xoá liên lạc", "Hiển thị lại danh sách", "Tìm Kiếm", "Sắp xếp lại danh bạ",
                         "Lưu ra file", "Thoát ứng dụng"],
                default="Hiển thị lại danh sách",
                carousel=True

            )
        ]

        action = inquirer.prompt(questions)["action"]

        match action:

            case "Thêm liên lạc":
                ten = Input.ask(
                    "Nhập tên mà bạn muốn thêm vào danh bạ"
                    , console=console

                )
                so_dien_thoai = Input.ask(
                    "Nhập số điện thoại",
                    console=console
                )
                email = Input.ask(
                    "Nhập email của người đó (nhấn enter để bỏ trống)",
                    default="",
                    console=console
                )
                result, reason = danhba.them_lien_lac(ten, so_dien_thoai, email)
                if result:
                    console.print(f"Đã thêm: {ten} vào danh bạ", style="bold green")
                else:
                    console.print(f"Không thể thêm {ten} vào danh bạ vì lý do: {reason}", style="bold red")

            case "Xoá liên lạc":
                check_box = [
                    inquirer.Checkbox(
                        "delete_contact",
                        "Chọn (các) liên hệ mà bạn muốn xoá",
                        choices=[f"{lh.ten} - {lh.sdt} - {lh.email}" for lh in lienhe],
                        carousel=False
                    )
                ]
                contacts_to_delete = inquirer.prompt(check_box)["delete_contact"]
                if Confirm.ask(f"Xoá (các) liên hệ: {contacts_to_delete} này chứ?", default="Y"):
                    for lh in contacts_to_delete:
                        result, reason = danhba.xoa_lien_he(lh)
                        if result:
                            console.print(f"Đã xoá: {lh}", style="bold green")
                        else:
                            console.print(f"Xoá thất bại: {reason}", style="bold red")
                else:
                    console.print("Không xoá liên hệ nào hết", style="yellow")

            case "Hiển thị lại danh sách":
                continue

            case "Tìm Kiếm":
                search_ten = CauHoi.ask(
                    "Nhập tên liên hệ mà bạn cần tìm",
                    console=console,
                    default=None
                )
                if search_ten:
                    result = danhba.tim_kiem(search_ten)
                    if result:
                        console.print(f"Đã tìm thấy (các) liên hệ", style="bold green")
                        for lh in result:
                            console.print(f"  {lh.ten} - {lh.sdt} - {lh.email}", style="cyan")
                    else:
                        console.print(f"Không tìm thấy liên hệ với tên {search_ten}", style="bold red")
                else:
                    console.print("Không tìm ai cả - Quay lại", style="yellow")

            case "Sắp xếp lại danh bạ":
                danhba.sap_xep()
                console.print("Đã sắp xếp lại danh bạ điện thoại", style="bold green")

            case "Lưu ra file":
                danhba.ghi_file()
                console.print("Đã lưu toàn bộ danh bạ ra file danhba.txt", style="bold green")

            case "Thoát ứng dụng":
                console.print("Tam biet nhe", style="bold bright_magenta")
                break

            case _:
                console.print("Lựa chọn không hợp lệ", style="bold red")

        # Dừng tí đọc tin nhắn cuối rồi mới clear screen
        time.sleep(3)

if __name__ == '__main__':
    main()

