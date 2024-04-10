import re

if __name__=="__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    # Extract the numbers from each line of text
    numbers_list: list[list[str]] = [re.findall("\d", line) for line in lines]

    # Combine the first and last element in each inner list to form a number
    # If a list has only one element then simply repeat it.
    result: list[str] = [f"{inner_list[0]}{inner_list[-1]}" if len(inner_list) > 1 else f"{inner_list[0]}{inner_list[0]}" for inner_list in numbers_list] 
    result = [int(element) for element in result]

    print(sum(result))