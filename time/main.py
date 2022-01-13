A, B, C, D = 0, 0, 0, 0
#
# while A <= 10:
#     A += 2
#     if A%3 == 0:
#         B += 1
#     else:
#         C += 1
#     D += 1
#
#     print(A)
#
# print(f"{A}, {B}, {C}, {D}")

for N in range(11):
    if N%2 == 0:
        A += 1
    elif N%3 ==0:
        B += 1
    else:
        C += 1

    print(f"{A}, {B}, {C}, {N}")


print(f"\n\n{A}, {B}, {C}, {N}")