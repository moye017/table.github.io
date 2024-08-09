import requests
import json
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string


def apii(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    url = 'https://idealab.alibaba-inc.com/aigc/v1/multimodalAskByUrl'
    headers = {
        'Content-Type': 'application/json',
        'X-AK': '8c865c363aafd67f68f6ddedc70a2b12',
    }
    data = {
        "model": "gpt-4-vision-preview",
        "prompt": "这是什么图片",
        "mediaEntities": [
            {
                "content": f"data:image/jpeg;base64,{base64_string}",
                "level": "low"
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.text)