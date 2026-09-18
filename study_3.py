import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

width_nm = np.array([
    100,
    50,
    30,
    20
])

length = 1e-3
aspect_ratio = 2

lambda_eff = 39e-9
rho_lambda = 6.7e-16

rho_bulk = rho_lambda / lambda_eff

p = 0
R = 0.4

capacitance_per_m = (
    0.2e-15 / 1e-6
)

width_m = width_nm * 1e-9

height_m = (
    aspect_ratio * width_m
)

area = (
    width_m * height_m
)

grain_size = width_m

rho_nanoscale = (
    rho_bulk
    + rho_bulk
    * lambda_eff
    * (3 * (1 - p))
    / (4 * width_m)
    + rho_bulk
    * lambda_eff
    * (3 * R)
    / (
        2
        * grain_size
        * (1 - R)
    )
)

resistance_geometry = (
    rho_bulk
    * length
    / area
)

resistance_nanoscale = (
    rho_nanoscale
    * length
    / area
)

capacitance = (
    capacitance_per_m
    * length
)

delay_geometry = (
    0.5
    * resistance_geometry
    * capacitance
)

delay_nanoscale = (
    0.5
    * resistance_nanoscale
    * capacitance
)

relative_resistance_geometry = (
    resistance_geometry
    / resistance_geometry[0]
)

relative_resistance_nanoscale = (
    resistance_nanoscale
    / resistance_geometry[0]
)

relative_delay_geometry = (
    delay_geometry
    / delay_geometry[0]
)

relative_delay_nanoscale = (
    delay_nanoscale
    / delay_geometry[0]
)

scattering_penalty = (
    resistance_nanoscale
    / resistance_geometry
)

coefficient_nm = (
    lambda_eff
    * 1e9
    * (
        (3 * (1 - p)) / 4
        +
        (3 * R)
        / (2 * (1 - R))
    )
)

critical_2x_width = (
    coefficient_nm
    / (2 - 1)
)

critical_3x_width = (
    coefficient_nm
    / (3 - 1)
)

critical_4x_width = (
    coefficient_nm
    / (4 - 1)
)

results = pd.DataFrame({
    "Width_nm": width_nm,
    "Geometry_only_relative_resistance":
        relative_resistance_geometry,
    "Nanoscale_relative_resistance":
        relative_resistance_nanoscale,
    "Scattering_penalty":
        scattering_penalty,
    "Geometry_only_relative_delay":
        relative_delay_geometry,
    "Nanoscale_relative_delay":
        relative_delay_nanoscale
})

print("\nSTUDY 3 RESULTS")

print(results.to_string(index=False))

print(
    f"\nWidth where scattering doubles "
    f"geometry-only resistance: "
    f"{critical_2x_width:.1f} nm"
)

print(
    f"Width where scattering triples "
    f"geometry-only resistance: "
    f"{critical_3x_width:.1f} nm"
)

print(
    f"Width where scattering gives "
    f"four times geometry-only resistance: "
    f"{critical_4x_width:.1f} nm"
)

print(
    f"\nAt 20 nm, scattering makes resistance "
    f"{scattering_penalty[-1]:.2f} times "
    f"the geometry-only prediction."
)

results.to_csv(
    "study3_interconnect_results.csv",
    index=False
)

plt.figure(figsize=(8, 5))

plt.plot(
    width_nm,
    relative_resistance_geometry,
    marker="o",
    label="Geometry-only copper"
)

plt.plot(
    width_nm,
    relative_resistance_nanoscale,
    marker="o",
    label="Copper with nanoscale scattering"
)

plt.xlabel(
    "Copper wire width (nm)"
)

plt.ylabel(
    "Resistance relative to ideal 100 nm wire"
)

plt.title(
    "Study 3: Copper Scaling and Interconnect Resistance"
)

plt.gca().invert_xaxis()
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    "study3_resistance_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.figure(figsize=(8, 5))

plt.plot(
    width_nm,
    relative_delay_geometry,
    marker="o",
    label="Geometry-only copper"
)

plt.plot(
    width_nm,
    relative_delay_nanoscale,
    marker="o",
    label="Copper with nanoscale scattering"
)

plt.xlabel(
    "Copper wire width (nm)"
)

plt.ylabel(
    "RC delay relative to ideal 100 nm wire"
)

plt.title(
    "Study 3: Copper Scaling and Signal Delay"
)

plt.gca().invert_xaxis()
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    "study3_delay_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

width_sweep = np.linspace(
    20,
    100,
    500
)

penalty_sweep = (
    1
    + coefficient_nm
    / width_sweep
)

plt.figure(figsize=(8, 5))

plt.plot(
    width_sweep,
    penalty_sweep
)

plt.axhline(
    y=2,
    linestyle="--",
    label="2× geometry only resistance"
)

plt.axvline(
    x=critical_2x_width,
    linestyle=":",
    label=f"2× threshold = {critical_2x_width:.1f} nm"
)

plt.xlabel(
    "Copper wire width (nm)"
)

plt.ylabel(
    "Resistance penalty relative to geometry only model"
)

plt.title(
    "Study 3: Nanoscale Scattering Penalty"
)

plt.gca().invert_xaxis()
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    "study3_scattering_threshold.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()