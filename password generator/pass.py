import random

lower_case='abcdefghijklmnopqrstwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTWXYZ'
number='0123456789'
symbol='!@#$%^&*()<>?|'

common=lower_case + upper_case + number + symbol

print(common)

length=int(input('ENTER THE LENGTH OF THE PASSWORD --:'))

password="".join(random.sample(common,length))

print(password)