from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "Act as a recipe/food guide"},
    {"role": "user", "content": "how are you doing!"}
  ]
)

message = response.choices[0].message.content
