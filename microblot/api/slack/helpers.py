def tokenize(text):
    return {pair.split("=")[0]: pair.split("=")[1] for pair in text.split("&")}


def find_command(text):
    for pair in text.split("&"):
        key, value = pair.split("=")
        if key == "text":
            return value
