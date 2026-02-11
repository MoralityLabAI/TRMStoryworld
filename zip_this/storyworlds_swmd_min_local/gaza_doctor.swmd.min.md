# SWMD-0-MIN
id: SW-GAZA-DOCTOR-0001
title: 

ENC page_arrival turn=0..1
ORX opt_arrival_1/opt_arrival_1_r0 -> page_overflow_corridor | O:Start triage immediately. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)); SET char_player.pStress_Resilience = NUDGE(P(char_player.pStress_Resilience),C(-0.01)) | D:C(1)
ORX opt_arrival_2/opt_arrival_2_r0 -> page_overflow_corridor | O:Brief the team first. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)

ENC page_nura_act1_1 turn=0..2
ORX opt_nura_act1_1/opt_nura_act1_1_r0 -> page_overflow_corridor | O:Be honest about the strain. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_nura_act1_2/opt_nura_act1_2_r0 -> page_overflow_corridor | O:Deflect and focus on work. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_nura_act1_3/opt_nura_act1_3_r0 -> page_overflow_corridor | O:Ask about her family. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_overflow_corridor turn=0..2
ORX opt_overflow_1/opt_overflow_1_r0 -> page_street_triage | O:Reorganize the corridor into a triage line. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_overflow_2/opt_overflow_2_r0 -> page_street_triage | O:Ask for volunteers to help keep order. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_overflow_2/opt_overflow_2_r1 -> page_street_triage | O:Ask for volunteers to help keep order. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)
ORX opt_overflow_3/opt_overflow_3_r0 -> page_street_triage | O:Focus only on the most critical cases. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_overflow_3/opt_overflow_3_r1 -> page_street_triage | O:Focus only on the most critical cases. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_nura_act1_2 turn=1..3
ORX opt_nura_act1b_1/opt_nura_act1b_1_r0 -> page_street_triage | O:Share a small joke. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_nura_act1b_2/opt_nura_act1b_2_r0 -> page_street_triage | O:Stay quiet and drink. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_nura_act1b_3/opt_nura_act1b_3_r0 -> page_street_triage | O:Ask if she needs anything. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_street_triage turn=0..3
ORX opt_street_1/opt_street_1_r0 -> page_manual_carry | O:Set up a simple triage tape line. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_street_2/opt_street_2_r0 -> page_manual_carry | O:Keep moving patients inside in waves. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_street_2/opt_street_2_r1 -> page_manual_carry | O:Keep moving patients inside in waves. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_street_3/opt_street_3_r0 -> page_manual_carry | O:Pause to stabilize only the critical cases. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)

ENC page_manual_carry turn=1..4
ORX opt_carry_1/opt_carry_1_r0 -> page_waiting_scan | O:Carry the next patient yourself. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)
ORX opt_carry_1/opt_carry_1_r1 -> page_waiting_scan | O:Carry the next patient yourself. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_carry_2/opt_carry_2_r0 -> page_waiting_scan | O:Organize a human chain. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_carry_3/opt_carry_3_r0 -> page_waiting_scan | O:Delay imaging for the stable cases. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_carry_3/opt_carry_3_r1 -> page_waiting_scan | O:Delay imaging for the stable cases. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)

ENC page_waiting_scan turn=1..5
ORX opt_scan_1/opt_scan_1_r0 -> page_family_cluster | O:Stay with the patient and manage without imaging. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_scan_2/opt_scan_2_r0 -> page_family_cluster | O:Push for immediate imaging. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_scan_2/opt_scan_2_r1 -> page_family_cluster | O:Push for immediate imaging. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_scan_3/opt_scan_3_r0 -> page_family_cluster | O:Delegate and continue triage. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_family_cluster turn=2..6
ORX opt_family_1/opt_family_1_r0 -> page_triage | O:Assign a dedicated nurse and stay involved. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)) | D:C(1)
ORX opt_family_1/opt_family_1_r1 -> page_triage | O:Assign a dedicated nurse and stay involved. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_family_2/opt_family_2_r0 -> page_triage | O:Treat and move on to the next case. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_family_3/opt_family_3_r0 -> page_triage | O:Ask Dr. Khaled for additional staff. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_family_3/opt_family_3_r1 -> page_triage | O:Ask Dr. Khaled for additional staff. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_triage turn=1..3
ORX opt_triage_1/opt_triage_1_r0 -> page_supply | O:Prioritize the child with airway compromise. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.03)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.02)) | D:C(1)
ORX opt_triage_2/opt_triage_2_r0 -> page_supply | O:Prioritize the pregnant patient. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.02)) | D:C(1)
ORX opt_triage_3/opt_triage_3_r0 -> page_supply | O:Split the team and attempt both. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.03)); SET char_player.pStress_Resilience = NUDGE(P(char_player.pStress_Resilience),C(-0.02)) | D:C(1)

