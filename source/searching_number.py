import random


# Time complexity is 0(n)
def searching_inlist_first_variant(mylist, number):
    for num in mylist:
        if number == num:
            return True
    return False


# Time complexity is 0(nlog(n))
def searching_inlist_second_variant(mylist, number):
    mylist = sorted(mylist)
    list_len = len(mylist)
    if list_len == 0:
        return False
    middle_index = int(list_len / 2)
    middle = mylist[middle_index]
    if number == middle:
        return True
    elif number < middle:
        return searching_inlist_second_variant(mylist[0:middle_index], number)
    elif number > middle:
        return searching_inlist_second_variant(mylist[middle_index + 1:list_len], number)


def generate_unique_numbers(X):
    unique_numbers = set()
    while len(unique_numbers) < X:
        unique_numbers.add(random.randint(1, X * 10))
    return list(unique_numbers)
