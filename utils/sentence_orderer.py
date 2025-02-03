import re
from collections import defaultdict


def extract_words(sentence):
    """Extracts words from a sentence using basic tokenization."""
    sentence = re.sub(r'[^\w\sぁ-んァ-ン一-龥]', '', sentence)  # Remove punctuation
    return sentence.split()  # Basic splitting (better with MeCab)


def order_sentences(sentences):
    """
    Orders sentences using the +1 word learning method:
    - Starts with the simplest sentence (fewest new words).
    - Introduces only 1 new word per sentence when possible.
    """
    ordered = []
    learned_words = set()

    while sentences:
        # Find the best next sentence (fewest new words)
        best_sentence = min(sentences, key=lambda s: sum(1 for w in extract_words(s["text"]) if w not in learned_words))

        # Add to ordered list
        ordered.append(best_sentence)

        # Mark words as learned
        learned_words.update(extract_words(best_sentence["text"]))

        # Remove from list
        sentences.remove(best_sentence)

    return ordered
