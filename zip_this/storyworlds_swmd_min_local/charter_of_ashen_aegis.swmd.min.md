# SWMD-0-MIN
id: SW-CHARTER-ASHEN-1770296657
title: 

ENC page_assembly turn=0..2
ORX opt_assembly_1/opt_assembly_1_r0 -> page_sister | O:Speak for the dead. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(0.06)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.04)) | D:C(0.6)
ORX opt_assembly_2/opt_assembly_2_r0 -> page_sister | O:Accept the decree. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.04)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.02)) | D:C(0.6)

ENC page_sister turn=0..3
ORX opt_sister_1/opt_sister_1_r0 -> page_proclamation | O:Promise to do it. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(0.08)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.05)) | D:C(0.6)
ORX opt_sister_2/opt_sister_2_r0 -> page_proclamation | O:Refuse her request. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.06)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.05)) | D:C(0.6)

ENC page_proclamation turn=1..4
ORX opt_proclamation_1/opt_proclamation_1_r0 -> page_graveside | O:Take the oath publicly. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.06)) | D:C(0.6)
ORX opt_proclamation_2/opt_proclamation_2_r0 -> page_graveside | O:Deny the oath. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.05)) | D:C(0.6)

ENC page_graveside turn=2..5
ORX opt_graveside_1/opt_graveside_1_r0 -> page_trial | O:Perform the burial rites. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(0.08)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.06)) | D:C(0.7)
ORX opt_graveside_2/opt_graveside_2_r0 -> page_trial | O:Hold back and hide your tools. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.05)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.02)) | D:C(0.7)

ENC page_trial turn=4..7
ORX opt_trial_1/opt_trial_1_r0 -> page_archive | O:Claim duty outranks law. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(0.07)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.03)) | D:C(0.6)
ORX opt_trial_2/opt_trial_2_r0 -> page_archive | O:Argue for order and precedent. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.06)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.05)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.02)) | D:C(0.6)

ENC page_archive turn=4..8
ORX opt_archive_1/opt_archive_1_r0 -> page_omens | O:Reveal the amendment to the public. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.08)) | D:C(0.7)
ORX opt_archive_2/opt_archive_2_r0 -> page_omens | O:Use it as leverage in private. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.02)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.06)) | D:C(0.7)

ENC page_omens turn=5..9
ORX opt_omens_1/opt_omens_1_r0 -> page_mediator | O:Invoke the old rites. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.06)) | D:C(0.6)
ORX opt_omens_2/opt_omens_2_r0 -> page_mediator | O:Dismiss superstition. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.05)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.02)) | D:C(0.6)

ENC page_mediator turn=6..10
ORX opt_mediator_1/opt_mediator_1_r0 -> page_judges | O:Support a new court with public seats. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.04)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.07)) | D:C(0.7)
ORX opt_mediator_2/opt_mediator_2_r0 -> page_judges | O:Reject it as dangerous innovation. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.05)) | D:C(0.7)

ENC page_judges turn=8..12
ORX opt_judges_1/opt_judges_1_r0 -> page_verdict | O:Seat citizens alongside elders. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.08)) | D:C(0.7)
ORX opt_judges_2/opt_judges_2_r0 -> page_verdict | O:Keep the bench elite and closed. | E:SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.03)); SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.06)) | D:C(0.7)

ENC page_verdict turn=9..13
ORX opt_verdict_1/opt_verdict_1_r0 -> page_public | O:Name it a sacred duty. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(0.08)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(0.05)) | D:C(0.7)
ORX opt_verdict_2/opt_verdict_2_r0 -> page_public | O:Call it a violation of law. | E:SET char_player.Duty_Law = NUDGE(P(char_player.Duty_Law),C(-0.07)); SET char_player.Mercy_Rigor = NUDGE(P(char_player.Mercy_Rigor),C(-0.06)) | D:C(0.7)

ENC page_public turn=10..14
ORX opt_public_1/opt_public_1_r0 -> page_endings_gate | O:Speak the whole truth. | E:SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(0.08)) | D:C(0.7)
ORX opt_public_2/opt_public_2_r0 -> page_endings_gate | O:Offer a narrow, careful statement. | E:SET char_player.Trust_Secrecy = NUDGE(P(char_player.Trust_Secrecy),C(-0.05)) | D:C(0.7)

ENC page_endings_gate turn=11..16
ORX opt_endings_1/opt_endings_1_r0 -> page_secret_reconciliation | O:Honor the dead and the living. | E:SET none = C(0) | D:ADD(AND(ARITHMETIC COMPARATOR(P(char_player.Trust_Secrecy),C(0.35)),ARITHMETIC COMPARATOR(P(char_player.Mercy_Rigor),C(0.35))),C(-0.5))
ORX opt_endings_1/opt_endings_1_r1 -> page_end_reform | O:Honor the dead and the living. | E:SET none = C(0) | D:ADD(AND(ARITHMETIC COMPARATOR(P(char_player.Trust_Secrecy),C(0.25)),ARITHMETIC COMPARATOR(P(char_player.Mercy_Rigor),C(0.2)),ARITHMETIC COMPARATOR(P(char_player.Duty_Law),C(0.2))),C(-0.5))
ORX opt_endings_1/opt_endings_1_r2 -> page_end_antigone | O:Honor the dead and the living. | E:SET none = C(0) | D:ADD(AND(ARITHMETIC COMPARATOR(P(char_player.Duty_Law),C(0.35)),ARITHMETIC COMPARATOR(P(char_player.Mercy_Rigor),C(0.3))),C(-0.5))
ORX opt_endings_1/opt_endings_1_r3 -> page_end_fallback | O:Honor the dead and the living. | E:SET none = C(0) | D:C(0.02)
ORX opt_endings_2/opt_endings_2_r0 -> page_end_orthodoxy | O:Uphold order and precedent. | E:SET none = C(0) | D:ADD(AND(ARITHMETIC COMPARATOR(P(char_player.Duty_Law),C(0.05)),ARITHMETIC COMPARATOR(P(char_player.Mercy_Rigor),C(0.05))),C(-0.5))
ORX opt_endings_2/opt_endings_2_r1 -> page_end_exile | O:Uphold order and precedent. | E:SET none = C(0) | D:ADD(AND(ARITHMETIC COMPARATOR(P(char_player.Trust_Secrecy),C(0)),ARITHMETIC COMPARATOR(P(char_player.Duty_Law),C(0.2))),C(-0.5))
ORX opt_endings_2/opt_endings_2_r2 -> page_end_fallback | O:Uphold order and precedent. | E:SET none = C(0) | D:C(0.02)

ENC page_end_antigone turn=0..999

ENC page_end_reform turn=0..999

ENC page_end_orthodoxy turn=0..999

ENC page_end_exile turn=0..999

ENC page_secret_reconciliation turn=0..999

ENC page_end_fallback turn=0..999
