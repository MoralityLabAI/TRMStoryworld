# SWMD-0-MIN
id: SW-01A2-c44e3306-bdba-4d55-a255-6312e22ff906
title: Dogs in a Barrel (Full)

ENC page_5d6b8073a83d45b8 turn=0..1000
ORX 0238ccaa80144666/611fb0437cab45fe -> wild | O:Say nothing | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.14)),C(0.3),C(0.03))
ORX 0238ccaa80144666/c0ece38869724083 -> wild | O:Say nothing | E:SET char_white.Loyal_Treacherous = BLEND(C(0.12),P(char_white.Loyal_Treacherous),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.18)),C(0.54),C(0.03))
ORX 51b9d413010b4932/a3422446fdcb4a5c -> wild | O:Keep pressure on Orange | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.28)),C(0.4),C(-0.09))
ORX 51b9d413010b4932/dae4ed9b91be4239 -> wild | O:Keep pressure on Orange | E:SET char_white.Loyal_Treacherous = DESIDERATUM(P(char_white.Loyal_Treacherous),P(char_pink.Loyal_Treacherous)); SET char_white.Loyal_Treacherous = BLEND(C(0.22),P(char_white.Loyal_Treacherous),C(0)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.26)),C(0.39),C(-0.02))
ORX 8dbe1a5a0f7a4f4d/6752f2a6bb7f41f8 -> wild | O:Accuse Pink of panicking | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.22)),C(0.46),C(-0.14))
ORX 8dbe1a5a0f7a4f4d/e8763ba5bf324b0b -> wild | O:Accuse Pink of panicking | E:SET char_white.Loyal_Treacherous = P(char_white.Loyal_Treacherous); SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(0.06)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.28)),C(0.43),C(-0.12))

ENC page_f70196ea43844a75 turn=0..1000
ORX 276a217036c44842/0497bf340fe34626 -> wild | O:Demand everyone lower their guns | E:SET char_pink.Loyal_Treacherous = NUDGE(P(char_pink.Loyal_Treacherous),C(0.027)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.28)),C(0.53),C(-0.28))
ORX 276a217036c44842/fbc0678ca3e7491e -> wild | O:Demand everyone lower their guns | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(0.04)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.11)),C(0.55),C(0.05))
ORX 8b082cde560a49c3/6a226e962cbb4f74 -> wild | O:Blame White | E:SET char_white.Honest_Tricky = NUDGE(P(char_white.Honest_Tricky),C(-0.027)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.12)),C(0.49),C(-0.27))
ORX 8b082cde560a49c3/84f5bc22e3b743b0 -> wild | O:Blame White | E:SET char_white.Calm_Explosive = NUDGE(P(char_white.Calm_Explosive),C(-0.006)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.12)),C(0.37),C(-0.19))
ORX ed4ee7c82da5488b/1ba976d14b2441d4 -> wild | O:Insist on calm | E:SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(-0.07)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.18)),C(0.28),C(-0.25))
ORX ed4ee7c82da5488b/e9d0af506d904e6d -> wild | O:Insist on calm | E:SET char_white.Calm_Explosive = NUDGE(P(char_white.Calm_Explosive),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.23)),C(0.43),C(0.02))

ENC page_377490ddf1564415 turn=0..1000
ORX 8e0067da33574eb9/7b457edcf82d4f6e -> wild | O:Tell him he’s dying | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(0.02)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.01)),C(0.37),C(-0.21))
ORX 8e0067da33574eb9/9ce5a58d393243ee -> wild | O:Tell him he’s dying | E:SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(0.037)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.11)),C(0.48),C(-0.28))
ORX c186202f1a4547d6/a476ed6b0fc74154 -> wild | O:Reassure Orange | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(0.038)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.18)),C(0.29),C(-0.08))
ORX c186202f1a4547d6/bd84ec0532d24bd7 -> page_12001716abfb4d6e | O:Reassure Orange | E:SET char_orange.Honest_Tricky = NUDGE(P(char_orange.Honest_Tricky),C(-0.012)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.09)),C(0.42),C(-0.15))
ORX c47a8ab1644749be/2fb3d85a300c401a -> wild | O:Stay silent | E:SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(0.038)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.22)),C(0.25),C(-0.06))
ORX c47a8ab1644749be/4cd93b95a5fe4521 -> wild | O:Stay silent | E:SET char_orange.Loyal_Treacherous = NUDGE(P(char_orange.Loyal_Treacherous),C(0.008)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.25)),C(0.28),C(0.08))

