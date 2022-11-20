import string
import random

def gernerate_random_email(emailprefix=None, domain =None):
    if not domain:
        domain = "test.com"
    if not emailprefix:
        emailprefix = " "
        alphabet = list(string.ascii_lowercase)
        for x in range(15):
            emailprefix += random.choice(alphabet)
    completed_string = emailprefix+'@'+domain
    return completed_string

def generate_random_username(name=None):
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    return random_string

def generate_random_password():
    s1 = ""
    for x in range(10):
        s1 += random.choice(string.ascii_lowercase)
        s1 += random.choice(string.digits)
    random_string = ''.join(random.sample(s1, len(s1)))
    return random_string


