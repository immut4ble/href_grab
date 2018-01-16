# packet
# Rudimentary href puller. takes an ip or domain as the only arg.

import sys
import subprocess

def grab_links():
    output = subprocess.check_output(['curl -L', sys.argv[1]], shell=True)
    lines = output.splitlines()
    links = []
    for line in lines:
        if "href" in line:
            links.append(line)
    for link in links:
        index = links.index(link)
        link = link[link.find("href") + 6:]
        link = link[:link.find("\"")]
        links[index] = link

    links = list(set(links))
    links.sort()
    for link in links:
        print(link)

if len(sys.argv) != 2:
    print("useage: href_grab address")
else:
    grab_links()
