import yaml
from pathlib import Path


CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config.yaml"


def load_config():
    if Path(CONFIG_DIR).exists():
        with open(CONFIG_DIR, "r") as f:
            return yaml.safe_load(f)


def save_config(config):
    import yaml

    with open(CONFIG_DIR, "w") as f:
        yaml.dump(config, f)


def load_token():
    config = load_config()
    return config["hf"]["token"]
