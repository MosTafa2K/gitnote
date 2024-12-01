import yaml
from pathlib import Path


CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config.yaml"


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
            return yaml.safe_load(f)
    else:
        init_config()
        return {"hf": {"token": ""}}


def save_config(config):
    import yaml

    with open(CONFIG_DIR, "w") as f:
        yaml.dump(config, f)


def load_token():
    if ensure_config_exists():
        config = load_config()
        return config["hf"]["token"]
    else:
        init_config()
