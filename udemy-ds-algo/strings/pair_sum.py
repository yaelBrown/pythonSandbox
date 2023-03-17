def pair_sum(arr, val):
    if len(arr) == 0:
        return 0

    sum_of_pairs = set()

    for n in arr:
        check = val - n

        if check in arr:
            if check not in sum_of_pairs:
                sum_of_pairs.add(check)
        else:
            continue

    print(sum_of_pairs)
    return len(sum_of_pairs)


ans1 = pair_sum([1, 3, 2, 2], 4)

print(ans1)


def pair_sum(arr, k):

    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    return len(output)
