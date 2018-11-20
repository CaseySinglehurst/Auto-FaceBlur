import cv2
import sys
from PIL import Image, ImageFilter

# Get user supplied values
imagePath = "gaffney-group.jpg"
cascadePath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))


im = Image.open(imagePath)
# Draw a rectangle around the faces
for (x, y, w, h) in faces:


    box = (x,y,x+w,y+w)
    ic = im.crop(box)
    for i in range(100):
        ic = ic.filter(ImageFilter.BLUR)
    im.paste(ic, box)


#if len(faces) > 0:
im.show()
#else:
    #print("No Faces In Picture")
cv2.waitKey(0)