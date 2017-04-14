import urllib.request, re, html2text

states=[]
with open("states.py") as f:
     states= eval(f.read()).values()

states = [re.sub(" ", "_", state) for state in states]
with open("alabama.html", 'w') as g:
    #http://stackoverflow.com/questions/34476403/cant-use-read-for-html2text
    http_state = urllib.request.urlopen("https://en.m.wikipedia.org/wiki/"+states[0])
    content = http_state.read()
    charset = http_state.headers.get_content_charset()
    content = content.decode(charset)
    content = html2text.html2text(content)
    content = re.sub("[^a-zA-Z0-9 ]+", " ", content)
    g.write(content)
