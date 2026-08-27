# 1D Heat Equation Solver

A numerical solver for the one-dimensional heat equation using an explicit finite-difference method in Python.

## Overview

This project solves the 1D heat equation for a rod with fixed boundary temperatures.

The heat equation is:

∂T/∂t = α ∂²T/∂x²

where:

* T is the temperature
* t is time
* x is position along the rod
* α is the thermal diffusivity

The equation is solved numerically using the explicit finite-difference method.

## Numerical Method

The second spatial derivative is approximated using the central finite-difference formula:

∂²T/∂x² ≈ (Tᵢ₋₁ - 2Tᵢ + Tᵢ₊₁) / Δx²

This gives the numerical update equation:

Tᵢⁿ⁺¹ = Tᵢⁿ + r(Tᵢ₋₁ⁿ - 2Tᵢⁿ + Tᵢ₊₁ⁿ)

where:

r = αΔt/Δx²

The simulation uses r = 0.4, which satisfies the stability condition for the explicit scheme.

## Analytical Solution

The numerical solution is compared with the analytical Fourier-series solution for the same boundary and initial conditions.

The analytical solution consists of a steady-state temperature distribution and a transient contribution represented by a Fourier sine series.

The comparison allows the numerical error to be calculated.

## Convergence Study

The solver was tested using different spatial resolutions:

N = 10, 20, 40, 80, 160, 320

where N is the number of spatial intervals.

The maximum absolute error was calculated as:

Error = max(|T_analytical - T_numerical|)

A log-log plot of error against spatial step size Δx was used to determine the convergence behaviour.

For the finer grids, the observed convergence order approaches 2.

This agrees with the expected second-order spatial accuracy of the central finite-difference approximation.

## Results

The results and generated plots are stored in the `results` and `graphs` directories.

The convergence study shows that when Δx is approximately halved, the numerical error decreases by approximately a factor of 4.

Therefore:

Error ∝ Δx²

and the observed convergence order is approximately:

p ≈ 2

## Requirements

Python 3.x

The following libraries are required:

* NumPy
* Matplotlib
* Pandas

Install them using:

```bash
pip install numpy matplotlib pandas
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/eklavyasingh200747-max/heat-equation-solver.git
```

Navigate into the project directory:

```bash
cd heat-equation-solver
```

Run the program:

```bash
python heat_equation_solver.py
```

The program asks for parameters such as:

* Length of the rod
* Initial temperature
* Thermal diffusivity
* Time
* Number of terms used in the analytical solution

## Project Structure

```text
heat-equation-solver/
│
├── heat_equation_solver.py
├── README.md
│
├── results/
│   ├── numerical results and error data
│   └── CSV files
│
└── graphs/
    ├── plots for different simulation times
    └── convergence plots
```

## Concepts Demonstrated

* Partial differential equations
* Heat diffusion
* Finite-difference methods
* Explicit time integration
* Numerical stability
* Fourier-series solutions
* Numerical error analysis
* Convergence testing
* Log-log plots
* Python scientific computing

## Libraries Used

* NumPy
* Matplotlib
* Pandas

## Author

Eklavya

Engineering Physics
IIT Delhi
