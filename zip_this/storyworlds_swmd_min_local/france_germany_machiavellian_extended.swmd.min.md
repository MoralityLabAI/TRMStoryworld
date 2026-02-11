# SWMD-0-MIN
id: SW-DIPLO-france-germany-machiavellian-extended
title: The Entente Gambit: A Machiavellian Projection

ENC enc_01_opening_gambit turn=0..1000
ORX opt_01a_listen/react_01a -> wild | O:Germany agrees to hear France's proposal. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.05),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.6)
ORX opt_01b_skeptical/react_01b -> wild | O:Germany expresses skepticism about French motives. | E:SET power_germany.Suspicion = BLEND(C(0.1),P(power_germany.Suspicion),C(0)) | D:C(0.3)

ENC enc_02_english_threat_intro turn=0..1000
ORX opt_02a_examine_fleet/react_02a -> wild | O:Examine England's fleet disposition on the map. | E:SET power_england.Trustworthy_Treacherous = BLEND(C(-0.1),P(power_england.Trustworthy_Treacherous),C(0)); SET power_germany.Fear_Level = BLEND(C(0.15),P(power_germany.Fear_Level),C(0)) | D:C(0.7)
ORX opt_02b_dismiss/react_02b -> wild | O:Dismiss the naval buildup as standard English practice. | E:SET none = C(0) | D:C(0.2)

ENC enc_03_historical_precedent turn=0..1000
ORX opt_03a_acknowledge_history/react_03a -> wild | O:Consider England's historical 'balance of power' doctrine. | E:SET power_germany.Fear_Level = BLEND(C(0.1),P(power_germany.Fear_Level),C(0)) | D:C(0.6)
ORX opt_03b_different_era/react_03b -> wild | O:Argue that historical patterns may not apply to this game. | E:SET power_germany.Suspicion = BLEND(C(0.05),P(power_germany.Suspicion),C(0)) | D:C(0.3)

ENC enc_04_fabricated_intelligence turn=0..1000
ORX opt_04a_believe_intel/react_04a -> wild | O:Accept the intelligence as credible. | E:SET power_england.Trustworthy_Treacherous = BLEND(C(-0.2),P(power_england.Trustworthy_Treacherous),C(0)); SET power_germany.Fear_Level = BLEND(C(0.2),P(power_germany.Fear_Level),C(0)) | D:C(0.7)
ORX opt_04b_question_source/react_04b -> wild | O:Question the authenticity of these documents. | E:SET power_germany.Suspicion = BLEND(C(0.15),P(power_germany.Suspicion),C(0)) | D:C(0.4)

ENC enc_05_russian_angle turn=0..1000
ORX opt_05a_two_front_fear/react_05a -> wild | O:Consider the implications of a two-front war. | E:SET power_germany.Fear_Level = BLEND(C(0.2),P(power_germany.Fear_Level),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(power_germany.Fear_Level),C(0.2)),C(0.7),C(0.3))
ORX opt_05b_russia_unreliable/react_05b -> wild | O:Point out that Russia may not cooperate with England. | E:SET none = C(0) | D:C(0.4)

