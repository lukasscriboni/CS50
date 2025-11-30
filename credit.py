def every_other_digit(credit_card):
    total_sum = 0
    alternate = False
    while credit_card > 0:
        last_digit = credit_card % 10
        if alternate:
            total_sum = total_sum + SumandMultiply(last_digit)
        else:
            total_sum = total_sum + last_digit

        alternate = not alternate
        credit_card //= 10
    return total_sum


def SumandMultiply(last_digit):
    multiply = last_digit * 2
    digit_sum = 0
    while multiply > 0:

        last_digit_multiply = multiply % 10
        digit_sum = digit_sum + last_digit_multiply
        multiply = multiply // 10

    return digit_sum


def count_digits(credit_card):
    counter = 0
    while credit_card > 0:
        credit_card = credit_card // 10
        counter = counter + 1

    return counter


def ValidVisa(credit_card, counter_digits):

    firstdigit = credit_card // 10 ** (counter_digits - 1)
    if ((counter_digits == 13 or counter_digits == 16) and (firstdigit == 4)):
        return True
    else:
      return False

def ValidMastercard(credit_card, counter_digits):
    first_two_digits = credit_card // 10 ** (counter_digits - 2)
    if ((counter_digits == 16 and (first_two_digits >= 51 and first_two_digits <= 55 ))):
        return True
    else:
        return False

def ValidAmericanExpress(credit_card, counter_digits):
    two_first_digits = credit_card // 10 ** (counter_digits - 2)
    if ((counter_digits == 15) and (two_first_digits == 34 or two_first_digits == 37)):
        return True
    else:
        return False

def main():

    credit_card = int(input("Card Number:"))
    final_sum = every_other_digit(credit_card)
    counter_digits = count_digits(credit_card)
    amex = ValidAmericanExpress(credit_card, counter_digits)
    master = ValidMastercard(credit_card, counter_digits)
    visa = ValidVisa(credit_card, counter_digits)

    if final_sum % 10 != 0:
        print("INVALID")
        return 0
    elif amex == True:
        print("AMEX")
    elif visa == True:
        print("VISA")
    elif master == True:
        print("MASTERCARD")
    else:
        print("INVALID")
    return 0

main()

