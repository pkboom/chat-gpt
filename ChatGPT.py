# # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# import openai
# import os
# from dotenv import load_dotenv

# from airportTopics import airport_prompts

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# CONVERSATION_STARTER = 1
# AI_RESPONSE = 2


# class ChatGPT:
#     def __init__(self, location, ai_persona, user_persona):
#         self.location = location
#         self.ai_persona = ai_persona
#         self.user_persona = user_persona

#     def openai_reply(
#         self,
#         system_content,
#         assistant_content,
#         user_content,
#         temperature=1,
#         frequency_penalty=0,
#     ):
#         messages = [
#             {"role": "system", "content": system_content},
#             {"role": "assistant", "content": assistant_content},
#             {"role": "user", "content": user_content},
#         ]

#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages,
#             temperature=temperature,
#             frequency_penalty=frequency_penalty,
#         )
#         return response

#     def generate_ai_response(
#         self, request_type, parent_scene, child_scenario, previous_conversation=[]
#     ):
#         system_content, assistant_content, user_content = "", "", ""
#         if previous_conversation:
#             previous_conversation_str = "\n\t - ".join(previous_conversation)

#         # generates the conversation starter for each dialogue
#         if request_type == CONVERSATION_STARTER:
#             system_content = f"You're a {self.ai_persona} at a {parent_scene} at an {self.location} who is talking to a non-native {self.user_persona}."
#             assistant_content = f"Scenario: {parent_scene} at {child_scenario}."
#             user_content = f'Give me an example of what the {self.ai_persona} might say to {self.user_persona} that will lead to this scenario. \
#                             Don\'t include further explanation, and provide the response in the form of: "{self.ai_persona}: <text>."'

#         elif request_type == AI_RESPONSE:
#             system_content = f"You're a {self.ai_persona} at a {parent_scene} at an {self.location} who is talking to a non-native {self.user_persona}."
#             assistant_content = f"Here's the previous conversation between a {self.ai_persona} and {self.user_persona}: \
#             \n\t - {previous_conversation_str}"
#             user_content = f'A {self.user_persona} is {child_scenario} at {parent_scene}. \
#                 After the {self.user_persona} says "{previous_conversation[-1]}", give me an example of what you might say to the {self.user_persona} here. \
#                 The response should be appropriate to the situation and help facilitate the prcoess of {child_scenario}. \
#                 Since Iris is a non-native speaker, don\'t use too complicated phrases. Keep the response under 25 words. \
#                 Don\'t include further explanation, and provide the response in the form of: "{self.ai_persona}: <text>."'

#         res = self.openai_reply(system_content, assistant_content, user_content)

#         reply = res["choices"][0]["message"]["content"]
#         reply = reply.split(f"{self.ai_persona}: ")[-1]
#         reply = reply.strip().replace('"', "")
#         reply = reply.strip().replace("\n", "")

#         return reply

#     def generate_recommendations(
#         self, parent_scene, child_scenario, previous_conversation
#     ):
#         system_content, assistant_content, user_content = "", "", ""

#         if previous_conversation:
#             previous_conversation_str = "\n\t - ".join(previous_conversation)

#         system_content = f"You're an English teacher that helps non-native speakers learn English through a role-play."
#         assistant_content = f"Here's the previous conversation between a {self.ai_persona} and a {self.user_persona} named Iris Kim: \
#             \n\t - {previous_conversation_str}"
#         user_content = f"The {self.user_persona} is {child_scenario} while {parent_scene}. \
#             To the {self.ai_persona} saying \"{previous_conversation[-1]}\", give me 3 different ways that the {self.user_persona} Iris might respond. \
#             Each response should be appropriate to the situation, and help facilitate the prcoess of {child_scenario}. \
#             Since Iris is a non-native speaker, avoid having complicated sentences. Each response should be ideally one sentence, and under 15 words. \
#             However, I want each response to include phrase that would be useful to learn for non-native speakers. \
#             Don't include further explanation, and provide the response in the form of '1. {self.user_persona}: <text>', '2. {self.user_persona}:  <text>', '3. {self.user_persona}:  <text>'"

#         res = self.openai_reply(system_content, assistant_content, user_content)
#         reply = res["choices"][0]["message"]["content"]

#         return reply

#     def summarize(self, full_sentences, previous_conversation):
#         full_sentences = "\n\t - ".join(full_sentences)
#         previous_conversation = "\n\t - ".join(previous_conversation)

#         system_content = ""
#         assistant_content = f"The {self.user_persona} is talking to {self.ai_persona} at a {self.location}. \
#                 Here's the previous conversation: \n\t - {previous_conversation}"
#         user_content = f"For each of the following sentences, summarize its context into less than 5 words. \n\t - {full_sentences} \n \
#             Use gerund instead of verbs. \
#             Provide them as a numbered list and don't say anything else."

#         res = self.openai_reply(system_content, assistant_content, user_content)
#         reply = res["choices"][0]["message"]["content"]

#         return reply

#     def summarize_sentence(self, ai_sentence, user_sentence):
#         system_content = ""
#         assistant_content = f"{self.ai_persona}: {ai_sentence}"
#         user_content = f'Summarize {self.user_persona}\'s sentence: "{user_sentence}" into less than 4 words. Use gerund isntead of verbs.'

#         res = self.openai_reply(system_content, assistant_content, user_content)
#         reply = res["choices"][0]["message"]["content"]
#         reply = reply.strip('"').removesuffix('"')
#         reply = reply.strip('"').removesuffix(".")

#         return reply

    def extract_keyphrase(self, user_content):
#         system_content = "You're an English tutor that teaches native expressions to non-native speakers."
#         system_content = ""
#         assistant_content = ""
#         user_content = f'Extract one word or a phrase(consisting of 1-3 words) in the following text that is commonly used by native English speakers, that would be useful to learn for non-native speakers. \
#             Don\'t include a phrase that is too complex or too trivial. If there is no appropriate word or phrase, simply say "None". \
#             Extract the phrase word-by-word, case-sensitive, in the exact order as shown in the text (it needs to be a span that can be represented with a starting index and an ending index). \
#             For example, given the expression "I\'m not sure if my name is spelled correctly on the reservation.", "spelled correctly" is a wrong answer, and the key phrase should be "correctly spelled". \
#             Give me the key phrase and don\'t say anything else. \
#             \n\t- "{expression}"'

#         res = self.openai_reply(system_content, assistant_content, user_content, 0, 0.8)
#         reply = res["choices"][0]["message"]["content"]
#         reply = reply.strip('"')
#         reply = reply.strip()
#         reply = reply.removesuffix(".")
#         reply = reply.split(" (")[0]
#         reply = reply.strip('"')
#         reply = reply.split(", ")[0]

#         return reply
