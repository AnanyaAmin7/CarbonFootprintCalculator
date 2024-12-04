def calculate_co2_savings(distance,fuel_type,traffic_condition,number_of_riders,idle_time_minutes,is_night_time):
    base_emission=251
    fuel_adjustment=1.0
    if fuel_type=='diesel':
        fuel_adjustment=1.15
    elif fuel_type=='petrol':
        fuel_adjustment=1.0
    elif fuel_type=='ev':
        fuel_adjustment=0.0
    traffic_adjustment=1.0
    if traffic_condition=='moderate':
        traffic_adjustment=1.10      
    elif traffic_condition=='heavy':
        traffic_adjustment=1.20
    idle_emissions=idle_time_minutes * 10
    night_time_adjustment=0.95 if is_night_time else 1.0
    co2_savings=distance*base_emission*fuel_adjustment*traffic_adjustment*(1-1/number_of_riders)*night_time_adjustment+idle_emissions
    return co2_savings
if __name__=="__main__":
    distance=float(input("Enter distance (in kilometers): "))
    fuel_type=input("Enter fuel type (petrol,diesel,ev): ").lower()
    traffic_condition=input("Enter traffic condition (light,moderate,heavy): ").lower()
    number_of_riders=int(input("Enter number of riders: "))
    idle_time_minutes=int(input("Enter idle time (in minutes): "))
    is_night_time=input("Is it night_time (yes/no): ").lower() == 'yes'
    savings=calculate_co2_savings(distance,fuel_type,traffic_condition,number_of_riders,idle_time_minutes,is_night_time)
    print(f"CO2 Savings: {savings} grams")
