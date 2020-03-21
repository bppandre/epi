
def count_bits(x):
    num_bits = 0
    while x:
        print(x)
        num_bits += x & 1
        x>>=1
    print(x)
    return num_bits

def close(x):
    return (x&(x-1))|((x&~(x-1))>>1) if x%2==0 else x+1


print(close(16))
print(close(8))
print(close(24))
print(close(23))
print(close(7))
