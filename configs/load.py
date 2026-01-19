# configs/load.py
import yaml
from pathlib import Path

def load_models_config(path: Path = Path("configs/models.yaml")):
    with path.open() as f:
        return yaml.safe_load(f)
