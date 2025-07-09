#wap to print the elements of a list in single line (list is the parameter)
subject=["math","physics","chemistry"]
def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(subject)
