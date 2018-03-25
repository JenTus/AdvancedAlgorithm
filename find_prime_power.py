# Given an integer N ∈ Z ≥2 as input, design an algorithm that either
# (i) outputs a prime p and a positive integer a such that N = p a or
# (ii) asserts that N is not a prime power.


# Given integers N, k ∈ Z ≥2 as input, find the largest integer b
# such that b ** k ≤ N .
def find_largest_b(N, k):

    def next_b(b_pre, b_next):
        if k ** b_next < N:
            return next_b(b_next, 2 * b_next)
        elif k ** b_next == N:
            return b_next
        else:
            if (b_pre + b_next) / 2 == b_pre:
                return b_pre
            else:
                return next_b(b_pre, (b_pre + b_next) / 2)

    return next_b(1, 1)


find_largest_b(8, 2)
