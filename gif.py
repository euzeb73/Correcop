import tkinter as tk
from PIL import Image, ImageTk

class Gif():
    def __init__(self,filename,size=220):
        """
        Default height 220 pix 
        """
        try:
            im = Image.open(filename)
            self.frames = []
            for i in range(im.n_frames):
                im.seek(i)
                w,h = im.size
                photo = ImageTk.PhotoImage(im.convert("RGBA").resize((round(220/h*w),220)))
                photo.__reduce__()
                self.frames.append(photo)
            self.nb_frames = len(self.frames)
            self.current_frame_index = 0
            self.current_frame = self.frames[0]
            self.nb_played = 0
        except Exception as e:
            print(f"Error loading GIF: {e}")
            return None
    def next_frame(self):
        next=self.current_frame_index + 1
        if next > self.nb_frames-1:
            self.nb_played += 1
            next = next % self.nb_frames
        self.current_frame_index = (self.current_frame_index + 1) % self.nb_frames
        self.current_frame = self.frames[self.current_frame_index]
    
    def reset(self):
        """
        Remets le compte de nb de fois joué à 0
        """
        self.nb_played = 0