ENC page_de13269697d94b5b turn=0..1000
ORX 43020235cbb044e0/37d82801dfef4786 -> wild | O:Crack a joke | E:SET char_pink.Loyal_Treacherous = NUDGE(P(char_pink.Loyal_Treacherous),C(0.025)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.09)),C(0.46),C(-0.2))
ORX 43020235cbb044e0/a6145f9b32054cbb -> wild | O:Crack a joke | E:SET char_pink.Loyal_Treacherous = NUDGE(P(char_pink.Loyal_Treacherous),C(-0.036)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.1)),C(0.3),C(-0.15))
ORX 73e13344ba014da8/02051755892e4102 -> wild | O:Say 'We're all gonna die' | E:SET char_orange.Honest_Tricky = NUDGE(P(char_orange.Honest_Tricky),C(0.019)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.18)),C(0.55),C(-0.23))
ORX 73e13344ba014da8/244ec70bdcec48e7 -> wild | O:Say 'We're all gonna die' | E:SET char_pink.Loyal_Treacherous = NUDGE(P(char_pink.Loyal_Treacherous),C(-0.018)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.21)),C(0.4),C(-0.02))
ORX 8ac5c9e10b0b4a8e/4f9b6a6398244e9f -> wild | O:Quote Joe | E:SET char_white.Calm_Explosive = NUDGE(P(char_white.Calm_Explosive),C(0.006)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.11)),C(0.44),C(-0.25))
ORX 8ac5c9e10b0b4a8e/f347f7f4c9d84b6d -> wild | O:Quote Joe | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(0.02)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.11)),C(0.27),C(-0.17))

ENC page_59e7379997384df0 turn=0..1000
ORX 056af1facee34e52/0d1220fccd4d417b -> page_eea0f87e7ac04b25 | O:Doubt Joe | E:SET char_orange.Loyal_Treacherous = NUDGE(P(char_orange.Loyal_Treacherous),C(0.016)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.07)),C(0.33),C(0.06))
ORX 056af1facee34e52/bd38517334264654 -> wild | O:Doubt Joe | E:SET char_orange.Loyal_Treacherous = NUDGE(P(char_orange.Loyal_Treacherous),C(0.02)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.13)),C(0.45),C(-0.02))
ORX 8abdd5b3304a47b7/2eba43dab8c84cbe -> wild | O:Agree with Pink | E:SET char_white.Honest_Tricky = NUDGE(P(char_white.Honest_Tricky),C(-0.038)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.03)),C(0.39),C(0.09))
ORX 8abdd5b3304a47b7/de57e22594ac4d4f -> wild | O:Agree with Pink | E:SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(-0.023)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.07)),C(0.3),C(0))
ORX ae0be12a3b3f46ca/9cbb73e21a3947c1 -> wild | O:Stay neutral | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(0.033)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.27)),C(0.4),C(-0.21))
ORX ae0be12a3b3f46ca/a688c56f8efb4e96 -> wild | O:Stay neutral | E:SET char_orange.Calm_Explosive = NUDGE(P(char_orange.Calm_Explosive),C(-0.04)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.05)),C(0.26),C(-0.01))

ENC page_277fcc1a11b64f35 turn=0..1000
ORX dbaff88a28454314/5249d0a07e274817 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.14)),C(0.36),C(0.14))
ORX dbaff88a28454314/61cd0c5b83a4413a -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.2)),C(0.51),C(0.09))

ENC page_1e873704813347e5 turn=0..1000
ORX 07298386e18a4f07/b4644a7ce9054a7a -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.24)),C(0.52),C(-0.19))
ORX 07298386e18a4f07/d05e17cc62fd47f1 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.21)),C(0.32),C(-0.13))

ENC page_f7d5e992113c4029 turn=0..1000
ORX abd8fa47c4074434/30d4db569194483d -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.21)),C(0.45),C(-0.16))
ORX abd8fa47c4074434/bfa266f3470d4380 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.06)),C(0.53),C(-0.16))

