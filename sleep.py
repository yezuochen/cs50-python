def main():
    n = int(input("What's n? "))

    # for i in range(n):
    #     # print("sheep" * i)
    #     print(sheep(i))
    for s in sheep(n):
        print(s)

# def sheep(n):
#     # return "sheep" * n
#     flock = []
#     for i in range(n):
#         flock.append("sheep" * i)
#     return flock

# generator
def sheep(n):
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()