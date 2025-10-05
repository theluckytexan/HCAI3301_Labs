"""Module for totaling pay for employees:
taking regular hours plus overtime hours and the employees
wages then returning the total"""

def total_pay(reGHours,houRWage,oveRHours):
    return (reGHours * houRWage) + (oveRHours * 1.5 * houRWage)
#I wanted to do this differently by oveRHours = reGHours - 40, but I didn't know how to
#exactly return a value of 0 if its negative
#also did it the way that you stated in the assignment.