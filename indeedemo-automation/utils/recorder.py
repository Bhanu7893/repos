# Optional: simple screen recorder using OpenCV (Windows only) - requires user to run locally
import cv2
import numpy as np
from datetime import datetime

class ScreenRecorder:
    def __init__(self, out_path='recordings/demo.mp4', fps=10):
        self.out_path = out_path
        self.fps = fps
        self.writer = None

    def start(self):
        # Use desktop duplication is platform specific; here we use a dummy placeholder
        print('Recorder: Start capturing - implement platform-specific recording if desired')

    def stop(self):
        print('Recorder: Stop capturing')

    def capture_frame(self, frame):
        # write frame if writer configured
        if self.writer is None:
            h, w, _ = frame.shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.writer = cv2.VideoWriter(self.out_path, fourcc, self.fps, (w, h))
        self.writer.write(frame)
