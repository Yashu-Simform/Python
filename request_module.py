import requests

url1 = 'https://img-getpocket.cdn.mozilla.net/296x148/filters:format(jpeg):quality(60):no_upscale():strip_exif()/https%3A%2F%2Fs3.us-east-1.amazonaws.com%2Fpocket-curatedcorpusapi-prod-images%2F4a309707-33af-47d5-9047-9cdd481376e5.jpeg'

url2 = 'https://httpbin.org/get'

arg_payload = {'name': 'ChotaDon', 'email': 'chotadon@gmail.com'}


def make_get_req(url, p_payload):
    req = requests.get(url,params=p_payload)
    print(req.url)
    print(req.status_code)
    print(req.text)
    print(req.content)


def make_post_req(p_url, p_payload):
    req = requests.post(p_url,data=p_payload)
    print(req.url)
    print(req.status_code)
    print(req.text)
    print(req.content)
    pass

auth_url = 'https://httpbin.org/basic-auth/chotadon/testing'
def basic_auth(p_url, p_username, p_pass):
    req = requests.get(p_url, auth=(p_username, p_pass))
    print(req.url)
    print(req.status_code)
    print(req.text)
    print(req.content)
    pass

def make_put_req():
    pass

def writeImg(url):
    r = requests.get(url)

    with open('image.png', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    # make_post_req('https://httpbin.org/post', arg_payload)
    basic_auth(auth_url, 'chotadon', 'testing')