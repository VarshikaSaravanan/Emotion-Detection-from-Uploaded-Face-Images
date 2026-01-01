# ======================================
# CASE STUDY: EMOTION DETECTION FROM UPLOADED FACE IMAGES
# ======================================

print("🔹 CASE STUDY: EMOTION DETECTION FROM UPLOADED FACE IMAGES")
print("AIM: Detect emotions from any uploaded face image and display results.\n")

# ================================
# STEP 1: Install Dependencies
# ================================
!pip install deepface matplotlib opencv-python-headless --quiet

# ================================
# STEP 2: Import Libraries
# ================================
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
from google.colab import files

# ================================
# STEP 3: Upload Face Image
# ================================
print("Upload a face image:")
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

# Read and convert image to RGB
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ================================
# STEP 4: Detect Emotion
# ================================
try:
    analysis = DeepFace.analyze(img_path, actions=['emotion'], enforce_detection=True)
    detected_emotion = analysis[0]['dominant_emotion']
except:
    print("No face detected. Make sure the image has a clear face.")
    detected_emotion = "Unknown"

# ================================
# STEP 5: Display Image with Emotion
# ================================
plt.figure(figsize=(6,6))
plt.imshow(img_rgb)
plt.title(f"Detected Emotion: {detected_emotion}")
plt.axis('off')
plt.show()

print(f"\n✅ Detected Emotion: {detected_emotion}")
