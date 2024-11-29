
from get_car_information import get_car_valuation
from get_all_registration import find_registration_words
from get_csv_compare import compare_car_details_out

def get_car_reg_from_web():

    all_reg = find_registration_words("car_input.txt")
    print(all_reg)
    result1 = list()
    mileage_value = 15000  # Replace with the car's mileage

    for num in all_reg:
        num = num.replace(' ', '')
        print("Car :", num)
        res = get_car_valuation(str(num), mileage_value)
        result1.append(res)

    print(f"Final : {result1}")
    num_matches = compare_car_details_out(result1)
    print(f"We found {num_matches} Matches")

if __name__ == "__main__":
    get_car_reg_from_web()