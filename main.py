from flask import Flask, render_template, request
import whisper
import os

app = Flask(__name__, template_folder='templates')
MODEL = whisper.load_model('base')

app.config['UPLOAD_FOLDER'] = './audios'


@app.route('/upload')
def render_upload():
    return render_template('./upload.html')


@app.route('/uploader', methods=['POST'])
def upload_audio():
    content = request.files['audio'].read()

    with open("audio.m4a", "wb+") as f:
        f.write(content)

    route = os.getcwd() + "\\audio.m4a"
    if os.path.exists(route):
        result = MODEL.transcribe("audio.m4a")

        # print the recognized text
        return result["text"]
    return f.content_type


if __name__ == '__main__':
    app.run(debug=True)
