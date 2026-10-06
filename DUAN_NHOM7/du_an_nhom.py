import sys
from sympy import symbols, Eq
from sympy.parsing.sympy_parser import parse_expr
from sympy.geometry import Point, Line, Circle

# Khởi tạo hai biến ký hiệu x và y
x, y = symbols('x y')

print("--- KIỂM TRA VỊ TRÍ TƯƠNG ĐỐI TỰ ĐỘNG ---")
print("Ví dụ đường tròn: x**2 + y**2 - 4*x - 6*y - 3")
print("Ví dụ đường thẳng: 3*x + 4*y - 12\n")

try:
    # 1. Nhập phương trình đường tròn và tự động tìm Tâm, Bán kính
    pt_tron_str = input("Nhập vế trái PT đường tròn (ép về = 0): ")
    pt_tron = parse_expr(pt_tron_str)
    
    # Tìm tâm và bán kính bằng cách đưa về dạng chính tắc thông qua bổ túc bình phương
    # Hệ số của x và y trong pt: x^2 + y^2 + 2gx + 2fy + c = 0
    g = pt_tron.coeff(x) / 2
    f = pt_tron.coeff(y) / 2
    c_val = pt_tron.subs({x: 0, y: 0})
    
    # Tính tọa độ tâm và bán kính
    tam_x = -g
    tam_y = -f
    r_binh_phuong = tam_x**2 + tam_y**2 - c_val
    
    if r_binh_phuong <= 0:
        print("Lỗi: Phương trình không phải là một đường tròn thực!")
        sys.exit()
        
    c = Circle(Point(tam_x, tam_y), r_binh_phuong**0.5)
    print(f"-> Khớp dữ liệu thành công! Tâm I({tam_x}, {tam_y}), Bán kính R = {c.radius}")

    # 2. Nhập phương trình đường thẳng
    pt_thang_str = input("Nhập vế trái PT đường thẳng (ép về = 0): ")
    pt_thang = parse_expr(pt_thang_str)
    
    # Tìm 2 điểm thuộc đường thẳng để khởi tạo đối tượng Line trong SymPy
    # Chọn x = 0 tìm y, và y = 0 tìm x
    A = pt_thang.coeff(x)
    B = pt_thang.coeff(y)
    C = pt_thang.subs({x: 0, y: 0})
    
    if A == 0 and B == 0:
        print("Lỗi: Phương trình đường thẳng không hợp lệ!")
        sys.exit()
        
    if B != 0:
        p1 = Point(0, -C/B)
        p2 = Point(1, -(A + C)/B)
    else:
        p1 = Point(-C/A, 0)
        p2 = Point(-C/A, 1)
        
    l = Line(p1, p2)

    # 3. Tính toán vị trí tương đối
    dist = c.center.distance(l)
    print(f"\nKhoảng cách từ tâm đến đường thẳng d = {dist}")
    
    if dist > c.radius:
        print("=> KẾT LUẬN: Đường thẳng và đường tròn KHÔNG GIAO NHAU.")
    elif dist == c.radius:
        print("=> KẾT LUẬN: Đường thẳng TIẾP XÚC với đường tròn.")
    else:
        print("=> KẾT LUẬN: Đường thẳng CẮT đường tròn tại 2 điểm phân biệt.")

except Exception as e:
    print(f"Đã xảy ra lỗi nhập liệu hoặc cú pháp: {e}")