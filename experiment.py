import json
import sys
import time


# run this file with arguments
# python use_separate_prompts.py 0


if len(sys.argv) < 2:
    prompt_num = 0
else:
    prompt_num = str(sys.argv[1])

print("prompt_num:", prompt_num)

with open("prompts.json") as file:
    prompt = json.load(file)

time.sleep(3)

print("prompt:", prompt[int(prompt_num)])
