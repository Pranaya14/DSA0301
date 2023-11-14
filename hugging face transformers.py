from transformers import pipeline

def machine_translation(text, source_lang, target_lang):
    translator = pipeline("translation", model=f"{source_lang}_to_{target_lang}")
    translation = translator(text, max_length=50)

    return translation[0]["translation_text"]

# Example usage
text = "Hello, how are you?"
source_lang = "en"
target_lang = "fr"
translated_text = machine_translation(text, source_lang, target_lang)

print("Original Text:", text)
print(f"Translated Text ({source_lang} to {target_lang}):", translated_text)


python -m spacy download en_core_web_sm
python -m nltk.downloader wordnet
