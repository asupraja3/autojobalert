import pandas as pd

def filter_data(jobs, keywords=["AI", "ML", "LLM"]):

    filtered_jobs = []
    for job in jobs:
        text = (job['title'] + job['description']).lower()
        if any(key.lower in text for key in keywords):
            filtered_jobs.append({"Title": job['title'],
                                  "Company": job['company_name'],
                                  "Location": job['candidate_required_location'],
                                  "URL": job['url'],
                                  "Posted": job['publication_date']
                                  })
    return pd.DataFrame(filtered_jobs)