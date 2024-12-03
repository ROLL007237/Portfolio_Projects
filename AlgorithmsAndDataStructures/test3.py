import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford",'Lambo', None],
  'passings': [3, 7, 2,10,0]
}

myvar = pandas.DataFrame(mydataset)

print(myvar.corr)