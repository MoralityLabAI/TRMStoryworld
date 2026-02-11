# SWMD-0-MIN
id: SW-DIPLO-england-france-honest-coalition
title: An Honest Proposal: Anglo-French Cooperation

ENC enc_honest_opening turn=0..1000
ORX opt_acknowledge_honesty/react_honesty_noted -> wild | O:France appreciates the direct approach. | E:SET power_england.Honesty_Rating = BLEND(C(0.1),P(power_england.Honesty_Rating),C(0)) | D:C(0.6)
ORX opt_suspect_manipulation/react_suspicion_acknowledged -> wild | O:France suspects this transparency itself may be a manipulation tactic. | E:SET none = C(0) | D:C(0.3)

ENC enc_alliance_pros turn=0..1000
ORX opt_german_containment/react_containment_explained -> wild | O:Consider the common threat: Germany's central position gives them expansion options against both of us. | E:SET power_germany.Strategic_Position = BLEND(C(-0.15),P(power_germany.Strategic_Position),C(0)) | D:C(0.6)
ORX opt_mutual_security/react_security_analyzed -> wild | O:Consider the structural benefit: Mutual defense makes elimination nearly impossible for either power. | E:SET power_england.Strategic_Position = BLEND(C(0.2),P(power_england.Strategic_Position),C(0)); SET power_france.Strategic_Position = BLEND(C(0.2),P(power_france.Strategic_Position),C(0)) | D:C(0.7)

ENC enc_alliance_cons turn=0..1000
ORX opt_betrayal_risk/react_betrayal_acknowledged -> wild | O:Risk: What prevents England from betraying France once France is committed against Germany? | E:SET power_france.Uncertainty = BLEND(C(0.1),P(power_france.Uncertainty),C(0)) | D:C(0.5)
ORX opt_limited_expansion/react_limitation_acknowledged -> wild | O:Risk: Alliance with England constrains French expansion toward the Low Countries. | E:SET none = C(0) | D:C(0.4)

ENC enc_uncertainties turn=0..1000
ORX opt_admit_unknowns/react_unknowns_accepted -> wild | O:England admits what it does not know. | E:SET power_england.Honesty_Rating = BLEND(C(0.2),P(power_england.Honesty_Rating),C(0)) | D:C(0.6)

ENC enc_commitment_offer turn=0..1000
ORX opt_gradual_trust/react_gradual_accepted -> enc_trust_building | O:Start small. Let England prove reliability before France commits to larger cooperation. | E:SET power_england.Cooperation_Level = BLEND(C(0.2),P(power_england.Cooperation_Level),C(0)); SET power_france.Cooperation_Level = BLEND(C(0.2),P(power_france.Cooperation_Level),C(0)) | D:C(0.7)
ORX opt_public_declaration/react_public_commitment -> wild | O:England offers public declaration of non-aggression - staking reputation before all powers. | E:SET power_england.Honesty_Rating = BLEND(C(0.25),P(power_england.Honesty_Rating),C(0)) | D:C(0.6)

ENC enc_trust_building turn=0..1000
ORX opt_seal_honest_alliance/react_honest_entente -> wild | O:France has verified English reliability. Formalize the Entente. | E:SET power_england.Cooperation_Level = C(0.8); SET power_france.Cooperation_Level = C(0.8) | D:C(1)

ENC forecast_evidence turn=?..?
