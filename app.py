from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        file_path = video_stream.download()
        
        return send_file(file_path, as_attachment=True, attachment_filename=yt.title + '.mp4')

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

