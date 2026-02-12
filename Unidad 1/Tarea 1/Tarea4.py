logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

ip_urls = {}
url_counts = {}
browser_counts = {}

for ip, url, navegador in logs:
    if ip not in ip_urls:
        ip_urls[ip] = set()
    ip_urls[ip].add(url)
    
    url_counts[url] = url_counts.get(url, 0) + 1
    
    browser_counts[navegador] = browser_counts.get(navegador, 0) + 1

navegador_top = max(browser_counts, key=browser_counts.get)

ips_ordenadas = sorted(ip_urls.keys())

print(f"URLs por IP: {ip_urls}")
print(f"Popularidad de URLs: {url_counts}")
print(f"Navegador más usado: {navegador_top} ({browser_counts[navegador_top]} veces)")
print(f"Lista de IPs (ordenadas): {ips_ordenadas}")