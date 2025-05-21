def read_input(filename: str) -> list[str]:
    with open(filename, "r", encoding="UTF-8") as f:
        return f.read().splitlines()
        # return f.readlines()

print(read_input("input.txt"))