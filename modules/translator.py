from transformers import MarianMTModel, MarianTokenizer

# Load MarianMT for English translation (you can add more language support)
model_name = "Helsinki-NLP/opus-mt-mul-en"  # multilingual to English
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


def translate_text(text, target_lang="en"):
    try:
        batch = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
        gen = model.generate(**batch)
        translated = tokenizer.batch_decode(gen, skip_special_tokens=True)
        return translated[0]
    except Exception:
        return text
