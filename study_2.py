import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

devices = np.array([
    "NFET",
    "PFET"
])

wkf = np.array([
    60.5,
    48.4
])

rdf = np.array([
    10.1,
    21.7
])

wkf_to_rdf_ratio = wkf / rdf

required_wkf_reduction = (
    1 - (rdf / wkf)
) * 100

wkf_nfet_vs_pfet = (
    wkf[0] / wkf[1]
)

rdf_pfet_vs_nfet = (
    rdf[1] / rdf[0]
)

results = pd.DataFrame({
    "Device": devices,
    "WKF_Ioff_RSD_percent": wkf,
    "RDF_Ioff_RSD_percent": rdf,
    "WKF_to_RDF_ratio": wkf_to_rdf_ratio,
    "WKF_reduction_needed_percent": required_wkf_reduction
})

print("\nSTUDY 2 RESULTS")

print(results.to_string(index=False))

print(
    f"\nFor the NFET, WKF causes "
    f"{wkf_to_rdf_ratio[0]:.2f} times "
    f"the leakage variability of RDF."
)

print(
    f"For the PFET, WKF causes "
    f"{wkf_to_rdf_ratio[1]:.2f} times "
    f"the leakage variability of RDF."
)

print(
    f"\nUnder WKF, NFET variability is "
    f"{wkf_nfet_vs_pfet:.2f} times "
    f"the PFET value."
)

print(
    f"Under RDF, PFET variability is "
    f"{rdf_pfet_vs_nfet:.2f} times "
    f"the NFET value."
)

print(
    f"\nNFET WKF would need to fall by "
    f"{required_wkf_reduction[0]:.1f}% "
    f"to reach the RDF level."
)

print(
    f"PFET WKF would need to fall by "
    f"{required_wkf_reduction[1]:.1f}% "
    f"to reach the RDF level."
)

results.to_csv(
    "study2_atomic_variability_results.csv",
    index=False
)

x = np.arange(len(devices))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(
    x - width / 2,
    wkf,
    width,
    label="Work function fluctuation (WKF)"
)

plt.bar(
    x + width / 2,
    rdf,
    width,
    label="Random dopant fluctuation (RDF)"
)

plt.xticks(
    x,
    devices
)

plt.ylabel(
    "Off state current variability, RSD (%)"
)

plt.xlabel(
    "Transistor type"
)

plt.title(
    "Study 2: Microscopic Variability and Off State Leakage"
)

plt.legend()
plt.tight_layout()

plt.savefig(
    "study2_atomic_leakage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.figure(figsize=(8, 5))

plt.bar(
    devices,
    required_wkf_reduction
)

plt.ylabel(
    "Required reduction in WKF variability (%)"
)

plt.xlabel(
    "Transistor type"
)

plt.title(
    "Study 2: WKF Reduction Needed to Reach RDF Levels"
)

plt.tight_layout()

plt.savefig(
    "study2_required_wkf_reduction.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()