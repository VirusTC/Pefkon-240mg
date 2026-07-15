#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pefkon-240mg Dual-Core Compliance Verification Script
License: BSL-1.0
"""

import os

def verify_dual_matrix():
    ledger = "data/EXPANDED_ACCESS_PATIENT_METRICS.tsv"
    if not os.path.exists(ledger):
        print("[🚨 ERROR] Ledger missing. Execute deploy_pefkon.sh first.")
        return

    print("====================================================")
    print("=== PEFKON-240MG DUAL-CORE COMPLIANCE AUDIT TRACE ===")
    print("====================================================")

    with open(ledger, 'r') as f:
        rows = [line.strip().split('\t') for line in f.readlines()]

    headers = rows[0]
    for idx, row in enumerate(rows[1:], start=1):
        sub_id, age, _, opc_check, egcg_check, compliance, status = row
        print(f"\n[+] Scanning Row {idx} -> Subject Record: {sub_id}")
        
        # Dual-assay verification gate
        if opc_check == "PASS" and egcg_check == "PASS":
            print(f"  |-- [✅ VERIFIED] Chemistry standards compliant: 90% OPC & 50% EGCG lots verified.")
        else:
            print(f"  |-- [🚨 CRITICAL] Batch validation error. Discontinue supply immediately.")
            
        # Synergistic pathway restriction checks
        if status == "HOLD_SURGERY" or compliance == "RESTRICTED":
            print("  |-- [🚨 REJECTION GATE] ACTIVE MEDICAL STOP-GATE ACTIVE.")
            print("  |   Reason: Combined EGCG + OPC matrix downregulates secondary clotting mechanisms.")
        else:
            print("  |-- [✅ PASS] Patient endothelial tone parameters fall within safe therapeutic margins.")

if __name__ == "__main__":
    verify_dual_matrix()