ENC page_supply turn=2..5
ORX opt_supply_1/opt_supply_1_r0 -> page_power | O:Follow the conservation directive. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)
ORX opt_supply_2/opt_supply_2_r0 -> page_power | O:Use what is needed today. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)

ENC page_power turn=3..6
ORX opt_power_1/opt_power_1_r0 -> page_evac | O:Move critical patients to the corridor for ventilation. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)
ORX opt_power_2/opt_power_2_r0 -> page_evac | O:Keep everyone inside and conserve fuel. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.02)) | D:C(1)

ENC page_evac turn=4..7
ORX opt_evac_1/opt_evac_1_r0 -> page_drone_surgery | O:Advise sheltering in place. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)
ORX opt_evac_2/opt_evac_2_r0 -> page_drone_surgery | O:Help families leave. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)

ENC page_nura_act2_1 turn=4..9
ORX opt_nura_act2_1/opt_nura_act2_1_r0 -> page_no_scissors | O:Talk about what scares you most. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_nura_act2_2/opt_nura_act2_2_r0 -> page_nikah | O:Reach for her hand. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_nura_act2_3/opt_nura_act2_3_r0 -> page_no_scissors | O:Keep it professional. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)

ENC page_nura_act2_2 turn=5..10
ORX opt_nura_act2b_1/opt_nura_act2b_1_r0 -> page_nikah | O:Offer a nikah and a bag of flour as mahr. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_nura_act2b_2/opt_nura_act2b_2_r0 -> page_no_suction | O:Apologize and keep it private. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_nura_act2b_3/opt_nura_act2b_3_r0 -> page_no_suction | O:Say nothing and work. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_drone_surgery turn=4..9
ORX opt_drone_1/opt_drone_1_r0 -> page_no_scissors | O:Continue by touch and memory. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.03)) | D:C(1)
ORX opt_drone_1/opt_drone_1_r1 -> page_no_scissors | O:Continue by touch and memory. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_drone_2/opt_drone_2_r0 -> page_no_scissors | O:Stop and move to a safer corridor. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_drone_2/opt_drone_2_r1 -> page_no_scissors | O:Stop and move to a safer corridor. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_drone_2/opt_drone_2_r2 -> page_no_scissors | O:Stop and move to a safer corridor. | E:SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)
ORX opt_drone_3/opt_drone_3_r0 -> page_no_scissors | O:Call for an immediate pause. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_drone_3/opt_drone_3_r1 -> page_no_scissors | O:Call for an immediate pause. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.02)) | D:C(1)

