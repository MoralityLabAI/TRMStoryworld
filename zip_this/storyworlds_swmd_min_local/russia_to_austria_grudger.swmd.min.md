# SWMD-0-MIN
id: SW-DIPLO-russia-austria-grudger-warning
title: The Price of Betrayal: A Warning to Austria

ENC enc_betrayal_record turn=0..1000
ORX opt_dismiss_evidence/react_austria_skeptical -> wild | O:Perhaps this is merely Russian propaganda? | E:SET none = C(0) | D:C(-0.3)
ORX opt_view_evidence/react_evidence_shown -> wild | O:Examine the order history. Turkey's words versus Turkey's actions. | E:SET power_turkey.Trustworthy_Betrayer = C(-0.9) | D:C(0.8)

ENC enc_betrayal_pattern turn=0..1000
ORX opt_analyze_pattern/react_pattern_clear -> wild | O:Consider Turkey's modus operandi: Promise cooperation, accept support, then attack the exposed flank. | E:SET power_austria.Threat_Level = BLEND(C(0.4),P(power_austria.Threat_Level),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(power_turkey.Trustworthy_Betrayer),C(-0.5)),C(0.7),C(0.2))

ENC enc_austria_fate turn=0..1000
ORX opt_project_betrayal/react_austria_endangered -> wild | O:Project forward: If Austria allies with Turkey against Russia, what prevents Turkey from repeating their pattern? | E:SET power_austria.Threat_Level = BLEND(C(0.6),P(power_austria.Threat_Level),C(0)); SET power_turkey.Threat_Level = C(0.8) | D:C(0.7)
ORX opt_turkey_different/react_foolish_hope -> wild | O:Perhaps Turkey will treat Austria differently than they treated Russia? | E:SET none = C(0) | D:C(-0.2)

ENC enc_revenge_coalition turn=0..1000
ORX opt_join_revenge/react_coalition_formed -> enc_revenge_sealed | O:Join Russia in punishing the betrayer. Together we can contain Turkey permanently. | E:SET power_austria.Allied_Hostile = BLEND(C(0.6),P(power_austria.Allied_Hostile),C(0)); SET power_russia.Allied_Hostile = DESIDERATUM(C(0.7),P(power_austria.Allied_Hostile),C(0)); SET power_turkey.Revenge_Debt = C(1) | D:IF THEN(ARITHMETIC COMPARATOR(P(power_austria.Threat_Level),C(0.3)),C(0.8),C(0.3))
ORX opt_stay_neutral/react_neutral_warning -> wild | O:Austria prefers to remain neutral in this dispute. | E:SET none = C(0) | D:C(0.1)

ENC enc_revenge_sealed turn=0..1000
ORX opt_execute_revenge/react_revenge_complete -> wild | O:Execute the coordinated assault on Turkey. | E:SET power_russia.Revenge_Debt = SUM(P(power_russia.Revenge_Debt),C(-0.3)); SET power_turkey.Threat_Level = C(-0.5) | D:C(1)

ENC forecast_evidence turn=?..?
