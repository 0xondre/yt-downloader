from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def get_file():
    if request.method == 'POST':
        url = request.form.get('text')
        if url:
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': './audio.mp3',
                    'noplaylist': True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                audio_path = 'audio.mp3'

                return send_file(audio_path,as_attachment=True,mimetype='audio/mp3')
            except Exception:
                return 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6868)