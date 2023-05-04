# import ChatGPT, Translator
import json
import random
import string
from restaurantTopics import reservation_content
from tourismTopics import tourism_content
from nativefriendTopics import nativefriend_content
from hotelTopics import hotel_content
from airportTopics import airport_content

from datetime import datetime
from typing import Optional, List, Dict
import sys


# run this file with arguments
# python use_separate_prompts.py 0

if len(sys.argv) < 2:
    prompt_num = 0
else: 
    prompt_num = str(sys.argv[1])

print("prompt_num:", prompt_num)

with open("user_content.json") as file:
    prompt = json.load(file)

print("prompt:", prompt[int(prompt_num)])

# class Turn:
#     id: str
#     mission_id: str
#     order: int
#     ai_conversation_starter_en: str
#     ai_conversation_starter_ko: str = ""
#     # option_name_en: str = ""
#     # option_name_ko: str = ""
#     user_response_option_en: str = ""
#     user_response_option_ko: str = ""
#     key_phrase_en: str = ""
#     key_phrase_ko: str = ""
#     next_turn_id: str
#     previous_turn_id: Optional[str]

#     def __str__(self) -> str:
#         dict_str = json.dumps(
#             {
#                 "id": self.id,
#                 "ai_conversation_starter_en": self.ai_conversation_starter_en,
#                 "user_response_option_en": self.user_response_option_en,
#                 "previous_turn_id": self.previous_turn_id,
#                 "next_turn_id": self.next_turn_id,
#             }
#         )
#         return dict_str


# class Mission:
#     id: str
#     title: str
#     order: int
#     turns: List[Turn]


# MISSION_DICTIONARY = dict()
# TURN_DB = dict()

# STARTING_NODE_ID_TEXT = "STARTING_NODE"


# def generate_random_id(length=16):
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = "".join(random.choice(letters) for i in range(length))

#     return result_str


# def get_all_previous_convo_ordered(one_turn: Turn):
#     if one_turn.previous_turn_id == STARTING_NODE_ID_TEXT:
#         return [one_turn.ai_conversation_starter_en, one_turn.user_response_option_en]
#     else:
#         prev_turn_id = one_turn.previous_turn_id
#         previous_turn = TURN_DB[prev_turn_id]
#         return get_all_previous_convo_ordered(previous_turn) + [
#             one_turn.ai_conversation_starter_en,
#             one_turn.user_response_option_en,
#         ]


# def generate_full_mission(scenario_name: str, mission_name: str):
#     """
#     EXAMPLE:
#         scene: Restaurant
#             > scenario_name: Making a reservation


#                 --- This is what generate_full_mission creates
#                 > mission_name: Calling the restaurant (to make the reservation)
#                     # and this tree, branching structure, we manage with linked lists
#                     > turn_1:
#                         > turn_1_1:
#                     > turn_2:
#                         > turn_2_1:
#                     > turn_3
#                         > turn_3_1
#                 > mission_name: ...
#                 > mission_name: ...
#                 ...
#             > scenario_name: ...
#             ...
#     """

#     mission_id = generate_random_id()
#     mission: Mission = {"id": mission_id}
#     MISSION_DICTIONARY[mission_id] = mission

#     # The AI needs to start the conversation here
#     conversationStarter = get_first_sentence(scenario_name, mission_name)

#     # The several ways the user can reply
#     response_options = get_recommendations(
#         scenario_name, mission_name, [conversationStarter]
#     )

#     for response_option in response_options:
#         # each of these constitute a potential "turn"
#         one_turn = Turn()
#         one_turn.id = generate_random_id()
#         one_turn.ai_conversation_starter_en = conversationStarter
#         one_turn.user_response_option_en = response_option
#         one_turn.mission_id = mission_id
#         one_turn.previous_turn_id = STARTING_NODE_ID_TEXT
#         one_turn.order = 1

#         TURN_DB[one_turn.id] = one_turn

#     how_many_turns = 3
#     for order in range(2, how_many_turns + 1):  # range(2, 4) = [2,3]
#         turns: List[Turn] = list(TURN_DB.values())

#         for one_prev_turn in turns:
#             # not optimal, but works 100%
#             if hasattr(one_prev_turn, "next_turn_id"):
#                 # Don't create next_turns for those that already have next_turns
#                 continue

#             # array of [AIspeak, userSpeak, AISpeak, userSpeak, ..., userSpeak] in this order, ends like so as well
#             prev_conversastions_from_turn = get_all_previous_convo_ordered(
#                 one_prev_turn
#             )
#             ai_conversation_starter_en = get_ai_response(
#                 scenario_name, mission_name, prev_conversastions_from_turn
#             )

#             branching_recs = get_recommendations(
#                 scenario_name,
#                 mission_name,
#                 prev_conversastions_from_turn + [ai_conversation_starter_en],
#             )

