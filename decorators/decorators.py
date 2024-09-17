
def summ(a, b):
    return a + b

def fout(func):
    print("Start")
    print("End")
    return func


if __name__ == "__main__":
    print(fout(summ))