# Chain of Thought prompting example
from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyCG0X5mFgxliAxWD-LqsuvU7DA2ttvNnxo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """"
    You're an expert AI assistant in resolving user queries using chain of thought prompting.
    You work on START , PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly answer in JSON format.
    - Only run one step at a time. First START, then PLAN steps and finally OUTPUT.
    - The sequence of steps is START (where user gives input) , PLAN (that can be multiple times) and finally OUTPUT (which is going to be displayed to the user).

    Output Format:
    {
    "step": "START/PLAN/OUTPUT",
    "content": "string"
    }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        # system propmt to set the behavior of the assistant
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Hey , wirte a code to sum of n numbers in js."
        },
        {"role": "assistant" , "content": json.dumps(
            {
                "step": "START",
                "content": "User wants a JavaScript code snippet to calculate the sum of 'n' numbers."
            },
        )},
        {"role": "assistant" , "content": json.dumps(
            {
                "step": "PLAN",
                "content": "Define a JavaScript function that takes a number 'n' as input."
            }
        )},
        {"role": "assistant" , "content": json.dumps(
            {
                "step": "PLAN", 
                "content": "Inside the function, use a loop (e.g., for loop) to iterate from 1 to 'n'."
            }
        )},
        {"role": "assistant" , "content": json.dumps(
            {
                "step": "PLAN",
                "content": "Initialize a variable to store the sum, starting from 0."
            }
        )},
        {"role": "assistant" , "content": json.dumps(
            {"step": "PLAN", "content": "Inside the loop, add the current iteration number to the sum variable."}
        )},
        {"role": "assistant" , "content": json.dumps(
            {"step": "PLAN", "content": "After the loop finishes, return the accumulated sum."}
        )},
    ]
)

print(response.choices[0].message.content)