from flask import Flask, request, jsonify
import base64
import requests
import json

app = Flask(__name__)

@app.route('/call-model', methods=['POST'])
def call_model():
    image_url = 'your_image_path.jpg'  # 替换成你的图片路径
    text_input = request.json.get('textInput')
    
    # 调用你的 apii 函数
    response = apii(image_url, text_input)
    
    return jsonify(response)

def apii(image_path, text_input):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        
    url = 'https://idealab.alibaba-inc.com/aigc/v1/multimodalAskByUrl'
    headers = {
        'Content-Type': 'application/json',
        'X-AK': '8c865c363aafd67f68f6ddedc70a2b12',  # 替换成你的 X-AK
    }
    data = {
        "model": "gpt-4-vision-preview",
        "prompt": text_input,
        "mediaEntities": [
            {
                "content": f"data:image/jpeg;base64,{base64_string}",
                "level": "low"
            }
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return json.loads(response.text)

if __name__ == '__main__':
    app.run(debug=True)
