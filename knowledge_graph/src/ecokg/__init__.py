"""Knowledge graph of the neuroscience data standards ecosystem."""

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PACKAGE_ROOT / "data"
CACHE_DIR = DATA_DIR / "cache"
HARVEST_DIR = DATA_DIR / "harvested"
OUTPUT_DIR = PACKAGE_ROOT / "output"
