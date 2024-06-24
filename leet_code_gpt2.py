def calculate_next_sequence(sequence):
    new_sequence = []
    for i in range(len(sequence)-1,0,-1):
        next_last_value = sequence[i - 1][-1] if i - 1 < len(sequence) else sequence[-1][-1]  # Get the last value of the next list in the big list
        new_seq = [val + next_last_value for val in sequence[i]]  # Add the last value of the next list to each element in the current list
        new_sequence.append(new_seq)
    return new_sequence

def generate_sequence_difference_lists(sequence):
    sequence_difference_lists = []
    while True:
        differences = calculate_differences(sequence)
        sequence_difference_lists.append(differences)
        if all(element == differences[0] for element in differences[1:]):
            # break
            sequence = calculate_next_sequence(sequence)
            return sequence_difference_lists

def calculate_differences(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i + 1] - sequence[i])
    return differences

def sum_last_elements(sequence_difference_lists):
    total_sum = 0
    for seq_diff_list in sequence_difference_lists:
        total_sum += seq_diff_list[-1]
    return total_sum

def main():
    with open('leet_test.txt', 'r') as file:
        total_sum = 0
        for line in file:
            stripped_line = line.strip()
            space_separated_values = stripped_line.split()
            int_values = [int(value) for value in space_separated_values]
            sequence_difference_lists = generate_sequence_difference_lists(int_values)
            total_sum += sum_last_elements(sequence_difference_lists)
    print("Total sum is:", total_sum)

if __name__ == "__main__":
    main()
