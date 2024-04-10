import re

if __name__=="__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    pattern  = '(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4", 
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    # Extract all valid numbers from each line
    numbers_list: list[list[str]] = [re.findall(pattern, line) for line in lines]
    
    # Transform written numbers to digits
    numbers_list_transformed = []
    for inner_list in numbers_list:
        inner_list = [mapping[item] if item in mapping else item for item in inner_list]
        numbers_list_transformed.append(inner_list)
    
    # Combine the first and last element in each inner list to form a number
    # If a list has only one element then simply repeat it.
    result: list[str] = [f"{inner_list[0]}{inner_list[-1]}" if len(inner_list) > 1 else f"{inner_list[0]}{inner_list[0]}" for inner_list in numbers_list_transformed] 
    result: list[int] = [int(element) for element in result]
    
    print(sum(result))