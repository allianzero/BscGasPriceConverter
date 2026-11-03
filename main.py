""" BscGasPriceConverter: Convert gas price from gwei to wei. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(gwei):
    return gwei * 1e9


def main():
    print(calculate(5))


if __name__ == "__main__":
    main()
