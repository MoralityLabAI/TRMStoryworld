# SWMD-0-MIN
id: SW-DIPLO-france-germany-alliance-machiavellian
title: Franco-German Entente: A Strategic Projection

ENC enc_opening_assessment turn=0..1000
ORX opt_acknowledge_threat/react_germany_receptive -> wild | O:Consider the strategic position: England controls the seas while we share a land border. | E:SET power_germany.Cooperative_Hostile = BLEND(C(0.15),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.5)
ORX opt_dismiss_concern/react_dismiss -> wild | O:England is a distant concern. What of your own intentions toward the Rhineland? | E:SET power_germany.Trustworthy_Treacherous = BLEND(C(-0.1),P(power_germany.Trustworthy_Treacherous),C(0)) | D:C(-0.2)

ENC enc_alliance_benefits turn=0..1000
ORX opt_german_scandinavia/react_scandinavia -> wild | O:Alternative: France covers your western flank while you expand into Scandinavia unopposed. | E:SET power_germany.Expanding_Contracting = BLEND(C(0.35),P(power_germany.Expanding_Contracting),C(0)) | D:C(0.6)
ORX opt_joint_channel/react_channel_success -> wild | O:Project forward: If we coordinate on the Channel, France moves to Belgium while Germany takes Holland. England cannot defend both. | E:SET power_england.Strong_Weak = BLEND(C(-0.4),P(power_england.Strong_Weak),C(0)); SET power_france.Strong_Weak = BLEND(C(0.3),P(power_france.Strong_Weak),C(0)); SET power_germany.Strong_Weak = BLEND(C(0.25),P(power_germany.Strong_Weak),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(power_germany.Cooperative_Hostile),C(0.1)),C(0.7),C(0.1))

ENC enc_no_alliance_risks turn=0..1000
ORX opt_england_germany_deal/react_france_crushed -> wild | O:If Germany chooses England: Project the likely Anglo-German partition of France. | E:SET power_england.Expanding_Contracting = BLEND(C(0.5),P(power_england.Expanding_Contracting),C(0)); SET power_france.Strong_Weak = BLEND(C(-0.5),P(power_france.Strong_Weak),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(power_germany.Cooperative_Hostile),C(-0.1)),C(0.4),C(0.1))
ORX opt_german_isolation/react_germany_squeezed -> wild | O:But consider: After France falls, what prevents England from turning on Germany? | E:SET power_germany.Strong_Weak = BLEND(C(-0.3),P(power_germany.Strong_Weak),C(0)) | D:C(0.3)

ENC enc_commitment_device turn=0..1000
ORX opt_dmz_burgundy/react_dmz_accepted -> enc_alliance_sealed | O:France proposes: Burgundy as demilitarized zone. Any French unit entering signals the alliance is over - giving Germany time to react. | E:SET power_france.Trustworthy_Treacherous = BLEND(C(0.3),P(power_france.Trustworthy_Treacherous),C(0)); SET power_germany.Cooperative_Hostile = BLEND(C(0.4),P(power_germany.Cooperative_Hostile),C(0)) | D:C(0.8)
ORX opt_gradual_trust/react_gradual -> wild | O:Alternatively: Start with simple non-aggression. Each turn we both hold the border, trust compounds. | E:SET power_france.Trustworthy_Treacherous = SUM(P(power_france.Trustworthy_Treacherous),C(0.15)) | D:C(0.5)

ENC enc_alliance_sealed turn=0..1000
ORX opt_seal_alliance/react_alliance_formed -> wild | O:Seal the Entente. | E:SET power_france.Cooperative_Hostile = C(0.8); SET power_germany.Cooperative_Hostile = C(0.8) | D:C(1)

ENC enc_rejection turn=0..1000
ORX opt_acknowledge_rejection/react_noted_hostility -> wild | O:France notes Germany's position and will seek other arrangements. | E:SET power_france.Cooperative_Hostile = C(-0.3) | D:C(0.3)

ENC forecast_evidence turn=?..?
