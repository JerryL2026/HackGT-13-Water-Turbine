# HackGT-13-Water-Turbine
A Python-based optimization algorithm developed for a water turbine that competed in HackGT 13 (2026) in the Social Good and Hardware categories.
This project investigates the benefits from hydrokinetic turbines in terms of optimizing the generation of energy using the adjustment of the turbine orientation according to the movement of water.

The code in the repository is for optimizing the process and finding an optimal turbine orientation through the electrical energy output.

How the Optimization Logic Works:
1. Evaluates an orientation and considers and turbine angle
2. Electrical output of the turbine at the angle is measured in voltage
3. If the measured voltage improves from previous measures the algorithm continues turning the turbine angle in the direction
- If the measured voltage worsens the direction of measurement changes
4. Runs algorithm periodically to continuously turn the turbine to the angle with most voltage output

# Project Context

This project was conceived as part of HackGT 13, a 36-hour hackathon. Our team comprised members from:
- Computer Science
- Mechanical Engineering
- Environmental Engineering
- Aerospace Engineering

# Social Impact

The availability of renewable energy is a problem for communities whose energy sources are scarce or expensive. This project investigates the possibility of harnessing hydrokinetic energy for the purpose of producing energy from water.
