def mapear(f, l):
  return list(map(f, l))

def algunoCumple(f, l):
  for i in l:
    if f(i):
      return True
  return False

def aplanar(ls):
  nl = []
  for l in ls:
    for x in l:
      nl.append(x)
  return nl

def singularSiEsta(x):
  return [] if (x is None) else [x]