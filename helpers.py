import random
import string


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_email():
    email = random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])
    return email


