from ruamel.yaml import YAML
from pathlib import Path


CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config.yaml"
yaml = YAML()
yaml.preserve_quotes = True


def init_config():
    if not Path(CONFIG_DIR).exists():
        with open(CONFIG_DIR, "w") as f:
            yaml.dump({"hf": {"token": ""}}, f)


def ensure_config_exists():
    if Path(CONFIG_DIR).exists():
        return True
    return False


def load_config():
    if Path(CONFIG_DIR).exists():
        with open(CONFIG_DIR, "r") as f:
            return yaml.load(f)
    init_config()


def save_config(config, show_message=True):
    with open(CONFIG_DIR, "w") as f:
        yaml.dump(config, f)
    if show_message:
        print("Config saved successfully!")


def load_token():
    if ensure_config_exists():
        config = load_config()
        return config["hf"]["token"]
    else:
        init_config()


def save_token(token: str):
    config = load_config()
    config["hf"]["token"] = token
    save_config(config, show_message=False)
    print("Token saved successfully!")
