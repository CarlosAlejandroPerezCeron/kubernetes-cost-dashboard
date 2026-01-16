import os
from dotenv import load_dotenv

load_dotenv()

def log(message):
    print(f"[INFO] {message}")

def get_env(var, default=None):
    value = os.getenv(var, default)
    if value is None:
        raise ValueError(f"Missing env var: {var}")
    return value
