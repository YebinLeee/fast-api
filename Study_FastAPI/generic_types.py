
''' Generic Types '''


from typing import List, Set, Tuple, Dict, Union, Optional

# List
def process_items(items:List[str]):
    for item in items:
        print(item)
        
# Tuple, Set
def process_items2(items_t:Tuple[int, int, str], items_s:Set[bytes]):
    return items_t, items_s

# Dict
def process_items3(prices:Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, ": ", item_price)

# Union
def process_items4(item:Union[int, str]):
    print(item)

# Optional (possibly none)
def say_hi(name:Optional[str]=None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello world")
        
        
        
        
process_items(["abs", "fds", "erw", "bmd"])
print(process_items2([3, 5, "bubble"], [123,432,623]))
process_items3({"banana":3.24, "apple":2.62})
process_items4("Yebinsss")
say_hi("Yebinee")
say_hi()

