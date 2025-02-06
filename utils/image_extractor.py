import os
import cv2
import config

def extract_image_frame(episode_path, timestamp, file_name):
    """Extracts a frame from the video at the given timestamp."""
    image_dir = config.IMAGE_DIR
    os.makedirs(image_dir, exist_ok=True)

    image_filename = f"{file_name}.jpg"
    image_path = os.path.join(image_dir, image_filename)

    cap = cv2.VideoCapture(episode_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
    success, frame = cap.read()
    if success:
        cv2.imwrite(image_path, frame)
    cap.release()

    return image_filename  # Anki expects just the filename
