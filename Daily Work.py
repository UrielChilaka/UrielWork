d = {'daniel':'555-5555', 'anna':'555-7777', 'linus':'555-6666'}

#for key,value in d.items():
#    print(key)
#    print(value)

d['bob'] = '555-2222'

for phone_number in d.vaules():
    print(phone_number)

print(len(d))

if 'daniel' in d:
    print(d['daniel'])
else:
    print('Not there!')

print(d['linus'])

for name in d.keys():
    print(name)
