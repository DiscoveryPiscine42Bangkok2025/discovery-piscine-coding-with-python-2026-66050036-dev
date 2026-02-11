#!/usr/bin/env python3

def main():
    # 1. กำหนด array เริ่มต้น
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    # 2. สร้าง array ใหม่ โดยเลือกเฉพาะค่าที่ > 5 แล้วบวก 2
    new_array = [value + 2 for value in original_array if value > 5]

    # 3. ใช้ set เพื่อลบค่าที่ซ้ำออก (set จะเก็บเฉพาะค่าที่ไม่ซ้ำกัน)
    unique_new_array = set(new_array)

    # 4. แสดงผล
    print(original_array)
    print(unique_new_array)

if __name__ == "__main__":
    main()