def is_sum_two(numbers, res):
    watched = set()
    for n in numbers:
        if res - n in watched:
            return True
        watched.add(n)
    return False
#
# def max_negative_repr(numbers):
#     num_set = set(numbers)
#     res = -1
#     for n in num_set:
#         if n > res and -n in num_set and n > 0:
#             res = n
#     return res

def max_negative_repr(numbers):
        num_set = set(numbers)
        return max((n for n in num_set if n > 0 and -n in num_set), default=-1)