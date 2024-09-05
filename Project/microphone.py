import speech_recognition as sr
import os
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"กรุณาเตรียมตัว พูดใน {i} วินาที")
        time.sleep(1)

# สร้าง recognizer object
recognizer = sr.Recognizer()

# ใช้ไมโครโฟนเป็นแหล่งที่มาเสียง
with sr.Microphone() as source:
    # นับถอยหลัง 5 วินาทีเพื่อเตรียมตัว
    countdown(3)

    print("กำลังฟัง...")

    # ปรับระดับเสียงรบกวนรอบข้าง
    recognizer.adjust_for_ambient_noise(source)

    try:
        # ฟังเสียงจากไมโครโฟน พร้อมกำหนด timeout
        audio = recognizer.listen(source, timeout=10)
        
        # ใช้ Google Web Speech API เพื่อแปลงเสียงเป็นข้อความ
        text = recognizer.recognize_google(audio, language="th-TH")
        print("คุณพูดว่า: " + text)
        
        # สร้างโฟลเดอร์ถ้ายังไม่มี
        os.makedirs("text", exist_ok=True)

        # บันทึกข้อความลงไฟล์ .txt ที่หน้าเดสก์ท็อป
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join("text", 'speech_to_text.txt')

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"ข้อความถูกบันทึกลงในไฟล์: {file_path}")

    except sr.UnknownValueError:
        print("ไม่สามารถเข้าใจเสียงได้")
    except sr.RequestError as e:
        print(f"ไม่สามารถร้องขอผลได้; {e}")
    except sr.WaitTimeoutError:
        print("การฟังเสียงใช้เวลานานเกินไป")

#ในโปรแกรมนี้จะใช้โมดูลต่อไปนี้:
#speech_recognition: สำหรับการรับเสียงจากไมโครโฟนและแปลงเสียงเป็นข้อความ
#os: สำหรับการจัดการเส้นทางไฟล์และการบันทึกไฟล์บนหน้าเดสก์ท็อป
#time: สำหรับการนับถอยหลัง