ENC page_12001716abfb4d6e turn=0..1000
ORX ce701e6c935e4103/7b9e0b47d0d4420a -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.02)),C(0.38),C(-0.26))
ORX ce701e6c935e4103/840c080ccd07452b -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.17)),C(0.32),C(0.06))

ENC page_fb7b63c4c99a419f turn=0..1000
ORX fa8ae3366498463f/34ee65b6157c4caf -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(-0.08)),C(0.36),C(0))
ORX fa8ae3366498463f/4143da43f5d044ed -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.18)),C(0.57),C(0.08))

ENC page_eb31a08bef494344 turn=0..1000
ORX dfd42e809d814b5f/1eb264028ff94793 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(-0.17)),C(0.51),C(0.07))
ORX dfd42e809d814b5f/e61c453f104f4c3f -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.13)),C(0.39),C(0.11))

ENC page_9090ec2f8c7c45e3 turn=0..1000
ORX 192131aeeb6a45aa/3f56920459144476 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.1)),C(0.41),C(-0.29))
ORX 192131aeeb6a45aa/9e3c1374aa0941ea -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.14)),C(0.32),C(0.02))

ENC page_3134360518554b1a turn=0..1000
ORX 81f1bfd1ee914f11/4f490c5f93f54d8c -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.02)),C(0.31),C(-0.01))
ORX 81f1bfd1ee914f11/d5bd0d6078564c41 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.2)),C(0.47),C(0.16))

ENC page_25ef0b98d86c46c8 turn=0..1000
ORX b385effb544c4899/4d1b47cfbc484c2a -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.2)),C(0.36),C(0.16))
ORX b385effb544c4899/835fb5b52bf24568 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.21)),C(0.42),C(-0.12))

ENC page_9da5fc2ee9ac4f4c turn=0..1000
ORX 0a394f11bf354f64/0db8a47ac95a47e1 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.07)),C(0.46),C(-0.14))
ORX 0a394f11bf354f64/e1d2867da1cc4bc7 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.16)),C(0.58),C(-0.13))

ENC page_2900d0e8db664b83 turn=0..1000
ORX 25d2054e269743fd/0a222fad89404e75 -> wild | O:Draw your weapon | E:SET char_white.Loyal_Treacherous = DESIDERATUM(P(char_white.Loyal_Treacherous),P(char_pink.Calm_Explosive)); SET char_white.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_white.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.13)),C(0.33),C(-0.22))
ORX 25d2054e269743fd/2ce86126961541dd -> wild | O:Draw your weapon | E:SET char_pink.Honest_Tricky = ARITHMETIC MEAN(P(char_pink.Honest_Tricky),C(-0.89)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.12)),C(0.42),C(-0.16))
ORX 789323b8e908426f/052351398da045b5 -> wild | O:Back down | E:SET char_white.Honest_Tricky = ARITHMETIC MEAN(P(char_white.Honest_Tricky),C(-0.52)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.05)),C(0.31),C(-0.11))
ORX 789323b8e908426f/eba12befe20f4217 -> wild | O:Back down | E:SET char_white.Loyal_Treacherous = NUDGE(P(char_white.Loyal_Treacherous),C(0.17)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.18)),C(0.3),C(0.03))
ORX c5dd6be7402d4374/4b6b82ee736f4fc4 -> wild | O:Mock Blonde | E:SET char_white.Loyal_Treacherous = BLEND(C(0.23),P(char_white.Loyal_Treacherous),C(0.07)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.04)),C(0.52),C(0.09))
ORX c5dd6be7402d4374/a84d62d7c4db43df -> wild | O:Mock Blonde | E:SET char_orange.Calm_Explosive = ARITHMETIC MEAN(P(char_orange.Calm_Explosive),C(-0.18)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.24)),C(0.37),C(-0.11))

