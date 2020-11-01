from PIL import Image, ImageSequence
import cv2
import numpy
from PIL import Image, ImageSequence
img = Image.open("object.gif")
numSaturated = 0
numUnsaturated = 0
isSaturated = False
for i, frame in enumerate(ImageSequence.Iterator(img)):
    dst = frame.convert("RGB")
    avg_color_per_row = numpy.average(dst, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    distance = (256-avg_color[2])**2 + avg_color[0]**2 + avg_color[1]**2
    if distance <= 20:
        numSaturated+=1
    else:
        numUnsaturated+=1
if numSaturated/(numSaturated + numUnsaturated) >= 0.25:
    isSaturated = True
print(isSaturated)
