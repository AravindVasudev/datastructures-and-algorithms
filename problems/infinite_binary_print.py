##########
# Write a program that infinitely prints the following
# binary pattern:
# 0
# 1
# 00
# 01
# 10
# 11
# 000
# 001
# 010
# 011
# 100
# ...
##########

def binary_print():
    q = ['0', '1']
    while q:
        cur = q.pop(0)

        print(cur)
        q.append(cur + '0')
        q.append(cur + '1')

if __name__ == '__main__':
    binary_print()
