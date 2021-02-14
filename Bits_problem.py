### We are Given an Integer and we need to convert all into an Bits
def append_bits(x,l):
    return [x + element for element in l]

def generate_bit(n):
    if n == 0:
        return []
    if n==1:
        return ["0" ,"1"]
    else:
        return (append_bits("0",generate_bit(n-1))+   
                append_bits("1",generate_bit(n-1)))

if __name__ == "__main__":
    print(generate_bit(3))