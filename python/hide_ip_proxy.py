import requests



# retrieving a response with a static IP address

url = 'https://httpbin.org/ip'

response = requests.get(url)
print(f'Static Response:\n{response.text}')



# retrieving a response with a dynamic IP address

proxies_list = {
        'https':'20.54.56.26:8080',
        'http':'169.57.1.85:8123',
        }
https_url = 'https://httpbin.org/ip'
http_url = 'http://httpbin.org/ip'

dynamic_response = requests.get(https_url, proxies=proxies_list)
print(f'Selected IP https Response:\n{dynamic_response.text}')

dynamic_response = requests.get(http_url, proxies=proxies_list)
print(f'Selected IP http Response:\n{dynamic_response.text}')
