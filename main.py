
def concatenate_strings(*args):
    concatenated = ''
    for string in args:
        concatenated += string
    
    return concatenated

# example_input = 'asd', 'qwe', 'example', 'test'
print(concatenate_strings('asd', 'qwe', 'example', 'test'))


