def main():
    display_list()


def display_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            for i, n in sorted(grocery_list.items()):
                        print(n, i)
            break

main()