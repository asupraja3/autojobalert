import requests

def fetch_jobs(url):
    response = requests.get(url)
    return response.json()["jobs"]