import requests
from gtts import gTTS
import os
from flask import Flask, request, send_file, jsonify, after_this_request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def text_to_speech(text):
    
    tts = gTTS(text=text, lang="en", slow=False)
    filename = "output.mp3"
    tts.save(filename)
    return filename  # Return the file name

@app.route("/api", methods=['POST'])
def convert_text_audio():
    """Receive text from Vue.js, convert to speech, and return as an audio file."""
    data = request.json
    text = data.get('text', "").strip()

    if not text:
        return jsonify({"error": "Please enter some valid text"}), 400  # Return HTTP 400 for invalid input

    filename = text_to_speech(text)  # Generate the speech file

    @after_this_request
    def remove_file(response):
        """Delete the file after sending it."""
        try:
            os.remove(filename)  
            print(f"Deleted: {filename}") 
        except Exception as e:
            print(f"Error deleting file: {e}")  
        return response

    return send_file(filename, mimetype="audio/mpeg", as_attachment=False)  # Send file response

if __name__ == "__main__":
    app.run(debug=True)
