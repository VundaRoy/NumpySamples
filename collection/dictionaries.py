d={'cat':'poonai','dog':'naay','man':'manithan'}
print(d)

print(d['cat'])
d['fish']='meen'
print(d)

print(d.get('ape','N/A'))
del d['fish']
print(d.get('fish','N/A'))