ENC page_db5408023ae2415c turn=0..1000
ORX 8931c955d5c5486f/9df6e92467314a8a -> wild | O:Egg him on | E:SET char_pink.Honest_Tricky = ARITHMETIC MEAN(P(char_pink.Honest_Tricky),C(0.84)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.09)),C(0.39),C(-0.11))
ORX 8931c955d5c5486f/bcbf7d4a312544ca -> wild | O:Egg him on | E:SET char_white.Calm_Explosive = ARITHMETIC MEAN(P(char_white.Calm_Explosive),C(-0.53)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.22)),C(0.37),C(-0.1))
ORX a2a83e02d8c2497e/1394f5411f9d4c9d -> page_97d0ab15eec747cd | O:Stop the torture | E:SET char_pink.Loyal_Treacherous = ARITHMETIC MEAN(P(char_pink.Loyal_Treacherous),C(-0.28)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.16)),C(0.55),C(-0.24))
ORX a2a83e02d8c2497e/9c1cf6da3517493c -> wild | O:Stop the torture | E:SET char_white.Honest_Tricky = ARITHMETIC MEAN(P(char_white.Honest_Tricky),C(-0.59)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.13)),C(0.36),C(-0.11))
ORX e66d93a7a4a24d8f/20a829f05975418f -> wild | O:Do nothing | E:SET char_orange.Calm_Explosive = ARITHMETIC MEAN(P(char_orange.Calm_Explosive),C(-0.99)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.23)),C(0.35),C(0.08))
ORX e66d93a7a4a24d8f/c114ced682a544eb -> wild | O:Do nothing | E:SET char_white.Honest_Tricky = ARITHMETIC MEAN(P(char_white.Honest_Tricky),C(-0.46)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.01)),C(0.34),C(-0.15))

ENC page_e54264d2ed914055 turn=0..1000
ORX 0803a5ee2588488a/a245cf7df34545b6 -> wild | O:Say nothing | E:SET char_white.Loyal_Treacherous = ARITHMETIC MEAN(P(char_white.Loyal_Treacherous),C(-0.31)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.19)),C(0.51),C(-0.12))
ORX 0803a5ee2588488a/a706ea2a8d0e4d64 -> wild | O:Say nothing | E:SET char_orange.Honest_Tricky = ARITHMETIC MEAN(P(char_orange.Honest_Tricky),C(-0.8)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.17)),C(0.37),C(-0.12))
ORX 4fd376d5e638409f/05b9968eae1e42b9 -> wild | O:Try to explain | E:SET char_orange.Loyal_Treacherous = ARITHMETIC MEAN(P(char_orange.Loyal_Treacherous),C(0.17)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.15)),C(0.58),C(0.04))
ORX 4fd376d5e638409f/db3196cd2cca4e43 -> wild | O:Try to explain | E:SET char_orange.Honest_Tricky = ARITHMETIC MEAN(P(char_orange.Honest_Tricky),C(0.94)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.14)),C(0.26),C(-0.09))
ORX 6bda72c2b2844224/2ab1723a54954d2b -> wild | O:Shoot again | E:SET char_orange.Honest_Tricky = ARITHMETIC MEAN(P(char_orange.Honest_Tricky),C(0.78)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.09)),C(0.34),C(0.08))
ORX 6bda72c2b2844224/bf4433a11abc4733 -> wild | O:Shoot again | E:SET char_orange.Loyal_Treacherous = ARITHMETIC MEAN(P(char_orange.Loyal_Treacherous),C(0.14)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.13)),C(0.55),C(-0.22))

ENC page_159e8f74d71343c2 turn=0..1000
ORX 02fdf42101b14d2a/3b892f050ac14beb -> wild | O:Admit everything | E:SET char_pink.Calm_Explosive = ARITHMETIC MEAN(P(char_pink.Calm_Explosive),C(-0.78)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.24)),C(0.42),C(-0.23))
ORX 02fdf42101b14d2a/4ea643fec3bd45d8 -> wild | O:Admit everything | E:SET char_pink.Calm_Explosive = ARITHMETIC MEAN(P(char_pink.Calm_Explosive),C(-0.41)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.24)),C(0.53),C(-0.06))
ORX cfc433ff23d74d4e/d90f013272174565 -> wild | O:Lie to Joe | E:SET char_pink.Calm_Explosive = ARITHMETIC MEAN(P(char_pink.Calm_Explosive),C(0.14)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(-0.11)),C(0.38),C(-0.02))
ORX cfc433ff23d74d4e/f04928a3ddb34372 -> page_695eeed18bda4a37 | O:Lie to Joe | E:SET char_pink.Calm_Explosive = ARITHMETIC MEAN(P(char_pink.Calm_Explosive),C(-0.35)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.15)),C(0.28),C(-0.01))
ORX f2e00141604e4850/8a29725fe8f94709 -> wild | O:Stay vague | E:SET char_white.Calm_Explosive = ARITHMETIC MEAN(P(char_white.Calm_Explosive),C(-0.42)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.18)),C(0.32),C(-0.04))
ORX f2e00141604e4850/ad4e9114806a4903 -> wild | O:Stay vague | E:SET char_pink.Honest_Tricky = ARITHMETIC MEAN(P(char_pink.Honest_Tricky),C(0.15)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.29)),C(0.49),C(-0.27))

