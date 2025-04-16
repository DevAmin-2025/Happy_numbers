"""
Provide different and colorful ways to print text.
"""


from termcolor import colored


def print_happy(text: str):
    print(colored(text, 'green', attrs=['reverse']))


def print_not_happy(text: str):
    print(colored(text, 'red', attrs=['reverse']))


def print_info(text: str):
    print(colored(text, 'white', attrs=['reverse']))
