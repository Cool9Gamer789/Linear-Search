import sys

# PUT YOUR ARRAY HERE
array = [10,7,8,6,4,5,3,2,1,9]

try:
    search = int(input("What do you want to search for? "))
except ValueError:
    sys.exit("Must type in a number")

def Lsearch(array, search):
    # Iterates through the array
    for i in range(len(array)):
        if int(array[i]) == search:
            return f"Index: {i}"

    # After completeing iteration through for loop -> return not found 
    return "Not Found"

# Print the return value strings 
print(Lsearch(array, search))
