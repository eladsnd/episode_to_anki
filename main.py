from tqdm import tqdm
import config

from utils.sentence_orderer import extract_words
from utils.transcriber import transcribe_episode
from utils.sentence_orderer import order_sentences
from utils.audio_extractor import extract_audio_clip
from utils.image_extractor import extract_image_frame
from utils.translator import translate_text
from utils.csv_writer import save_to_csv
from utils.transliterator import convert_to_romanji, convert_to_kana


def process_episode():
    """Processes an episode and extracts data for Anki flashcards."""
    print("🔍 Transcribing episode...")
    sentences = transcribe_episode(config.EPISODE_FILE)

    print("🔄 Ordering sentences for optimal learning...")
    ordered_sentences = order_sentences(sentences)

    print("🎵 Extracting audio, images, and translations...")

    data = []
    for i, sentence in tqdm(enumerate(ordered_sentences), total=len(ordered_sentences), desc="Processing Sentences"):
        audio_file = extract_audio_clip(config.EPISODE_FILE, sentence["start_time"], sentence["end_time"], i)
        image_file = extract_image_frame(config.EPISODE_FILE, (sentence["start_time"] + sentence["end_time"]) / 2, i)

        translation = translate_text(sentence["text"])
        new_words = ", ".join(extract_words(sentence["text"]))

        # Generate Romanji & Kana
        romanji = convert_to_romanji(sentence["text"])
        kana = convert_to_kana(sentence["text"])

        # Append to dataset
        data.append([sentence["text"], romanji, kana, audio_file, image_file, translation, new_words])

    print("📄 Saving CSV...")
    save_to_csv(data, columns=["Sentence", "Romanji", "Kana", "Audio File", "Image", "Translation", "New Words"])


if __name__ == "__main__":
    process_episode()
