import urllib.request


def url_open(path):

    url = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={path})')

    resposta = url.read()
    resposta = str(resposta)
    path = []

    for word in resposta:
        if word.isdigit() == True:
            path.append(word)

    path = ''.join(path)
    return path, resposta


code = '12345'
print(url_open(code))
for i in range(1, 401):
    print(url_open(code))
    code = (url_open(code)[0])
    

# peak.html
