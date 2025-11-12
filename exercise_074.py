# Genera la sucesion de look and say

def look_and_say(number):
    if number <= 1:
        return "1"
    
    string_to_return = "1"

    for _ in range(number):
        set_unit= ""
        for unit in string_to_return:
            if unit not in set_unit:
                set_unit += str(unit)
            else:
                string_to_return += set_unit
                set_unit = ""
                
    return string_to_return

print("----------", look_and_say(83))

# 1 
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221