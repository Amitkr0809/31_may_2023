name = "amit"
enumerate_name = enumerate(name)
print(list(enumerate_name))


set = {1,2,3,4,5}
enumerate_set = enumerate(set)
print(list(enumerate_set))


set_b = {1,2,3,4,5}
enumerate_set = list(enumerate(set_b, 10))
print(enumerate_set)


names = ["Jack", "John", "James"]
for each_name in enumerate(names):
    print(each_name)


names = ["Jack", "John", "James"]
for count, each_name in enumerate(names):
    tuple_a = (count, each_name)
    print(tuple_a)