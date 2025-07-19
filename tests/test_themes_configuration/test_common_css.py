import os

def test_common_css_exists(load_css):
    content = load_css("assets/themes/common.css")
    assert content is not None, "CSS file not found"

def test_common_css_not_empty(load_css):
    content = load_css("assets/themes/common.css")
    assert content.strip() != "", "CSS file is empty"
