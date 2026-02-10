# กำหนดรหัสผ่านที่ถูกต้องเก็บไว้ในตัวแปร
password = "1234"

# ขอให้ผู้ใช้กรอกรหัสผ่าน
user_input = input()

# ตรวจสอบว่ารหัสผ่านที่กรอกตรงกับที่กำหนดไว้หรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")