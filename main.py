import random

def get_random_number(number_from, number_to):
    x=random.randint(number_from, number_to)
    return x

def get_sequence_of_numbers(number_of_numbers, number_from, number_to):
    sequence = []
    for x in range(number_of_numbers):
        sequence.append(int(get_random_number(number_from, number_to)))
    return sequence

def main():
    number_of_numbers = int(input("Enter the number of numbers in the sequence: "))
    number_from = int(input("The numbers in the sequence will be generated from: "))
    number_to = int(input("to: "))
    sequence = get_sequence_of_numbers(number_of_numbers, number_from, number_to)
    while sequence.count(sequence[0])!=len(sequence):
        sequence = get_sequence_of_numbers(number_of_numbers, number_from, number_to)
        print(sequence)

    input("Press \"Enter\" to exit")

main()
