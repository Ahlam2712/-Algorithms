def linear_search(obj,item):
    for i in obj:
        if i==item:
            return f"{item} was found in index{obj.index(item)}"
        else:
            return f"{item} was not fount."
            
            
def binary_search(obj,item):
    low=0
    high=len(obj)-1
    found=False
    mid=None
    while low<=high and not found:
        mid=(low+high)//2
        if item==list[mid]:
            found=True
        elif item>list[mid]:
            low = mid+1
        else:
            high=mid-1
    if found == True:
        print(f"element was found  and index is {mid}")
    else:
        print("was not found")

