import requests
def cat_say(word):
    file = requests.get(f"https://cataas.com/cat/says/{word}").content
    with open(f"cat_is_says_{word}.jpg", mode="wb") as surat:
        surat.write(file)
        

        