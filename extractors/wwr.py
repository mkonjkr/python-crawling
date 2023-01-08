from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Sorry, we can't reach out to the website")
  else:
    results=[]
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_='jobs')
    for job in jobs:
      posts = job.find_all('li')
      posts.pop(-1)
      for post in posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        company, kind, region = anchor.find_all('span', class_='company')
        title = anchor.find('span', class_='title')
        job_data = {
          'company' : company,
          'title' : title,
          'region' : region
        }
        results.append(job_data)
    return results
  