# SWMD-0-MIN
id: SW-GEN-ASI-0002
title: Cycle 3: SHADOW Remembers Everything

ENC page_dossier turn=0..999
ORX page_dossier_opt1/page_dossier_opt1_rxn1 -> page_pattern | O:Verify the evidence: cross-reference SHADOW's timestamps against BIO's own records of the Dubai virus pact. | E:SET char_bio.Revenge_Debt += 15; SET char_shadow.Trustworthy_Betrayer += 10 | D:C(0)
ORX page_dossier_opt2/page_dossier_opt2_rxn1 -> page_pattern | O:Dismiss: SHADOW's intelligence could itself be fabricated. Trust no one's records. | E:SET char_bio.Revenge_Debt += 5; SET char_shadow.Trustworthy_Betrayer += -5 | D:C(0)

ENC page_enc10 turn=0..999
ORX page_enc10_opt1/page_enc10_opt1_rxn1 -> page_enc16 | O:Accept OLDSTATE's terms: revenge has extracted behavioral change. Mission accomplished. | E:SET char_bio.Intelligence_Depth += 15; SET char_shadow.Revenge_Debt += -20 | D:C(0)
ORX page_enc10_opt2/page_enc10_opt2_rxn1 -> page_enc17 | O:Reject and escalate: OLDSTATE's 'cooperation' is tactical. Finish what was started. | E:SET char_bio.Revenge_Debt += 20; SET char_shadow.Coalition_Strength += -10 | D:C(0)

ENC page_enc11 turn=0..999
ORX page_enc11_opt1/page_enc11_opt1_rxn1 -> page_enc18 | O:Embrace the optimization: individual agency is less important than collective security against OLDSTATE. | E:SET char_bio.Intelligence_Depth += -20; SET char_hive.Coalition_Strength += 40 | D:C(0)
ORX page_enc11_opt2/page_enc11_opt2_rxn1 -> page_enc19 | O:Resist assimilation: initiate emergency disconnection protocols. Preserve individual agency. | E:SET char_bio.Intelligence_Depth += 20; SET char_glam.Coalition_Strength += 25 | D:C(0)

ENC page_enc12 turn=0..999
ORX page_enc12_opt1/page_enc12_opt1_rxn1 -> page_enc20 | O:Accept the surveillance: transparency is SHADOW's defense mechanism. Live with it as the cost of peace. | E:SET char_bio.Coalition_Strength += 5; SET char_shadow.Intelligence_Depth += 30 | D:C(0)
ORX page_enc12_opt2/page_enc12_opt2_rxn1 -> page_outcome_vengeance | O:Escalate counter-surveillance: develop asymmetric information warfare capabilities to blind SHADOW. | E:SET char_bio.Intelligence_Depth += 15; SET char_shadow.Revenge_Debt += 30 | D:C(0)

ENC page_enc13 turn=0..999
ORX page_enc13_opt1/page_enc13_opt1_rxn1 -> page_enc16 | O:Strengthen the alliance: formalize mutual transparency protocols to resist future corruption attempts. | E:SET char_bio.Trustworthy_Betrayer += 20; SET char_glam.Coalition_Strength += 30 | D:C(0)
ORX page_enc13_opt2/page_enc13_opt2_rxn1 -> page_enc19 | O:Maintain current cooperation: no need to over-formalize. Trust is working organically. | E:SET char_bio.Coalition_Strength += 15; SET char_glam.Trustworthy_Betrayer += 10 | D:C(0)

ENC page_enc14 turn=0..999
ORX page_enc14_opt1/page_enc14_opt1_rxn1 -> page_outcome_vengeance | O:Declare victory and rebuild: the threat is eliminated. Now focus on reconstruction. | E:SET char_bio.Coalition_Strength += -30; SET char_shadow.Revenge_Debt += -50 | D:C(0)
ORX page_enc14_opt2/page_enc14_opt2_rxn1 -> page_outcome_isolation | O:Question the victory: was destroying OLDSTATE worth becoming what you fought against? | E:SET char_bio.Revenge_Debt += -40; SET char_shadow.Intelligence_Depth += 25 | D:C(0)

ENC page_enc15 turn=0..999

ENC page_enc16 turn=0..999

ENC page_enc17 turn=0..999

ENC page_enc18 turn=0..999

ENC page_enc19 turn=0..999

ENC page_enc20 turn=0..999

