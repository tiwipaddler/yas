import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
response = client.images.generate(
    model="dall-e-3",
    prompt=input("Describe what you are after:"),
    size="1024x1024",
    n=1,
    style="vivid"
 )
print(response.data[0].url)