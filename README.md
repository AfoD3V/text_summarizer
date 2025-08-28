# Text Summarizer

A tiny Python app that uses Hugging Face Transformers (BART `facebook/bart-large-cnn`) to create concise summaries of plain-text files.

## Requirements
- Python 3.9+
- `uv` (recommended) or `pip`

## Setup

Using uv (recommended):

```bash
uv sync
```

Using pip (CPU only):

```bash
pip install transformers torch
```

## Usage

```bash
python main.py
```

By default, the script summarizes the file at `./txt_files/news_article.txt`. Edit that file or change the path in `main.py` to summarize a different text.

## How it works
- Loads the summarization pipeline with BART (`facebook/bart-large-cnn`).
- Reads a `.txt` file into memory.
- Generates a summary with length constraints (`min_length=50`, `max_length=150`) and deterministic decoding (`do_sample=False`).

## Notes
- You can tweak summary length and sampling options in `main.py` line calling `summarizer(...)`.