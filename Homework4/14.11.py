# 1254732 Mauricio Corado

def selection_sort_descend_trace(numbers):  # section 14.6 in the book helped with the layout since it was similar
    for i in range(len(numbers) - 1):
        small_indx = i
        for j in range(i + 1, len(numbers)):        # nested loops used
            if numbers[small_indx] < numbers[j]:
                small_indx = j
        temporary = numbers[i]                  # used to swap the numbers
        numbers[i] = numbers[small_indx]
        numbers[small_indx] = temporary
        for num in numbers:                 # iterates through the list and prints
            print(num, end=' ')
        print()
    return numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input('').split()]                 # splits the input
    selection_sort_descend_trace(numbers)   # calls the method