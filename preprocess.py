import pandas as pd

def filter_data(jobs, keywords=["AI", "ML", "LLM"]):

    filtered_jobs = []
    for job in jobs:
        text = job['title'].lower()
        # text = (job['title'] + job['description']).lower()
        if any(key.lower() in text for key in keywords) and job['candidate_required_location'] == "USA":
            filtered_jobs.append({"Title": job['title'],
                                  "Company": job['company_name'],
                                  "Location": job['candidate_required_location'],
                                  "URL": job['url'],
                                  "Posted": job['publication_date']
                                  })
    df = pd.DataFrame(filtered_jobs)
    df.to_csv("filtered_jobs.csv", index=False)
    return df