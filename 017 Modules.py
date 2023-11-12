# A module is a file with some Python code. We use modules to break up our
# program into multiple files. This way, our code will be better organized. We won’t
# have one gigantic file with a million lines of code in it!
# There are 2 ways to import modules: we can import the entire module, or specific
# objects in a module.

# importing the entire converters module

import converters

print(converters.kg_to_lbs(70))

# importing one function in the converters module

from converters import lbs_to_kg

print(lbs_to_kg(70))
