#!/usr/bin/env python3

def main():
    # 1. กำหนด array เริ่มต้น
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # 2. สร้าง array ใหม่ โดยเลือกเฉพาะค่าที่ > 5 แล้วบวก 2
    new_array = []
    for value in original_array:
        if value > 5:
            new_array.append(value + 2)

    # 3. แสดงผลทั้งสอง array
    print(original_array)
    print(new_array)

if __name__ == "__main__":
    main()