# SWMD-0-MIN
id: SW-TEMPLATE-1758411561
title: Dogs in a Barrel (Full)

ENC page_1 turn=0..1
ORX page_1_option1/page_1_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_1_option1/page_1_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_1_option2/page_1_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_1_option2/page_1_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_1_option3/page_1_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_1_option3/page_1_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_10 turn=5..6
ORX page_10_option1/page_10_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_10_option1/page_10_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_10_option2/page_10_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_10_option2/page_10_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_10_option3/page_10_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_10_option3/page_10_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_11 turn=5..6
ORX page_11_option1/page_11_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_11_option1/page_11_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_11_option2/page_11_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_11_option2/page_11_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_11_option3/page_11_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_11_option3/page_11_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_12 turn=5..6
ORX page_12_option1/page_12_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_12_option1/page_12_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_12_option2/page_12_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_12_option2/page_12_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_12_option3/page_12_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_12_option3/page_12_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_13 turn=7..8
ORX page_13_option1/page_13_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_13_option1/page_13_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_13_option2/page_13_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_13_option2/page_13_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_13_option3/page_13_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_13_option3/page_13_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_14 turn=7..8
ORX page_14_option1/page_14_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_14_option1/page_14_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_14_option2/page_14_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_14_option2/page_14_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_14_option3/page_14_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_14_option3/page_14_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_15 turn=8..9
ORX page_15_option1/page_15_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_15_option1/page_15_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_15_option2/page_15_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_15_option2/page_15_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_15_option3/page_15_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_15_option3/page_15_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_16 turn=8..9
ORX page_16_option1/page_16_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_16_option1/page_16_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_16_option2/page_16_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_16_option2/page_16_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_16_option3/page_16_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_16_option3/page_16_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_17 turn=10..10
ORX page_17_option1/page_17_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(-1); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(-0.5)) | D:C(0.5)
ORX page_17_option1/page_17_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_17_option2/page_17_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_17_option2/page_17_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_17_option3/page_17_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_17_option3/page_17_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_18 turn=10..10
ORX page_18_option1/page_18_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(-0.3); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(0)) | D:C(0.5)
ORX page_18_option1/page_18_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_18_option2/page_18_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_18_option2/page_18_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_18_option3/page_18_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_18_option3/page_18_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_19 turn=10..10
ORX page_19_option1/page_19_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(0); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_19_option1/page_19_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_19_option2/page_19_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_19_option2/page_19_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_19_option3/page_19_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_19_option3/page_19_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_2 turn=0..1
ORX page_2_option1/page_2_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_2_option1/page_2_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_2_option2/page_2_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_2_option2/page_2_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_2_option3/page_2_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_2_option3/page_2_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_20 turn=10..10
ORX page_20_option1/page_20_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(0.4); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(0.3)) | D:C(0.5)
ORX page_20_option1/page_20_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_20_option2/page_20_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_20_option2/page_20_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_20_option3/page_20_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_20_option3/page_20_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_21 turn=10..10
ORX page_21_option1/page_21_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(1); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(0.6)) | D:C(0.5)
ORX page_21_option1/page_21_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_21_option2/page_21_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_21_option2/page_21_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_21_option3/page_21_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_21_option3/page_21_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_22 turn=10..10
ORX page_22_option1/page_22_option1_reaction1 -> wild | O:Accept the ending. | E:SET char_lira.Stable_Volatile = C(0.6); SET char_vega.Trust_Betrayal = BLEND(C(0.4),P(char_vega.Trust_Betrayal),C(-0.2)) | D:C(0.5)
ORX page_22_option1/page_22_option1_reaction2 -> wild | O:Accept the ending. | E:SET char_axel.Pragmatic_Idealistic = BLEND(C(0.25),P(char_axel.Pragmatic_Idealistic),C(0)) | D:C(0.5)
ORX page_22_option2/page_22_option2_reaction1 -> wild | O:Resist the tide. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(-0.15)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.1)) | D:C(0.5)
ORX page_22_option2/page_22_option2_reaction2 -> wild | O:Resist the tide. | E:SET char_lira.Pragmatic_Idealistic = BLEND(C(0.2),P(char_lira.Pragmatic_Idealistic),C(0.1)) | D:C(0.5)
ORX page_22_option3/page_22_option3_reaction1 -> wild | O:Walk the third path. | E:SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
ORX page_22_option3/page_22_option3_reaction2 -> wild | O:Walk the third path. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)) | D:C(0.5)

