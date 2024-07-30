import requests

# API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-small-stage1"
# headers = {"Authorization": "Bearer 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"}
#
# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()
#
# output = query("image_2.jpg")
# print(output)

import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def chunk_text(text, chunk_size):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

# Read text from a file
with open('extracted_text.txt', 'r') as file:
    input_text = file.read().replace('\n', ' ')


batch_size = 600
summarized_text = []

for chunk in chunk_text(input_text, batch_size):
    output = query({
        "inputs": chunk
    })

    if 'error' in output:
        print(f"Error: {output['error']}")
    else:
        try:
            summary = output[0]['summary_text']
            summarized_text.append(summary)
        except KeyError as e:
            print(f"KeyError: {e}")
            print(f"Full output: {output}")

final_summary = ' '.join(summarized_text)
print(final_summary)
