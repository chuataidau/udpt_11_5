from xmlrpc.server import SimpleXMLRPCServer
import math

# Khởi tạo máy chủ RPC tại địa chỉ và cổng cụ thể
server = SimpleXMLRPCServer(("localhost", 8000))
print("Máy chủ RPC đang chạy tại localhost:8000...")

# Định nghĩa các hàm có thể gọi từ xa
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Lỗi: Không thể chia cho 0"
    return a / b

def square_root(x):
    if x < 0:
        return "Lỗi: Không thể tính căn bậc hai của số âm"
    return math.sqrt(x)

# Đăng ký các hàm với máy chủ
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(square_root, "square_root")

# Chạy máy chủ
server.serve_forever()