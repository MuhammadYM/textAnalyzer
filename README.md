# Text Analyzer

A Python-based text analysis tool that performs part-of-speech tagging and chunking using NLTK.

## Features

- Sentence and word tokenization
- Part-of-speech tagging
- Noun phrase (NP) and verb phrase (VP) chunking
- Frequency analysis of the most common chunks

## Requirements

- Python 3.7+
- NLTK library
- Jupyter notebook (for running the interactive analysis)

## Setup Instructions

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download required NLTK data:**
   
   **Easy way (recommended):**
   ```bash
   python setup.py
   ```
   
   **Manual way:**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```

## Usage

### Option 1: Using Jupyter Notebook (Recommended)
```bash
jupyter notebook script.ipynb
```

### Option 2: Using Python Scripts
```python
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# Load your text file
with open("dorian_gray.txt", encoding='utf-8') as f:
    text = f.read().lower()

# Tokenize and analyze
word_tokenized_text = word_sentence_tokenize(text)
# ... continue with analysis
```

## Using Your Own Text Files

The project comes with "The Picture of Dorian Gray" as a sample text, but you can easily analyze your own text files:


### Method 2: Modify the Code
1. Place your text file in the project directory
2. In the Jupyter notebook, change Cell 2 from:
   ```python
   text = open("dorian_gray.txt",encoding='utf-8').read().lower()
   ```
   to:
   ```python
   text = open("your_filename.txt",encoding='utf-8').read().lower()
   ```

```

### Supported Text Formats
- **Plain text files** (.txt) work best
- **UTF-8 encoding** is recommended for international characters
- Large files are supported, but processing time will increase
- The text will automatically be converted to lowercase for analysis

## Files

- `script.ipynb` - Main analysis notebook
- `tokenize_words.py` - Text tokenization functions
- `chunk_counters.py` - Chunk counting and analysis functions
- `dorian_gray.txt` - Sample text file for analysis
- `requirements.txt` - Python dependencies
- `setup.py` - Automated setup script for NLTK data

## Notes

- Make sure to place your text file in the same directory as the scripts
- The current setup analyzes "The Picture of Dorian Gray" but can be adapted for any text file 