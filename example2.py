a = ['kaushal', 'Python', 'Ramesh', 'Hi', '', False, [1,2,3, 'hi'], {'a': [1,2,3],
                                                                    'b':[4,5,'whatsapp']}, ('a', 'b', False), {'pasha', 'nandi'}]
# type(a[0])
# type(str)
def lena(obj):
    for i in obj:
        if isinstance(i, str):
            print(i + ' is a string')
            print('len('+i+') is ', len(i))
        if isinstance(i, (list, tuple, set)):
            print('type('+str(i)+') is: ', type(i))
            lena(i)
        if isinstance(i, dict):
            print('type('+str(i)+') is ', type(i))
            for k,v in i.items():
                lena(k)
                lena(v)
#     return f'\nEND OF LIST'
#     return 'CHINAL'
    return '\nend oflist'
lena(a)
