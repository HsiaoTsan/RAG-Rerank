import os

def load_documents(path):
    text = ""
    for file in os.listdir(path):
        with open(os.path.join(path, file), "r") as f:
            text += f.read() + "\n"
    return text