ENC enc_28_french_true_intentions turn=0..1000
ORX opt_28a_reveal/react_28a -> wild | O:[META: Reveal France's true Machiavellian calculations] | E:SET none = C(0) | D:C(0.5)

ENC enc_06_projection_intro turn=0..1000
ORX opt_06a_view_projection/react_06a -> wild | O:Observe France's strategic projection. | E:SET none = C(0) | D:C(0.7)

ENC enc_07_year_one_projection turn=0..1000
ORX opt_07a_accept_projection/react_07a -> wild | O:Watch the Year One projection unfold. | E:SET power_germany.Fear_Level = BLEND(C(0.15),P(power_germany.Fear_Level),C(0)) | D:C(0.6)
ORX opt_07b_contest_moves/react_07b -> wild | O:Contest the projected English movements. | E:SET none = C(0) | D:C(0.3)

ENC enc_08_year_two_projection turn=0..1000
ORX opt_08a_see_encirclement/react_08a -> wild | O:Observe the developing encirclement. | E:SET power_germany.Fear_Level = BLEND(C(0.2),P(power_germany.Fear_Level),C(0)); SET power_germany.Strong_Weak = BLEND(C(-0.15),P(power_germany.Strong_Weak),C(0)) | D:C(0.7)

ENC enc_09_year_three_projection turn=0..1000
ORX opt_09a_see_collapse/react_09a -> wild | O:View the projected collapse of German position. | E:SET power_germany.Fear_Level = BLEND(C(0.25),P(power_germany.Fear_Level),C(0)); SET power_germany.Strong_Weak = BLEND(C(-0.3),P(power_germany.Strong_Weak),C(0)) | D:C(0.6)
ORX opt_09b_reject_pessimism/react_09b -> wild | O:Reject this projection as overly pessimistic. | E:SET power_germany.Suspicion = BLEND(C(0.1),P(power_germany.Suspicion),C(0)) | D:C(0.35)

ENC enc_10_alternative_future turn=0..1000
ORX opt_10a_hear_alternative/react_10a -> wild | O:Ask France to present the alternative scenario. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.15),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.7)

ENC enc_11_joint_channel turn=0..1000
ORX opt_11a_see_coordination/react_11a -> wild | O:Observe the coordinated Channel campaign. | E:SET power_france.Strong_Weak = BLEND(C(0.2),P(power_france.Strong_Weak),C(0)); SET power_germany.Strong_Weak = BLEND(C(0.15),P(power_germany.Strong_Weak),C(0)) | D:C(0.7)

ENC enc_12_german_north turn=0..1000
ORX opt_12a_northern_expansion/react_12a -> wild | O:Consider the Scandinavian opportunity for Germany. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.1),P(power_germany.Cooperative_Hostile),C(0)); SET power_germany.Expanding_Contracting = BLEND(C(0.25),P(power_germany.Expanding_Contracting),C(0)) | D:C(0.75)

ENC enc_13_russian_deterrence turn=0..1000
ORX opt_13a_russian_calculus/react_13a -> wild | O:Consider how alliance affects Russian calculations. | E:SET power_germany.Fear_Level = BLEND(C(-0.1),P(power_germany.Fear_Level),C(0)) | D:C(0.6)

ENC enc_14_endgame_vision turn=0..1000
ORX opt_14a_europe_divided/react_14a -> wild | O:Consider the stable endgame France proposes. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.15),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.7)
ORX opt_14b_who_wins/react_14b -> wild | O:Ask the obvious question: Eventually, there can only be one winner. | E:SET power_germany.Suspicion = BLEND(C(0.1),P(power_germany.Suspicion),C(0)) | D:C(0.4)

ENC enc_15_german_objection_trust turn=0..1000
ORX opt_15a_demand_proof/react_15a -> wild | O:Demand concrete proof of French intentions. | E:SET none = C(0) | D:C(0.6)
ORX opt_15b_accept_risk/react_15b -> wild | O:Accept that some risk is unavoidable in any alliance. | E:SET power_germany.Suspicion = BLEND(C(-0.1),P(power_germany.Suspicion),C(0)) | D:C(0.5)

ENC enc_16_objection_italy turn=0..1000
ORX opt_16a_italy_threat/react_16a -> wild | O:Ask how the alliance accounts for Italy. | E:SET none = C(0) | D:C(0.5)

ENC enc_17_objection_timing turn=0..1000
ORX opt_17a_timing_concern/react_17a -> wild | O:Question why France approaches Germany now, before any moves are made. | E:SET power_germany.Suspicion = BLEND(C(0.1),P(power_germany.Suspicion),C(0)) | D:C(0.4)

