import os
from dotenv import load_dotenv
import json
import requests
from typing import List

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_ACCESS_TOKEN = os.getenv("DEEPL_ACCESS_TOKEN")


class Translator:
    def __init__(self, source_lang, target_lang):
        # self.__init__(source_lang, target_lang)
        self.source_lang = source_lang
        self.target_lang = target_lang

    def translate(self, text: List[str]):
        params = {
            "text": text,
            "source_lang": self.source_lang,
            "target_lang": self.target_lang,
        }

        headers = {"Authorization": DEEPL_ACCESS_TOKEN}

        translations = requests.post(DEEPL_API_KEY, params=params, headers=headers)

        return translations.json()["translations"][0]["text"]


if __name__ == "__main__":
    translator = Translator(source_lang="EN", target_lang="KO")
    result = translator.translate(["I feel so good right now"])
    print(result)
    my_dict = dict()
    my_dict["sample"] = result

    with open("sampleTranslation.json", "w", encoding="utf-8") as f:
        json.dump(my_dict, f, ensure_ascii=False)
