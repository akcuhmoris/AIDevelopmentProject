import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')

import cv2 as cv
import os

import cv2
import os

video_path = 'path_to_your_video.mp4'
output_dir = 'extracted_frames'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f'{output_dir}/frame_{frame_count:04d}.jpg', frame)
    frame_count += 1

cap.release()