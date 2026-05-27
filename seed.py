"""Script để seed dataset mẫu"""
import random
from rich import print

ho = [
    "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan",
    "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương"
]

dem = [
    "Văn", "Minh", "Thanh", "Quốc", "Gia", "Hoài", "Ngọc",
    "Anh", "Đức", "Khánh", "Tuấn", "Hải", "Nhật", "Thành"
]

ten = [
    "An", "Bảo", "Bình", "Chi", "Dũng", "Đạt", "Giang", "Hà",
    "Hải", "Hiếu", "Hòa", "Hùng", "Huy", "Khánh", "Kiệt",
    "Lâm", "Lan", "Linh", "Long", "Mai", "Minh", "Nam",
    "Ngân", "Nhung", "Phong", "Phúc", "Quân", "Sơn",
    "Tâm", "Thảo", "Trang", "Trí", "Trung", "Tùng", "Vy"
]

with open("danhba.txt", "w", encoding="utf-8") as f:
    for i in range(30):
        full_name = f"{random.choice(ho)} {random.choice(dem)} {random.choice(ten)}"
        phone = "0" + "".join([str(random.randint(0, 9)) for _ in range(9)])
        email = (
            full_name.lower()
            .replace(" ", "")
            .replace("đ", "d")
            + str(i)
            + "@gmail.com"
        )

        f.write(f"{full_name},{phone},{email}\n")

print("[bold green]Seed xong 30 liên hệ[/]")