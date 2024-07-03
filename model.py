import numpy as np
from scipy.optimize import minimize
import pandas as pd

from config import InitialGuessVelocity, ModelMethod, seg_array, slope, wind_speed, Wind_dir
from constraints import get_bounds, objective, battery_acc_constraint_func, objective_for_result #, final_battery_constraint_func
from profiles import extract_profiles
from car import calculate_dt

def main(segments, slope, wind_speed, wind_dir):
    segment_array = segments
    slope_array = slope
    winds_array= wind_speed
    winddir_array=wind_dir
    N_V = len(segment_array) + 1
    # velocity_profile = np.ones(N_V) * state.InitialGuessVelocity
    velocity_profile = np.concatenate([[0], np.ones(N_V-2) * InitialGuessVelocity, [0]])

    bounds = get_bounds(N_V)
    constraints = [
        {
            "type": "ineq",
            "fun": battery_acc_constraint_func,
            "args": (
                segment_array, slope_array, winds_array, winddir_array
            )
        },
        # {
        #     "type": "ineq",
        #     "fun": final_battery_constraint_func,
        #     "args": (
        #         segment_array, slope_array, lattitude_array, longitude_array,winds_array,winddir_array
        #     )
        # },
    ]


    print("Starting Optimisation")
    print("=" * 60)

    optimised_velocity_profile = minimize(
        objective, velocity_profile,
        args=(segment_array, slope_array, winds_array, winddir_array),
        bounds=bounds,
        method=ModelMethod,
        constraints=constraints,
        options={
            'disp': True, 'maxiter':5000, 'tol': 1e-6, 
        }
    )
    optimised_velocity_profile = np.array(optimised_velocity_profile.x)*1

    time_taken= objective_for_result(optimised_velocity_profile, segment_array)
    dt = calculate_dt(optimised_velocity_profile[:-1], optimised_velocity_profile[1:], segment_array)
    print(dt)
    print("done.")
    print("Total time taken for race:", time_taken/3600, "hrs")

    outdf = pd.DataFrame(
        dict(zip(
            ['CummulativeDistance', 'Velocity', 'Acceleration', 'Battery', 'EnergyConsumption', 'Solar', 'Time'],
            extract_profiles(optimised_velocity_profile, segment_array, slope_array, winds_array, winddir_array)
        ))
    )
    print((outdf['CummulativeDistance'].cumsum()).iloc[-1]/1000)
    return outdf, time_taken

if __name__ == "__main__":
    outdf, _ = main(seg_array, slope, wind_speed, Wind_dir)
    outdf.to_csv('run_dat.csv', index=False)
    print("Written results to `run_dat.csv`")
