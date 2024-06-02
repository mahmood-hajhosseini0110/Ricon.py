import requests
from bs4 import BeautifulSoup
from termcolor import colored
import re
import whois
import socket
import argparse
import dns.resolver


parser = argparse.ArgumentParser(description='Process some inputs.')
parser.add_argument('--tag', type=str, help='process a number')
parser.add_argument('--sub', type=str, help='process a number')
parser.add_argument('--cod', type=str, help='process a number')
parser.add_argument('--title', type=str, help='process a number')
parser.add_argument('--whoiss', type=str, help='process a number')
parser.add_argument('--emile', type=str, help='process a number')
parser.add_argument('--phone', type=str, help='process a number')
parser.add_argument('--ip', type=str, help='process a number')
parser.add_argument('--ports', type=str, help='process a number')
args = parser.parse_args()
if args.tag is not None:
    v = str(args.tag)
    x = requests.get(v)
    soup = BeautifulSoup(x.text, "html.parser")
    a = soup.find_all('a')
    w = []
    e = []
    i = 0
    for q in a:
        w.insert(i , q)
        i+=1
        sdc = open("tag.txt", "a+")
        sdc.write(str(q))
        sdc.close()
        print(colored(q,"blue"))
        print("\n")
        e.append(q.get('href'))
    for d in e:
        print(colored(d,"blue"))
        print("\n")
    for c in e:
        try:
            vb = requests.get(c)
            sop  = BeautifulSoup(vb.text,"html.parser")
            wwe = sop.find_all('a')
            for hf in wwe:   
                        sdc = open("tag.txt", "a+")
                        sdc.writelines(str(hf))
                        sdc.close()
                        print(colored(hf,"blue"))
                        print("\n")
                        print(colored("next","blue"))
        except:
            pass
        
if args.sub is not None:
    to = int(input(colored("html namber 1" + "\n" + "txt namber 2" + "\n","green")))
    if to == 1:
        domain = args.sub
        r = open('wordlist.txt','r')
        w = r.readlines()
        for subdomain in w:
            subdomain = subdomain.replace('\n','')
            try:
                dddd = subdomain
                answers = dns.resolver.query(dddd+'.'+domain, 'A')
                for ip in answers:
                        ddz = open("subdomain.html","a+")
                        ddz.write(domain + "\t"+ dddd + "." + domain + " - " + str(ip) + "\n")
                        ddz.close()
                        print(colored(dddd + "." + domain + " - " + str(ip), "green"))
            except:
                    print(colored("eroeo!!!","red"))
    elif to == 2:
        domain =args.sub
        r = open('wordlist.txt','r')
        w = r.readlines()
        for subdomain in w:
            subdomain = subdomain.replace('\n','')
            try:
                dddd = subdomain
                answers = dns.resolver.query(dddd+'.'+domain, 'A')
                for ip in answers:
                        ddz = open("subdomain.txt","a+")
                        ddz.write(domain + "\t" + dddd + "." + domain + " - " + str(ip) + "\n")
                        ddz.close()
                        print(colored(dddd + "." + domain + " - " + str(ip), "green"))
            except:
                    print(colored("eroeo!!!","red"))

if args.cod is not None:
    ereeddd = int( input(colored("html namber 1" + "\n" + "txt namber 2" + "\n","light_blue")))
    if ereeddd == 1:
        v = args.cod
        x = requests.get(v)
        x = x.status_code
        if x == 200:
            ddz = open("status.html","a+")
            print(colored("Success!","light_blue"))
            ddz.write(v + "   " + "Success!" + "\n")
            ddz.close()
        elif x == 404:
            ddz = open("status.html","a+")
            print(colored("Page not found.","light_blue"))
            ddz.write(v +  "    " + "Page not found." + "\n")
            ddz.close()
        elif x == 500:
            ddz = open("status.html","a+")
            print(colored("Internal server error.","light_blue"))
            ddz.write(v + "   " + "Internal server error." + "\n")
            ddz.close()
        else:
            ddz = open("status.html","a+")
            print(colored("Unknown status code:" +  x ,"light_blue"))
            ddz.write(v + "   " + "Unknown status code:" + "\n")
            ddz.close()
    elif ereeddd == 2:
        v = args.cod
        x = requests.get(v)
        x = x.status_code
        if x == 200:
            ddz = open("status.txt","a+")
            print(colored("Success!","light_blue"))
            ddz.write(v + "   " + "Success!" + "\n")
            ddz.close()
        elif x == 404:
            ddz = open("status.txt","a+")
            print(colored("Page not found.","light_blue"))
            ddz.write(v +  "    " + "Page not found." + "\n")
            ddz.close()
        elif x == 500:
            ddz = open("status.txt","a+")
            print(colored("Internal server error.","light_blue"))
            ddz.write(v + "   " + "Internal server error." + "\n")
            ddz.close()
        else:
            ddz = open("status.txt","a+")
            print(colored("Unknown status code:" +  x ,"light_blue"))
            ddz.write(v + "   " + "Unknown status code:" + "\n")
            ddz.close()

if args.title is not None:
    url = args.title
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    xxxd = open("title.txt","a+")
    xxxd.write(title)
    xxxd.close()
    print(colored(title,"cyan"))

if args.whoiss is not None:
    urls = args.whoiss
    sddf = whois.whois(urls)
    xxxde = open("whois.txt","a+")
    xxxde.write(str(sddf))
    xxxde.close()
    print(colored(sddf,"magenta"))

if args.emile is not None:
    kro = args.emile
    texts = requests.get(kro)
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email = re.search(pattern, texts.text)
    if email:
        ow = open("email.txt","a+")
        ow.write(str(email.group()))
        ow.close()
        print(colored(email.group(),"dark_grey"))
    else:
        print(colored("No email found","red"))

if args.phone is not None:
    ertpg = args.phone
    tel = requests.get(ertpg)
    
    pat = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    gpat = re.search(pat,tel.text)
    if gpat:
        oww= open("phone.txt","a+")
        oww.write(str(email.group()))
        oww.close()
        print(colored(gpat.group(),"light_red"))
    else:
        print(colored("No phone found","red"))

if args.ip is not None:
    rssx = open('wordlist.txt','r')
    wer = rssx.readlines()
    for wew in wer:
        wew = wew.replace('\n','')
        domain =wew+"."+args.ip
        try:
            ip_address = socket.gethostbyname(domain)
            rew = open("ip.txt","a+")
            rew.write(domain + "    " + ip_address + "\n")
            rew.close()
            print(f"The IP address of {domain} is {ip_address}")
        except:
             print("erororo!!")

if args.ports is not None:
    Ip = args.ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]

    for port in common_ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((Ip, port))
        if result == 0:
            ov = open("port.txt", "a+")
            ov.write(ip + "   " + "port" + str(port) + "is open")
            ov.close()
            print("Port {} is open".format(port))
        else:
            ov = open("port.txt", "a+")
            ov.write(ip + "   " + "port" + str(port) + "is closed")
            ov.close()
            print("Port {} is closed".format(port))
        sock.close()
