from bs4 import BeautifulSoup
with open("source.html","r", encoding = "utf-8") as f:
    doc = BeautifulSoup(f,"html.parser")

print(doc.prettify())