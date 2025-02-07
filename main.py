import os
from tqdm import tqdm
import config
import warnings
warnings.simplefilter("ignore", category=UserWarning)

from utils.transcriber import transcribe_episode
from utils.sentence_orderer import order_sentences
from utils.audio_extractor import extract_audio_clip
from utils.image_extractor import extract_image_frame
from utils.translator import translate_text
from utils.csv_writer import save_to_csv
from utils.transliterator import convert_to_romanji, convert_to_kana

# Extract the base episode name (without extension)
EPISODE_NAME = os.path.splitext(os.path.basename(config.EPISODE_FILE))[0]


def process_episode():
    """Processes an episode and extracts data for Anki flashcards."""
    print("🔍 Transcribing episode...")
    sentences = transcribe_episode(config.EPISODE_FILE)

    print("🔄 Removing duplicates and ordering sentences for optimal learning...")

    # Remove duplicate sentences
    unique_sentences = []
    seen_sentences = set()
    for sentence in sentences:
        if sentence["text"] not in seen_sentences:
            seen_sentences.add(sentence["text"])
            unique_sentences.append(sentence)

    # Order sentences to introduce minimal new words
    ordered_sentences = order_sentences(unique_sentences)

    print("🎵 Extracting audio, images, and translations...")

    data = []
    for i, sentence in tqdm(enumerate(ordered_sentences), total=len(ordered_sentences), desc="Processing Sentences"):
        # Generate filenames with the episode prefix
        audio_file = extract_audio_clip(config.EPISODE_FILE, sentence["start_time"], sentence["end_time"],
                                        f"{EPISODE_NAME}_audio_{i}", extend_duration=0.5)
        image_file = extract_image_frame(config.EPISODE_FILE, (sentence["start_time"] + sentence["end_time"]) / 2,
                                         f"{EPISODE_NAME}_image_{i}")

        translation = translate_text(sentence["text"])

        # Generate Romanji & Kana
        romanji = convert_to_romanji(sentence["text"])
        kana = convert_to_kana(sentence["text"])

        # Append to dataset
        data.append([sentence["text"], romanji, kana, audio_file, image_file, translation])

    print("📄 Saving CSV...")
    output_csv = os.path.join("data", f"anki_sentences_{EPISODE_NAME}.csv")
    save_to_csv(data, output_csv, columns=["Sentence", "Romanji", "Kana", "Audio File", "Image", "Translation"])


if __name__ == "__main__":
    process_episode()
