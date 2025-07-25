from email_utils import *
from fetch_jobs import *
from preprocess import *
import schedule
import time

def job_alert():
    #Fetch jobs and filter them
    filtered_jobs = filter_data(fetch_jobs())
    #Send email with the filtered jobs
    if not filtered_jobs.empty:
        send_email()
    else:
        print("No new jobs")

if __name__ == "__main__":

    job_alert()
    # print("Starting job alert service...")
    # # Schedule the job to run every day at 9 AM
    # schedule.every().day.at("09:00").do(job_alert)
    # print("Job alert service started. Waiting for the next scheduled time...")
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)  # Sleep for a short time to avoid busy waiting


