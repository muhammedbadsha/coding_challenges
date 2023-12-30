
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# lookup = {
#     13:[65,89,98,33,65,878],
#     24:[98,54,123,235,67],
#     33:[43,76,9],
#     41:[4,13,23,56,89,00,87,654,789,54],
#     88:[13,33],
#     98:[88,76,77,55,32]
# }
# arr = [4,13,98,54,88,16,33]
class Heap:
    def check_match_numbers(self,arr , lookup ):
        val=int(input(f"enter a key list {[lookup.keys()]} :"))
        find = lookup[val]
        count = 0
        i = 0
        if len(find) < len(arr):
            
            while i < len(find):
                j = 0
                while j < len(arr):
                    if find[i] == arr[j]:
                        count += 1
                    j += 1
                i += 1
        else:
            while i < len(arr)-1:
                j = 0
                while j < len(find)-1:
                    if find[i] == arr[j]:
                        count += 1
                    j += 1
                i =+ 1
            
        return f"as it matches upto {count} values given in the list"
        
    def create_a_sample_array(self):
        size = int(input('enter the size of an array: '))
        arr=[]
        for i in range(size):
            num = int(input('enter number :'))
            arr.append(num)
            
        return arr
        
    def create_sample_table_data(self):
        rows = int(input("how many rows you want: "))
        lookup = {}
        
        for i in range(rows):
            valuesof =  list(input("enter the values like this format key,size eg = 12,32 :").split(','))
            keys_value,size_of_value = [int(i) for i in valuesof]
            lookup[keys_value] = []
            for j in range(size_of_value):
                numbers = int(input("enter numbers"))
                lookup[keys_value].append(numbers)
        return lookup
            
obj = Heap()
lookup = obj.create_sample_table_data()
print(lookup)
arr = obj.create_a_sample_array()
print(arr)
result = obj.check_match_numbers(arr, lookup)
print(result)
