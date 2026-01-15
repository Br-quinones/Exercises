# Create a function that takes two arrays, a boolean, and returns an array.
# - If the boolean is true, it will search for and return the common elements
# of the two arrays.
# - If the boolean is false, it will search for and return the non-common elements
# of the two arrays.
# - Language operations that directly resolve this, such as '&' or '^', cannot be used.

def set_without_set(list_01: list, list_02: list, bool_01: bool):
    list_to_return = []
    
    if bool_01:
        for number_01 in list_01:
            for number_02 in list_02:
                if number_01 == number_02 and number_02 not in list_to_return:
                    list_to_return.append(number_02)
    else:
        for number_01 in list_01:
            if number_01 not in list_02:
                list_to_return.append(number_01)

        for number_02 in list_02:
            if number_02 not in list_01:
                list_to_return.append(number_02)

    return list_to_return

user_list_01 = [3,5,8,10,10,11,45]
user_list_02 = [2,2,9,10,10,-1,10,10]

print(set_without_set(user_list_01, user_list_02, False))

# 45 minutes