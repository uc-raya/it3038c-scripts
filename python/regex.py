import requests, re

data = "Hello my email is raya9@mail.uc.edu. Please contact me!"
email = re.compile('[A-Za-z0-9_%.-]+@[A-Za-z0-9_%.-]+\.[A-z0-9{2,}]')
print(email.search(data).group())