s = set()
s.add(20)
s.add(20.0)
s.add('20')  # length of s after these operations
# due to python ,it does,nt care about data type if it is umarrically equal like 20 and 20.0
print(s)