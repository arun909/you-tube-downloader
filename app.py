from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

# Ensure the downloads directory exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Use yt-dlp to download the video
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save the video to 'downloads' folder
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return jsonify({'message': 'Video downloaded successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to serve the HTML frontend
@app.route('/')
def index():
    return open("index.html").read()


if __name__ == '__main__':
    app.run(debug=True)

