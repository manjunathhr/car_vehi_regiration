import re

def substring_after(s, dlim):
    return s.partition(dlim)[2]

def validate_number(num):
    uk_pattern1 = r'^[A-Z]{2}\d{2} [A-Z]{3}$'
    uk_pattern2 = r'^[A-Z]{2}\d{2}[A-Z]{3}$'

    if num.find(' ') == -1:
        regex = re.compile(uk_pattern2)
        if regex.match(num):
            return True
        return False
    else:
        regex = re.compile(uk_pattern1)
        if regex.match(num):
            return True
        return False

def check_veh_num(num_list):
    valid_reg_num = []
    for x in num_list:
        num = x.replace('.', '')
        if (len(x) > 5) & validate_number(num):
            valid_reg_num.append(num)
    return valid_reg_num

def find_registration_words(filename):
    valid_numbers = list()
    # Open the file and read line by line
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if len(line) == 1:
                continue
            reg = substring_after(line, "registration")
            new_s = [i for i in reg if re.findall('^[A-Z\d_\W]+$', i)]
            reg_num = ''.join(new_s)
            reg2 = [x.strip() for x in reg_num.split("  ") if x.strip()]
            if reg2:
                valid_numbers.append(check_veh_num(reg2))
    print("valid number :", valid_numbers)
    return [x for xs in valid_numbers for x in xs]

if __name__ == "__main__":
    #Example usage
    all_reg = find_registration_words("car_input.txt")
    print(all_reg)