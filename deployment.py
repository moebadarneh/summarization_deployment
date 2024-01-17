
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the summarization model from Hugging Face
summarizer = pipeline("summarization")

@app.route('/summarize', methods=['GET'])
def summarize_text():
    try:
        # Get the input text from the request
        data = request.get_json()
        input_text = data['text']

        # Perform summarization
        summary = summarizer(input_text, max_length=50, min_length=15,do_sample=False)

        # Extract the summarized text from the result
        summarized_text = summary[0]['summary_text'].strip()

        # Return the summarized text as JSON
        return jsonify({'summary': summarized_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


