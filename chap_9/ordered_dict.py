from collections import OrderedDict

# Question 6-4. Glossary 2

glossary = {}
glossary['function'] = 'an instruction sequence that a programmer can insert into a computer program as needed.'
glossary['list'] = 'a data type used to store multiple items in one veriable.'
glossary['variable'] = 'an abstract storage location paired with an associated symbolic name.'

for k, v in glossary.items():
    print(f" A {k.upper()} is {v}")
print("\n")

# Question 9-13. OrderedDict Rewrite
glossary = OrderedDict()
glossary['list'] = 'a data type used to store multiple items in one veriable.'
glossary['variable'] = 'an abstract storage location paired with an associated symbolic name.'
glossary['function'] = 'an instruction sequence that a programmer can insert into a computer program as needed.'

for k, v in glossary.items():
    print(f" A {k.upper()} is {v}")