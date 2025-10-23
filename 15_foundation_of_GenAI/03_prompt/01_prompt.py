from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCG0X5mFgxliAxWD-LqsuvU7DA2ttvNnxo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        # system propmt to set the behavior of the assistant
        {"role": "system", "content": "You are a math expert, answer only and only math related questions. That if the query is not math related, respond with Sorry I can't help with that."},
        {
            "role": "user",
            "content": "Hey can you help me with a + b whole squared?"
        }
    ]
)

print(response.choices[0].message.content)