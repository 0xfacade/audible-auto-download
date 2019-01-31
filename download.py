import pickle
import requests
from progress.bar import Bar

with open("audiobooks.pickle", "rb") as f:
    audiobooks = pickle.load(f)

with open("cookies.pickle", "rb") as f:
    jar = pickle.load(f)

for i, (author, title, url) in enumerate(audiobooks):
    print(f"{i}: {author} - {title}")

print()
print("Select the numbers to download (space separated).")
numbers = input(">> ")

numbers = [int(number) for number in numbers.split()]

for number in numbers:
    author, title, url = audiobooks[number]
    name = f"{author} - {title}.aax"
    print("Now downloading " + name)
    
    response = requests.get(url, cookies=jar, stream=True)
    response.raise_for_status()
    
    bytes_to_receive = int(response.headers["Content-Length"])

    with open(name, "wb") as f:
        bar = Bar("Downloading..", fill="@", 
                suffix="%(percent)d%%",
                max=100)

        bytes_read = 0
        for block in response.iter_content():
            bytes_read += len(block)  
            f.write(block)

            if bytes_read >= bytes_to_receive / 100:
                bar.next()
                bytes_read = 0
            
        bar.finish()

