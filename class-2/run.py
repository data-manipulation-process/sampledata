"""
in
find  - is like substring start and end arguments, index
index
find- first occurance, rfind is the last occurance
"""
text_phrase = "0123456world!"

search_fave_phrase = text_phrase.find("w", 3, 8)
search_fave_phrase2 = text_phrase.find("d")
search_index = text_phrase.index("o")

print('text_phrase.find("w", 3, 8): ', search_fave_phrase)
print('text_phrase.find("d") :', search_fave_phrase2)
print('text_phrase.index("o") :', search_index)

print("------11111")
search_in =  "a" in "Hello world!"
print("a" in "Hello world!")
print(search_in)
print("------2222")
"""
find string in the line
"""
message = 'Python is a fun programming language'

find_message = message.find("fun")

print(find_message)

"""
Find occurance 
"""

quote = 'let it be, let it be, let it be2'
result_1 = quote.find('let it')
result_2 = quote.find('small')
result_3 = quote.rfind('be')

print("Substing 'let it':", result_1)
print("Substing 'let it':", result_2)
print("Substing 'let it':", result_3)

if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

"""
"""

quote2 = 'Dosmall things with great smalllove'

k1 = quote2.rfind('small', 2, 40)
print(k1)

