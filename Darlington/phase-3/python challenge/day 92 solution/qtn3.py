#program to check whether a given number is an ugly number.
def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

print(is_ugly(12))
print(is_ugly(13))