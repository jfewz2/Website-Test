from flask import Flask, request, send_file, render_template
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Template.html')

@app.route('/download', methods=['POST'])
def download_video():
    youtube_url = request.form['youtube_url']
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        download_path = stream.download()
        return send_file(download_path, as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
