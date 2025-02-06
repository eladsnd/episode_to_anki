from deep_translator import GoogleTranslator


def translate_text(text):
    """Translates a given Japanese sentence into English using Deep Translator."""
    translator = GoogleTranslator(source="ja", target="en")
    return translator.translate(text)
