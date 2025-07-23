# Energy Consumption Estimator for Small-Scale Computing Systems

This program estimates the computational energy consumption of small-scale computing systems based on user-provided inputs. It calculates the total energy used by a given number of operations, applies efficiency factors for large workloads, and accounts for overhead energy costs.

---

## Features

- Calculates raw energy consumption as the product of power per operation and number of operations.
- Adjusts energy based on efficiency factor when operation counts are large.
- Adds overhead energy based on the adjusted energy consumption.
- Outputs detailed breakdown of energy components and final estimate.

---

## Usage

Run the program and provide the following inputs when prompted:

1. **Power consumption per operation** (in watts)
2. **Number of operations**

Example:

```bash
Enter power consumption per operation (watts): 0.002
Enter number of operations: 600000
