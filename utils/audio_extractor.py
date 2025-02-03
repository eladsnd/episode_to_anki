import ffmpeg
import os
import config


def extract_audio_clip(episode_path, start_time, end_time, file_index):
    """Extracts an audio clip from the episode using FFmpeg."""
    audio_filename = f"audio_{file_index}.mp3"
    audio_path = os.path.join(config.AUDIO_DIR, audio_filename)

    ffmpeg.input(episode_path, ss=start_time, to=end_time).output(audio_path).run(overwrite_output=True)

    return f"[sound:{audio_filename}]"  # Anki format
