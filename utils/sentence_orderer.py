import fugashi

tagger = fugashi.Tagger()

def extract_words(sentence):
    """Extracts unique words from a Japanese sentence using a tokenizer."""
    return set(w.surface for w in tagger(sentence))

def order_sentences(sentences):
    """
    Orders sentences to introduce the least amount of new words at a time.
    Removes duplicate sentences completely.
    """
    known_words = set()
    ordered_sentences = []
    seen_sentences = set()  # Store unique sentences to avoid duplicates

    # Convert sentences into tuples of (original_sentence, extracted_words)
    sentence_word_pairs = []
    for sentence in sentences:
        if sentence["text"] not in seen_sentences:  # Ensure uniqueness
            seen_sentences.add(sentence["text"])
            sentence_word_pairs.append((sentence, extract_words(sentence["text"])))

    # Sort sentences based on the number of already known words
    while sentence_word_pairs:
        # Pick the sentence with the fewest new words (most overlap with known_words)
        best_sentence = min(sentence_word_pairs, key=lambda x: len(x[1] - known_words))

        # Add to the ordered list and update known words
        ordered_sentences.append(best_sentence[0])
        known_words.update(best_sentence[1])  # Update known words

        # Remove the selected sentence from the list
        sentence_word_pairs.remove(best_sentence)

    return ordered_sentences
