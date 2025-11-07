import re
from collections import Counter

log_file_path = "access.log"

ip_pattern = r"\d+\.\d+\.\d+\.\d+"

def analyze_log(log_file_path):
    with open(log_file_path, "r") as file:
        log_lines = file.readlines()

    num_requests = len(log_lines)
    
    ip_addresses = re.findall(ip_pattern, "".join(log_lines))
    unique_ips = set(ip_addresses)
    
    url_counter = Counter()
    for line in log_lines:
        match = re.search(r'"GET (.*?) HTTP', line)
        if match:
            url = match.group(1)
            url_counter[url] += 1
    
    return num_requests, unique_ips, url_counter.most_common(3)

if __name__ == "__main__":
    num_requests, unique_ips, popular_urls = analyze_log(log_file_path)

    print("Log Analysis Results:")
    print(f"Number of Requests: {num_requests}")
    print(f"Number of Unique IP Addresses: {len(unique_ips)}")
    
    print("Popular URLs:")
    for url, count in popular_urls:
        print(f"{url}: {count} requests")