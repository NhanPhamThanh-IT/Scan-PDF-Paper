import os
import pytest

@pytest.fixture
def load_css():
    def _load(relative_path):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_dir, "app", *relative_path.split("/"))
        with open(full_path, encoding="utf-8") as f:
            return f.read()
    return _load

@pytest.fixture
def load_folder():
    def _load(relative_path):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_dir, "app", *relative_path.split("/"))
        if not os.path.exists(full_path):
            return None
        return full_path
    return _load