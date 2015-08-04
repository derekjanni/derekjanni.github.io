---
layout: post
title: The Joys of Webscraping (An Intro in Python)
---

Scraping data from websites is one of those things that *sounds* really cool and high-tech, but it's pretty simple and fun.
In case you're too lazy to read the docs for [Beautiful Soup](https://beautiful-soup-4.readthedocs.org/en/latest/) and
[Requests](http://docs.python-requests.org/en/latest/), here's a quick and intro to webscraping in Python. The most basic 
functionality is demo'd below:

 ```python
import requests
from bs4 import BeautifulSoup
url = "http://pitchfork.com/"
page = requests.get(url).text
soup = BeautifulSoup(page)
```

The `soup` object is basically a parsed representation of the page. That's right, `Beautiful Soup` does it for you.
Once you've made your soup, it's easy to pull out who lists of objects with the `find` and `findall` methods.

```python
h1 = find_all('h1')
link = find_all('a', href=True)
```

Now one caveat is that if you want if a particular element, you'll have to do a little nit-picking to get that out.

```python
anchor_text = soup.find_all(class_='alt')[0].find_all('a')[1].text
```

Notice that you can adjust which element you're pointing at by ajusting the `[i]` that you're calling. This the part that can
be both really frustrating if you're bad and really cool if you're less bad. 

![Hmmm...](http://evolvingweb.ca/sites/default/files/styles/large/public/web-scraper-670x300.png?itok=9YlboANH)

The fun part about webscraping in Python is that you have access to a lot of different tools after you've got the data: you can load it into a SQLite db using the `sqlite` module or into a `pandas` dataframe so you can analyze them. If you want to see an example of how webscraping can be used in a full scale project (along with some linear modeling tricks in Python) check out [my recent project](https://github.com/derekjanni/Mining-Movie-Reviews) on GitHub.
