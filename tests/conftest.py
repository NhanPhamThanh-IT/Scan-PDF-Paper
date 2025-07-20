import pytest
import os
import json


@pytest.fixture
def load_json():
    def _load(relative_path):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(base_dir, "app", *relative_path.split("/"))
        with open(full_path, encoding="utf-8") as f:
            return json.load(f)
    return _load