import pandas as pd

def compare_car_details_out(my_full_list):

    # Load the CSV file into a DataFrame
    df = pd.read_csv('car_out.txt', header=None)  # Use `header=None` if there are no column names
    count = 0
    for out_ele in my_full_list:
        # Iterate through each row and compare
        for index, row in df.iterrows():
            # Convert the row to a list
            row_list = row.tolist()
            #print(row_list)
            #Compare the list with the row
            if set(out_ele) == set(row_list):
                print(f"Car {out_ele[0]} Matches in Output at index row {index} list exactly.")
                count = count+1
                break

    return count
if __name__ == "__main__":
    full_list = [['AD58VNF', 'BMW', '1 SERIES DIESEL COUPE - 120d M Sport 2dr', '2008'],
                 ['KT17DLX', 'SKODA', 'SUPERB DIESEL ESTATE - 2.0 TDI CR 190 Sport Line 5dr DSG', '2017']]
    compare_car_details_out(full_list)