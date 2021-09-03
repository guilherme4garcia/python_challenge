import urllib.request, urllib.parse


path = '12345'
url = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=,{path})')

resposta = url.read()
parsed = urllib.parse.urlparse(url)
captured_value = urllib.parse.parse_qs(parsed.query)

print(captured_value)

print(type(resposta))
