def load_css(file_path):
    with open(file_path, "r") as f:
        css = f.read()
    return css