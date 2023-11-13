import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
from datetime import datetime
import numpy as np

class VideoCamera(object):
    # Default resolution and framerate for stream
    DEFAULT_RESOLUTION = (1920, 1080)
    DEFAULT_FRAMERATE = 30

    def __init__(self, flip=False, file_type=".jpg", photo_string="farmbot_photo", resolution=None, framerate=None):
        # Initialize stream with the default resolution and framerate
        self.vs = PiVideoStream(resolution=resolution or self.DEFAULT_RESOLUTION, framerate=framerate or self.DEFAULT_FRAMERATE).start()

        #Attributes for camera settings
        self.flip = flip  # Initialize self.flip, from VideoCamera to determine if frame should be flipped
        self.file_type = file_type  # image type i.e. .jpg
        self.photo_string = photo_string  # Name to save the photo as
        time.sleep(2.0) # Just allowing camera to boot up

    def __del__(self):
        # Stop the stream when the object has been deleted
        self.vs.stop()

    def flip_if_needed(self, frame):
        # Flips the frame if set to true via main.py
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def capture_frame(self):
        # Capture frames from the stream and flip if required
        return self.flip_if_needed(self.vs.read())

    def save_picture(self, frame):
        # Saves a frame as an image with a timestamp
        ret, image = cv.imencode(self.file_type, frame)
        today_date = datetime.now().strftime("%m%d%Y-%H%M%S")
        file_path = str(self.photo_string + "_" + today_date + self.file_type)
        with open(file_path, 'wb') as f:
            f.write(image.tobytes())

    def take_picture(self):
        # Save the frame and save it as a picture
        frame = self.capture_frame()
        self.save_picture(frame)

    def get_frame(self):
        # Capture the frame and encode it as JPEG format for streaming
        frame = self.capture_frame()
        ret, jpeg = cv.imencode(self.file_type, frame)
        return jpeg.tobytes()