import webbrowser

print("===== Amazon Product Search =====")

product = input("Enter product name: ")

search = product.replace(" ", "+")

url = "https://www.amazon.in/s?k=" + search

print("Opening Amazon...")

webbrowser.open(url)
