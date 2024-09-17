
def summ(a, b):
    return a + b

def fout(func):
    def wrapper(a, b):
        print("Start")
        result = func(a, b)
        print("End")
        return result
    return wrapper


if __name__ == "__main__":
    summ = fout(summ)
    print(summ)