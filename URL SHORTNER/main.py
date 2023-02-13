import pyshorteners
url = input("Enter your URl")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted URL is ",s)