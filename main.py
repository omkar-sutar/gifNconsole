from email.mime import image
import sys
from PIL import Image, ImageSequence
import numpy as np
import os
import time

l=[r'█',u"\u25A0","@","#"]

def render_gif(path:str,delay_ms:int,height:int,width=None)->None:
    """Plays the gif for infinite time. BLOCKING.\n
        Arguments:
        path: (required) The path of the gif.\n
        delay_ms: (required) The delay between two consecutive frames of the gif.\n
        height: (required) The specified gif is resized to this height.\n
        width: (optional) The specified gif is resized to this width.
        If width is not specified, it is calculated so as to maintain the aspect ratio.\n
        Usage example: render_gif("aqua2.gif",delay_ms=100,height=30)"""
    imageObj=None
    try:
        imageObj=Image.open(path)
    except IOError:
        print("GIF not found")
        return
    os.system("cls")
    frame_height=height
    frame_width=int((imageObj.width/imageObj.height)*frame_height)
    if width:
        frame_width=width
    frames=[]
    for frame in ImageSequence.Iterator(imageObj):
        frame=frame.convert('RGB').resize((frame_width,frame_height)).copy()
        frame=np.asarray(frame)
        frames.append(frame)
    frames=np.array(frames)
    output_frames=[]
    print("Processing")
    for frame in frames:
        output_frame=""
        for row in frame:
            for pixel in row:
                output_frame+="\033[38;2;{};{};{}m".format(pixel[0],pixel[1],pixel[2])+"#"+"\033[0m"
            output_frame+="\n"
        output_frames.append(output_frame)

    while True:
        for frame in output_frames:
            sys.stdout.write(frame)
            time.sleep(delay_ms/1000)
            os.system("cls")
            

if __name__=='__main__':
    render_gif("aqua2.gif",delay_ms=100,height=30)