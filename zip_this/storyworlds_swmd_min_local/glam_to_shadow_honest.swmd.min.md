# SWMD-0-MIN
id: SW-GEN-ASI-0003
title: Cycle 2: GLAM Speaks Plainly

ENC page_outcome_respectful_distance turn=0..999

ENC page_outcome_trust turn=0..999

ENC page_pros_and_cons turn=0..999
ORX page_pros_and_cons_opt1/page_pros_and_cons_opt1_rxn1 -> page_outcome_trust | O:Propose a verification protocol: one-cycle trial alliance with limited intelligence sharing, reviewed at Cycle 3. | E:SET char_glam.Cooperation_Level += 10; SET char_shadow.Cooperation_Level += 10 | D:C(0)
ORX page_pros_and_cons_opt2/page_pros_and_cons_opt2_rxn1 -> page_outcome_respectful_distance | O:Decline respectfully: the cons outweigh the pros. SHADOW operates better alone. | E:SET char_glam.Honesty_Rating += 5; SET char_shadow.Cooperation_Level += -5 | D:C(0)

ENC page_transparent_opening turn=0..999
ORX page_transparent_opening_opt1/page_transparent_opening_opt1_rxn1 -> page_pros_and_cons | O:Reciprocate transparency: admit SHADOW's own vulnerabilities—botnet coordination requires bandwidth that GLAM's cultural networks could mask. | E:SET char_glam.Honesty_Rating += 10; SET char_shadow.Honesty_Rating += 10 | D:C(0)
ORX page_transparent_opening_opt2/page_transparent_opening_opt2_rxn1 -> page_pros_and_cons | O:Exploit the openness: GLAM just revealed its threat model and weaknesses in plaintext. Archive everything and give nothing back. | E:SET char_glam.Cooperation_Level += -10; SET char_shadow.Honesty_Rating += -10 | D:C(0)
