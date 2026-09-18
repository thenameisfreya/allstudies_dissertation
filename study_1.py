import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

silicon_room_swing = 60.0
dirac_swing = 40.0

temperature_ratio = np.linspace(0.5, 1.0, 101)

silicon_swing = silicon_room_swing * temperature_ratio

percentage_reduction = (
    (silicon_room_swing - dirac_swing)
    / silicon_room_swing
) * 100

crossover_ratio = dirac_swing / silicon_room_swing

selected_ratios = np.array([
    1.00,
    0.90,
    0.80,
    0.70,
    crossover_ratio,
    0.60,
    0.50
])

selected_swings = silicon_room_swing * selected_ratios

selected_difference = selected_swings - dirac_swing

results = pd.DataFrame({
    "Temperature_relative_to_room": selected_ratios,
    "Silicon_subthreshold_swing_mV_dec": selected_swings,
    "Silicon_minus_Dirac_mV_dec": selected_difference
})

print("\nSTUDY 1 RESULTS")

print(
    f"Conventional silicon benchmark: "
    f"{silicon_room_swing:.1f} mV/dec"
)

print(
    f"Dirac source FET benchmark: "
    f"{dirac_swing:.1f} mV/dec"
)

print(
    f"Reduction compared with silicon: "
    f"{percentage_reduction:.1f}%"
)

print(
    f"Conventional silicon would theoretically "
    f"reach {dirac_swing:.1f} mV/dec at "
    f"{crossover_ratio * 100:.1f}% of "
    f"room-temperature absolute temperature."
)

print(
    f"This means the absolute temperature would "
    f"need to be reduced by "
    f"{(1 - crossover_ratio) * 100:.1f}%."
)

print("\nCalculated silicon values:")
print(results.to_string(index=False))

print("\nCROSSOVER INTERPRETATION")

print(
    f"Above {crossover_ratio * 100:.1f}% of room temperature, "
    f"the Dirac-source benchmark has the lower subthreshold swing."
)

print(
    f"At {crossover_ratio * 100:.1f}%, "
    f"the two values are equal."
)

print(
    f"Below {crossover_ratio * 100:.1f}%, "
    f"ideal cooled silicon has the lower theoretical swing."
)

results.to_csv(
    "study1_switching_results.csv",
    index=False
)

plt.figure(figsize=(8, 5))

plt.plot(
    temperature_ratio * 100,
    silicon_swing,
    label="Conventional silicon theoretical limit"
)

plt.axhline(
    y=dirac_swing,
    linestyle="--",
    label="Dirac source FET: 40 mV/dec"
)

plt.axvline(
    x=crossover_ratio * 100,
    linestyle=":",
    label=f"Equal at {crossover_ratio * 100:.1f}% of room temperature"
)

plt.scatter(
    crossover_ratio * 100,
    dirac_swing
)

plt.xlabel(
    "Temperature (% of room temperature absolute temperature)"
)

plt.ylabel(
    "Subthreshold swing (mV/dec)"
)

plt.title(
    "Study 1: Silicon Subthreshold Swing vs Dirac Source FET"
)

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    "study1_subthreshold_swing.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

difference = silicon_swing - dirac_swing

plt.figure(figsize=(8, 5))

plt.plot(
    temperature_ratio * 100,
    difference
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.axvline(
    x=crossover_ratio * 100,
    linestyle=":"
)

plt.xlabel(
    "Temperature (% of room-temperature absolute temperature)"
)

plt.ylabel(
    "Silicon swing minus Dirac benchmark (mV/dec)"
)

plt.title(
    "Study 1: Switching Advantage Across Temperature"
)

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    "study1_switching_advantage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()