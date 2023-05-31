is_true_in_list = all([0, 0, 2, 0])
is_true_in_set = all({"", None, 0})
is_true_in_tuple = all(("hello", "world"))

print(is_true_in_list)
print(is_true_in_set)
print(is_true_in_tuple)