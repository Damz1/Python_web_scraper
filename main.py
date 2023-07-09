import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# find element by ID
results = soup.find(id="ResultsContainer")

# find all elements with a class name
job_elements = results.find_all("div", class_="card-content")

# finds jobs that has python in the text
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# iterate over python jobs 3 generations up to find all the info about them
python_jobs_element = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_jobs_element:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"apply here: {link_url}\n")
    print()
