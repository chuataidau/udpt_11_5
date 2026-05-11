import xmlrpc.client

# Kết nối đến máy chủ RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Gọi các hàm từ xa và hiển thị kết quả
try:
    print("5 + 3 =", server.add(5, 3))
    print("10 - 7 =", server.subtract(10, 7))
    print("6 * 4 =", server.multiply(6, 4))
    print("8 / 2 =", server.divide(8, 2))
    print("Căn bậc hai của 16 là:", server.square_root(16))
    print("Căn bậc hai của -4 là:", server.square_root(-4))
except Exception as e:
    print("Lỗi khi gọi RPC:", e)