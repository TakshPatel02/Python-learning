from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCG0X5mFgxliAxWD-LqsuvU7DA2ttvNnxo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works in a few words"
        }
    ]
)

print(response.choices[0].message.content)