# from numpy import zeros, int


# def permutations(n, length):
#     numbers = range(n)
#     permutations = n**length
#     output = zeros((permutations, length), dtype=int)

#     for i in range(length):
#         t2 = n**i
#         p1 = 0
#         while (p1 < permutations):
#             for al in range(n):
#                 for p2 in range(t2):
#                     output[p1, i] = numbers[al]
#                     p1 += 1
#     return output


# def find_combination(choices, total):
#     """
#     choices: a non-empty list of ints
#     total: a positive int

#     Returns result, a numpy.array of length len(choices)
#     such that
#         * each element of result is 0 or 1
#         * sum(result*choices) == total
#         * sum(result) is as small as possible
#     In case of ties, returns any result that works.
#     If there is no result that gives the exact total,
#     pick the one that gives sum(result*choices) closest
#     to total without going over.
#     """
#     result_x_choices = 0
#     all_permutations = permutations(2, len(choices))
#     for result in all_permutations:
#         for i in range(len(result)):
#             result_x_choices += result[i]*choices[i]
#             sum_of_result = sum(result)
#         # TODO: check if any of the result_x_choices == total
#         print(result_x_choices)


# print(find_combination([1,2,2], 1))


def permutations_recur(lst, num, max_depth, result_list, depth=0):
    if depth < max_depth:
        lst.append(num)
        depth += 1
        permutations_recur(lst[:], 0, max_depth, result_list, depth)
        if depth < max_depth:
            # if max depth already reached with "permutations_recur(lst[:], 0, max_depth, result_list, depth)"
            # don't call this line bc it would append the same list to result_list.
            # not nice, need to find proper break condition.
            permutations_recur(lst[:], 1, max_depth, result_list, depth)
    else:
        result_list.append(lst)
        return


def gen_permutations(n):
    permutations = []
    max_depth = n
    permutations_recur([], 0, max_depth, permutations)
    permutations_recur([], 1, max_depth, permutations)
    return permutations


print(gen_permutations(3))