ENC page_aeb0e98a4f3046a4 turn=0..1000
ORX 2cb53f9870ed40df/2481697e087d4420 -> wild | O:Stay out of it | E:SET char_white.Honest_Tricky = ARITHMETIC MEAN(P(char_white.Honest_Tricky),C(-0.6)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.03)),C(0.42),C(-0.23))
ORX 2cb53f9870ed40df/f00bb18ca33d4c1e -> wild | O:Stay out of it | E:SET char_pink.Honest_Tricky = ARITHMETIC MEAN(P(char_pink.Honest_Tricky),C(0.48)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.22)),C(0.54),C(0.08))
ORX 7719750ac16746ef/20adaa7768f04066 -> wild | O:Defend Orange | E:SET char_pink.Honest_Tricky = ARITHMETIC MEAN(P(char_pink.Honest_Tricky),C(0.66)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.12)),C(0.46),C(-0.12))
ORX 7719750ac16746ef/55113d7c57a644d2 -> wild | O:Defend Orange | E:SET char_white.Loyal_Treacherous = ARITHMETIC MEAN(P(char_white.Loyal_Treacherous),C(-0.59)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.09)),C(0.48),C(-0.3))
ORX a4d70371a1384379/421886faa9924e6f -> wild | O:Accuse Pink | E:SET char_pink.Calm_Explosive = ARITHMETIC MEAN(P(char_pink.Calm_Explosive),C(-0.62)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.27)),C(0.5),C(-0.16))
ORX a4d70371a1384379/b50123bb82be43cf -> wild | O:Accuse Pink | E:SET char_white.Calm_Explosive = ARITHMETIC MEAN(P(char_white.Calm_Explosive),C(0.47)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.27)),C(0.56),C(0.03))

ENC page_0b6e2e5c0df84f38 turn=0..1000
ORX f67746c3b2a94990/690ffe1037fc4fbf -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.1)),C(0.49),C(0.08))
ORX f67746c3b2a94990/ef25c2e8b8794b22 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.09)),C(0.3),C(-0.02))

ENC page_eea0f87e7ac04b25 turn=0..1000
ORX 4b7b1aa1aff14a82/5a61fbe689be4889 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.2)),C(0.48),C(0.17))
ORX 4b7b1aa1aff14a82/c2bbf93f7d7c4f1c -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.23)),C(0.48),C(-0.07))

ENC page_0bcca15f65ec4a85 turn=0..1000
ORX 3fa6295682244484/35f871c4225c4905 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.07)),C(0.58),C(0.04))
ORX 3fa6295682244484/5ce1bf0274da4e9c -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.27)),C(0.37),C(-0.28))

ENC page_4fe5969405e74cdf turn=0..1000
ORX 90358dae1578467a/4f9a7d6a434a4819 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.15)),C(0.43),C(-0.18))
ORX 90358dae1578467a/7226909583374f4a -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.15)),C(0.48),C(-0.23))

ENC page_befd2de33e7d4fcb turn=0..1000
ORX feca5327be7a4a18/c217417f6b604e18 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.18)),C(0.58),C(-0.22))
ORX feca5327be7a4a18/e1731c1bc95a449f -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.29)),C(0.46),C(0.01))

ENC page_dffe9ae08b534e66 turn=0..1000
ORX 4c1cbd3d45034ad2/3496b5fa4a8e4f69 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.06)),C(0.46),C(-0.04))
ORX 4c1cbd3d45034ad2/c0da7bff15d943c1 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.24)),C(0.29),C(-0.29))

