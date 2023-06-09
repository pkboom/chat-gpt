"""
Prompt: 
    system_content = f"You're an English teacher that helps non-native speakers learn English through role-playing."
    assistant_content = f"Here's the previous conversation between a {self.ai_persona} and a {self.user_persona} named Iris Kim: \
        \n\t - {previous_conversation_str}"
    user_content = f"The {self.user_persona} named Iris Kim is {child_scenario} while {parent_scene}. \
        After the {self.ai_persona} says \"{previous_conversation[-1]}\", give me 3 different ways Iris Kim might respond to the server here. \
        Each response should be different but all should be appropriate to the situation, and help facilitate the prcoess of {child_scenario}. \
        Since the script is for non-native speakers, avoid having complicated sentences and keep each resposne under 14 words. \
        Return a numbered list and don't say anything else."
"""

response = {
    "id": "brzoyozrflpkxuqz",
    "title": "Making a complaint about bad food",
    "order": 5,
    "turns": [
        {
            "id": "vewbsifayoxrhyjn",
            "ai_conversation_starter_en": "Is everything okay with your meal?",
            "user_response_option_en": "Food is not good, I'm afraid.",
            "mission_id": "brzoyozrflpkxuqz",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "pstvpdaekdcmwcmk",
            "key_phrase_en": "Not Good",
        },
        {
            "id": "eirvfuovistpbkgv",
            "ai_conversation_starter_en": "Is everything okay with your meal?",
            "user_response_option_en": "Taste is not what I expected.",
            "mission_id": "brzoyozrflpkxuqz",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "pvtxqauvidvpqkch",
            "key_phrase_en": "Not expected",
        },
        {
            "id": "rtszpvkmhsfmaomw",
            "ai_conversation_starter_en": "Is everything okay with your meal?",
            "user_response_option_en": "This meal is not very enjoyable.",
            "mission_id": "brzoyozrflpkxuqz",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "xmlvzsqnllgvwrio",
            "key_phrase_en": "Not very enjoyable",
        },
        {
            "id": "hlbskfsgzenitfgn",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm so sorry to hear that, Iris. Would you like to try something else instead?",
            "user_response_option_en": "Can you recommend something else, please?",
            "previous_turn_id": "vewbsifayoxrhyjn",
            "order": 2,
            "next_turn_id": "rwyxwsrpwkulkofr",
            "key_phrase_en": "recommend something else",
        },
        {
            "id": "xtyklexuylntojko",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm so sorry to hear that, Iris. Would you like to try something else instead?",
            "user_response_option_en": "No, thank you. Could you bring the bill, please?",
            "previous_turn_id": "vewbsifayoxrhyjn",
            "order": 2,
            "next_turn_id": "ldwrevmofhfkyoem",
            "key_phrase_en": "Bring the bill",
        },
        {
            "id": "pstvpdaekdcmwcmk",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm so sorry to hear that, Iris. Would you like to try something else instead?",
            "user_response_option_en": "Yes, I'd like to try the vegetarian pasta.",
            "previous_turn_id": "vewbsifayoxrhyjn",
            "order": 2,
            "next_turn_id": "mixcwxfgmzljacow",
            "key_phrase_en": "Vegetarian pasta",
        },
        {
            "id": "pvzkmdrhpcrpiqlk",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the disappointment. Could you please tell me what specifically is not to your liking?",
            "user_response_option_en": "The chicken is dry.",
            "previous_turn_id": "eirvfuovistpbkgv",
            "order": 2,
            "next_turn_id": "slrbkbbauvitgtej",
            "key_phrase_en": "Chicken is dry",
        },
        {
            "id": "uaiyejusqcblnopb",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the disappointment. Could you please tell me what specifically is not to your liking?",
            "user_response_option_en": "The rice is overcooked.",
            "previous_turn_id": "eirvfuovistpbkgv",
            "order": 2,
            "next_turn_id": "wlgejpcdvlqjfwoy",
            "key_phrase_en": "overcooked rice",
        },
        {
            "id": "pvtxqauvidvpqkch",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the disappointment. Could you please tell me what specifically is not to your liking?",
            "user_response_option_en": "The sauce is too salty.",
            "previous_turn_id": "eirvfuovistpbkgv",
            "order": 2,
            "next_turn_id": "vjrupukbphmemnei",
            "key_phrase_en": "Too salty",
        },
        {
            "id": "givihkktaflubrtb",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that. Can you tell me what seems to be the problem with your meal?",
            "user_response_option_en": "It tastes bland, can you add some sauce?",
            "previous_turn_id": "rtszpvkmhsfmaomw",
            "order": 2,
            "next_turn_id": "uepnsvvpqdpkmwuo",
            "key_phrase_en": "add sauce",
        },
        {
            "id": "heczulkdyeelrybx",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that. Can you tell me what seems to be the problem with your meal?",
            "user_response_option_en": "The steak is overcooked and dried.",
            "previous_turn_id": "rtszpvkmhsfmaomw",
            "order": 2,
            "next_turn_id": "kucxhtviuhrienot",
            "key_phrase_en": "overcooked steak",
        },
        {
            "id": "xmlvzsqnllgvwrio",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that. Can you tell me what seems to be the problem with your meal?",
            "user_response_option_en": "The soup is cold, please reheat.",
            "previous_turn_id": "rtszpvkmhsfmaomw",
            "order": 2,
            "next_turn_id": "ggrwhnfvcskehzdu",
            "key_phrase_en": "reheat",
        },
        {
            "id": "mbvziyvzflvuvvdg",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Certainly, Iris. Our chef recommends the grilled salmon or our vegetarian pasta dish. Would you like me to bring one of those options for you to try instead?",
            "user_response_option_en": "Yes please. I'll try the grilled salmon. Thank you for the recommendation.",
            "previous_turn_id": "hlbskfsgzenitfgn",
            "order": 3,
            "key_phrase_en": "Grilled salmon",
        },
        {
            "id": "dnfidjmuknjzlayq",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Certainly, Iris. Our chef recommends the grilled salmon or our vegetarian pasta dish. Would you like me to bring one of those options for you to try instead?",
            "user_response_option_en": "No, thanks. Not hungry anymore. Can I just have the bill?",
            "previous_turn_id": "hlbskfsgzenitfgn",
            "order": 3,
            "key_phrase_en": "Just the bill",
        },
        {
            "id": "rwyxwsrpwkulkofr",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Certainly, Iris. Our chef recommends the grilled salmon or our vegetarian pasta dish. Would you like me to bring one of those options for you to try instead?",
            "user_response_option_en": "Maybe next time. I appreciate your service. Can I get a discount?",
            "previous_turn_id": "hlbskfsgzenitfgn",
            "order": 3,
            "key_phrase_en": "Maybe next time",
        },
        {
            "id": "vswbkseajcacuavi",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry again about the food, Iris. I'll bring the bill right away.",
            "user_response_option_en": "Okay, thank you for your help.",
            "previous_turn_id": "xtyklexuylntojko",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "utyfvoubxzguikec",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry again about the food, Iris. I'll bring the bill right away.",
            "user_response_option_en": "I appreciate your attention to my complaint.",
            "previous_turn_id": "xtyklexuylntojko",
            "order": 3,
            "key_phrase_en": "Appreciate attention",
        },
        {
            "id": "ldwrevmofhfkyoem",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry again about the food, Iris. I'll bring the bill right away.",
            "user_response_option_en": "Thank you for listening to my feedback.",
            "previous_turn_id": "xtyklexuylntojko",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "epwjqqqamyxotezo",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, Iris. I'll make sure to communicate your feedback to the chef. Thank you for letting me know.",
            "user_response_option_en": "Thank you, I appreciate it.",
            "previous_turn_id": "pstvpdaekdcmwcmk",
            "order": 3,
            "key_phrase_en": "appreciate it",
        },
        {
            "id": "tfjktdcntydybyok",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, Iris. I'll make sure to communicate your feedback to the chef. Thank you for letting me know.",
            "user_response_option_en": "Can you also bring me some water, please?",
            "previous_turn_id": "pstvpdaekdcmwcmk",
            "order": 3,
            "key_phrase_en": "bring me water",
        },
        {
            "id": "mixcwxfgmzljacow",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, Iris. I'll make sure to communicate your feedback to the chef. Thank you for letting me know.",
            "user_response_option_en": "I hope it will be better next time.",
            "previous_turn_id": "pstvpdaekdcmwcmk",
            "order": 3,
            "key_phrase_en": "next time",
        },
        {
            "id": "ibyitwnxedrjtijg",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the dryness, would you like me to replace the chicken for you?",
            "user_response_option_en": "Yes, please replace it.",
            "previous_turn_id": "pvzkmdrhpcrpiqlk",
            "order": 3,
            "key_phrase_en": "Replace it",
        },
        {
            "id": "xmqgphtyinrzrynv",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the dryness, would you like me to replace the chicken for you?",
            "user_response_option_en": "No, it's okay. Just take it off the bill.",
            "previous_turn_id": "pvzkmdrhpcrpiqlk",
            "order": 3,
            "key_phrase_en": "take it off",
        },
        {
            "id": "slrbkbbauvitgtej",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the dryness, would you like me to replace the chicken for you?",
            "user_response_option_en": "Could I have some sauce with it?",
            "previous_turn_id": "pvzkmdrhpcrpiqlk",
            "order": 3,
            "key_phrase_en": "some sauce",
        },
        {
            "id": "ppputdwujchshtmg",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the overcooked rice.",
            "user_response_option_en": "Could you bring me another dish instead?",
            "previous_turn_id": "uaiyejusqcblnopb",
            "order": 3,
            "key_phrase_en": "Another dish",
        },
        {
            "id": "yhysfpbkxzfhfwuh",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the overcooked rice.",
            "user_response_option_en": "Thanks for apologizing, I appreciate it.",
            "previous_turn_id": "uaiyejusqcblnopb",
            "order": 3,
            "key_phrase_en": "I appreciate it",
        },
        {
            "id": "wlgejpcdvlqjfwoy",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the overcooked rice.",
            "user_response_option_en": "Can I speak with the chef about my disappointment?",
            "previous_turn_id": "uaiyejusqcblnopb",
            "order": 3,
            "key_phrase_en": "speak with chef",
        },
        {
            "id": "fagstuewrixcgouw",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that the sauce is too salty. Would you like me to have the chef adjust it?",
            "user_response_option_en": "No, thank you. I don't want to waste food.",
            "previous_turn_id": "pvtxqauvidvpqkch",
            "order": 3,
            "key_phrase_en": "waste food",
        },
        {
            "id": "hdjzxsvqzsmxgdgl",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that the sauce is too salty. Would you like me to have the chef adjust it?",
            "user_response_option_en": "Yes, please. I appreciate your concern.",
            "previous_turn_id": "pvtxqauvidvpqkch",
            "order": 3,
            "key_phrase_en": "appreciate your concern",
        },
        {
            "id": "vjrupukbphmemnei",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I'm sorry to hear that the sauce is too salty. Would you like me to have the chef adjust it?",
            "user_response_option_en": "Maybe, I'll consider it. Thank you for your help.",
            "previous_turn_id": "pvtxqauvidvpqkch",
            "order": 3,
            "key_phrase_en": "Consider it",
        },
        {
            "id": "huijdwjeiwmdwswz",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, I apologize for the lack of flavor. I'll bring some sauce for you right away.",
            "user_response_option_en": "Thank you, I appreciate your quick response and attention.",
            "previous_turn_id": "givihkktaflubrtb",
            "order": 3,
            "key_phrase_en": "Quick response",
        },
        {
            "id": "imiawzntrydrmhdp",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, I apologize for the lack of flavor. I'll bring some sauce for you right away.",
            "user_response_option_en": "Could you please also bring some salt and pepper as well?",
            "previous_turn_id": "givihkktaflubrtb",
            "order": 3,
            "key_phrase_en": "some salt pepper",
        },
        {
            "id": "uepnsvvpqdpkmwuo",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Of course, I apologize for the lack of flavor. I'll bring some sauce for you right away.",
            "user_response_option_en": "Is there any way to make this dish more flavorful?",
            "previous_turn_id": "givihkktaflubrtb",
            "order": 3,
            "key_phrase_en": "More flavorful",
        },
        {
            "id": "oaqbnuiijyceuncs",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the inconvenience, let me have the chef prepare you a new steak to your liking.",
            "user_response_option_en": "Thank you for resolving the issue. I appreciate your help.",
            "previous_turn_id": "heczulkdyeelrybx",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "yjcwvpxrybtcozct",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the inconvenience, let me have the chef prepare you a new steak to your liking.",
            "user_response_option_en": "That would be great, thank you. I hope the next steak is better.",
            "previous_turn_id": "heczulkdyeelrybx",
            "order": 3,
            "key_phrase_en": "That would be great",
        },
        {
            "id": "kucxhtviuhrienot",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "I apologize for the inconvenience, let me have the chef prepare you a new steak to your liking.",
            "user_response_option_en": "Okay, I'll look forward to trying the new steak. Thank you.",
            "previous_turn_id": "heczulkdyeelrybx",
            "order": 3,
            "key_phrase_en": "Look forward to",
        },
        {
            "id": "njnwbgnsryvqvibp",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Sure, here's an example response by a server in this situation: I'm sorry about that, let me take it back and have it reheated for you.",
            "user_response_option_en": "Thank you, please do so.",
            "previous_turn_id": "xmlvzsqnllgvwrio",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "vzsyxgcqrqixemcm",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Sure, here's an example response by a server in this situation: I'm sorry about that, let me take it back and have it reheated for you.",
            "user_response_option_en": "It's okay, I'd rather not wait.",
            "previous_turn_id": "xmlvzsqnllgvwrio",
            "order": 3,
            "key_phrase_en": "I'd rather not",
        },
        {
            "id": "ggrwhnfvcskehzdu",
            "mission_id": "brzoyozrflpkxuqz",
            "ai_conversation_starter_en": "Sure, here's an example response by a server in this situation: I'm sorry about that, let me take it back and have it reheated for you.",
            "user_response_option_en": "Can I have something else instead?",
            "previous_turn_id": "xmlvzsqnllgvwrio",
            "order": 3,
            "key_phrase_en": "Something else instead",
        },
    ],
}

