import re
import wikipedia

states=[line.strip() for line in open("states.txt")]

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.ignore_emphasis = True
h.body_width = 0

# for state in states:
for state in states:
    with open('states/' + re.sub(" ", "_", state).lower() + ".txt", 'w') as g:
        print("Getting article for " + state)
        # Only use disambiguation if needed
        try:
            page = wikipedia.page(state)
        except:
            page = wikipedia.page(state + " (U.S. state)")
        print("Got page for " + page.title)
        g.write(page.content)