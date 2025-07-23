# THIS PROGRAM CALCULATES THE COMPUTATIONL ENERGY CONSUMPTION BASED ON THE USER INPUT VALUES FOR SMALL-SCALE COMPUTING SYSTEMS

def estimate_energy(power_per_op, num_operations): 

    total_energy = power_per_op * num_operations  # RAW ENERGY IN WATT-OPERATIONS

    # num_operations LOGIC
    if num_operations >= 500_000:
        efficiency_factor = 0.95
    else:
        efficiency_factor = 1.0

    adjusted_energy = total_energy * efficiency_factor

    # OVERHEAD ENERGY LOGIC
    if adjusted_energy < 500:
        overhead = 5
    else:
        overhead = 2

    final_energy_consumption = adjusted_energy + overhead

    return {
        "raw_energy": total_energy,
        "efficiency_factor": efficiency_factor,
        "adjusted_energy": adjusted_energy,
        "overhead": overhead,
        "final_energy": final_energy_consumption
    }

if __name__ == "__main__":
    
    power_per_op = float(input("Enter power consumption per operation (watts): "))
    num_operations = int(input("Enter number of operations: "))

    results = estimate_energy(power_per_op, num_operations)

    print(f"Total raw energy: {results['raw_energy']:.2f} watt-ops")
    print(f"Adjusted energy (efficiency factor {results['efficiency_factor']}): {results['adjusted_energy']:.2f} watt-ops")
    print(f"Overhead energy cost: {results['overhead']:.2f} watts")
    print(f"Final estimated energy consumption: {results['final_energy']:.2f} watt-ops")