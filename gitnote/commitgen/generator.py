import time
import importlib.resources as pkg_resources
from huggingface_hub import InferenceClient
import gitnote.commitgen as commitgen_module


with pkg_resources.open_text(commitgen_module, "prompt.txt") as prompt:
    messages = [
        {
            "role": "system",
            "content": prompt.read(),
        }
    ]

client = InferenceClient()


def commit_generator(diff_output: str):
    response = ""
    local_messages = messages.copy()
    local_messages.append({"role": "user", "content": diff_output})
    stream = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=local_messages,
        temperature=0.5,
        max_tokens=1024,
        top_p=0.7,
        stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content, end="", flush=True)
        time.sleep(0.1)
        response += chunk.choices[0].delta.content
    print()
    messages.append({"role": "assistant", "content": response})
