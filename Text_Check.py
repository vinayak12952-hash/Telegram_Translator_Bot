from Translator_Engine import Translator_Engine

def translate(text):

    if isinstance(text,str):
        if not text.strip():
            return "⚠️  Error: Text cannot be empty."
        elif len(text.strip()) > 5000:
            return "⚠️  Error: Text exceeds the 5000-character limit."
        else:
            a = Translator_Engine(text)
            return f"Translation: {a}"
        
    else:
        return "⚠️  Error: Input must be a string."

