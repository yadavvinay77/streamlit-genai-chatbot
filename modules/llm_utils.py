import os
from llama_cpp import Llama

# Lazy-load the model
_llm = None


def get_llm():
    global _llm
    if _llm is None:
        model_path = os.path.join("llama_model", "llama-2-7b.gguf")
        _llm = Llama(model_path=model_path, n_ctx=2048)
    return _llm


def get_llm_answer(context, question):
    """
    Prompt the local LLaMA model with context + question and return
    its completion (stripped).
    """
    llm = get_llm()
    prompt = (
        "[INST] You are a helpful assistant.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:[/INST]\n"
    )
    resp = llm(prompt, max_tokens=150, stop=["[/INST]"])
    return resp["choices"][0]["text"].strip()
