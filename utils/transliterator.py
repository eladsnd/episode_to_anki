import pykakasi
import fugashi

# Initialize the Japanese tokenizer and transliteration engine
tagger = fugashi.Tagger()
kakasi = pykakasi.kakasi()
kakasi.setMode("H", "a")  # Hiragana → Romaji
kakasi.setMode("K", "a")  # Katakana → Romaji
kakasi.setMode("J", "a")  # Kanji → Romaji
kakasi.setMode("r", "Hepburn")  # Use Hepburn Romanization
conv = kakasi.getConverter()


def convert_to_romanji(sentence):
    """Converts a Japanese sentence into properly spaced Romanji."""
    words = [w.surface for w in tagger(sentence)]
    romanized_words = [conv.do(word) for word in words]
    return " ".join(romanized_words)  # Ensures spacing between words


def convert_to_kana(sentence):
    """Converts a Japanese sentence into hiragana/katakana representation."""
    kana_sentence = ""

    for word in tagger(sentence):
        original = word.surface
        kana = getattr(word.feature, "pron", None)  # Get pronunciation if available
        kana_sentence += kana if kana else original  # Use kana if available, else original

    return kana_sentence
