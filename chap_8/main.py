"""
    M. Ashuza 
    july 26 2022
    Python Crash Course Book chapter 8 Exercises 
"""
# import user_profile
# from user_profile import build_profile
# from user_profile import build_profile as bp
# import user_profile as up
from user_profile import *

# Question 8-16. Imports
user_profile = build_profile('MUHIGIR', 'Ashuza',
location='Goma',
field='Electrical & CS engineering', hobbies='Reading books, exercising')
for k, v in user_profile.items():
    print(k +': '+ v)
