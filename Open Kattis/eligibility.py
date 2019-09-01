import sys
import time

def determine_eligibility(student):
    name, school_dt, birth_dt, courses = student
    print(name, end = ' ')
    if school_dt >= "2010/01/01" or birth_dt >= "1991/01/01":
        print("eligible")
        return
    if int(courses) > 40:
        print("ineligible")
        return
    print("coach petitions")

def main():
    inp  = [line.split() for line in sys.stdin.read().splitlines()]

    for student in inp[1:]:
        determine_eligibility(student)
        
main()
