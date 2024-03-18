from search_engines import Google
import pyfiglet
from pyfiglet import Figlet
import time 
from time import sleep

def banner():
    bannerfont = Figlet(font='whimsy')
    print(bannerfont.renderText('CYAN HAT'))
    print("                                                            *beta testing")
    print("-----------------------------TYPE HELP FOR MENU-----------------------------")

def menu():
    print(" ")
    print("help  DISPLAYS MENU")
    print("setdork  SETS DORK MODE")
    print("dorks  DISPLAYS DORKS")
    print(" ")

def domain():
    print("received")
    f= input("URL:")
    dom=str("site:"+f)
    print(dom)
    results = engine.search(dom)
    links = results.links()
    print(links)
        
def filetype():
    filetype= input("Filetype: ")
    if filetype == "pdf":
        l=str("inurl:pdf")
        results = engine.search(l,pages=1)
        links = results.links()
        print(" ")
        print(links)
        print(" ")
    else:
        ext=str("inurl: ext:"+filetype)
        print(ext)
        results = engine.search(ext,pages=1)
        links = results.links()
        print(" ")
        print(links)
        print(" ")

def keyword():
    print("received")
    f= input("Word:")
    dom=str("allintext:"+f)
    print(dom)
    results = engine.search(dom)
    links = results.links()
    print(links)



banner()





while True:

    cmd=input("> ")

    if cmd == "help":
        menu()

    elif cmd == "dorks":
        print(" ")
        print("domain CRAWLS ALL SUBDOMAINS OF A SITE")
        print("extension SEARCHES FOR TYPE OF FILE PROVIDED")
        print("keyword RETURNS ALL URLS CONTAINING WORD PROVIDED")
        print(" ")

    elif cmd == "setdork":
        engine = Google()
        f=input("Mode> ")

        if f == "domain":
            domain()
            
            

        elif f == "extension":
            filetype()
        
        elif f == "keyword":
            keyword()

        
            
   
