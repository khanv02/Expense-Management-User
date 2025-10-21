# Expense-Management-User
# ------THIẾT KẾ HỆ THỐNG QUẢN LÝ CHI TIÊU CÁ NHÂN (CLI)------

# - Mô tả bài toán: Ứng dụng console theo dõi thu/chi hằng ngày, phân tích thói quen tiêu dùng và quản lý ngân sách
+ Console : CLI (Command Line Interface).
# - Đầu vào (Input):
+ Giao dịch: Ngày (dd/mm/yyyy), Loại (thu/chi), Số tiền (VND), Danh mục (ăn uống, học tập, giải trí, y tế, khác), Mô tả. 
+ Tệp dữ liệu: transactions.json (Lưu danh sách giao dịch), categories.json (Lưu danh sách thu/chi).
# - Đầu ra (Output): 
+ Menu tương tác (thêm giao dịch, xem lịch sử, thống kê theo tháng/danh mục, kiểm tra số dư, thoát)
+ Báo cáo thống kê: tổng thu/chi theo tháng, top 3 danh mục chi, biểu đồ cột ASCII, cảnh báo vượt ngân sách.
+ Tệp xuất: monthly_report.txt, cập nhật transactions.json.
# - Các hàm xử lý:
+ def add_transaction() # Thêm giao dịch mới 
+ def load_data() # Đọc file JSON 
+ def save_data() # Lưu file JSON 
+ def show_history() # Hiển thị lịch sử 
+ def monthly_stats() # Thống kê tháng 
+ def category_stats() # Thống kê danh mục 
+ def calculate_balance() # Tính số dư 
+ def main_menu() # Menu chính 
+ def validate_date() # Kiểm tra date hợp lệ
+ def validate_amount() # Kiểm tra tiền hợp lệ
+ add_category() # Thêm một danh mục
+ def report_stats() # Báo cáo thống kê
# - Chức năng chi tiết:
+ Thêm giao dịch: Validate ngày, số tiền > 0, danh mục hợp lệ
+ Xem lịch sử: Hiển thị 10 giao dịch gần nhất, có thể lọc theo tháng
+ Thống kê tháng: Tính tổng thu/chi, số dư, so với tháng trước
+ Thống kê danh mục: Phân bố chi tiêu, tỷ lệ % cho từng danh mục
+ Kiểm tra số dư: Tính từ tổng thu - tổng chi tất cả giao dịch 
# - Mô tả tổng quan: Xây dựng ứng dụng console giúp người dùng theo dõi thu chi hàng ngày, phân tích thói quen tiêu dùng và quản lý ngân sách cá nhân.

