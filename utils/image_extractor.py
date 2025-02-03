import cv2
import os
import config


def extract_image_frame(video_path, timestamp, file_index):
    """Extracts an image frame from the video at a specific timestamp."""
    image_filename = f"image_{file_index}.jpg"
    image_path = os.path.join(config.IMAGE_DIR, image_filename)

    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)  # Convert seconds to milliseconds
    success, frame = cap.read()
    if success:
        cv2.imwrite(image_path, frame)
    cap.release()

    return f"<img src='{image_filename}'>"