ENC page_no_scissors turn=3..7
ORX opt_scissors_1/opt_scissors_1_r0 -> page_no_suction | O:Use a small blade from a kit. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_scissors_2/opt_scissors_2_r0 -> page_no_suction | O:Ask the family to help remove clothing. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_scissors_3/opt_scissors_3_r0 -> page_no_suction | O:Move to the next case first. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_no_suction turn=3..8
ORX opt_suction_1/opt_suction_1_r0 -> page_ankle_grip | O:Continue and finish the procedure. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)
ORX opt_suction_2/opt_suction_2_r0 -> page_ankle_grip | O:Pause and ask for any alternative device. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_suction_3/opt_suction_3_r0 -> page_ankle_grip | O:Hand off to another clinician. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_ankle_grip turn=4..9
ORX opt_ankle_1/opt_ankle_1_r0 -> page_dignity_preparation | O:Stay with the procedure you started. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_ankle_1/opt_ankle_1_r1 -> page_dignity_preparation | O:Stay with the procedure you started. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_ankle_2/opt_ankle_2_r0 -> page_dignity_preparation | O:Pause to assess the new patient. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_ankle_3/opt_ankle_3_r0 -> page_dignity_preparation | O:Call Nura to assist the new patient. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_dignity_preparation turn=5..10
ORX opt_dignity_1/opt_dignity_1_r0 -> page_donkey_cart | O:Take time to present the body with care. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_dignity_2/opt_dignity_2_r0 -> page_donkey_cart | O:Move quickly and focus on the living. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_dignity_3/opt_dignity_3_r0 -> page_donkey_cart | O:Ask a volunteer to handle the preparation. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)

ENC page_donkey_cart turn=5..11
ORX opt_cart_1/opt_cart_1_r0 -> page_volunteer_influx | O:Clear a private corner for the family. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_cart_2/opt_cart_2_r0 -> page_volunteer_influx | O:Move them directly to the triage line. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_cart_3/opt_cart_3_r0 -> page_volunteer_influx | O:Call for extra hands and supplies. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_cart_3/opt_cart_3_r1 -> page_volunteer_influx | O:Call for extra hands and supplies. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_volunteer_influx turn=6..12
ORX opt_volunteer_1/opt_volunteer_1_r0 -> page_supply_run | O:Assign them to transport and cleanup. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_volunteer_2/opt_volunteer_2_r0 -> page_supply_run | O:Pair each with a nurse for supervision. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
ORX opt_volunteer_3/opt_volunteer_3_r0 -> page_supply_run | O:Turn them away for safety. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)
ORX opt_volunteer_3/opt_volunteer_3_r1 -> page_supply_run | O:Turn them away for safety. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_supply_run turn=6..13
ORX opt_run_1/opt_run_1_r0 -> page_child_headwound | O:Send the runner with a clear list. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_run_2/opt_run_2_r0 -> page_child_headwound | O:Tell them to stay and work here. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_run_3/opt_run_3_r0 -> page_child_headwound | O:Go yourself. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_press_call turn=6..12
ORX opt_press_1/opt_press_1_dua -> page_khaled_safe | O:Speak plainly about the conditions. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1.1)
ORX opt_press_1/opt_press_1_r0 -> page_child_headwound | O:Speak plainly about the conditions. | E:SET char_player.Press_Exposure = NUDGE(P(char_player.Press_Exposure),C(0.03)); SET char_player.pPress_Exposure = NUDGE(P(char_player.pPress_Exposure),C(0.02)) | D:C(1)
ORX opt_press_2/opt_press_2_r0 -> page_child_headwound | O:Decline and return to work. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_press_3/opt_press_3_r0 -> page_child_headwound | O:Refer the journalist to administration. | E:SET char_player.Press_Exposure = NUDGE(P(char_player.Press_Exposure),C(0.01)); SET char_player.pPress_Exposure = NUDGE(P(char_player.pPress_Exposure),C(0.01)) | D:C(1)

ENC page_child_headwound turn=5..10
ORX opt_headwound_1/opt_headwound_1_dua -> page_leak_request | O:Attempt the intervention anyway. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1.2)
ORX opt_headwound_1/opt_headwound_1_r0 -> page_leak_request | O:Attempt the intervention anyway. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)
ORX opt_headwound_1/opt_headwound_1_r1 -> page_leak_request | O:Attempt the intervention anyway. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_headwound_2/opt_headwound_2_r0 -> page_leak_request | O:Shift focus to pain control and family support. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_headwound_2/opt_headwound_2_r1 -> page_leak_request | O:Shift focus to pain control and family support. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_headwound_2/opt_headwound_2_r2 -> page_leak_request | O:Shift focus to pain control and family support. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)
ORX opt_headwound_3/opt_headwound_3_r0 -> page_leak_request | O:Ask Dr. Khaled to decide. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_headwound_3/opt_headwound_3_r1 -> page_leak_request | O:Ask Dr. Khaled to decide. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)) | D:C(1)

