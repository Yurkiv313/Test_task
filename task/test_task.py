import datetime


def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]


def sort_numbers(numbers):
    return sorted(numbers)


def find_min_and_max(sorted_list):
    return sorted_list[0], sorted_list[-1]


def find_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (sorted_list[mid1] + sorted_list[mid2]) / 2


def calculate_mean(sorted_list):
    return sum(sorted_list) / len(sorted_list)


def find_sequence(numbers, increasing=True):
    max_length = 1
    current_length = 1
    max_sequence = []
    current_sequence = [numbers[0]]

    for i in range(1, len(numbers)):
        if increasing:
            condition = numbers[i] >= numbers[i - 1]
        else:
            condition = numbers[i] <= numbers[i - 1]

        if condition:
            current_sequence.append(numbers[i])
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_sequence = list(current_sequence)
        else:
            current_sequence = [numbers[i]]
            current_length = 1

    return max_sequence


def main():
    start_time = datetime.datetime.now()

    file_path = '/Users/macbookair/Desktop/10m.txt'  # вкажіть свій шлях до файлу
    numbers = read_numbers_from_file(file_path)
    sorted_numbers = sort_numbers(numbers)

    min_number, max_number = find_min_and_max(sorted_numbers)
    print('Найменше число:', min_number)
    print('Найбільше число:', max_number)

    median = find_median(sorted_numbers)
    print('Медіана:', median)

    mean = calculate_mean(sorted_numbers)
    print('Середнє арифметичне:', mean)

    increasing_sequence = find_sequence(numbers, increasing=True)
    print("Зростаюча послідовність:", increasing_sequence)

    decreasing_sequence = find_sequence(numbers, increasing=False)
    print("Спадна послідовність:", decreasing_sequence)

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f'Програма працювала {elapsed_time}')


if __name__ == "__main__":
    main()
