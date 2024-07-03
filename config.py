import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------------------------------------
# Car Data

# Battery
BatteryCapacity = 3055 # Wh
DeepDischargeCap = 0.2

# Physical Attributes
R_In = 0.214 # inner radius of wheel
R_Out = 0.2785  # outer radius of wheel
Mass = 267 # kg
Wheels = 3
StatorRotorAirGap = 1.5 * 10**-3

# Resistive Coeff
ZeroSpeedCrr = 0.0045
FrontalArea = 1 # m^2
Cd = 0.092# coefficient of drag
CDA = Cd * FrontalArea

# Solar Panel Data
PanelArea = 6 # m^2
PanelEfficiency = 0.19

# Bus Voltage
BusVoltage = 4.2 * 38  # V

# ---------------------------------------------------------------------------------------------------------
# Physical Constants
AirDensity = 1.192 # kg/m^3
g = GravityAcc = 9.81 # m/s^2
AirViscosity = 1.524 * 10**-5  # kinematic viscosity of air
Ta = 295

# ---------------------------------------------------------------------------------------------------------
# Car Constraints
MaxVelocity = 35 # m/s
MaxCurrent = 12.3  # Am
MaxAcc=0.1

# ---------------------------------------------------------------------------------------------------------
# Race config settings

# Model Settings
ModelMethod = "COBYLA"
InitialGuessVelocity = 25
seg_length= 5000 

# Race settings
RaceStartTime = 8 * 3600 
wind_speed=3
Wind_dir=180
slope=0
Race_distance=800 * 10 ** 3
dist_array=np.array(list(range(0,Race_distance,seg_length)))
seg_array=dist_array[1:]-dist_array[:-1]
 
#Baterry Settings
InitialBatteryCapacity = BatteryCapacity
FinalBatteryCapacity = 0


