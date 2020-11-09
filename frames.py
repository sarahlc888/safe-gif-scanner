from PIL import Image, ImageSequence
import cv2
import numpy
from PIL import Image, ImageSequence
img = Image.open("object.gif")
numSaturated = 0
numUnsaturated = 0
isSaturated = False
isFlashing = False
relLuminance = 0
luminances = []
for i, frame in enumerate(ImageSequence.Iterator(img)):
    dst = frame.convert("RGB")
    avg_color_per_row = numpy.average(dst, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    distance = (256-avg_color[2])**2 + avg_color[0]**2 + avg_color[1]**2
    if distance <= 20:
        numSaturated+=1
    else:
        numUnsaturated+=1
    #from http://en.wikipedia.org/wiki/Luminance_(relative)
    relLuminance = 0.2126*avg_color[2] + 0.7152*avg_color[1] + 0.0722*avg_color[0]
    luminances.append(relLuminance)
if numSaturated/(numSaturated + numUnsaturated) >= 0.25:
    isSaturated = True
luminanceChanges = [luminances[i+1]-luminances[i] for i in range(len(luminances)-1)]
avgLuminanceChange = sum(luminanceChanges) / len(luminanceChanges)
numFlashes = 0
for change in luminanceChanges:
    if change >= 2*avgLuminanceChange:
        numFlashes += 1
numFrames = numSaturated + numUnsaturated #clean up later
if numFlashes >= 0.25 * numFrames:
    isFlashing = True
print(isFlashing)
print(isSaturated)
