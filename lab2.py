def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    nums = get_user_input()
    calc_average(nums)
    sorted=sort_temperature(nums)
    print(f"Sorted List {sorted}")
    find_min_max(sorted)
    calc_median_temperature(nums)



def display_main_menu():
    print("Hi:)")

def get_user_input():
    num_list = []
    
    for i in range(5):   # loop 5 times
        user = input("Enter numbers separated by commas: ")
        sep = user.split(",")
        
        for item in sep:
            num_list.append(float(item.strip()))
    unique = list(set(num_list))
    return unique
def calc_average(num_list):
    total=sum(num_list)
    amount=len(num_list)
    average=total/amount
    print(f"The average is {average:.2f}")

def find_min_max(index):
    extreme=max(index)
    notex=min(index)
    print(f"Maximum is {extreme}")
    print(f"Minimum is {notex}")

def sort_temperature(num_list):
    return sorted(num_list)


def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    
    if n % 2 == 1:   # odd
        median = sorted_list[n // 2]
    else:            # even
        mid1 = sorted_list[n // 2]
        mid2 = sorted_list[n // 2 - 1]
        median = (mid1 + mid2) / 2
    
    print(f"Median is {median:.2f}")

main()