Carbon Footprint Tracker

Overview:-
This program calculates the CO2 savings for a trip based on various parameters such as distance, fuel type, traffic conditions, number of riders, idle time, and whether the trip occurs at night. The result is displayed in grams of CO2 savings.

Features:-
- Calculates CO2 emissions based on:
- Distance traveled.
- Type of fuel used (petrol, diesel, electric vehicle).
- Traffic conditions (light, moderate, heavy).
- Number of riders.
- Idle time during the trip.
  - Night-time adjustment.
- Displays the calculated CO2 savings in grams.

Requirements:-
- Python 3.x installed on your system.

How to Run the Program:-
1. Clone or download the script file.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the command:
    python co2_savings_calculator.py

Inputs:-
When prompted, provide the following details:
1. Distance: Enter the trip distance in kilometers (e.g., 50).
2. Fuel Type: Specify the type of fuel used ('petrol', ' diesel' or 'ev' for electric vehicle).
3. Traffic Condition: Indicate the traffic level ('light', 'moderate' or 'heavy').
4. Number of Riders: Enter the number of riders in the vehicle (must be an integer greater than 0).
5. Idle Time: Enter the idle time in minutes (e.g., 5).
6. Night-Time: Specify whether the trip occurs at night by entering yes or no.

Output:-
- The program calculates the CO2 savings and displays the result in grams:
  CO2 Savings: <value> grams
  
Code Explanation:-
1. CO2 Calculation Logic:
- A base emission rate of 251 grams per kilometer is used.
- Adjustments are applied based on:
- Fuel type ('petrol', 'diesel', or 'ev').
- Traffic conditions (light', 'moderate', 'heavy').
- Night-time (a slight reduction if it's night).
- Idle time.
- Number of riders to distribute emissions.
- The formula used:
 co2_savings = distance * base_emission * fuel_adjustment * traffic_adjustment * (1 - 1 / number_of_riders) * night_time_adjustment + idle_emissions
     
2. Input Handling:
- User inputs are validated to ensure correct values are provided.

3. Output:
- The calculated CO2 savings are displayed in grams.

Example:-

Input: 

Enter distance (in kilometers): 70

Enter fuel type (petrol,diesel,ev): petrol

Enter traffic condition (light,moderate,heavy): moderate

Enter number of riders: 3

Enter idle time (in minutes): 15

Is it night_time (yes/no): no

Output:

CO2 Savings: 13034.666666666668 grams
