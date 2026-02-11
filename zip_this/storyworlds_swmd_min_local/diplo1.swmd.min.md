# SWMD-0-MIN
id: SW-GEN-DIPLO-0001
title: Spring 1901: An English Overture

ENC page_opening turn=0..999
ORX page_opening_opt1/page_opening_opt1_rxn1 -> page_private_talk | O:Signal goodwill: propose a Demilitarized Zone in the English Channel and a joint eye on Germany. | E:SET char_england.Cooperative_Competitive += 5; SET char_france.Trust_Betrayal += 10 | D:C(0)
ORX page_opening_opt2/page_opening_opt2_rxn1 -> page_private_talk | O:Keep it ambiguous: hint that England might tolerate French moves in Belgium, but never quite commit. | E:SET char_england.Cooperative_Competitive += -5; SET char_france.Trust_Betrayal += -5 | D:C(0)

ENC page_outcome_alliance turn=0..999

ENC page_outcome_cold turn=0..999

ENC page_private_talk turn=0..999
ORX page_private_talk_opt1/page_private_talk_opt1_rxn1 -> page_outcome_alliance | O:Propose a formal alliance: England promises no fleet in the Channel, France promises no move to the North Sea. | E:SET char_england.Trust_Betrayal += 10; SET char_france.Cooperative_Competitive += 10 | D:C(0)
ORX page_private_talk_opt2/page_private_talk_opt2_rxn1 -> page_outcome_cold | O:Keep things vague: suggest "mutual respect" in the west without drawing any real lines. | E:SET char_england.Trust_Betrayal += -5; SET char_france.Trust_Betrayal += -5 | D:C(0)
