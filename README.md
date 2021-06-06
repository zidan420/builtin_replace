"# builtin_replace" 

It is a very simple and friendly tool to replace the built-in PYTHON DICTIONARY.

Example:

from pylab import dict

var = dict("apple, banana: 20 ; mango, tea: True ; habit = 'good'")

print(var)


Output:

{'apple': 20, 'banana': 20, 'mango': True, 'tea': True, 'habit': 'good'}


Explanation:

  (i) semi-colons(;) are used to seperate each key-value pair
  
  (ii) we can set many keys to the same value just by seperating them with ","
  
  (iii) colons(:) are used to seperate a key from value
  
  (iv) dict() converts the string to BUILT-IN Dictionary
  

Advantages:

(i) No need to write the Quotation mark ("" or '') each time for defining a key

(ii) More User friendly Syntax

(iii) Assigns several keys consisting of same value more quickly

(iv) Reduces coding when working with many key-value pairs



Disadvantages:

(i) Annoying to import a library
