
def shiny_gold_size(values, value=1, bag="shiny gold bag", res=0):
    stores = values[bag]
    if not stores:
        return res
    for k, v in stores.items():
        res += v * value
        res = shiny_gold_size(values, v * value, k, res)
    return res


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
                    formatted_values[key][name] = int(amount)
                else:
                    formatted_values[key] = None
        print(formatted_values)
    print(f"Result is {shiny_gold_size(formatted_values)}")


if __name__ == "__main__":
    main()
