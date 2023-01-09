from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_page_count(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  
  browser = webdriver.Chrome(options=options)
  browser.get(f"https://www.indeed.com/jobs?q={keyword}")

  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", role="navigation")
  if pagination == None:
    return 1
  else:
    pages = pagination.find_all("div", recursive=False)
    count = (len(pages))
    if count >= 5:
      return 5
    else:
      return count




def extract_indeed_jobs(keyword):
  
  pages = get_page_count(keyword)
  print("Found", pages, "pages")
  
  results=[]
  
  for page in range(pages):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    browser = webdriver.Chrome(options=options)
    
    browser.get(f"https://www.indeed.com/jobs?q={keyword}&start{page*10}")
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList css-0")
    jobs = job_list.find_all("li", recursive=False) #recursive=False will find a li right under the ul
    
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          
          'company':company.string,
          'location':location.string,
          'position': title,
          'link':f"https://indeed.com{link}"
        }
        for each in job_data:
          if job_data[each]!=None:
            job_data[each] = job_data[each].replace(",", " ")
        results.append(job_data)
  return results