##### ------ Busqueda binaria  ------ #####

ordered_list = [2,4,6,8,10]
fish_number = 8

list_to_sum = []

##### Primera fase 
half = len(ordered_list) // 2

list_to_sum.append(half)

if ordered_list[half] == fish_number:
    print("Lo encontrastes !")
if ordered_list[half] < fish_number:
    print(ordered_list[sum(list_to_sum)+1:])
elif ordered_list[half] > fish_number:
    print(ordered_list[:sum(list_to_sum)+1])

###### Segunda fase

# No puede ser no puedo la busqueda binaria, solo puedo la teoria.