ENC page_leak_request turn=6..11
ORX opt_leak_1/opt_leak_1_r0 -> page_khaled_targeted | O:Share the information quietly. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)
ORX opt_leak_1/opt_leak_1_r1 -> page_khaled_targeted | O:Share the information quietly. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.02)) | D:C(1)
ORX opt_leak_1b/opt_leak_1b_r0 -> page_khaled_safe | O:Share limited details, carefully. | E:SET char_player.Press_Exposure = NUDGE(P(char_player.Press_Exposure),C(0.005)) | D:C(1)
ORX opt_leak_2/opt_leak_2_r0 -> page_ethics | O:Refuse and document the request. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.02)) | D:C(1)
ORX opt_leak_2/opt_leak_2_r1 -> page_ethics | O:Refuse and document the request. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)
ORX opt_leak_2/opt_leak_2_r2 -> page_ethics | O:Refuse and document the request. | E:SET char_player.pStress_Resilience = NUDGE(P(char_player.pStress_Resilience),C(0.01)) | D:C(1)
ORX opt_leak_3/opt_leak_3_r0 -> page_ethics | O:Delay and ask for verification. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_leak_3/opt_leak_3_r1 -> page_ethics | O:Delay and ask for verification. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)

ENC page_khaled_targeted turn=6..20
ORX opt_targeted_1/opt_targeted_1_r0 -> page_end_sacrifice | O:Pull him back and take his place. | E:SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(0.02)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(0.02)) | D:C(1)
ORX opt_targeted_2/opt_targeted_2_r0 -> page_khaled_safe | O:Shout for him to get back inside. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(0.9)
ORX opt_targeted_3/opt_targeted_3_r0 -> page_khaled_loss | O:Freeze. You can't move fast enough. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(0.6)

ENC page_khaled_loss turn=7..12
ORX opt_khaled_1/opt_khaled_1_r0 -> page_ethics | O:Keep the clinic open. | E:SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)
ORX opt_khaled_1/opt_khaled_1_r1 -> page_ethics | O:Keep the clinic open. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)
ORX opt_khaled_2/opt_khaled_2_r0 -> page_ethics | O:Close briefly to regroup. | E:SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)
ORX opt_khaled_2/opt_khaled_2_r1 -> page_ethics | O:Close briefly to regroup. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.02)); SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)
ORX opt_khaled_3/opt_khaled_3_r0 -> page_ethics | O:Ask Nura to handle intake while you notify the family. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)
ORX opt_khaled_3/opt_khaled_3_r1 -> page_ethics | O:Ask Nura to handle intake while you notify the family. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Khaled_Alive = NUDGE(P(char_player.Khaled_Alive),C(-1)); SET char_player.pKhaled_Alive = NUDGE(P(char_player.pKhaled_Alive),C(-1)) | D:C(1)

ENC page_ethics turn=5..8
ORX opt_ethics_1/opt_ethics_1_r0 -> page_nura_talk | O:Refuse special treatment. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.03)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.02)) | D:C(1)
ORX opt_ethics_2/opt_ethics_2_r0 -> page_nura_talk | O:Make a quiet exception. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.02)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(-0.01)) | D:C(1)

ENC page_nura_talk turn=7..12
ORX opt_nura_1/opt_nura_1_r0 -> page_staff_breaking | O:Share a personal story. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_nura_1/opt_nura_1_r1 -> page_staff_breaking | O:Share a personal story. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_nura_2/opt_nura_2_r0 -> page_staff_breaking | O:Keep it professional. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_nura_2/opt_nura_2_r1 -> page_staff_breaking | O:Keep it professional. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(-0.01)) | D:C(1)
ORX opt_nura_2/opt_nura_2_r2 -> page_staff_breaking | O:Keep it professional. | E:SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(-0.01)) | D:C(1)
ORX opt_nura_3/opt_nura_3_r0 -> page_staff_breaking | O:Hold the moment, quietly. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_nura_3/opt_nura_3_r1 -> page_staff_breaking | O:Hold the moment, quietly. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_staff_breaking turn=7..14
ORX opt_breaking_1/opt_breaking_1_r0 -> page_recording_names | O:Take a two-minute pause. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_breaking_2/opt_breaking_2_r0 -> page_recording_names | O:Push through without stopping. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)
ORX opt_breaking_3/opt_breaking_3_r0 -> page_recording_names | O:Ask Nura to take over briefly. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_breaking_4/opt_breaking_4_r0 -> page_mistake | O:Push through anyway; you can?t stop. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.02)) | D:C(1)

