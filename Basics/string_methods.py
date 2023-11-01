url = "www.redhat.com"
result = url.startswith("www")
# so the url is starting with www then its true 
print(result)
print(url.endswith(".org"))
# but here the url is not ending with org then it is false
new_url = url.upper()
print("ORIGINAL", url, "RETURNED", new_url)