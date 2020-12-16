
def can_store_shiny_gold(values, bag):
    stores = values[bag]
    if not stores:
        return False
    for k, v in stores.items():
        if k == "shiny gold bag":
            return True
        else:
            if not can_store_shiny_gold(values, k):
                continue
            else:
                return True
    return False


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        formatted_values = {}
        for line in lines:
            key, values = line.split(" contain ")
            key = key[:-1]
            values = values.split(", ")
            formatted_values[key] = {}
            for value in values:
                value = value.replace("bags", "bag").replace(".", "")
                amount, name = value.split(" ", 1)
                if amount != "no":
                    formatted_values[key][name] = amount
                else:
                    formatted_values[key] = None
        res = 0
        for bag, values in formatted_values.items():
            if can_store_shiny_gold(formatted_values, bag): res += 1
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