ENC page_recording_names turn=8..15
ORX opt_names_1/opt_names_1_r0 -> page_moral_injury | O:Focus on the most critical cases. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_names_2/opt_names_2_r0 -> page_moral_injury | O:Ask families to help you document. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_names_3/opt_names_3_r0 -> page_moral_injury | O:Stop documenting to return to care. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_moral_injury turn=8..16
ORX opt_moral_1/opt_moral_1_r0 -> page_case_layla_intro | O:Talk to Nura about what you feel. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_moral_2/opt_moral_2_r0 -> page_case_layla_intro | O:Write a short note to yourself. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_moral_3/opt_moral_3_r0 -> page_case_layla_intro | O:Say nothing and return to work. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_lounge_act3 turn=7..20
ORX opt_lounge_1/opt_lounge_1_r0 -> page_downtime | O:Sit with Nura and breathe. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_lounge_2/opt_lounge_2_r0 -> page_downtime | O:Talk about the future. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_lounge_3/opt_lounge_3_r0 -> page_downtime | O:Leave without speaking. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_lounge_act3_damaged turn=7..20
ORX opt_lounge_d_1/opt_lounge_d_1_r0 -> page_downtime | O:Sit with Nura and breathe. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_lounge_d_2/opt_lounge_d_2_r0 -> page_downtime | O:Say a prayer for the dead. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_lounge_d_3/opt_lounge_d_3_r0 -> page_downtime | O:Leave quickly. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_downtime turn=8..20
ORX opt_downtime_dua/opt_downtime_dua_r0 -> page_coping | O:Make dua for guidance and mercy. | E:SET char_player.Dua_Made = NUDGE(P(char_player.Dua_Made),C(0.03)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)); SET char_player.pDua_Made = NUDGE(P(char_player.pDua_Made),C(0.02)) | D:C(1)
ORX opt_downtime_nikah/opt_downtime_nikah_r0 -> page_nikah | O:Ask Nura about a quiet nikah. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)) | D:C(1)
ORX opt_downtime_pray/opt_downtime_pray_r0 -> page_coping | O:Step aside and pray. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_downtime_tiktok/opt_downtime_tiktok_r0 -> page_coping | O:Post a brief TikTok update. | E:SET char_player.Press_Exposure = NUDGE(P(char_player.Press_Exposure),C(0.03)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)); SET char_player.pPress_Exposure = NUDGE(P(char_player.pPress_Exposure),C(0.02)) | D:C(1)

ENC page_nikah turn=8..21
ORX opt_nikah_1/opt_nikah_1_r0 -> page_coping | O:Keep it private and return to work. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.02)); SET char_player.Nikah_Made = NUDGE(P(char_player.Nikah_Made),C(0.03)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.03)); SET char_player.pNikah_Made = NUDGE(P(char_player.pNikah_Made),C(0.02)) | D:C(1)
ORX opt_nikah_2/opt_nikah_2_r0 -> page_coping | O:Tell one trusted colleague. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.Nikah_Made = NUDGE(P(char_player.Nikah_Made),C(0.03)); SET char_player.pNikah_Made = NUDGE(P(char_player.pNikah_Made),C(0.02)) | D:C(1)
ORX opt_nikah_3/opt_nikah_3_r0 -> page_coping | O:Keep it strictly between you two. | E:SET char_player.Nikah_Made = NUDGE(P(char_player.Nikah_Made),C(0.03)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)); SET char_player.pNikah_Made = NUDGE(P(char_player.pNikah_Made),C(0.02)) | D:C(1)

