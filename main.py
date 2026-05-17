def concatenate_strings(*args):
    concatenated = ""
    for string in args:
        concatenated += string

    return concatenated


def get_string_length(string):
    return len(string)


def reverse_string(string):
    return string[::-1]


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count


# example_input = 'asd', 'qwe', 'example', 'test'
print(concatenate_strings("asd", "qwe", "example", "test"))
