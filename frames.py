from PIL import ImageSequence

gif = Image.open("object.gif")

oldFrame = gif.seek(0) #get first frame as oldFrame to start with
for frame in ImageSequence.Iterator(gif):
    newFrame = frame
    # add analysis code here
    oldFrame = frame #update oldFrame
