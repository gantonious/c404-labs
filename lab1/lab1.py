import requests

def print_requests_version():
    print("requests version: {0}".format(requests.__version__))

def get_google():
    request = requests.get("http://google.com")
    print("Response code for GET http://google.com: {0}".format(request.status_code))

def post_ccid(ccid):
    request_url = "http://ccideddieantonio.rhcloud/com/{0}".format(ccid)
    request = requests.post(request_url)
    print("Response code for POST {0}: {1}".format(request_url, request.status_code))

def get_plain_text(url):
    request = requests.get(url)
    print("Response body from {0}\n{1}".format(url, request.text))

if __name__ == "__main__":
    print_requests_version()
    get_google()
    # fails due to unresolvable hostname
    # post_ccid("antoniou")
    get_plain_text("https://raw.githubusercontent.com/gantonious/c404-labs/master/lab1/lab1.py")