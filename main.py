from utils import print_happy, print_info, print_not_happy


def is_happy_number(number: int) -> bool:
    """
    Determine if the input number is happy number or not.

    :param number: Input number.
    :return: True if the number is happy number False if is not.
    """
    seen_number = set()

    while True:
        if number == 1:
            return True
        if number in seen_number:
            return False

        seen_number.add(number)
        sum_ = 0

        while number:
            digit = number % 10
            sum_ += digit ** 2
            number = number // 10
        number = sum_


if __name__ == '__main__':
    while True:
        user_number = input('Please enter a whole number (q to exit): ')
        if user_number.lower() == 'q':
            print_info('Exiting the app...')
            break
        try:
            user_number = int(user_number)
            if user_number < 0:
                print_info('Negetive numbers are not allowed. Please try again.')
                continue
        except ValueError:
            print_info('Invalid input. Please try again.')
            continue

        if is_happy_number(user_number):
            print_happy(f'{user_number} is a happy number!')
        else:
            print_not_happy(f'{user_number} is not a happy number!')
