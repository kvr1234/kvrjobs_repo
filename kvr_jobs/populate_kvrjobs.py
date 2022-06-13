import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kvr_jobs.settings')
import django
django.setup()

from jobs_app.models import HydJobs,BangaloreJobs,MumbaiJobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate1(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        fposition = fake.random_element(elements=('python developer','full stack developer,backend developer','front end developer','java developer'))
        feligibility = fake.random_element(elements=('B.tech','M.tech','Phd','BSC','MCA'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = str(phonenumbergen())

        hyd_jobs_record = HydJobs.objects.get_or_create(
        date = fdate,
        company = fcompany,
        position = fposition,
        eligibility = feligibility,
        address = faddress,
        email = femail,
        phonenumber = fphonenumber)

n = int(input('Enter Number of Records to Entered for Hyderabad:'))
populate1(n)
print(f'{n} Records Inserted Successfully')


def populate2(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        fposition = fake.random_element(elements=('python developer','full stack developer,backend developer','front end developer','java developer'))
        feligibility = fake.random_element(elements=('B.tech','M.tech','Phd','BSC','MCA'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = str(phonenumbergen())

        blr_jobs_record = BangaloreJobs.objects.get_or_create(
        date = fdate,
        company = fcompany,
        position = fposition,
        eligibility = feligibility,
        address = faddress,
        email = femail,
        phonenumber = fphonenumber)

n = int(input('Enter Number of Records to Entered for Bangalore:'))
populate2(n)
print(f'{n} Records Inserted Successfully')


def populate3(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        fposition = fake.random_element(elements=('python developer','full stack developer,backend developer','front end developer','java developer'))
        feligibility = fake.random_element(elements=('B.tech','M.tech','Phd','BSC','MCA'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = str(phonenumbergen())

        mumbai_jobs_record = MumbaiJobs.objects.get_or_create(
        date = fdate,
        company = fcompany,
        position = fposition,
        eligibility = feligibility,
        address = faddress,
        email = femail,
        phonenumber = fphonenumber)

n = int(input('Enter Number of Records to Entered for Mumbai:'))
populate3(n)
print(f'{n} Records Inserted Successfully')