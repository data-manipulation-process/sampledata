
"""
find - Start  and end arguments
rindex - last occurance
"""
text = 'Python is fun is'

result = text.index('is')
result2 = text.find('fun')
result3 = text.index('is', 2, -4)
result4 = text.rindex('is')

result5 = text.count('i')

print(result)
print(result2)
print(result3)
print(result4)
print(result5)
