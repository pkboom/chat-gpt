from prompt1 import response as data
from prompt4 import response as data4
import re
import json
from typing import List

# def split_sentences(text):
#     sentence_endings = r"([.?!])([\s|$])"
#     sentences = re.split(sentence_endings, text)
#     sentence_tuples = []
#     for i in range(0, len(sentences), 3):
#         if len(sentences) > i + 2:
#             sentence_tuples.append((sentences[i] + sentences[i + 1], sentences[i + 2]))
#         else:
#             sentence_tuples.append((sentences[i], ""))
#     return sentence_tuples

# turns = data["turns"]
# for turn in turns:
#     ai_sentences = split_sentences(turn["ai_conversation_starter_en"])
#     ai_conversation_starter_en = []
#     for sentence in ai_sentences:
#         ai_conversation_starter_en.append(sentence[0])
#     turn["ai_conversation_starter_en"] = ai_conversation_starter_en

#     user_sentences = split_sentences(turn["user_response_option_en"])
#     user_response_option_en = []
#     for sentence in user_sentences:
#         user_response_option_en.append(sentence[0])
#     turn["user_response_option_en"] = user_response_option_en


def _split_sentences(sentences: str) -> List[str]:
    sentences = re.split(r"(?<=[.!?])\s*", sentences)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


turns = data4["turns"]
for turn in turns:
    turn["ai_conversation_starter"] = _split_sentences(
        turn["ai_conversation_starter_en"]
    )


with open(
    "testingPrompts/userResponseLength/prompt4b.json", "w", encoding="utf-8",
) as file:
    json.dump(data4, file, ensure_ascii=False)
