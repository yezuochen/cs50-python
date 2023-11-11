def main():
    # yell(["This", "is", "cs50"])
    yell("This", "is", "cs50")

def yell(*words):
    # print(phrase.upper())
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())

    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
