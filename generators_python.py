# generators python
# list comprehension also uses generators

# examples

def csv_reader(file_name):
    for row in open(file_name,'r'):
        yield row

gen= csv_reader()
print(next(gen))
print(next (gen))

