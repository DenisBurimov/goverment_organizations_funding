import requests

files_list = ['https://itdashboard.gov/drupal/summary/422/422-000001328', 'https://itdashboard.gov/drupal/summary/422/422-000000004', 'https://itdashboard.gov/drupal/summary/422/422-000001327']

url = files_list[1] + "#"
filename = f"{files_list[1][-9:]}.pdf"
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)