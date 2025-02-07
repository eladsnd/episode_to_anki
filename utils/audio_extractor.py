import os
import ffmpeg
import config
import shutil  # For safely replacing files

def extract_audio_clip(episode_path, start_time, end_time, file_name, extend_duration=1.0):
    """
    Extracts an audio clip from the episode using FFmpeg.
    Ensures a small extension so words are not cut off early.
    """
    audio_dir = config.AUDIO_DIR
    os.makedirs(audio_dir, exist_ok=True)

    audio_filename = f"{file_name}.mp3"
    audio_path = os.path.join(audio_dir, audio_filename)
    temp_audio_path = os.path.join(audio_dir, f"temp_{file_name}.mp3")  # Temporary file

    # Calculate final duration
    duration = (end_time - start_time) + extend_duration

    try:
        # Step 1: Extract the audio clip
        (
            ffmpeg
            .input(episode_path, ss=start_time)
            .output(audio_path, format="mp3", acodec="libmp3lame", t=duration)
            .run(overwrite_output=True, quiet=False)
        )

        # Step 2: Add silent padding (write to a temp file)
        (
            ffmpeg
            .input(audio_path)
            .filter("apad", pad_dur=extend_duration)
            .output(temp_audio_path, format="mp3")
            .run(overwrite_output=True, quiet=False)
        )

        # Step 3: Replace the original file with the padded version
        shutil.move(temp_audio_path, audio_path)

    except ffmpeg.Error as e:
        print(f"❌ FFmpeg failed for: {file_name}")
        if e.stderr:
            print(f"❗ FFmpeg Error Output: {e.stderr.decode(errors='ignore')}")  # Decode safely

    return f"[sound:{audio_filename}]"  # Anki format
