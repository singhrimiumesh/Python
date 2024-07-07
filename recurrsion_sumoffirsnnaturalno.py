def sum_of_first_n_nutural_no(n):
    if n == 0:
        return 0
    return n + sum_of_first_n_nutural_no(n-1)

n = int(input("Enter number: "))

print(sum_of_first_n_nutural_no(n))