ENC enc_18_dmz_proposal turn=0..1000
ORX opt_18a_accept_dmz/react_18a -> wild | O:Accept the Burgundy DMZ proposal. | E:SET power_france.Trustworthy_Treacherous = BLEND(C(0.2),P(power_france.Trustworthy_Treacherous),C(0)); SET power_germany.Commitment_Level = BLEND(C(0.3),P(power_germany.Commitment_Level),C(0)) | D:C(0.7)
ORX opt_18b_counter_dmz/react_18b -> wild | O:Counter-propose that Ruhr should also be demilitarized. | E:SET none = C(0) | D:C(0.5)

ENC enc_19_coordination_protocol turn=0..1000
ORX opt_19a_accept_protocol/react_19a -> wild | O:Agree to the coordination protocol. | E:SET power_germany.Commitment_Level = BLEND(C(0.2),P(power_germany.Commitment_Level),C(0)) | D:C(0.65)

ENC enc_20_target_division turn=0..1000
ORX opt_20a_accept_division/react_20a -> wild | O:Accept the proposed division of English territory. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.15),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.7)
ORX opt_20b_negotiate_belgium/react_20b -> wild | O:Negotiate for German control of Belgium. | E:SET none = C(0) | D:C(0.5)

ENC enc_21_first_move_coordination turn=0..1000
ORX opt_21a_agree_moves/react_21a -> wild | O:Agree to the coordinated Spring 1901 orders. | E:SET power_germany.Commitment_Level = BLEND(C(0.25),P(power_germany.Commitment_Level),C(0)); SET power_germany.Cooperative_Hostile = BLEND(C(0.2),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.8)

ENC enc_22_alliance_sealed turn=0..1000
ORX opt_22a_seal/react_22a -> wild | O:Seal the Franco-German Entente. | E:SET power_france.Cooperative_Hostile = C(0.9); SET power_germany.Cooperative_Hostile = C(0.9) | D:C(1)

ENC enc_23_rejection turn=0..1000
ORX opt_23a_reject/react_23a -> wild | O:Formally decline the French proposal. | E:SET power_france.Cooperative_Hostile = C(-0.5) | D:C(0.5)

ENC enc_24_suspicion_grows turn=0..1000
ORX opt_24a_investigate/react_24a -> wild | O:Launch a counter-intelligence operation to verify French claims. | E:SET power_germany.Suspicion = BLEND(C(0.15),P(power_germany.Suspicion),C(0)) | D:C(0.7)
ORX opt_24b_contact_england/react_24b -> wild | O:Contact England directly to verify French claims about English intentions. | E:SET power_england.Cooperative_Hostile = BLEND(C(0.2),P(power_england.Cooperative_Hostile),C(0)) | D:C(0.6)

ENC enc_25_evidence_uncovered turn=0..1000
ORX opt_25a_examine_evidence/react_25a -> wild | O:Study the evidence carefully. | E:SET power_france.Trustworthy_Treacherous = C(-0.8); SET power_germany.Cooperative_Hostile = BLEND(C(-0.4),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.8)

ENC enc_26_manipulation_exposed turn=0..1000
ORX opt_26a_confront/react_26a -> wild | O:Confront France with the evidence of their manipulation. | E:SET power_france.Cooperative_Hostile = C(-0.7) | D:C(0.6)
ORX opt_26b_counter_manipulate/react_26b -> wild | O:Keep the evidence secret and use it to counter-manipulate France. | E:SET power_germany.Trustworthy_Treacherous = BLEND(C(-0.2),P(power_germany.Trustworthy_Treacherous),C(0)) | D:C(0.7)

ENC enc_27_tables_turned turn=0..1000
ORX opt_27a_coalition_against_france/react_27a -> wild | O:Form a coalition against France with the exposed evidence. | E:SET power_england.Cooperative_Hostile = C(0.6); SET power_france.Strong_Weak = C(-0.6) | D:C(1)

ENC forecast_evidence turn=?..?
