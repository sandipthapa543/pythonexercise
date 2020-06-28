def swap(str1, str2):
  str =str1.replace('c', 'z')
  strs =str2.replace('z', 'c')
  return ''.join(strs) + '  '+ '' .join(str)


print(swap('abc', 'xyz'))



