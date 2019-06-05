def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    carDrive=mpg*fuel_left
    if distance_to_pump<=carDrive :
        return True
    elif distance_to_pump>carDrive:
        return False
    