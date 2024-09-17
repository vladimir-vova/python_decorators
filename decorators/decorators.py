def fout(func):
    def wrapper(*args):
        print("Start")
        result = func(*args)
        print("End")
        return result
    return wrapper

@fout
def summ(a, b):
    return a + b


if __name__ == "__main__":
    print(summ(1, 2))