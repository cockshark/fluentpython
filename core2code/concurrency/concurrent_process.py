"""多进程编程"""

import concurrent.futures
import requests
import threading


def download(url: str):
    resp = requests.get(url=url)
    print(f"read {len(resp.content)} from {url}")


def download_all(sites):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(download, sites)


