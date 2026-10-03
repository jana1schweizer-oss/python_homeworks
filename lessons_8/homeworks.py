def calculate_fuel(distance, fuel_per_100, tank_capacity):
    total_fuel = (distance / 100) * fuel_per_100
    refuels = total_fuel / tank_capacity
    return total_fuel, refuels
