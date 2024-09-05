import cv2

# โหลดตัวตรวจจับใบหน้าที่เป็นไฟล์ XML
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# เปิดกล้องเว็บแคม
cap = cv2.VideoCapture(0)

while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()

    # เปลี่ยนภาพเป็นสีเทา
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ตรวจจับใบหน้า
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # วาดกรอบรอบใบหน้าที่ตรวจจับได้
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # แสดงภาพ
    cv2.imshow('Face Detection', frame)

    # หยุดโปรแกรมเมื่อกดปุ่ม 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการใช้งานกล้องและปิดหน้าต่างทั้งหมด
cap.release()
cv2.destroyAllWindows()