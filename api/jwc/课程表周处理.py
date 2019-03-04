import re
c='value="jBj9p94vPQaCUljVC7CBMV7h1jmE9w4/dykUmrE6E8wJ/EjdfCmmIGNlLa7SBnjqcQra04+Oam0lTdAs9YX1wg=="'
print(type(c))
t=re.search('value.*',c).group()
print(t)