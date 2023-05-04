clinic_content = [
    {
        "parent_scene": "Making a reservation",
        "child_scenarios": [
            "Asking if it's possible to book an appointment on a specific date",
            "Requesting a doctor who speaks my native language Korean",
            "You have a minor injury and need to schedule an appointment to have it checked out.",
            "You have been feeling unwell and want to see a doctor as soon as possible.",
            "Requesting an email confirmation of the appointment in case of language barriers during the phone call",
            "Asking if there are any documents or forms you need to bring to the appointment",
            "Inquiring if the clinic accepts your travel insurance",
        ],
        "ai_persona": "Receptionist",
        "user_persona": "Patient",
    },
    {
        "parent_scene": "Reporting symptoms",
        "child_scenarios": [
            "You have a fever and chills and are feeling very weak.",
            "You have a persistent cough and are having trouble breathing.",
            "You have a severe headache and are experiencing vision changes.",
            "You have been experiencing stomach pain and vomiting.",
            "You have been experiencing joint pain and swelling.",
            "You have an ear infection and are experiencing severe pain and discharge.",
            "You have a cut that is not healing properly and is becoming infected.",
            "Asking for clarification or further explanation",
        ],
        "ai_persona": "Healthcare provider",
        "user_persona": "Patient",
    },
    {
        "parent_scene": "Receiving the treatment",
        "child_scenarios": [
            "Asking questions about the treatment process",
            "Expressing discomfort or pain during the treatment",
            "Inquiring about potential side effects or complications of the treatment",
            "You need stitches for a cut.",
            "You are given antihistamines for an allergic reaction.",
            "You need to undergo a minor surgical procedure.",
        ],
        "ai_persona": "Healthcare provider",
        "user_persona": "Patient",
    },
    {
        "parent_scene": "Getting a medication prescription",
        "child_scenarios": [
            "You need a prescription for antibiotics to treat an infection.",
            "You need a prescription for pain medication to manage chronic pain.",
            "You need a prescription for an EpiPen to manage severe allergies.",
            "Asking questions about the medication",
            "Confirming dosage and frequency",
            "Discussing potential side effects or interactions",
            "Arranging for refills or follow-up appointments",
        ],
        "ai_persona": "Pharmacist",
        "user_persona": "Patient",
    },
]

clinic_prompt = {
    "ai_conversation_starter_prompt": "",
    "ai_response_prompt": "",
    "user_response_rpompt": "",
}
