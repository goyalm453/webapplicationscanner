import requests
from bs4 import BeautifulSoup

# Prompt the user to enter the target URL
url = input("Enter the target URL: ")

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the response HTML
soup = BeautifulSoup(response.text, "html.parser")

# Print the response status code
print("Status code:", response.status_code)

# Print the first 100 characters of the response HTML
print("HTML:", soup.prettify()[:100])

# Check for common vulnerabilities
if "password" in soup.prettify():
    print("Possible password vulnerability found!")
if "sql" in soup.prettify():
    print("Possible SQL injection vulnerability found!")
if "script" in soup.prettify():
    print("Possible XSS vulnerability found!")
if "csrf" in soup.prettify():
    print("Possible CSRF vulnerability found!")

# Check for missing security headers
security_headers = ["x-xss-protection", "x-content-type-options", "content-security-policy"]
headers = response.headers
for header in security_headers:
    if header not in headers:
        print("Missing security header:", header)

# Check for insecure cookies
if "secure" not in headers.get("set-cookie", ""):
    print("Insecure cookies found!")

# Check for insecure transport
if "https" not in url:
    print("Insecure transport (HTTP) found!")

# Check for XXE vulnerabilities
if "xml" in response.headers.get("content-type", ""):
    print("Possible XXE vulnerability found!")

# Check for broken authentication
if "login" in soup.prettify():
    print("Possible broken authentication vulnerability found!")
