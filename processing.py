import json
import ChatGPT, Translator

chatgpt = ChatGPT.ChatGPT("restaurant", "server", "guest")
translator = Translator.Translator(source_lang="EN", target_lang="KO")

for i in range(6):
    with open(f"tourismTopics/scene2/mission{i+1}.json") as file:
        data = json.load(file)
    turns = data["turns"]
    for turn in turns:
        turn["ai_conversation_starter_ko"] = translator.translate(
            [turn["ai_conversation_starter_en"]]
        )
        turn["user_response_option_ko"] = translator.translate(
            [turn["user_response_option_en"]]
        )
    data["turns"] = turns

    with open(
        f"tourismTopics/scene2/mission{i+1}.json", "w", encoding="utf-8",
    ) as file:
        json.dump(data, file, ensure_ascii=False)

# with open("restaurantTopics/restaurant_scene2_mission1.json") as file:
#     data = json.load(file)


# def summarize(expression):
#     summary = chatgpt.summarize_sentence(expression)
#     return summary


# turns = data["turns"]
# for turn in turns:
#     option_name = summarize(turn["user_response_option_en"])
#     turn["option_name_en"] = option_name
#     turn["option_name_ko"] = translator.translate([option_name])

# data["turns"] = turns

# with open(
#     "restaurant_scene2_mission1_with_option.json", "w", encoding="utf-8",
# ) as file:
#     json.dump(data, file, ensure_ascii=False)

