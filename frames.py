from PIL import Image, ImageSequence
import cv2
import numpy
from PIL import Image, ImageSequence
img = Image.open("object.gif")
for i, frame in enumerate(ImageSequence.Iterator(img)):
    dst = frame.convert("RGB")
    avg_color_per_row = numpy.average(dst, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    print(avg_color) #BGR order
