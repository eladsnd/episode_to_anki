import whisper
import config


def transcribe_episode(episode_path):
    """Transcribes the episode using OpenAI Whisper."""
    model = whisper.load_model(config.WHISPER_MODEL)
    result = model.transcribe(episode_path)

    # Extract relevant data
    sentences = []
    for segment in result["segments"]:
        sentences.append({
            "text": segment["text"],
            "start_time": segment["start"] ,
            "end_time": segment["end"] ,
        })

    return sentences
