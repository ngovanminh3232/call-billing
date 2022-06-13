### Project: call-billing

# Các công cụ sử dụng : 
* Python 3.10.5
* Fastapi
* Uvicorn
* Pgadmin4

# Hướng dẫn sử dụng : 
1. Bước 1 : Mở project với vscode
2. Bước 2 : Cài dặt fastapi và uvicorn
##### Dùng lệnh pip install fastapi và pip install "uvicorn[standard]"

3. Bước 3 : Tiếp tục ta tạo database trong pgadmin với tên là Vin
4. Bước 4.1 : Restore với file Vin.sql đã được backup sẵn trong project
5. Bước 5 : Chạy lệnh uvicorn app.main:app --reload
##### Project sẽ tự động tạo cho các bảng được định nghĩa trong models.py
5. Bước 5 : Truy cập vào http://127.0.0.1:8000/docs 
6. Bước 6 : Kiểm thử các API

Danh sách API:
*   Get_All : Đưa ra tất cả các cuộc gọi trong database
*   Creat_call: tạo một cuộc gọi mới
****
Example_values:
{
  "user_name": "Thanh,
  "call_duration": 200
  "call_count": 3,
  "block_count": 4
}

*   Get_call : Tìm một cuộc gọi với user_name
*   Get_biling : Gọi ra block_count,call_count của user_name
*   Update_call :Cập nhập call_duration của user_name
****
Example_values:
{
  "call_duration": 200
}

