#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pefkon-240mg Synergistic Endothelial Kinetic Graph Engine
License: BSL-1.0
"""

import numpy as np
import matplotlib.pyplot as plt

def model_synergy_curves():
    t = np.linspace(0, 24, 1000)
    
    # Core mathematical baselines
    Dose_Pinus = 216  # Net active OPC weight (240mg * 0.90)
    F = 0.45          # Base Bioavailability coefficient
    Vd = 1.6          # Distribution volume (L/kg)
    ka = 0.78         # Absorption rate constant (hr^-1)
    
    # Baseline elimination vs Synergistic elimination due to EGCG COMT-Inhibition
    ke_baseline = 0.46   # Standard clearance rate (t_1/2 = 1.5 hr)
    ke_synergistic = 0.21 # Slowed clearance rate due to EGCG presence (t_1/2 = 3.3 hr)
    
    # Bateman open oral pharmacokinetic calculation models
    C_baseline = (F * Dose_Pinus * ka) / (Vd * (ka - ke_baseline)) * (np.exp(-ke_baseline * t) - np.exp(-ka * t))
    C_synergistic = (F * Dose_Pinus * ka) / (Vd * (ka - ke_synergistic)) * (np.exp(-ke_synergistic * t) - np.exp(-ka * t))

    # Initiate rendering dark-grid notebook profile layout
    plt.figure(figsize=(11, 5.5))
    plt.plot(t, C_synergistic, color='#008080', linewidth=2.5, label='Synergistic Profile (Pefkon Core + EGCG COMT-Inhibition)')
    plt.plot(t, C_baseline, color='#C0392B', linewidth=1.5, linestyle='--', label='Un-adjuvanted Pinus pinaster Baseline (No EGCG)')
    
    plt.title('Pefkon-240mg Endothelial Optimization: Synergistic COMT Kinetic Shielding', fontsize=11, fontweight='bold', pad=15)
    plt.xlabel('Time Post-Ingestion (Hours)', fontsize=10)
    plt.ylabel('Systemic Plasma Concentration (ng/mL)', fontsize=10)
    
    plt.xlim(0, 24)
    plt.ylim(0, 45)
    plt.xticks(np.arange(0, 25, 2))
    plt.grid(True, which='both', linestyle=':', color='#BDC3C7', alpha=0.6)
    plt.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#E0E0E0')
    
    output_path = "images/synergistic_kinetic_shielding.png"
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"[✅ SUCCESS] Graph asset exported to: {output_path}")

if __name__ == "__main__":
    model_synergy_curves()
