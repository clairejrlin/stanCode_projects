

def main():
    number_lst = [1, 1, 2, 5, 10]
    print(can_make_sum(number_lst, 9))


def can_make_sum(lst, target):
    # ans_lst = []
    # can_make_sum_helper(lst, target, [], ans_lst)
    # return sum(ans_lst) >= 1
    return can_make_sum_helper(lst, target, 0, 0)


def can_make_sum_helper(lst, target, current, index):
    if index == len(lst):
        return current == target
    else:
        return can_make_sum_helper(lst, target, current, index+1) or \
               can_make_sum_helper(lst, target, current+lst[index], index+1)


# def can_make_sum_helper(lst, target, current, ans_lst):
#     if len(lst) == 0:
#         if sum(current) == target:
#             ans_lst.append(1)
#         else:
#             ans_lst.append(0)
#     else:
#         ele = lst.pop()
#         # Choose and explore
#         current.append(ele)
#         can_make_sum_helper(lst, target, current, ans_lst)
#         # Not choose and explore
#         current.pop()
#         can_make_sum_helper(lst, target, current, ans_lst)
#         # Un-choose
#         lst.append(ele)


if __name__ == '__main__':
    main()