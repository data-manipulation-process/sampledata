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

print("1111111")

content7 = 'this is fun, this is fun, this is fun, this is fun, this is fun'

print(content7.find('this'))
print(content7.rfind('this'))
print(content7.find('this', 5, 30))
print(content7.rfind('this', 5, -12))
print(content7.rfind('this', 5, -1))

content8 = 'Hello {}, your balalnce is {}'
print(content8.format("Jagan", 9000))

print("88888898")
content9 = 'the number is:{:50d}'
content10 = 'the number is:{:20d}'
print(content9.format(32323))
print(content10.format(32323))
print('999999')

print('000000000000000000')

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))
print("{:f} {:f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))
