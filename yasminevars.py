import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
response = client.images.create_variation(
  image=open("yasroom.png", "rb"),
  n=1,
  size="1024x1024"
)
print(f"Variation: {response.data[0].url}")