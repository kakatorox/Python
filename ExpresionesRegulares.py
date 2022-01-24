#regex(regularexpression)
#en python esta la funcion re
#los patrones so operadore so 
#. es un caracter
import re
patron=re.compile("\d\d\d")
print(patron.search("kilo912metro").group())

if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
    print("se encontro el patrón")

#busqueda con sustitucion
print(re.sub(r"\d","*","mpangu8era990"))
print(re.sub(r"\d","*","mpangu8era990",2))

#modificadores del comportamiento del patron

regex=re.compile(r"ab",re.IGNORECASE)
print(regex.search("juntimillaAbasdqewweewr"))
