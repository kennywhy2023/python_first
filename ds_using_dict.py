#"ab"是地址（Address）薄（Book）的缩写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'matsumoto': 'matz@ll.org',
    'spammer': 'spammer@hostmail.com'
}

print("swaroop's address is", ab['Swaroop'])

#删除一对键值对
del ab['spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

#添加一对键值对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])