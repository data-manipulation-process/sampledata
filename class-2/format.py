
content = 'Hello {}, your balance is {}.'
content2 = 'Hello {0}, your balance is {1}.'
content3 = 'Hello {name}, your balance is {blc}.'
content4 = 'Hello {0}, your balance is {blc}.'

print(content.format("Adam", 230.000))
print(content2.format("Adam", 230.000))
print(content3.format(name="Adam", blc=230.000))
print(content4.format("Adam", blc=230.000))

content5 = 'the number is:{:d}'
content6 = 'the number is:{:f}'
print(content5.format(11111))
print(content6.format(11111.2323))
