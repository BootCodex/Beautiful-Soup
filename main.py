from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read

soup = BeautifulSoup(contents)