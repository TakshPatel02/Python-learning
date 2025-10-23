import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4")

text = "Hello, My name is Taksh Patel."

tokens = encoder.encode(text)

# Tokens:  [9906, 11, 3092, 836, 374, 34390, 939, 63855, 13]
print("Tokens: " , tokens)

encoded_text = encoder.decode(tokens)

# Encoded Text:  Hello, My name is Taksh Patel.
print("Encoded Text: ", encoded_text)