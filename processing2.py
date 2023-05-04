from nativefriendTopics import scenes

for scene in scenes:
    for scenario in scene["child_scenarios"]:
        new_dict = dict()
        new_dict["scenario_en"] = scenario
        new_dict["scenario_ko"] = " "
        scene["child_scenarios"] = scene["child_scenarios"][1:]
        scene["child_scenarios"].append(new_dict)

print(scenes)
