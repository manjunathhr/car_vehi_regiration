
Test Description:
Write a test automation suite which does following.

1. Reads given input file: car_input.txt
2. Extracts vehicle registration numbers based on pattern(s).
3. Each number extracted from input file is fed to any car valuation website for e.g. webuyanycar
(Perform vehicle details search car valuation page with random mileage details)
4. Compare the output returned by car valuation website with given car_output.txt
5. Highlight/fail the test for any mismatches. Showcase your skills so it’s easier to add more
input files in future. Utilise any JVM based language with browser automation tools. Use
design patterns where appropriate.


Buy Running 
python3 validate_veh_registration.py 
reads car_input and finds right car registrations, 
then execute playwright chrome and validates the data from car_out.txt  

Note: Currently I am finding 2 card details from webuyanycar



================Sample output ==========================
/home/mramaiah/PythonDev/car-valuation/pythonProject1/.venv/bin/python /home/mramaiah/PythonDev/car-valuation/pythonProject1/car_veh_details/validate_veh_registration.py 
valid number : [['AD58 VNF'], ['BW57 BOW'], ['KT17DLX', 'SG18 HTN']]
['AD58 VNF', 'BW57 BOW', 'KT17DLX', 'SG18 HTN']
Car : AD58VNF
AD58VNF : Error Not Found : None
Car : BW57BOW
BW57BOW : Error Not Found :  If your registration can't be found, you can use our manual lookup. 
Car : KT17DLX
KT17DLX : Error Not Found : None
Car : SG18HTN
SG18HTN : Error Not Found :  If your registration can't be found, you can use our manual lookup. 
Final : [['AD58VNF', 'BMW', '1 SERIES DIESEL COUPE - 120d M Sport 2dr', '2008'], ['BW57BOW', 'Invalid Vehicle'], ['KT17DLX', 'SKODA', 'SUPERB DIESEL ESTATE - 2.0 TDI CR 190 Sport Line 5dr DSG', '2017'], ['SG18HTN', 'Invalid Vehicle']]
Car AD58VNF Matches in Output at index row 2 list exactly.
Car KT17DLX Matches in Output at index row 4 list exactly.
We found 2 Matches

Process finished with exit code 0