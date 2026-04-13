# POS Tagging Web Application

This is a lightweight web application that allows users to upload plain text files (`.txt`) and receive the corresponding Part-of-Speech (POS) tagged output in JSON format. The app uses NLTK's POS tagger and is built with Python and Flask.

## Features

- Upload a `.txt` file via a simple web interface.
- Automatically tokenize and tag each word using NLTK's `averaged_perceptron_tagger`.
- Download the resulting POS-tagged data as a `.json` file.

## Project Structure

```

pos-tagging-app/
├── app.py                # Main Flask app
├── utils.py              # POS tagging logic
├── templates/
│   └── upload.html       # HTML form for file upload
├── uploads/              # Directory where uploaded and result files are stored

````

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pos-tagging-app.git
cd pos-tagging-app
````

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask nltk
```

### 4. Download NLTK data

The app will automatically download required NLTK data (`punkt`, `averaged_perceptron_tagger`) at runtime, but you can also do this manually:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

## Usage

### 1. Start the Flask server

```bash
python app.py
```

### 2. Open the web browser and navigate to:

```
http://127.0.0.1:5000/
```

### 3. Upload a `.txt` file

* The app will process the file and return a downloadable JSON file containing word–POS tag pairs.

## Output Format

The output JSON will be a list of dictionaries with the following format:

```json
[
  {"word": "The", "pos": "DT"},
  {"word": "dog", "pos": "NN"},
  {"word": "barked", "pos": "VBD"},
  ...
]
```

## Notes

* Only `.txt` files are supported.
* Files are saved in the `uploads/` directory during processing.
* The result file will be named `<original_filename>_pos.json`.

