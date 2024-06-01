import requests
from openai import OpenAI
import time

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
client = OpenAI(api_key="XXXXX")


PROMPT = "A Doctor"

start_time = time.time()

for i in range(0,1):
    response = client.images.generate(
    model="dall-e-3",
    prompt=PROMPT,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    
    # Send a GET request to download the image data
    image_data = requests.get(i).content

    # Specify the file path where you want to save the image
    file_path = f'doctor/doctor_{image_url}.jpg'

    # Write the image data to the specified file
    with open(file_path, "wb") as f:
        f.write(image_data)


print(" Total time --- %s seconds ---" % (time.time() - start_time))





