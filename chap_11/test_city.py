"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 11-1. City, Country
import unittest
from city_functions import country_city

class NamesTestCases(unittest.TestCase):
    """Test for 'city_country.py'"""

    def test_city_country(self):
        """Do names like 'santiago' and 'chile' works?"""
        formated_name = country_city('santiago', 'chile')
        self.assertEqual(formated_name, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Do names like 'santiago, chile, 500000' works?"""
        formated_name = country_city(
            'santiago', 'chile', 5000000
        )
        self.assertEqual(formated_name, 'Santiago, Chile, - Population 5000000')

unittest.main()