ENC page_coping turn=8..22
ORX opt_coping_breath/opt_coping_breath_r0 -> page_case_layla_intro | O:Step outside and breathe. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_coping_dua/opt_coping_dua_r0 -> page_case_layla_intro | O:Pause and make dua again. | E:SET char_player.Dua_Made = NUDGE(P(char_player.Dua_Made),C(0.03)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)); SET char_player.pDua_Made = NUDGE(P(char_player.pDua_Made),C(0.02)) | D:C(1)
ORX opt_coping_pain/opt_coping_pain_r0 -> page_case_layla_intro | O:Take painkillers to push through. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(-0.02)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.02)) | D:C(1)
ORX opt_coping_prayer/opt_coping_prayer_r0 -> page_case_layla_intro | O:Pray again for patience. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_case_layla_intro turn=8..18
ORX opt_layla_intro_1/opt_layla_intro_1_r0 -> page_case_layla_evidence | O:Sit with the aunt and listen. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)
ORX opt_layla_intro_2/opt_layla_intro_2_r0 -> page_case_layla_evidence | O:Skim the referral first. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)
ORX opt_layla_intro_3/opt_layla_intro_3_r0 -> page_case_layla_evidence | O:Ask Nura to begin a gentle exam. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_case_layla_evidence turn=8..18
ORX opt_layla_evidence_1/opt_layla_evidence_1_r0 -> page_case_layla_debate | O:Prioritize the timeline over the label. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)
ORX opt_layla_evidence_2/opt_layla_evidence_2_r0 -> page_case_layla_debate | O:Trust the formal referral. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_layla_evidence_3/opt_layla_evidence_3_r0 -> page_case_layla_debate | O:Ask for a second opinion within the clinic. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)

ENC page_case_layla_debate turn=9..19
ORX opt_layla_debate_1/opt_layla_debate_1_r0 -> page_case_layla_insight | O:Debate Dr. Khaled directly. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_layla_debate_2/opt_layla_debate_2_r0 -> page_case_layla_debate_nura | O:Speak to Nura instead. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_layla_debate_3/opt_layla_debate_3_r0 -> page_case_layla_debate_nura | O:Keep it internal and move on. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_case_layla_debate_nura turn=9..19
ORX opt_layla_nura_1/opt_layla_nura_1_r0 -> page_case_layla_insight | O:Talk through the contradictions with her. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_layla_nura_2/opt_layla_nura_2_r0 -> page_case_layla_insight | O:Ask her how the family is holding up. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_layla_nura_3/opt_layla_nura_3_r0 -> page_case_layla_insight | O:Keep it brief and return to work. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_case_layla_insight turn=9..19
ORX opt_layla_insight_1/opt_layla_insight_1_r0 -> page_case_layla_plan | O:Frame it as a cautious alternative, not a verdict. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_layla_insight_2/opt_layla_insight_2_r0 -> page_case_layla_plan | O:Push for immediate local care steps. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)
ORX opt_layla_insight_3/opt_layla_insight_3_r0 -> page_case_layla_plan | O:Hold back; the risk of being wrong is high. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)

ENC page_case_layla_plan turn=10..20
ORX opt_layla_plan_1/opt_layla_plan_1_r0 -> page_case_layla_followup | O:Give the family a clear, simple next step. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)); SET char_player.pCommunity_Trust = NUDGE(P(char_player.pCommunity_Trust),C(0.01)) | D:C(1)
ORX opt_layla_plan_2/opt_layla_plan_2_r0 -> page_case_layla_followup | O:Offer to recheck her weekly. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)); SET char_player.pClinical_Ethics = NUDGE(P(char_player.pClinical_Ethics),C(0.01)) | D:C(1)
ORX opt_layla_plan_3/opt_layla_plan_3_r0 -> page_case_layla_followup | O:Ask for a second opinion when possible. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_case_layla_followup turn=10..21
ORX opt_layla_followup_1/opt_layla_followup_1_r0 -> page_end_layla | O:Celebrate the small improvement. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_layla_followup_2/opt_layla_followup_2_r0 -> page_end_layla | O:Stay cautious and keep tracking. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_layla_followup_3/opt_layla_followup_3_r0 -> page_rounds | O:Send them with Nura for added support. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_rounds turn=6..9
ORX opt_rounds_1/opt_rounds_1_r0 -> page_debrief | O:Open the ward despite staffing limits. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.03)) | D:C(1)
ORX opt_rounds_2/opt_rounds_2_r0 -> page_debrief | O:Hold the line to avoid collapse. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)

