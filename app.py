from flask import Flask, request, jsonify
import time
import os
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask YouTube Transcript API is running!"})

@app.route("/get_transcript", methods=["GET"])
def get_transcript():
    try:
        video_url = request.args.get("video_url")
        if not video_url:
            return jsonify({"error": "Missing video_url parameter"}), 400
        
        # Extract video ID
        video_id = video_url.split("v=")[1].split("&")[0]
        
        time.sleep(8)

        # Fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Convert to plain text
        transcript_text = "\n".join([entry['text'] for entry in transcript])

        return jsonify({"video_id": video_id, "transcript": transcript_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway ka default port use karega
    app.run(host="0.0.0.0", port=port)