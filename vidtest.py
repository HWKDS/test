import os
from openai import OpenAI
from flask import Flask, request, render_template
client = OpenAI(
  api_key="YOUR API KEY",
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    picUrl = request.form['user_input']
    response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[
        {
          "role": "system", "content": "You are a medical assistant, skilled in explaining complex concepts with creative flair.",
          "role": "user",
          "content": [
            {"type": "text", "text": "What’s in this image?, explain in 2 words"},
            {
              "type": "image_url",
              "image_url": {
                "url": picUrl,},},],}],
      max_tokens=150,)
    return f'{response.choices[0].message.content}'

if __name__ == '__main__':
    app.run(debug=True, port="8080")
