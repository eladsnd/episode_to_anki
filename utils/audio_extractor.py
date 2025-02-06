import os
import ffmpeg
import config

def extract_audio_clip(episode_path, start_time, end_time, file_name):
    """Extracts an audio clip from the episode using FFmpeg."""
    audio_dir = config.AUDIO_DIR
    os.makedirs(audio_dir, exist_ok=True)

    audio_filename = f"{file_name}.mp3"
    audio_path = os.path.join(audio_dir, audio_filename)

    (
        ffmpeg
        .input(episode_path, ss=start_time, to=end_time)
        .output(audio_path, format="mp3", acodec="libmp3lame")
        .run(overwrite_output=True)
    )

    return f"[sound:{audio_filename}]"  # Anki format
