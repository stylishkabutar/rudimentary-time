import config
import pandas as pd
import numpy as np

# Model Settings
ModelMethod = "COBYLA"
InitialGuessVelocity =25

RaceStartTime = 8 * 3600  # 8:00 am
# RaceEndTime = (17) * 3600  # 5:00 pm
# DT = RaceEndTime - RaceStartTime

Day=1
TimeOffset = 0




# Settings
InitialBatteryCapacity = config.BatteryCapacity
FinalBatteryCapacity = 0
wind_speed=50
Wind_dir=0
slope=3
seg_length=10 
Race_distance=100 * 10 ** 3
seg_array=np.array(list(range(0,Race_distance,seg_length)))

