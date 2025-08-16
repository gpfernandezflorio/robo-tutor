def algunoCumple(f, l):
  for i in l:
    if f(i):
      return True
  return False