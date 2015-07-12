# thaiopencv
Thai fonts Project for openCV in Python

- ฟอนท์ภาษาไทย สำหรับ Python OpenCV 
- 
- Basic LCD font
- มี font generator LCD_gen.py สำหรับการดัดแปลง เปลี่ยนแปลง font ได้ด้วยตัวเอง
- การใช้งาน LCD_gen.py จะสร้าง lcd_font.py ซึ่งเป็นข้อมูลบรรจุฟอนท์ไว้
- เรียกใช้งานโดย import lcd_font
- สร้างตัวแปร font_data = lcd_font.font()
- เรียกใช้งาน write_text(image, x, y, text)
