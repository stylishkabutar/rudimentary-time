import numpy as np
from config import BatteryCapacity, InitialBatteryCapacity
from car import calculate_dt, calculate_power
from solar import calculate_incident_solarpower

def extract_profiles(velocity_profile, segment_array, slope_array, wind_speed, wind_dir):
    start_speeds, stop_speeds = velocity_profile[:-1], velocity_profile[1:]
    ws=wind_speed
    wd=wind_dir
    avg_speed = (start_speeds + stop_speeds) / 2
    dt = calculate_dt(start_speeds, stop_speeds, segment_array)
    acceleration = (stop_speeds - start_speeds) / dt

    P,_ = calculate_power(avg_speed, acceleration, slope_array,ws,wd)
    SolP = calculate_incident_solarpower(dt.cumsum())

    energy_consumption = P * dt /3600
    energy_gain = SolP * dt /3600

    net_energy_profile = energy_consumption.cumsum() - energy_gain.cumsum()
    
    battery_profile = InitialBatteryCapacity - net_energy_profile
    battery_profile = np.concatenate((np.array([InitialBatteryCapacity]), battery_profile))

    battery_profile = battery_profile * 100 / (BatteryCapacity)

    distances = np.append([0], segment_array)

    return [
        distances,
        velocity_profile,
        np.concatenate((np.array([np.nan]), acceleration,)),
        battery_profile,
        np.concatenate((np.array([np.nan]), energy_consumption,)),
        np.concatenate((np.array([np.nan]), energy_gain)),
        np.concatenate((np.array([0]), dt.cumsum())),
    ]