input = [100, 4, 200, 1, 3, 2, 7, 8, 9, 10, 11, 12, 13, 50, 51, 52, 53, 54, 55, 56, 99, 101, 102, 103]


sorted_input = sorted(input)
current_count = 1
max_count = 0

for i in range(len(sorted_input) - 1):
    if sorted_input[i] + 1 == sorted_input[i + 1]:
        current_count += 1
    else:
        # Update max_count if current_count is greater
        if current_count > max_count:
            max_count = current_count
        # Reset current count after a break
        current_count = 1

# Final update after the loop ends to ensure the last sequence is considered
if current_count > max_count:
    max_count = current_count

print(max_count)
