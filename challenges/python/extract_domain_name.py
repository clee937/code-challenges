# CodeWars Challenge: [Extract Domain Name]
# Link: [https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python]
# Difficulty: [5 Kyu]

# Instructions
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# with regex
import re


def domain_name(url):
    return re.search(r'(https?://)?(www\.)?([^/.]+)', url).group(3)


# Using string methods
def domain_name(url):
    url = url.replace("https://", "").replace("http://", "")
    # if statement ensures www is only removed/replaced if at the beginning, and not if it's in the middle or the end.
    if url[0:4] == 'www.':
        url = url[4:]
        # url = url.replace("www.", "")
    return url.split(".")[0]


print(domain_name("http://google.com"))  # --> "google"
print(domain_name("http://google.co.jp"))  # --> "google"
print(domain_name("https://123.net"))  # --> "123"
print(domain_name("https://hyphen-site.org"))  # --> "hyphen-site"
print(domain_name("www.xakep.ru"))  # --> "xakep"
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("icann.org"))  # --> "icann"
print(domain_name("ssec1qe2.jp/index.php"))  # --> "ssec1qe2"
print(domain_name("vpfqtmvu.co.za/default.html"))  # --> "vpfqtmvu"
print(domain_name("etesvx67h3tcia0v3c3gsf3whjs.tv/default.html"))
# --> "etesvx67h3tcia0v3c3gsf3whjs"
print(domain_name("2vbah3c0e6h86g.br/default.html"))
# --> "2vbah3c0e6h86g"
print(domain_name("http://5ijyb36sb7c.jp/index.php"))
# --> "5ijyb36sb7c"
print(domain_name("ssec1qe2.jp/index.php"))
# --> "ssec1qe2"
print(domain_name("zu2jz61nkddo5vn7pi46gw4xnj6so.edu/index.php"))
# --> "zu2jz61nkddo5vn7pi46gw4xnj6so"
print(domain_name('focksvn4w2d6deni0fhsmb.us/default.html'))
# --> "focksvn4w2d6deni0fhsmb"
print(domain_name("googlewww.com"))
# --> "googlewww"
