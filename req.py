import requests

r = requests.get('https://www.youtube.com/watch?v=tb8gHvYlCFs&t=38s')

print(dir(r))