def trim_text(text):
    new_text = text[:8]
    return new_text+ "..."

text = trim_text("ini adalah tulisan yang sangat panjang")
print(text)