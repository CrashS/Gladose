def insert_sting_middle(str, word, index):
    return str[:index] + word + str[index:]

numbers = ['123456789']
locations = [1,3,5,7,9,11,13,15]

for loci in locations:
    removenumbers = numbers[:]
    for item in range(0,len(numbers)):
        numbers.append(insert_sting_middle(numbers[item], '+', loci))
        numbers.append(insert_sting_middle(numbers[item], '*', loci))
        numbers.append(insert_sting_middle(numbers[item], '_', loci))
    for item in removenumbers:
        numbers.remove(item)

for item in numbers:
    newitem = item.replace('_', '')
    newitem = insert_sting_middle(newitem,'result = ', 0)
    exec(newitem)
    if(result is 100):
