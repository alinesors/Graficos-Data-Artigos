from wordcloud import WordCloud

text = " ".join([
    "phishing", "detection", "emails", "websites", "NLP", 
    "deep learning", "machine learning", "IA", "sites miméticos"
])

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()