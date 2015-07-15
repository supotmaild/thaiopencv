# thaiopencv
Thai fonts Project for openCV in Python
- update วันที่ 15 กรกฎาคม 2558 สามารถใช้ True Type Fonts ได้แล้ว
- เข้าไปดูที่ write_tt_text.py

- ฟอนท์ภาษาไทย สำหรับ Python OpenCV (แบบเก่าใช้ LCD ฟอนท์) 
- 
- Basic LCD font
- มี font generator LCD_gen.py สำหรับการดัดแปลง เปลี่ยนแปลง font ได้ด้วยตัวเอง
- การใช้งาน LCD_gen.py จะสร้าง lcd_font.py ซึ่งเป็นข้อมูลบรรจุฟอนท์ไว้
- เรียกใช้งานโดย import lcd_font
- สร้างตัวแปร font_data = lcd_font.font()
- เรียกใช้งาน write_text(image, x, y, text)
