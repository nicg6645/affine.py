import sympy
def encrypto(a,b,c,d):
  l = list(c)
  g = []
  for entry in l:
      e = ord(entry) - 97
      f = ((a*e + b)%d)
      g.append(chr(f+97))
  return ''.join(g)
def decrypto(a,b,c,d):
  from sympy import mod_inverse
  y = mod_inverse(a,d)
  l = list(c)
  g = []
  for entry in l:
      e = ord(entry) - 97
      f = ((y*(e - b))%d)
      g.append(chr(f+97))
  return ''.join(g)
print(encrypto(5,8,'jamflowman',26))
print (decrypto(5,8,'biqhlaoqiv',26))




