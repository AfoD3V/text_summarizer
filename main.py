from transformers import pipeline

def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = read_txt("./txt_files/news_article.txt")
summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

print(summary[0]['summary_text'])