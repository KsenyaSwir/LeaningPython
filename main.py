import sys
import logging
import datetime
import random
import math
import statistics
import urllib

example = set()  # order doesnt matter
example.add(42)
example.add(False)
example.add('Fuck')
print(example)

post = {"user_id": 209,
        "message": "Hi, Ksenya",
        "language": "English"}
print(post)

post2 = dict(message="ss cotopaxi", lang="English")
post2['user_id'] = 209
post2['id'] = 200
print(post2)

list_eg = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
turtle_eg = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)  # IMMUTABLE, different size, faster
print("List size = ", sys.getsizeof(list_eg))
print("Turtle size = ", sys.getsizeof(turtle_eg))

logging.basicConfig(filename="D:\\logger",
                    level=logging.DEBUG);
logger = logging.getLogger()
logger.info("First message")
print(logger.level)

for i in range(10):
    print(random.random())

squares = []
for i in range(1, 101):
    squares.append(i ** 2)
print(squares)

squares_2 = [i ** 2 for i in range(1, 101)]
print(squares_2)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

    def age(self):
        today = datetime.date(1994, 12, 26)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Mr Whom i never loved", "20210427")
print(user.age())


def id_prime_v1(n):
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
        return True


for n in range(1, 10):
    print(n, id_prime_v1(n))

g = lambda x: 5 * x
print(g(2))


def area(r):
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]
areas = []

for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

print(list(map(area, radii)))

data = [1.2, 2.7, 5, 7.7]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x: x > avg, data)))

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.56)
]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)

density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

dir(urllib)
from  urllib import request

resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))
print(resp.code)
print(resp.length)
data = resp.read()
html = data.decode("UTF-8")
print(html)
