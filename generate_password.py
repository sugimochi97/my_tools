import random

def generate_password(mozisu=10):

    komozi = [chr(i) for i in range(ord("a"), ord("z")+1)]
    oomozi = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    suzi = [str(i) for i in range(10)]
    kigou = ["&", "@", "_"]

    use_chr = komozi + oomozi + suzi + kigou

    password = ""
    for i in range(mozisu):
        password += random.choice(use_chr)

    return password

if __name__ == "__main__":
    print(generate_password(12))