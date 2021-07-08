# 1254732 Mauricio Corado
number_calls = 0                           # keeps count of calls
# Section 14.8.1 helps with this lab


def partition(user_ids, i, k):          # Partition method/function
    partition_indx = i             # sets pivot
    pivot = (i + k) // 2
    while partition_indx <= k:
        while user_ids[partition_indx] < user_ids[pivot]:
            partition_indx = partition_indx+1
        while user_ids[k] > user_ids[pivot]:
            k = k-1
        if partition_indx <= k:                               # partitions data in list
            t = user_ids[partition_indx]
            user_ids[partition_indx] = user_ids[k]
            user_ids[k] = t
            partition_indx = partition_indx + 1
            k = k-1
    return partition_indx


def quicksort(user_ids, i, k):
    global number_calls
    number_calls = number_calls + 1           # increments calls in quicksort method
    if i >= k:
        return
    partition_indx = partition(user_ids, i, k)
    quicksort(user_ids, i, partition_indx-1)
    quicksort(user_ids, partition_indx, k)

if __name__ == "__main__":
    ids = []                    # creates empty list to be populated
    user_id = input()           # receives user input
    while user_id != '-1':          # similar loop as in exercise 12.9 which runs until -1
        ids.append(user_id)
        user_id = input()
    quicksort(ids, 0, len(ids) - 1)         # calls for a quicksort
    print(number_calls)
    for user_id in ids:
        print(user_id)