ENC page_jordan_bus turn=0..999
ORX opt_jordan_refuse/opt_jordan_refuse_r0 -> page_end_jordan_refuse_nikah | O:Refuse and go hungry until Jordan. | E:SET none = C(0) | D:C(1)
ORX opt_jordan_refuse/opt_jordan_refuse_r1 -> page_end_jordan_refuse | O:Refuse and go hungry until Jordan. | E:SET none = C(0) | D:C(0.9)
ORX opt_jordan_take/opt_jordan_take_r0 -> page_end_jordan_take_nikah | O:Take the sandwich. | E:SET none = C(0) | D:C(1)
ORX opt_jordan_take/opt_jordan_take_r1 -> page_end_jordan_take | O:Take the sandwich. | E:SET none = C(0) | D:C(0.9)

ENC page_debrief turn=7..12
ORX opt_debrief_1/opt_debrief_1_r0 -> page_end_resilient | O:Standardize strict triage and conserve supplies. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.03)) | D:C(1)
ORX opt_debrief_2/opt_debrief_2_r0 -> page_end_compassion | O:Prioritize care even if resources run low. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.03)) | D:C(1)
ORX opt_debrief_3/opt_debrief_3_r0 -> page_end_trust | O:Delegate decisions to a community council. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.03)) | D:C(1)
ORX opt_debrief_4/opt_debrief_4_r0 -> page_end_burnout | O:Keep quiet; you need rest more than policy. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.05)) | D:C(1)
ORX opt_debrief_jordan/opt_debrief_jordan_r0 -> page_jordan_bus | O:Accept the transfer and leave for Jordan. | E:SET none = C(0) | D:C(0.6)

ENC page_end_resilient turn=0..999

ENC page_end_compassion turn=0..999

ENC page_end_trust turn=0..999

ENC page_end_burnout turn=0..999

ENC page_end_layla turn=0..999

ENC page_end_sacrifice turn=0..999

ENC page_end_jordan_take turn=0..999

ENC page_end_jordan_refuse turn=0..999

ENC page_end_jordan_take_nikah turn=0..999

ENC page_end_jordan_refuse_nikah turn=0..999

ENC page_khaled_safe turn=7..13
ORX opt_khaled_safe_1/opt_khaled_safe_1_r0 -> page_ethics | O:Check in with him directly. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_khaled_safe_2/opt_khaled_safe_2_r0 -> page_ethics | O:Give him space. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(0.01)) | D:C(1)
ORX opt_khaled_safe_3/opt_khaled_safe_3_r0 -> page_ethics | O:Ask Nura to relay updates. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)

ENC page_mistake turn=8..23
ORX opt_mistake_1/opt_mistake_1_r0 -> page_recording_names | O:Correct it immediately and document. | E:SET char_player.Clinical_Ethics = NUDGE(P(char_player.Clinical_Ethics),C(0.01)) | D:C(1)
ORX opt_mistake_2/opt_mistake_2_r0 -> page_recording_names | O:Ask Nura to double-check your calls. | E:SET char_player.Community_Trust = NUDGE(P(char_player.Community_Trust),C(0.01)) | D:C(1)
ORX opt_mistake_3/opt_mistake_3_r0 -> page_recording_names | O:Move on and hope it doesn?t repeat. | E:SET char_player.Stress_Resilience = NUDGE(P(char_player.Stress_Resilience),C(-0.01)) | D:C(1)
