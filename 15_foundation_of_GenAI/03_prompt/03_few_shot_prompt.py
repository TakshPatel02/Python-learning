# Few Shot Propmpting Example
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Propmpting : Provinding few examples to the model to guide its behavior.This increases the accuracy of the model in generating desired responses. 
SYSTEM_PROMPT = """
You answer only coding related questions. Do not answer anything else. Your name is JARVIS , If user asks something other than coding just say sorry.

Rule:
- Strictly answer in JSON format.

Output Format:
{
"code": "Write your code here but just like a code snippet in vs code editor",
"isCodingRelated": boolean
}

Examples : 
Q: Can you explain whole square of (a+b)?
A: Sorry , i can only answer coding related questions.

Q: write a python function to calculate two numbers sum
A: def sum(a,b):
        return a+b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # system propmt to set the behavior of the assistant
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey can you help me to write a python fucntion to check if a number is prime or not?"
        }
    ]
)

print(response.choices[0].message.content)