ENC page_23 turn=3..4
ORX page_23_option1/page_23_option1_reaction1 -> wild | O:Lean into volatility. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_axel.Stable_Volatile),C(0.1)),C(0.7),C(0.2))
ORX page_23_option2/page_23_option2_reaction1 -> wild | O:Pursue the ruins. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_lira.Pragmatic_Idealistic),C(0.05)),C(0.6),C(0.25))
ORX page_23_option3/page_23_option3_reaction1 -> wild | O:Play the market. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_vega.Trust_Betrayal),C(-0.05)),C(0.55),C(0.3))

ENC page_24 turn=5..6
ORX page_24_option1/page_24_option1_reaction1 -> wild | O:Thread the minefield. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_axel.Stable_Volatile),C(0)),C(0.65),C(0.25))
ORX page_24_option2/page_24_option2_reaction1 -> wild | O:Seek an embassy favor. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_lira.Pragmatic_Idealistic),C(-0.05)),C(0.6),C(0.25))
ORX page_24_option3/page_24_option3_reaction1 -> wild | O:Dip into smugglers’ lanes. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_vega.Trust_Betrayal),C(-0.1)),C(0.6),C(0.25))

ENC page_3 turn=1..2
ORX page_3_option1/page_3_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_3_option1/page_3_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_3_option2/page_3_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_3_option2/page_3_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_3_option3/page_3_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_3_option3/page_3_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_4 turn=1..2
ORX page_4_option1/page_4_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_4_option1/page_4_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_4_option2/page_4_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_4_option2/page_4_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_4_option3/page_4_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_4_option3/page_4_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_5 turn=2..3
ORX page_5_option1/page_5_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_5_option1/page_5_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_5_option2/page_5_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_5_option2/page_5_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_5_option3/page_5_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_5_option3/page_5_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_6 turn=2..3
ORX page_6_option1/page_6_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_6_option1/page_6_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_6_option2/page_6_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_6_option2/page_6_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_6_option3/page_6_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_6_option3/page_6_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_7 turn=3..4
ORX page_7_option1/page_7_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_7_option1/page_7_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_7_option2/page_7_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_7_option2/page_7_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_7_option3/page_7_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_7_option3/page_7_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_8 turn=3..4
ORX page_8_option1/page_8_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_8_option1/page_8_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_8_option2/page_8_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_8_option2/page_8_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_8_option3/page_8_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_8_option3/page_8_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)

ENC page_9 turn=3..4
ORX page_9_option1/page_9_option1_reaction1 -> wild | O:Take the pragmatic route. | E:SET char_lira.Trust_Betrayal = NUDGE(P(char_lira.Trust_Betrayal),C(0.05)); SET char_vega.Pragmatic_Idealistic = NUDGE(P(char_vega.Pragmatic_Idealistic),C(-0.08)) | D:C(0.5)
ORX page_9_option1/page_9_option1_reaction2 -> wild | O:Take the pragmatic route. | E:SET char_axel.Stable_Volatile = BLEND(C(0.2),P(char_axel.Stable_Volatile),C(0)) | D:C(0.5)
ORX page_9_option2/page_9_option2_reaction1 -> wild | O:Push the ideal. | E:SET char_lira.Pragmatic_Idealistic = NUDGE(P(char_lira.Pragmatic_Idealistic),C(0.09)); SET char_vega.Trust_Betrayal = NUDGE(P(char_vega.Trust_Betrayal),C(0.03)) | D:C(0.5)
ORX page_9_option2/page_9_option2_reaction2 -> wild | O:Push the ideal. | E:SET char_axel.Stable_Volatile = BLEND(C(0.15),P(char_axel.Stable_Volatile),C(-0.1)) | D:C(0.5)
ORX page_9_option3/page_9_option3_reaction1 -> wild | O:Take a reckless shortcut. | E:SET char_axel.Stable_Volatile = NUDGE(P(char_axel.Stable_Volatile),C(0.12)); SET char_axel.Trust_Betrayal = NUDGE(P(char_axel.Trust_Betrayal),C(-0.05)) | D:C(0.5)
ORX page_9_option3/page_9_option3_reaction2 -> wild | O:Take a reckless shortcut. | E:SET char_vega.Pragmatic_Idealistic = BLEND(C(0.25),P(char_vega.Pragmatic_Idealistic),C(-0.05)) | D:C(0.5)
