from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

base_url = "https://www.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")
