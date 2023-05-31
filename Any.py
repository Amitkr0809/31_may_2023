list_a = [True, False]
is_any_true = any(list_a)

print(is_any_true)





dict_a = {"name": "raj","age": 25 }
is_any_true = any(dict_a)
print(is_any_true)




is_true_in_list = any([0, 0, 2, 0])
is_true_in_set = any({"", None, 0})
is_true_in_set1 = any({"", None, 1})
is_true_in_tuple = any(("hello", "world"))

print(is_true_in_list)
print(is_true_in_set)
print(is_true_in_set1)
print(is_true_in_tuple)



