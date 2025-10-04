import threading
import requests
import time

def download_file(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"completed download from {url} with {len(resp.content)} bytes.")

start = time.time()

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]
threads = []

for url in urls:
    t = threading.Thread(target=download_file , args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Total time taken is : {end - start:.2f} seconds")

# in I/O bound task we can use threading to improve the performance.
