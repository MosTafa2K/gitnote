import time
from importlib.resources import files
from huggingface_hub import InferenceClient
import gitnote.commitgen as commitgen_module
from gitnote.config.settings import load_token
from requests.exceptions import ConnectionError


prompt_path = files(commitgen_module).joinpath("prompt.txt")
with prompt_path.open("r", encoding="utf-8") as prompt:
    messages = [
        {
            "role": "system",
            "content": prompt.read(),
        }
    ]

token = load_token()
client = InferenceClient(api_key=token)


def commit_generator(diff_output: str):
    try:
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
    except ConnectionError:
        print("Connection Error: Please check your internet connection and try again.")
