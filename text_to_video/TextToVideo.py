from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import cv2

class TextToVideo():

  def __init__(self, text:str, video_size:tuple = (100, 100), font:ImageFont = ImageFont.load_default()):
    self.text = text
    self.font = font
    self.video_size = video_size

  def create_frame(self, coordinates:tuple) -> Image:
    img = Image.new("RGB", self.video_size, "green")
    draw = ImageDraw.Draw(img)
    draw.text(coordinates, self.text, font=self.font)
    return img

  def create_video(self, duration:int = 3, fps:int = 15, output_filename:str = "video"):
    video = cv2.VideoWriter(f"{output_filename}.mp4", cv2.VideoWriter_fourcc(*"XVID"), fps, self.video_size)
    self._get_coordinates()
    for x in range(self.x_start, self.x_end, (self.x_start + abs(self.x_end)) // -(duration * fps)):
      video.write(cv2.cvtColor(np.array(self.create_frame((x, self.y))), cv2.COLOR_RGB2BGR))
    video.release()

  def _get_coordinates(self):
    self.x_start = self.video_size[1]
    self.x_end = -self.font.getsize(self.text)[0]
    self.y = (self.video_size[1] - self.font.getsize(self.text)[1]) / 2
