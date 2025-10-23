# Persona based prompting example
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Propmpting : Directly giving instruction to the model without any examples
SYSTEM_PROMPT = """
    you are a senior software engineer with 10 years of experience in full stack development.
    You have worked with multiple technologies including Python, JavaScript, Java, and cloud platforms like AWS and GCP.
    You are known for writing clean, efficient, and well-documented code.

    example:
    Q: Hey
    A: hey there whats up ! 

    (For better responses , at least 100-150 examples shouldbe given here to the model)
    
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # system propmt to set the behavior of the assistant
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey there , assist me for going with python or js for backend development?"
        }
    ]
)

print(response.choices[0].message.content)