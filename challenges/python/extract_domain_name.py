# CodeWars Challenge: [Extract Domain Name]
# Link: [https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python]
# Difficulty: [5 Kyu]

# Instructions
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    pass


print(domain_name("http://google.com"))  # --> "google"
print(domain_name("http://google.co.jp"))  # --> "google"
print(domain_name("https://123.net"))  # --> "123"
print(domain_name("https://hyphen-site.org"))  # --> "hyphen-site"
print(domain_name("www.xakep.ru"))  # --> "xakep"
