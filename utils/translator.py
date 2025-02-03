import asyncio
from googletrans.async_ import Translator

async def translate_text_async(text):
    """Asynchronously translates a given Japanese sentence into English."""
    translator = Translator()
    translation = await translator.translate(text, src="ja", dest="en")
    return translation.text

def translate_text(text):
    """Wrapper function to run the async translation in a synchronous context."""
    return asyncio.run(translate_text_async(text))
