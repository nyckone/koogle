from koogle_engine.koogle import Koogle


def main():
    koogle = Koogle()
    koogle.search("hey yall")
    koogle.search("hey")
    koogle.search("wow")
    koogle.search("hey")
    koogle.search("hello")
    koogle.search("hello")
    koogle.search("hel")
    koogle.search("hel")
    koogle.search("hell")
    koogle.search("hell")
    koogle.search("hell")
    koogle.search("hello")

    print(koogle.suggest("h"))
    print(koogle.suggest("he"))
    print(koogle.suggest("hel"))
    print(koogle.suggest("hell"))
    print(koogle.suggest("hello"))
    print(koogle.suggest("w"))
    print(koogle.suggest(""))


if __name__ == "__main__":
    main()
