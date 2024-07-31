# Project Title
DAP304x_asm1

# Description
File Python chấm điểm bài kiểm tra của học sinh dựa trên đáp án đã cho trước, phân tích kết quả và tạo báo cáo.

# Installation
### Python Environment:
- Python 3.x
- Thư viện `numpy`
- Đặt file .py và các file dữ liệu trong cùng thư mục.
### Required Libraries:
```
pip install numpy
```

# Usage
- Khởi chạy file lastname_firstname_grade_the_exams.py
- Khi được yêu cầu, nhập tên file lớp học (từ class1 đến class8)

_**Lưu ý :** có thể nhập đầy đủ phần mở rộng (.txt) hoặc không. Ví dụ, có thể nhập class1 hoặc class1.txt_

### Examples
File dữ liệu mẫu:
```
N12345678,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y
```
Trong đó, N12345678 là ID của sinh viên. Các (25) ký tự chữ cái sau đó là câu trả lời của học sinh cho kỳ thi, tất cả các giá trị được phân tách bằng dấu phẩy. Nếu không có chữ cái nào sau dấu phẩy, điều này có nghĩa là học sinh đã bỏ qua việc trả lời câu hỏi.

### Project Structure
```
project-folder/
│
├── lastname_firstname_grade_the_exams.py
├── class1.txt
├── ...
└── class8.txt
```

# Contact
Email: huydmFX29833@funix.edu.vn