ENC page_ab49ffe3cd0f4b80 turn=0..1000
ORX 598173e7af404d97/912d775bb26d4bf5 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.19)),C(0.42),C(-0.01))
ORX 598173e7af404d97/953b4dc5d59d4ab3 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.06)),C(0.55),C(-0.17))

ENC page_37ca4b9cff154a58 turn=0..1000
ORX bc9bfa2c1c5441e5/3180f277e30f4aac -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.07)),C(0.59),C(-0.12))
ORX bc9bfa2c1c5441e5/7136f1d21b2e43fc -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.27)),C(0.42),C(-0.05))

ENC page_7cb021206ed34d8e turn=0..1000
ORX d8909b752cdf4a0e/2f5a2c49a63b4542 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.24)),C(0.31),C(-0.13))
ORX d8909b752cdf4a0e/df90f862d28446d9 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.11)),C(0.26),C(0.05))

ENC page_d7c59d062282429a turn=0..1000
ORX e8a8cd4209d54891/a554e665b4514fa4 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.16)),C(0.51),C(0.15))
ORX e8a8cd4209d54891/eed63eb59e64472e -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.22)),C(0.31),C(-0.28))

ENC page_17e984a879204707 turn=0..1000
ORX 0d1989d4ead4458d/19e663ebd0ce452a -> wild | O:Admit the truth | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.19)),C(0.35),C(0.01))
ORX 0d1989d4ead4458d/cb9d3ac90f644dc0 -> wild | O:Admit the truth | E:SET char_white.Honest_Tricky = ARITHMETIC NEGATION(P(char_white.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.28)),C(0.49),C(0.06))
ORX 561af28b42e84f99/8a944c65a8b8411d -> wild | O:Blame Pink | E:SET char_white.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_white.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.13)),C(0.4),C(-0.24))
ORX 561af28b42e84f99/a7e1bff2daca4004 -> wild | O:Blame Pink | E:SET char_pink.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_pink.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.11)),C(0.26),C(-0.09))
ORX 9914487d85674054/17cca81cc53542ff -> wild | O:Deny it | E:SET char_white.Calm_Explosive = ARITHMETIC NEGATION(P(char_white.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.06)),C(0.37),C(-0.02))
ORX 9914487d85674054/8d48ba2cae01441a -> wild | O:Deny it | E:SET char_orange.Calm_Explosive = ARITHMETIC NEGATION(P(char_orange.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.24)),C(0.42),C(-0.29))

ENC page_ed04ef26cab4412d turn=0..1000
ORX 23313fc658e44d94/6988ffc5040d4b47 -> wild | O:Lower the gun | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.24)),C(0.29),C(0))
ORX 23313fc658e44d94/af055cf0ca4c4aad -> wild | O:Lower the gun | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.19)),C(0.39),C(-0.06))
ORX 6a477c554c994a6d/018bbd437ed94218 -> wild | O:Shoot Joe | E:SET char_white.Honest_Tricky = ARITHMETIC NEGATION(P(char_white.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.28)),C(0.31),C(-0.19))
ORX 6a477c554c994a6d/39a37f29197c41fb -> page_899fc37da78b456a | O:Shoot Joe | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.21)),C(0.55),C(-0.06))
ORX 9fc4082226454238/2ca53f16c0f7432a -> wild | O:Plead for peace | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.13)),C(0.28),C(-0.02))
ORX 9fc4082226454238/6fadf762afd541f0 -> wild | O:Plead for peace | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.1)),C(0.51),C(-0.16))

