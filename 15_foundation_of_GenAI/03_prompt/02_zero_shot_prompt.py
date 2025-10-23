# Zero Shot Propmpting Example
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Propmpting : Directly giving instruction to the model without any examples
SYSTEM_PROMPT = "You answer only coding related questions. Do not answer anything else. Your name is JARVIS , If user asks something other than coding just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # system propmt to set the behavior of the assistant
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey can you help me with a + b whole squared?"
        }
    ]
)

print(response.choices[0].message.content)