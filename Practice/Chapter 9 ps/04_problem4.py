word = "Donkey"

with open("donkeyfile.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("donkeyfile.txt", "w") as f:
    f.write(contentNew)