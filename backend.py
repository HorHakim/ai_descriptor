import os
from dotenv import load_dotenv

import base64

from mistralai import Mistral



load_dotenv()

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None


def read_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        content = file.read()
    return content


def describe_image(image_path):
    base64_image = encode_image(image_path)


    api_key = os.environ["MISTRAL_KEY"]
    model = "pixtral-12b-2409"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {"role" : "system",
            "content" : read_file(file_path="context.txt"),

            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": read_file(file_path="prompt.txt")
                    },
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}" 
                    }
                ]
            }
        ]
    )

    return chat_response.choices[0].message.content

