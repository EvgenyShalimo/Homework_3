lst = 'The cat sat on the mat'
lst = lst.lower()
lst = lst.split() 
res = {x:lst.count(x) for x in lst}
print(max(res, key=res.get))