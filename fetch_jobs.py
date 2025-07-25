import requests

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs?category=software-dev"
    response = requests.get(url)
    return response.json()["jobs"]