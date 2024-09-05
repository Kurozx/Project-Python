import cv2
import os

# Open the first connected camera
cam = cv2.VideoCapture(0)
cam.set(3, 640) # Set video width
cam.set(4, 480) # Set video height

# Absolute path to the Haar cascade file
haar_cascade_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'haarcascade_frontalface_default.xml')

# Check if the Haar cascade file exists
if not os.path.exists(haar_cascade_path):
    print(f"Error: Haar cascade file not found at {haar_cascade_path}")
    exit()

# Load the Haar cascade file
face_detector = cv2.CascadeClassifier(haar_cascade_path)

# Check if the face detector loaded correctly
if face_detector.empty():
    print(f"Error: Failed to load Haar cascade file from {haar_cascade_path}")
    exit()

# For each person, enter one numeric face id
face_id = input('\n Enter face ID: ')

print("\n [INFO] Initializing face capture. Look at the camera and wait ...")
# Initialize individual sampling face count
count = 0

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        os.makedirs("img", exist_ok=True)  # Ensure the directory exists
        cv2.imwrite(f"img/{face_id}.{count}.jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face samples and stop video
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()