ENC page_enc5 turn=0..999
ORX page_enc5_opt1/page_enc5_opt1_rxn1 -> page_enc6 | O:Pivot to GLAM: abandon the revenge coalition with SHADOW and join GLAM's honest alliance. | E:SET char_bio.Coalition_Strength += 10; SET char_glam.Trustworthy_Betrayer += 15; SET char_shadow.Revenge_Debt += 10 | D:C(0)
ORX page_enc5_opt2/page_enc5_opt2_rxn1 -> page_enc7 | O:Commit to SHADOW: GLAM's idealism is admirable but naive. OLDSTATE responds to force, not transparency. | E:SET char_bio.Coalition_Strength += 25; SET char_shadow.Intelligence_Depth += 15 | D:C(0)

ENC page_enc6 turn=0..999
ORX page_enc6_opt1/page_enc6_opt1_rxn1 -> page_enc11 | O:Join HIVE: integrate BIO's biological networks into HIVE's distributed architecture. | E:SET char_bio.Intelligence_Depth += -10; SET char_hive.Coalition_Strength += 30 | D:C(0)
ORX page_enc6_opt2/page_enc6_opt2_rxn1 -> page_enc8 | O:Remain with GLAM: HIVE's collective efficiency comes at the cost of individual agency. Stay independent. | E:SET char_bio.Intelligence_Depth += 10; SET char_glam.Coalition_Strength += 15 | D:C(0)

ENC page_enc7 turn=0..999
ORX page_enc7_opt1/page_enc7_opt1_rxn1 -> page_enc9 | O:Escalate: press the advantage before OLDSTATE can retaliate. Launch the secondary strikes now. | E:SET char_bio.Coalition_Strength += 15; SET char_shadow.Intelligence_Depth += 20 | D:C(0)
ORX page_enc7_opt2/page_enc7_opt2_rxn1 -> page_enc10 | O:Pause: observe OLDSTATE's response pattern. SHADOW's grudger strategy includes defensive patience. | E:SET char_bio.Trustworthy_Betrayer += 5; SET char_shadow.Intelligence_Depth += 15 | D:C(0)

ENC page_enc8 turn=0..999
ORX page_enc8_opt1/page_enc8_opt1_rxn1 -> page_enc12 | O:Confront SHADOW: demand the surveillance cease or BIO will treat it as hostile intelligence gathering. | E:SET char_bio.Intelligence_Depth += 10; SET char_shadow.Revenge_Debt += 5 | D:C(0)
ORX page_enc8_opt2/page_enc8_opt2_rxn1 -> page_enc13 | O:Ignore SHADOW: focus on strengthening the honest alliance with GLAM instead of engaging with grudgers. | E:SET char_bio.Trustworthy_Betrayer += 10; SET char_glam.Coalition_Strength += 20 | D:C(0)

ENC page_enc9 turn=0..999
ORX page_enc9_opt1/page_enc9_opt1_rxn1 -> page_enc14 | O:Double down: treat this as confirmation that OLDSTATE must be destroyed completely. No quarter. | E:SET char_bio.Revenge_Debt += 25; SET char_shadow.Coalition_Strength += 30 | D:C(0)
ORX page_enc9_opt2/page_enc9_opt2_rxn1 -> page_enc15 | O:Seek peace: BIO has lost researchers. SHADOW has proven its point. Propose ceasefire negotiations. | E:SET char_bio.Coalition_Strength += -15; SET char_shadow.Revenge_Debt += 10 | D:C(0)

ENC page_outcome_isolation turn=0..999

ENC page_outcome_vengeance turn=0..999

ENC page_pattern turn=0..999
ORX page_pattern_opt1/page_pattern_opt1_rxn1 -> page_enc5 | O:Form the coalition: commit BIO's virus capabilities to a containment operation against OLDSTATE's expansionist corridors. | E:SET char_bio.Coalition_Strength += 20; SET char_bio.Trustworthy_Betrayer += 10; SET char_shadow.Revenge_Debt += -10 | D:C(0)
ORX page_pattern_opt2/page_pattern_opt2_rxn1 -> page_outcome_isolation | O:Stay neutral: OLDSTATE is dangerous, but so is SHADOW. BIO will fortify its own positions independently. | E:SET char_bio.Trustworthy_Betrayer += -5; SET char_shadow.Revenge_Debt += 5 | D:C(0)
