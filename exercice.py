import math
import copy
import itertools


def get_even_keys(dictionary):
    return set([i for i in dictionary if i%2==0])


def join_dictionaries(dictionaries):
    result = {}
    for _ in dictionaries:
        result.update(_)

    return result
    #return {**dictionaries[0], **dictionaries[1]}


def dictionary_from_lists(keys, values):
    result = {}

    for i in range(min(len(keys),len(values))):
        result[keys[i]] = values[i]

    return result


def get_greatest_values(dictionnary, num_values):
    values = [x for x in dictionnary.values()]
    result = []
    for _ in range(num_values):
        result.append(max(values))
        values.remove(max(values))

    return result



def get_sum_values_from_key(dictionnaries, key):
    sum = 0
    for d in dictionnaries:
        if key in d:
            sum += d[key]

    return sum


if __name__ == "__main__":
    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    print(get_even_keys(yeet))
    print()

    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    doot = {
        0xBEEF: "doot",
        0xDEAD: "DOOT",
        0xBABE: "dOoT"
    }
    print(join_dictionaries([yeet, doot]))
    print()

    doh = [
        "D'OH!",
        "d'oh",
        "DOH!"
    ]
    nice = [
        "NICE!",
        "nice",
        "nIcE",
        "NAIIIIICE!"
    ]
    print(dictionary_from_lists(doh, nice))
    print()

    nums = {
        "nice": 69,
        "nice bro": 69420,
        "AGH!": 9000,
        "dude": 420,
        "git gud": 1337
    }
    print(get_greatest_values(nums, 1))
    print(get_greatest_values(nums, 3))
    print()

    bro1 = {
        "money": 12,
        "problems": 14,
        "trivago": 1
    }
    bro2 = {
        "money": 56,
        "problems": 406
    }
    bro3 = {
        "money": 1,
        "chichis": 1,
        "power-level": 9000
    }
    print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
    print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
    print()