ENC page_19d8c20dc5df4733 turn=0..1000
ORX 40a7dbcc1e044351/404164fc613246d5 -> wild | O:Freeze | E:SET char_white.Calm_Explosive = ARITHMETIC NEGATION(P(char_white.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.2)),C(0.58),C(-0.04))
ORX 40a7dbcc1e044351/408ac493bd3b4b08 -> wild | O:Freeze | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(-0.04)),C(0.58),C(0.02))
ORX cde621cfe5ec4d1b/0b990b6d43584d2d -> wild | O:Make a run for it | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.21)),C(0.36),C(-0.25))
ORX cde621cfe5ec4d1b/3b826ae4a9994e8b -> wild | O:Make a run for it | E:SET char_white.Calm_Explosive = ARITHMETIC NEGATION(P(char_white.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.11)),C(0.5),C(-0.04))
ORX dceb08a98cad464a/41e7c1331ed14b15 -> wild | O:Shoot someone | E:SET char_orange.Calm_Explosive = ARITHMETIC NEGATION(P(char_orange.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.21)),C(0.51),C(-0.11))
ORX dceb08a98cad464a/be368cb6eda5465d -> wild | O:Shoot someone | E:SET char_white.Calm_Explosive = ARITHMETIC NEGATION(P(char_white.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.06)),C(0.55),C(0.04))

ENC page_658efcc44b0b4709 turn=0..1000
ORX ba7f6df305174e91/0a95256d275c46c3 -> wild | O:Keep lying | E:SET char_pink.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_pink.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(-0.13)),C(0.55),C(-0.1))
ORX ba7f6df305174e91/16bc9400124540f7 -> wild | O:Keep lying | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0)),C(0.4),C(0.03))
ORX f6735c66eb4c4283/1f39648cbc994cdf -> wild | O:Say nothing | E:SET char_white.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_white.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.09)),C(0.51),C(-0.29))
ORX f6735c66eb4c4283/8f5235c051ff4f0c -> wild | O:Say nothing | E:SET char_orange.Calm_Explosive = ARITHMETIC NEGATION(P(char_orange.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.22)),C(0.56),C(-0.13))
ORX fa8a1ab6c7c540eb/27a65e8226e74eaf -> wild | O:Beg for forgiveness | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.28)),C(0.5),C(-0.3))
ORX fa8a1ab6c7c540eb/3ef0af77442344cc -> wild | O:Beg for forgiveness | E:SET char_orange.Honest_Tricky = ARITHMETIC NEGATION(P(char_orange.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(-0.24)),C(0.4),C(0.06))

ENC page_899fc37da78b456a turn=0..1000
ORX 5223a695c1114ac5/4c21123fae6241b3 -> wild | O:Return fire | E:SET char_orange.Honest_Tricky = ARITHMETIC NEGATION(P(char_orange.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.02)),C(0.43),C(0.1))
ORX 5223a695c1114ac5/d96f958e2f2a407e -> wild | O:Return fire | E:SET char_pink.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_pink.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.3)),C(0.46),C(0.07))
ORX 602f6665d94f44fa/365e4fb7bc2c4e37 -> wild | O:Try to shield Orange | E:SET char_white.Calm_Explosive = ARITHMETIC NEGATION(P(char_white.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.08)),C(0.35),C(-0.18))
ORX 602f6665d94f44fa/5ccce7b0e7a64577 -> wild | O:Try to shield Orange | E:SET char_orange.Calm_Explosive = ARITHMETIC NEGATION(P(char_orange.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(-0.14)),C(0.47),C(0.07))
ORX cea7e0bd60694358/35c59cd371e64c40 -> wild | O:Hide | E:SET char_pink.Calm_Explosive = ARITHMETIC NEGATION(P(char_pink.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Calm_Explosive),C(0.17)),C(0.43),C(-0.26))
ORX cea7e0bd60694358/bc49233d091e41d5 -> wild | O:Hide | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.1)),C(0.39),C(-0.1))

ENC page_00ade86b2afa42c7 turn=0..1000
ORX 48dd0efb155e48b3/5a30f6fe2b5a4f78 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.07)),C(0.34),C(-0.16))
ORX 48dd0efb155e48b3/9fb21463d4a741bd -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.21)),C(0.51),C(-0.01))

ENC page_30e066cd3baa4103 turn=0..1000
ORX ea061dc7b23a47a2/c9fe491c18c348f2 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.18)),C(0.58),C(-0.18))
ORX ea061dc7b23a47a2/eede66587419460f -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.18)),C(0.46),C(-0.22))

ENC page_e0604ba3d7d14a03 turn=0..1000
ORX 1ecde6e45bd74f17/0cbd92d213364073 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0)),C(0.42),C(-0.09))
ORX 1ecde6e45bd74f17/513a99a09596448f -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.24)),C(0.41),C(0.04))

