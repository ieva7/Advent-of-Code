import hashlib

if __name__ == "__main__":

    for i in range(1000000000):
        string = "bgvyzdsv" + str(i)
        result = hashlib.md5(bytes(string, 'utf-8'))

        result = result.hexdigest()

        if str(result)[:6] == "000000":
            print(i)
            break