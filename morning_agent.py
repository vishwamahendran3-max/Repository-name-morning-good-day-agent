from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a short and friendly GOOD DAY message for me."
)

print(response.output_text)
