key = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_numbers(text) -> list:
    numbers = []
    for letter in text:
        if letter.isdigit():
            numbers.append(letter)

    return numbers


def replace_numbers(text) -> str:
    modified_text = text
    for val in key:
        modified_text = modified_text.replace(val, key[val])

    return modified_text


numbers = []
calibration_numbers = []
with open("source.txt", "r") as reader:
    for line in reader:
        numbers.append(find_numbers(replace_numbers(line)))


for nums in numbers:
    if len(nums) == 1:
        calibration_numbers.append(int(nums[0] + nums[0]))
    if len(nums) > 1:
        calibration_numbers.append(int(nums[0] + nums[-1]))


print(sum(calibration_numbers))