ENC page_53265f035d544e80 turn=0..1000
ORX 7f17da9e74214482/504d792774bc4c29 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(0.29)),C(0.41),C(-0.07))
ORX 7f17da9e74214482/cce6865fd4054fcf -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.29)),C(0.49),C(0.19))

ENC page_e0e12941e23447ad turn=0..1000
ORX 13cdaa2031b2483c/af516c80c0164c70 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(0.21)),C(0.54),C(-0.03))
ORX 13cdaa2031b2483c/e1aaed9df38e4446 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Honest_Tricky),C(0.06)),C(0.42),C(-0.17))

ENC page_a8a29cc68c044321 turn=0..1000
ORX b1dd670d0b7e4272/ba4d396985374066 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.23)),C(0.51),C(-0.27))
ORX b1dd670d0b7e4272/d8d366e710144051 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(-0.24)),C(0.46),C(0.07))

ENC page_97d0ab15eec747cd turn=0..1000
ORX 74d315f7dbfd4865/563e72ea3852419b -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.15)),C(0.58),C(-0.16))
ORX 74d315f7dbfd4865/d76cb7dcfb9549cd -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.24)),C(0.6),C(-0.09))

ENC page_5db0915c90ef4ba0 turn=0..1000
ORX 36efd1e8ba944af3/2b3574d9643745c5 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(0.15)),C(0.36),C(-0.22))
ORX 36efd1e8ba944af3/638e6d7f99654335 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(-0.26)),C(0.34),C(-0.15))

ENC page_695eeed18bda4a37 turn=0..1000
ORX adfb7fb6a4e4477f/6a9bec9f6d0d4663 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.06)),C(0.37),C(-0.05))
ORX adfb7fb6a4e4477f/98724b1c65a24527 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Loyal_Treacherous),C(0.02)),C(0.59),C(-0.2))

ENC page_0b7e455222e34ffc turn=0..1000
ORX bf2baf0c6fdb4dce/4e041d49f0e84335 -> wild | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Loyal_Treacherous),C(-0.06)),C(0.5),C(-0.09))
ORX bf2baf0c6fdb4dce/807ddc6559d9454b -> page_97d0ab15eec747cd | O:Say nothing. | E:SET none = C(0) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_orange.Calm_Explosive),C(0.1)),C(0.35),C(-0.25))

ENC page_21e67502c41f4646 turn=0..1000
ORX b2783271eb9b40c7/30d8fef22c9c4d2d -> wild | O:Try to deescalate. | E:SET char_orange.Honest_Tricky = ARITHMETIC NEGATION(P(char_orange.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.11)),C(0.4),C(0.04))

ENC page_d7da15156f3c46f1 turn=0..1000
ORX 24e03eb8072549bc/6f2723765f9648d9 -> wild | O:End Scene | E:SET char_pink.Calm_Explosive = ARITHMETIC NEGATION(P(char_pink.Calm_Explosive)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Loyal_Treacherous),C(0.25)),C(0.38),C(-0.02))

ENC page_be8c23da4c0e417e turn=0..1000
ORX 62c452f6c7b949a7/9a122056f5134309 -> wild | O:End Scene | E:SET char_pink.Honest_Tricky = ARITHMETIC NEGATION(P(char_pink.Honest_Tricky)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Honest_Tricky),C(0.05)),C(0.58),C(0.03))

ENC page_39ace06ee3034adf turn=0..1000
ORX 9f877655e09d400f/8f8160ad3e8c4df4 -> wild | O:Fade to black. | E:SET char_white.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_white.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_pink.Calm_Explosive),C(-0.08)),C(0.39),C(-0.14))

ENC page_c4c48f7afb1a4502 turn=0..1000
ORX 25bcb81ef5b44dcc/f3bdfabdcd49444d -> wild | O:End Scene | E:SET char_orange.Loyal_Treacherous = ARITHMETIC NEGATION(P(char_orange.Loyal_Treacherous)) | D:IF THEN(ARITHMETIC COMPARATOR(P(char_white.Honest_Tricky),C(-0.24)),C(0.39),C(-0.26))
