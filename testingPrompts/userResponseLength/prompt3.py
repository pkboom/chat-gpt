"""
Prompt:
    system_content = f"You're an English teacher that helps non-native speakers learn English through role-playing."
    assistant_content = f"Here's the previous conversation between a {self.ai_persona} and a {self.user_persona} named Iris Kim: \
        \n\t - {previous_conversation_str}"
    user_content = f'The {self.user_persona} named Iris Kim is {child_scenario} while {parent_scene}. \
        After the {self.ai_persona} says "{previous_conversation[-1]}", give me 3 different ways Iris Kim might respond to the server here. \
        Each response should be different but all should be appropriate to the situation, and help facilitate the prcoess of {child_scenario}. \
        Since the script is for non-native speakers, avoid having complicated sentences and keep each resposne under 14 words. \
        However, I want each response to include a unique key phrase, commonly used by natives, that would be useful to learn for non-native speakers.\
        Return a numbered list and don\'t say anything else.'
"""

response = {
    "id": "tjgqrrynoxmjgisn",
    "title": "Making a complaint about bad food",
    "order": 5,
    "turns": [
        {
            "id": "utyapnlmtwwowhca",
            "ai_conversation_starter_en": "Excuse me, sir, is everything okay with your meal?",
            "user_response_option_en": "No, it's not good. Something's wrong with the taste.",
            "mission_id": "tjgqrrynoxmjgisn",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "tgrzgrqivuxjisaj",
            "key_phrase_en": "Something's wrong",
        },
        {
            "id": "qxtvkotpjndbuqok",
            "ai_conversation_starter_en": "Excuse me, sir, is everything okay with your meal?",
            "user_response_option_en": "I'm sorry, but this isn't what I ordered. It's not edible.",
            "mission_id": "tjgqrrynoxmjgisn",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "kjstwcejgmuqdsha",
            "key_phrase_en": "Not edible",
        },
        {
            "id": "yitncwhxcajigjqn",
            "ai_conversation_starter_en": "Excuse me, sir, is everything okay with your meal?",
            "user_response_option_en": "I think this meal may have gone bad. It smells off.",
            "mission_id": "tjgqrrynoxmjgisn",
            "previous_turn_id": "STARTING_NODE",
            "order": 1,
            "next_turn_id": "qsduxdnhbutlkyen",
            "key_phrase_en": "smells off",
        },
        {
            "id": "tnqwmmzzgjtdubmd",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that. Would you like me to bring the manager over?",
            "user_response_option_en": "Yes, please. I'd like to get a replacement dish. Thank you.",
            "previous_turn_id": "utyapnlmtwwowhca",
            "order": 2,
            "next_turn_id": "lydmgfqcwuseaenj",
            "key_phrase_en": "Replacement dish",
        },
        {
            "id": "bswtrrrlsjteysjs",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that. Would you like me to bring the manager over?",
            "user_response_option_en": "Could you bring me the menu? I want to order something else.",
            "previous_turn_id": "utyapnlmtwwowhca",
            "order": 2,
            "next_turn_id": "kdieblnpneaewkuw",
            "key_phrase_en": "bring me menu",
        },
        {
            "id": "tgrzgrqivuxjisaj",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that. Would you like me to bring the manager over?",
            "user_response_option_en": "Can you let the chef know there's a problem with the seasoning?",
            "previous_turn_id": "utyapnlmtwwowhca",
            "order": 2,
            "next_turn_id": "zlktnttjdiikrzjg",
            "key_phrase_en": "Problem with seasoning",
        },
        {
            "id": "phixzeltyrossezg",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm very sorry to hear that, ma'am. Let me see what I can do to fix the situation.",
            "user_response_option_en": 'Can I get a new dish?" - Requesting a replacement.',
            "previous_turn_id": "qxtvkotpjndbuqok",
            "order": 2,
            "next_turn_id": "pnuknoizeztxwoeu",
            "key_phrase_en": "replacement dish",
        },
        {
            "id": "vkzdfkicfoqyjzew",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm very sorry to hear that, ma'am. Let me see what I can do to fix the situation.",
            "user_response_option_en": 'Can I speak to the manager?" - Asking to escalate the situation.',
            "previous_turn_id": "qxtvkotpjndbuqok",
            "order": 2,
            "next_turn_id": "pxbdjlictmbvmaxd",
            "key_phrase_en": "Speak to manager",
        },
        {
            "id": "kjstwcejgmuqdsha",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm very sorry to hear that, ma'am. Let me see what I can do to fix the situation.",
            "user_response_option_en": 'Can you describe the dish?" - Asking for clarification to avoid future issues.',
            "previous_turn_id": "qxtvkotpjndbuqok",
            "order": 2,
            "next_turn_id": "jpnbdpmgtberjndl",
            "key_phrase_en": "Describe the dish",
        },
        {
            "id": "euakqdxntzcvyvuq",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that, let me grab the manager to help you with that.",
            "user_response_option_en": "Please hurry. I don't feel well.\" (Indicating urgency)",
            "previous_turn_id": "yitncwhxcajigjqn",
            "order": 2,
            "next_turn_id": "zfejggiyxovlhgpc",
            "key_phrase_en": "Please hurry",
        },
        {
            "id": "faokkmustmokugrb",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that, let me grab the manager to help you with that.",
            "user_response_option_en": 'Can I get a to-go box?" (Wanting to take the meal home for further examination)',
            "previous_turn_id": "yitncwhxcajigjqn",
            "order": 2,
            "next_turn_id": "jjjwurqhwesbduxm",
            "key_phrase_en": "to-go box",
        },
        {
            "id": "qsduxdnhbutlkyen",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm so sorry to hear that, let me grab the manager to help you with that.",
            "user_response_option_en": 'Can I see the kitchen, please?" (Curious to see how food is prepared)',
            "previous_turn_id": "yitncwhxcajigjqn",
            "order": 2,
            "next_turn_id": "nxkdxhzwsvghngzu",
            "key_phrase_en": "kitchen, please",
        },
        {
            "id": "osvwzbqqradddqvn",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I am sorry that your meal was not up to your expectations. What would you like as a replacement dish?",
            "user_response_option_en": "Can I try the salmon instead? It was recommended by a friend.",
            "previous_turn_id": "tnqwmmzzgjtdubmd",
            "order": 3,
            "key_phrase_en": "Recommended by friend",
        },
        {
            "id": "kvyjuwrcztpjxgrp",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I am sorry that your meal was not up to your expectations. What would you like as a replacement dish?",
            "user_response_option_en": "Could I see the menu again? Maybe a new item would be better.",
            "previous_turn_id": "tnqwmmzzgjtdubmd",
            "order": 3,
            "key_phrase_en": "See the menu",
        },
        {
            "id": "lydmgfqcwuseaenj",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I am sorry that your meal was not up to your expectations. What would you like as a replacement dish?",
            "user_response_option_en": "Is it possible to speak with the chef? Maybe they could help.",
            "previous_turn_id": "tnqwmmzzgjtdubmd",
            "order": 3,
            "key_phrase_en": "speak with chef",
        },
        {
            "id": "neqqnsciebafeqkp",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry that you didn't enjoy your meal. I'll bring you a new menu right away.",
            "user_response_option_en": 'Thank you, I appreciate that." ',
            "previous_turn_id": "bswtrrrlsjteysjs",
            "order": 3,
            "key_phrase_en": "appreciate that",
        },
        {
            "id": "hgabhsshrvlfgzac",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry that you didn't enjoy your meal. I'll bring you a new menu right away.",
            "user_response_option_en": 'Can you tell me what the chef recommends?" ',
            "previous_turn_id": "bswtrrrlsjteysjs",
            "order": 3,
            "key_phrase_en": "Chef recommends",
        },
        {
            "id": "kdieblnpneaewkuw",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry that you didn't enjoy your meal. I'll bring you a new menu right away.",
            "user_response_option_en": "Do you have any vegetarian options?",
            "previous_turn_id": "bswtrrrlsjteysjs",
            "order": 3,
            "key_phrase_en": "Vegetarian options",
        },
        {
            "id": "ltulzabtnantbbeo",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Certainly, I will let the chef know about the issue with the seasoning right away.",
            "user_response_option_en": 'Can I speak to the manager, please?" (asking for higher authority)',
            "previous_turn_id": "tgrzgrqivuxjisaj",
            "order": 3,
            "key_phrase_en": "speak to manager",
        },
        {
            "id": "nlinhkztmogmajxt",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Certainly, I will let the chef know about the issue with the seasoning right away.",
            "user_response_option_en": 'Could you recommend something else?" (suggesting an alternative)',
            "previous_turn_id": "tgrzgrqivuxjisaj",
            "order": 3,
            "key_phrase_en": "Recommend something else",
        },
        {
            "id": "zlktnttjdiikrzjg",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Certainly, I will let the chef know about the issue with the seasoning right away.",
            "user_response_option_en": 'Is it possible to get a refund?" (asking for the money back)',
            "previous_turn_id": "tgrzgrqivuxjisaj",
            "order": 3,
            "key_phrase_en": "get a refund",
        },
        {
            "id": "eqjasuimllapdqlp",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I apologize for the inconvenience. Let me bring you another dish right away.",
            "user_response_option_en": 'Thank you, I appreciate your help." - Expressing gratitude and accepting the offer. ',
            "previous_turn_id": "phixzeltyrossezg",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "hslvafewxetirqix",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I apologize for the inconvenience. Let me bring you another dish right away.",
            "user_response_option_en": 'Could I have a suggestion for another dish?" - Asking for a recommendation.',
            "previous_turn_id": "phixzeltyrossezg",
            "order": 3,
            "key_phrase_en": "Another dish",
        },
        {
            "id": "pnuknoizeztxwoeu",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I apologize for the inconvenience. Let me bring you another dish right away.",
            "user_response_option_en": 'Would it be possible to speak with the manager, please?" - Requesting to talk to someone in charge.',
            "previous_turn_id": "phixzeltyrossezg",
            "order": 3,
            "key_phrase_en": "speak with manager",
        },
        {
            "id": "tgyhfhgmbilwxtmy",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Absolutely, I'll go get my manager for you right away.",
            "user_response_option_en": 'Thank you, I appreciate it." - Showing gratitude for help.',
            "previous_turn_id": "vkzdfkicfoqyjzew",
            "order": 3,
            "key_phrase_en": "appreciate it",
        },
        {
            "id": "euvyyvfupeamalcx",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Absolutely, I'll go get my manager for you right away.",
            "user_response_option_en": 'I hope we can find a solution." - Expressing hope for a resolution.',
            "previous_turn_id": "vkzdfkicfoqyjzew",
            "order": 3,
            "key_phrase_en": "Find a solution",
        },
        {
            "id": "pxbdjlictmbvmaxd",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Absolutely, I'll go get my manager for you right away.",
            "user_response_option_en": 'Can I get a refund or a different dish?" - Asking for options to fix the problem.',
            "previous_turn_id": "vkzdfkicfoqyjzew",
            "order": 3,
            "key_phrase_en": "refund options",
        },
        {
            "id": "uknxuwajaiupflyo",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Sure, I understand. The dish you ordered was the chicken Alfredo pasta with a creamy garlic sauce, grilled chicken pieces, and parmesan cheese. Does that description match what you were expecting?",
            "user_response_option_en": "No, that doesn't sound right. Can I show you what I received? - Asking to physically show the dish to the server to clarify the issue.",
            "previous_turn_id": "kjstwcejgmuqdsha",
            "order": 3,
            "key_phrase_en": "physically show dish",
        },
        {
            "id": "zrgzawgpldrhittw",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Sure, I understand. The dish you ordered was the chicken Alfredo pasta with a creamy garlic sauce, grilled chicken pieces, and parmesan cheese. Does that description match what you were expecting?",
            "user_response_option_en": "",
            "previous_turn_id": "kjstwcejgmuqdsha",
            "order": 3,
            "key_phrase_en": "None",
        },
        {
            "id": "leafbifrwlsvqkhf",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Sure, I understand. The dish you ordered was the chicken Alfredo pasta with a creamy garlic sauce, grilled chicken pieces, and parmesan cheese. Does that description match what you were expecting?",
            "user_response_option_en": "I'm sorry, but the chicken doesn't taste fresh. Can you replace it?\" - Politely asking for a replacement of the chicken instead of the entire dish.",
            "previous_turn_id": "kjstwcejgmuqdsha",
            "order": 3,
            "key_phrase_en": "Replace the chicken",
        },
        {
            "id": "sbdbsziumqhpsjyu",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Sure, I understand. The dish you ordered was the chicken Alfredo pasta with a creamy garlic sauce, grilled chicken pieces, and parmesan cheese. Does that description match what you were expecting?",
            "user_response_option_en": "",
            "previous_turn_id": "kjstwcejgmuqdsha",
            "order": 3,
            "key_phrase_en": "None",
        },
        {
            "id": "jpnbdpmgtberjndl",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Sure, I understand. The dish you ordered was the chicken Alfredo pasta with a creamy garlic sauce, grilled chicken pieces, and parmesan cheese. Does that description match what you were expecting?",
            "user_response_option_en": "The sauce is too salty, and there's too little chicken in it.\" - Mentioning specific issues with the dish to help the server address the problem.",
            "previous_turn_id": "kjstwcejgmuqdsha",
            "order": 3,
            "key_phrase_en": "salty sauce",
        },
        {
            "id": "xxzqosnojlazapoh",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry for the inconvenience, let me take your plate and get you a new meal right away.",
            "user_response_option_en": 'Thank you, I appreciate your help." (Expressing gratitude)',
            "previous_turn_id": "euakqdxntzcvyvuq",
            "order": 3,
            "key_phrase_en": "Thank you",
        },
        {
            "id": "mpukwfndpbzdmdfs",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry for the inconvenience, let me take your plate and get you a new meal right away.",
            "user_response_option_en": 'Could you also speak with the chef, please?" (Asking for extra assistance)',
            "previous_turn_id": "euakqdxntzcvyvuq",
            "order": 3,
            "key_phrase_en": "speak with chef",
        },
        {
            "id": "zfejggiyxovlhgpc",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry for the inconvenience, let me take your plate and get you a new meal right away.",
            "user_response_option_en": 'I hope the next dish will be better." (Remaining optimistic)',
            "previous_turn_id": "euakqdxntzcvyvuq",
            "order": 3,
            "key_phrase_en": "next dish better",
        },
        {
            "id": "syqtqwodkjajcngz",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Of course, would you like me to pack up the rest of your meal for you?",
            "user_response_option_en": "No thanks, I want the restaurant to take responsibility.",
            "previous_turn_id": "faokkmustmokugrb",
            "order": 3,
            "key_phrase_en": "Take responsibility",
        },
        {
            "id": "wgeeeokntawnqtsl",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Of course, would you like me to pack up the rest of your meal for you?",
            "user_response_option_en": "Yes, please. I'd like to take a closer look at home.",
            "previous_turn_id": "faokkmustmokugrb",
            "order": 3,
            "key_phrase_en": "Closer look home",
        },
        {
            "id": "jjjwurqhwesbduxm",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "Of course, would you like me to pack up the rest of your meal for you?",
            "user_response_option_en": "Could I also talk to the manager before I go? Thank you.",
            "previous_turn_id": "faokkmustmokugrb",
            "order": 3,
            "key_phrase_en": "Talk to manager",
        },
        {
            "id": "zvptrhmfoatwiysf",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry, Iris, but it's against our policy to let guests into the kitchen for safety and health reasons.",
            "user_response_option_en": "Can you ask the chef to come speak to me about it?",
            "previous_turn_id": "qsduxdnhbutlkyen",
            "order": 3,
            "key_phrase_en": "Ask the chef",
        },
        {
            "id": "xclulhskhlviosph",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry, Iris, but it's against our policy to let guests into the kitchen for safety and health reasons.",
            "user_response_option_en": "May I have a different dish instead, please?",
            "previous_turn_id": "qsduxdnhbutlkyen",
            "order": 3,
            "key_phrase_en": "different dish please",
        },
        {
            "id": "nxkdxhzwsvghngzu",
            "mission_id": "tjgqrrynoxmjgisn",
            "ai_conversation_starter_en": "I'm sorry, Iris, but it's against our policy to let guests into the kitchen for safety and health reasons.",
            "user_response_option_en": "How can we resolve this issue, can I speak to a manager?",
            "previous_turn_id": "qsduxdnhbutlkyen",
            "order": 3,
            "key_phrase_en": "speak to manager",
        },
    ],
}