#             for branching_rec in branching_recs:
#                 new_turn = Turn()
#                 new_turn.id = generate_random_id()
#                 new_turn.mission_id = mission_id
#                 new_turn.ai_conversation_starter_en = ai_conversation_starter_en
#                 new_turn.user_response_option_en = branching_rec

#                 new_turn.previous_turn_id = one_prev_turn.id
#                 new_turn.order = order

#                 prev_turn_id = one_prev_turn.id

#                 one_prev_turn.next_turn_id = new_turn.id

#                 TURN_DB[prev_turn_id] = one_prev_turn
#                 TURN_DB[new_turn.id] = new_turn


# def get_first_sentence(scenario_name, mission_name):
#     res = chatgpt.generate_ai_response(
#         ChatGPT.CONVERSATION_STARTER, scenario_name, mission_name
#     )
#     return res


# def get_ai_response(scenario_name, mission_name, previous_conversation):
#     res = chatgpt.generate_ai_response(
#         ChatGPT.AI_RESPONSE, scenario_name, mission_name, previous_conversation
#     )
#     return res


# def get_recommendations(
#     scenario_name, mission_name, previous_conversation
# ) -> List[str]:
#     res = chatgpt.generate_recommendations(
#         scenario_name, mission_name, previous_conversation
#     )
#     recommendations = list(res.split("\n"))
#     recommendations_processed = []
#     for recommendation in recommendations:
#         if ": " in recommendation:
#             recommendations_processed.append(
#                 recommendation[3:]
#                 .split(": ", 1)[-1]
#                 .strip('"')
#                 .strip()
#                 .strip('"')
#                 .split(" (")[0]
#             )
#         else:
#             recommendations_processed.append(recommendation[3:].removesuffix('"'))
#     # recommendations = [x[3:].split(": ")[1].removesuffix('"') for x in recommendations]

#     return recommendations_processed


# def summarize_sentences(full_sentences, previous_conversations):
#     res = chatgpt.summarize(full_sentences, previous_conversations)
#     summaries = list(res.split("\n"))
#     summaries = [x[3:] for x in summaries]
#     return summaries


# def extract_keyphrase(expression):
#     res = chatgpt.extract_keyphrase(expression)
#     return res


# def play_mission_one_full_branch(mission_id: str):
#     # because too much branching is confusing,
#     # we just choose the first branch

#     all_turns: List[Turn] = list(TURN_DB.values())
#     this_mission_turns = [
#         one_turn for one_turn in all_turns if one_turn.mission_id == mission_id
#     ]

#     for turn in this_mission_turns:
#         # translate
#         # turn.ai_conversation_starter_ko = translator.translate(
#         #     [turn.ai_conversation_starter_en]
#         # )
#         # turn.user_response_option_ko = translator.translate(
#         #     [turn.user_response_option_en]
#         # )

#         # extract key phrase
        turn.key_phrase_en = chatgpt.extract_keyphrase(f'{prompt}\n\t- "{turn.user_response_option_en}"')
#         # turn.key_phrase_ko = translator.translate([turn.key_phrase_en])

#         # summarize response options
#         # turn.option_name_en = chatgpt.summarize_sentence(
#         #     turn.ai_conversation_starter_en, turn.user_response_option_en
#         # )
#         # turn.option_name_ko = translator.translate([turn.option_name_en])

#     this_mission_turns_dict = [t.__dict__ for t in this_mission_turns]

#     return this_mission_turns_dict


# if __name__ == "__main__":
#     print(f"Execution time: {datetime.now().time()}")

#     scene_num = 5
#     mission_num = 6

#     location = "airport"
#     ai_persona = airport_content[scene_num - 1]["ai_persona"]
#     user_persona = airport_content[scene_num - 1]["user_persona"]
#     chatgpt = ChatGPT.ChatGPT(location, ai_persona, user_persona)
#     translator = Translator.Translator(source_lang="EN", target_lang="KO")

#     parent_scene = airport_content[scene_num - 1]["parent_scene"]
#     child_scenario = airport_content[scene_num - 1]["child_scenarios"][mission_num - 1]

#     result = generate_full_mission(parent_scene, child_scenario)
#     mission_obj: Mission = list(MISSION_DICTIONARY.values())[0]

#     this_mission_turns_dict = play_mission_one_full_branch(mission_obj["id"])

#     mission_obj["title"] = child_scenario
#     mission_obj["order"] = mission_num
#     mission_obj["turns"] = this_mission_turns_dict

    with open(
        f"airportTopics/prompt{prompt_num}/scene{scene_num}/mission{mission_num}e.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(mission_obj, file, ensure_ascii=False)

#     print(f"Completion time: {datetime.now().time()}")
