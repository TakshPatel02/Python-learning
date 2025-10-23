from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCG0X5mFgxliAxWD-LqsuvU7DA2ttvNnxo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# For validating the input text as a question
def is_question(text):
    question_keywords = [
        "what", "who", "why", "when", "where", "how",
        "tell", "explain", "define", "meaning", "describe"
    ]
    return any(word in text for word in question_keywords)

# For generating response from Gemini model
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            # system propmt to set the behavior of the assistant
            {"role": "system", "content": "You are a helpful assistant. Answer only in 5-10 words. And if the question is not related to you then politely refuse to answer."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
