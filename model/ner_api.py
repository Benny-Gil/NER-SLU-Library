from flask import Flask, request, jsonify
import spacy

# Create Flask app
app = Flask(__name__)

# Load spaCy model
try:
    # You can use a different model if needed
    nlp = spacy.load("../training/output/model-best")
except OSError:
    # If model not found, download it
    import spacy.cli

    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


@app.route("/api/ner", methods=["POST"])
def extract_entities():
    """
    Extract named entities from text using spaCy
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data["text"]
    if not text or len(text.strip()) == 0:
        return jsonify({"error": "Text cannot be empty"}), 400

    # Process text with spaCy
    doc = nlp(text)

    # Extract entities
    entities = [
        {
            "text": ent.text,
            "start_char": ent.start_char,
            "end_char": ent.end_char,
            "label": ent.label_,
        }
        for ent in doc.ents
    ]

    return jsonify({"entities": entities, "processed_text": text})


@app.route("/")
def read_root():
    return jsonify(
        {"message": "NER API is running. Use /api/ner endpoint for entity recognition."}
    )


# Enable CORS if needed
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)