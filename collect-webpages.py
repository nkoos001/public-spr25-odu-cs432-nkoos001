import requests
from bs4 import BeautifulSoup
import sys
import time
from urllib.parse import urljoin, urlparse

def extract_links(seed_url):
    try:
        response = requests.get(seed_url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching {seed_url}: {e}")
        return set()

    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()

    for a_tag in soup.find_all('a', href=True):
        absolute_url = urljoin(seed_url, a_tag['href'])
        if urlparse(absolute_url).scheme in ["http", "https"]:
            links.add(absolute_url)

    return links

def is_valid_html_page(url):
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        final_url = response.url  # Get the final redirected URL
        content_type = response.headers.get('Content-Type', '')

        if "text/html" in content_type:
            content_length = int(response.headers.get('Content-Length', 0))
            if content_length > 1000:
                return final_url  # Return the final URL
    except requests.RequestException:
        return None

    return None

def collect_uris(seed_url, max_count=500, output_file="collected_uris.txt"):
    unique_uris = set()

    while len(unique_uris) < max_count:
        print(f"Processing seed: {seed_url}")
        links = extract_links(seed_url)

        for link in links:
            if len(unique_uris) >= max_count:
                break

            final_uri = is_valid_html_page(link)
            if final_uri and final_uri not in unique_uris:
                unique_uris.add(final_uri)
                print(final_uri)

        seed_url = list(unique_uris)[-1]  # Use the last valid URI as the next seed

        time.sleep(1)  # Respect website resources by adding a delay

    with open(output_file, "w") as file:
        for uri in unique_uris:
            file.write(uri + "\n")

    print(f"Collected {len(unique_uris)} URIs and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 collect-webpages.py <seed_url>")
        sys.exit(1)

    seed_url = sys.argv[1]
    collect_uris(seed_url)
