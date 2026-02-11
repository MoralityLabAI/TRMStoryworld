# SWMD-0-MIN
id: 88051457-3533-4092-A08C-7ED1ADFE1E75
title: First and Last Men: Escape from the Solar Cul-de-sac

ENC page_0000 turn=0..0
ORX opt_page_0000_0/opt_page_0000_0_r1 -> page_0001 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0000_1/opt_page_0000_1_r1 -> page_0001 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0001 turn=0..0
ORX opt_page_0001_0/opt_page_0001_0_r1 -> page_0002 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0001_1/opt_page_0001_1_r1 -> page_0002 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0002 turn=0..0
ORX opt_page_0002_0/opt_page_0002_0_r1 -> page_0003 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0002_1/opt_page_0002_1_r1 -> page_0003 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0003 turn=0..0
ORX opt_page_0003_0/opt_page_0003_0_r1 -> page_0004 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0003_1/opt_page_0003_1_r1 -> page_0004 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0004 turn=0..0
ORX opt_page_0004_0/opt_page_0004_0_r1 -> page_0005 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0004_1/opt_page_0004_1_r1 -> page_0005 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0005 turn=0..0
ORX opt_page_0005_to_next/opt_page_0005_to_next_r1 -> page_0006 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0006 turn=1..1
ORX opt_page_0006_0/opt_page_0006_0_r1 -> page_0007 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0006_1/opt_page_0006_1_r1 -> page_0007 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0007 turn=1..1
ORX opt_page_0007_0/opt_page_0007_0_r1 -> page_0008 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0007_1/opt_page_0007_1_r1 -> page_0008 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0008 turn=1..1
ORX opt_page_0008_0/opt_page_0008_0_r1 -> page_0009 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0008_1/opt_page_0008_1_r1 -> page_0009 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0009 turn=1..1
ORX opt_page_0009_0/opt_page_0009_0_r1 -> page_0010 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0009_1/opt_page_0009_1_r1 -> page_0010 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0010 turn=1..1
ORX opt_page_0010_0/opt_page_0010_0_r1 -> page_0011 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0010_1/opt_page_0010_1_r1 -> page_0011 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0011 turn=1..1
ORX opt_page_0011_to_next/opt_page_0011_to_next_r1 -> page_0012 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0012 turn=2..2
ORX opt_page_0012_0/opt_page_0012_0_r1 -> page_0013 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0012_1/opt_page_0012_1_r1 -> page_0013 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0013 turn=2..2
ORX opt_page_0013_0/opt_page_0013_0_r1 -> page_0014 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0013_1/opt_page_0013_1_r1 -> page_0014 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0014 turn=2..2
ORX opt_page_0014_0/opt_page_0014_0_r1 -> page_0015 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0014_1/opt_page_0014_1_r1 -> page_0015 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0015 turn=2..2
ORX opt_page_0015_0/opt_page_0015_0_r1 -> page_0016 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0015_1/opt_page_0015_1_r1 -> page_0016 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0016 turn=2..2
ORX opt_page_0016_0/opt_page_0016_0_r1 -> page_0017 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0016_1/opt_page_0016_1_r1 -> page_0017 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0017 turn=2..2
ORX opt_page_0017_to_next/opt_page_0017_to_next_r1 -> page_0018 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0018 turn=3..3
ORX opt_page_0018_0/opt_page_0018_0_r1 -> page_0019 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0018_1/opt_page_0018_1_r1 -> page_0019 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0019 turn=3..3
ORX opt_page_0019_0/opt_page_0019_0_r1 -> page_0020 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0019_1/opt_page_0019_1_r1 -> page_0020 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0020 turn=3..3
ORX opt_page_0020_0/opt_page_0020_0_r1 -> page_0021 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0020_1/opt_page_0020_1_r1 -> page_0021 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0021 turn=3..3
ORX opt_page_0021_0/opt_page_0021_0_r1 -> page_0022 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0021_1/opt_page_0021_1_r1 -> page_0022 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0022 turn=3..3
ORX opt_page_0022_0/opt_page_0022_0_r1 -> page_0023 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0022_1/opt_page_0022_1_r1 -> page_0023 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0023 turn=3..3
ORX opt_page_0023_to_next/opt_page_0023_to_next_r1 -> page_0024 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0024 turn=4..4
ORX opt_page_0024_0/opt_page_0024_0_r1 -> page_0025 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0024_1/opt_page_0024_1_r1 -> page_0025 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0025 turn=4..4
ORX opt_page_0025_0/opt_page_0025_0_r1 -> page_0026 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0025_1/opt_page_0025_1_r1 -> page_0026 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0026 turn=4..4
ORX opt_page_0026_0/opt_page_0026_0_r1 -> page_0027 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0026_1/opt_page_0026_1_r1 -> page_0027 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0027 turn=4..4
ORX opt_page_0027_0/opt_page_0027_0_r1 -> page_0028 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0027_1/opt_page_0027_1_r1 -> page_0028 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0028 turn=4..4
ORX opt_page_0028_0/opt_page_0028_0_r1 -> page_0029 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0028_1/opt_page_0028_1_r1 -> page_0029 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0029 turn=4..4
ORX opt_page_0029_to_next/opt_page_0029_to_next_r1 -> page_0030 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0030 turn=5..5
ORX opt_page_0030_0/opt_page_0030_0_r1 -> page_0031 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0030_1/opt_page_0030_1_r1 -> page_0031 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0031 turn=5..5
ORX opt_page_0031_0/opt_page_0031_0_r1 -> page_0032 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0031_1/opt_page_0031_1_r1 -> page_0032 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0032 turn=5..5
ORX opt_page_0032_0/opt_page_0032_0_r1 -> page_0033 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0032_1/opt_page_0032_1_r1 -> page_0033 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0033 turn=5..5
ORX opt_page_0033_0/opt_page_0033_0_r1 -> page_0034 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0033_1/opt_page_0033_1_r1 -> page_0034 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0034 turn=5..5
ORX opt_page_0034_0/opt_page_0034_0_r1 -> page_0035 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0034_1/opt_page_0034_1_r1 -> page_0035 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0035 turn=5..5
ORX opt_page_0035_to_next/opt_page_0035_to_next_r1 -> page_0036 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0036 turn=6..6
ORX opt_page_0036_0/opt_page_0036_0_r1 -> page_0037 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0036_1/opt_page_0036_1_r1 -> page_0037 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0037 turn=6..6
ORX opt_page_0037_0/opt_page_0037_0_r1 -> page_0038 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0037_1/opt_page_0037_1_r1 -> page_0038 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0038 turn=6..6
ORX opt_page_0038_0/opt_page_0038_0_r1 -> page_0039 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0038_1/opt_page_0038_1_r1 -> page_0039 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0039 turn=6..6
ORX opt_page_0039_0/opt_page_0039_0_r1 -> page_0040 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0039_1/opt_page_0039_1_r1 -> page_0040 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0040 turn=6..6
ORX opt_page_0040_0/opt_page_0040_0_r1 -> page_0041 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0040_1/opt_page_0040_1_r1 -> page_0041 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0041 turn=6..6
ORX opt_page_0041_to_next/opt_page_0041_to_next_r1 -> page_0042 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0042 turn=7..7
ORX opt_page_0042_0/opt_page_0042_0_r1 -> page_0043 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0042_1/opt_page_0042_1_r1 -> page_0043 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0043 turn=7..7
ORX opt_page_0043_0/opt_page_0043_0_r1 -> page_0044 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0043_1/opt_page_0043_1_r1 -> page_0044 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0044 turn=7..7
ORX opt_page_0044_0/opt_page_0044_0_r1 -> page_0045 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0044_1/opt_page_0044_1_r1 -> page_0045 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0045 turn=7..7
ORX opt_page_0045_0/opt_page_0045_0_r1 -> page_0046 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0045_1/opt_page_0045_1_r1 -> page_0046 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0046 turn=7..7
ORX opt_page_0046_0/opt_page_0046_0_r1 -> page_0047 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0046_1/opt_page_0046_1_r1 -> page_0047 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0047 turn=7..7
ORX opt_page_0047_to_next/opt_page_0047_to_next_r1 -> page_0048 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0048 turn=8..8
ORX opt_page_0048_0/opt_page_0048_0_r1 -> page_0049 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0048_1/opt_page_0048_1_r1 -> page_0049 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0049 turn=8..8
ORX opt_page_0049_0/opt_page_0049_0_r1 -> page_0050 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0049_1/opt_page_0049_1_r1 -> page_0050 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0050 turn=8..8
ORX opt_page_0050_0/opt_page_0050_0_r1 -> page_0051 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0050_1/opt_page_0050_1_r1 -> page_0051 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0051 turn=8..8
ORX opt_page_0051_0/opt_page_0051_0_r1 -> page_0052 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0051_1/opt_page_0051_1_r1 -> page_0052 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0052 turn=8..8
ORX opt_page_0052_0/opt_page_0052_0_r1 -> page_0053 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0052_1/opt_page_0052_1_r1 -> page_0053 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0053 turn=8..8
ORX opt_page_0053_to_next/opt_page_0053_to_next_r1 -> page_0054 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0054 turn=9..9
ORX opt_page_0054_0/opt_page_0054_0_r1 -> page_0055 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0054_1/opt_page_0054_1_r1 -> page_0055 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0055 turn=9..9
ORX opt_page_0055_0/opt_page_0055_0_r1 -> page_0056 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0055_1/opt_page_0055_1_r1 -> page_0056 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0056 turn=9..9
ORX opt_page_0056_0/opt_page_0056_0_r1 -> page_0057 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0056_1/opt_page_0056_1_r1 -> page_0057 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0057 turn=9..9
ORX opt_page_0057_0/opt_page_0057_0_r1 -> page_0058 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0057_1/opt_page_0057_1_r1 -> page_0058 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0058 turn=9..9
ORX opt_page_0058_0/opt_page_0058_0_r1 -> page_0059 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0058_1/opt_page_0058_1_r1 -> page_0059 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0059 turn=9..9
ORX opt_page_0059_to_next/opt_page_0059_to_next_r1 -> page_0060 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0060 turn=10..10
ORX opt_page_0060_0/opt_page_0060_0_r1 -> page_0061 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0060_1/opt_page_0060_1_r1 -> page_0061 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0061 turn=10..10
ORX opt_page_0061_0/opt_page_0061_0_r1 -> page_0062 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0061_1/opt_page_0061_1_r1 -> page_0062 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0062 turn=10..10
ORX opt_page_0062_0/opt_page_0062_0_r1 -> page_0063 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0062_1/opt_page_0062_1_r1 -> page_0063 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0063 turn=10..10
ORX opt_page_0063_0/opt_page_0063_0_r1 -> page_0064 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0063_1/opt_page_0063_1_r1 -> page_0064 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0064 turn=10..10
ORX opt_page_0064_0/opt_page_0064_0_r1 -> page_0065 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0064_1/opt_page_0064_1_r1 -> page_0065 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0065 turn=10..10
ORX opt_page_0065_to_next/opt_page_0065_to_next_r1 -> page_0066 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0066 turn=11..11
ORX opt_page_0066_0/opt_page_0066_0_r1 -> page_0067 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0066_1/opt_page_0066_1_r1 -> page_0067 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0067 turn=11..11
ORX opt_page_0067_0/opt_page_0067_0_r1 -> page_0068 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0067_1/opt_page_0067_1_r1 -> page_0068 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0068 turn=11..11
ORX opt_page_0068_0/opt_page_0068_0_r1 -> page_0069 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0068_1/opt_page_0068_1_r1 -> page_0069 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0069 turn=11..11
ORX opt_page_0069_0/opt_page_0069_0_r1 -> page_0070 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0069_1/opt_page_0069_1_r1 -> page_0070 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0070 turn=11..11
ORX opt_page_0070_0/opt_page_0070_0_r1 -> page_0071 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0070_1/opt_page_0070_1_r1 -> page_0071 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0071 turn=11..11
ORX opt_page_0071_to_next/opt_page_0071_to_next_r1 -> page_0072 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0072 turn=12..12
ORX opt_page_0072_0/opt_page_0072_0_r1 -> page_0073 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0072_1/opt_page_0072_1_r1 -> page_0073 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0073 turn=12..12
ORX opt_page_0073_0/opt_page_0073_0_r1 -> page_0074 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0073_1/opt_page_0073_1_r1 -> page_0074 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0074 turn=12..12
ORX opt_page_0074_0/opt_page_0074_0_r1 -> page_0075 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0074_1/opt_page_0074_1_r1 -> page_0075 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0075 turn=12..12
ORX opt_page_0075_0/opt_page_0075_0_r1 -> page_0076 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0075_1/opt_page_0075_1_r1 -> page_0076 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0076 turn=12..12
ORX opt_page_0076_0/opt_page_0076_0_r1 -> page_0077 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0076_1/opt_page_0076_1_r1 -> page_0077 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0077 turn=12..12
ORX opt_page_0077_to_next/opt_page_0077_to_next_r1 -> page_0078 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0078 turn=13..13
ORX opt_page_0078_0/opt_page_0078_0_r1 -> page_0079 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0078_1/opt_page_0078_1_r1 -> page_0079 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0079 turn=13..13
ORX opt_page_0079_0/opt_page_0079_0_r1 -> page_0080 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0079_1/opt_page_0079_1_r1 -> page_0080 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0080 turn=13..13
ORX opt_page_0080_0/opt_page_0080_0_r1 -> page_0081 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0080_1/opt_page_0080_1_r1 -> page_0081 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0081 turn=13..13
ORX opt_page_0081_0/opt_page_0081_0_r1 -> page_0082 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0081_1/opt_page_0081_1_r1 -> page_0082 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0082 turn=13..13
ORX opt_page_0082_0/opt_page_0082_0_r1 -> page_0083 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0082_1/opt_page_0082_1_r1 -> page_0083 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0083 turn=13..13
ORX opt_page_0083_to_next/opt_page_0083_to_next_r1 -> page_0084 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0084 turn=14..14
ORX opt_page_0084_0/opt_page_0084_0_r1 -> page_0085 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0084_1/opt_page_0084_1_r1 -> page_0085 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0085 turn=14..14
ORX opt_page_0085_0/opt_page_0085_0_r1 -> page_0086 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0085_1/opt_page_0085_1_r1 -> page_0086 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0086 turn=14..14
ORX opt_page_0086_0/opt_page_0086_0_r1 -> page_0087 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0086_1/opt_page_0086_1_r1 -> page_0087 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0087 turn=14..14
ORX opt_page_0087_0/opt_page_0087_0_r1 -> page_0088 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0087_1/opt_page_0087_1_r1 -> page_0088 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0088 turn=14..14
ORX opt_page_0088_0/opt_page_0088_0_r1 -> page_0089 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0088_1/opt_page_0088_1_r1 -> page_0089 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0089 turn=14..14
ORX opt_page_0089_to_next/opt_page_0089_to_next_r1 -> page_0090 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0090 turn=15..15
ORX opt_page_0090_0/opt_page_0090_0_r1 -> page_0091 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0090_1/opt_page_0090_1_r1 -> page_0091 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0091 turn=15..15
ORX opt_page_0091_0/opt_page_0091_0_r1 -> page_0092 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0091_1/opt_page_0091_1_r1 -> page_0092 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0092 turn=15..15
ORX opt_page_0092_0/opt_page_0092_0_r1 -> page_0093 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0092_1/opt_page_0092_1_r1 -> page_0093 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0093 turn=15..15
ORX opt_page_0093_0/opt_page_0093_0_r1 -> page_0094 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0093_1/opt_page_0093_1_r1 -> page_0094 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0094 turn=15..15
ORX opt_page_0094_0/opt_page_0094_0_r1 -> page_0095 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0094_1/opt_page_0094_1_r1 -> page_0095 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0095 turn=15..15
ORX opt_page_0095_to_next/opt_page_0095_to_next_r1 -> page_0096 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0096 turn=16..16
ORX opt_page_0096_0/opt_page_0096_0_r1 -> page_0097 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)) | D:C(1)
ORX opt_page_0096_1/opt_page_0096_1_r1 -> page_0097 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0097 turn=16..16
ORX opt_page_0097_0/opt_page_0097_0_r1 -> page_0098 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)) | D:C(1)
ORX opt_page_0097_1/opt_page_0097_1_r1 -> page_0098 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0098 turn=16..16
ORX opt_page_0098_0/opt_page_0098_0_r1 -> page_0099 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0098_1/opt_page_0098_1_r1 -> page_0099 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0099 turn=16..16
ORX opt_page_0099_0/opt_page_0099_0_r1 -> page_0100 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0099_1/opt_page_0099_1_r1 -> page_0100 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0100 turn=16..16
ORX opt_page_0100_0/opt_page_0100_0_r1 -> page_0101 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0100_1/opt_page_0100_1_r1 -> page_0101 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0101 turn=16..16
ORX opt_page_0101_to_next/opt_page_0101_to_next_r1 -> page_0102 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0102 turn=17..17
ORX opt_page_0102_0/opt_page_0102_0_r1 -> page_0103 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)) | D:C(1)
ORX opt_page_0102_1/opt_page_0102_1_r1 -> page_0103 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0103 turn=17..17
ORX opt_page_0103_0/opt_page_0103_0_r1 -> page_0104 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)) | D:C(1)
ORX opt_page_0103_1/opt_page_0103_1_r1 -> page_0104 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0104 turn=17..17
ORX opt_page_0104_0/opt_page_0104_0_r1 -> page_0105 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0104_1/opt_page_0104_1_r1 -> page_0105 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0105 turn=17..17
ORX opt_page_0105_0/opt_page_0105_0_r1 -> page_0106 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0105_1/opt_page_0105_1_r1 -> page_0106 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0106 turn=17..17
ORX opt_page_0106_0/opt_page_0106_0_r1 -> page_0107 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0106_1/opt_page_0106_1_r1 -> page_0107 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0107 turn=17..17
ORX opt_page_0107_to_next/opt_page_0107_to_next_r1 -> page_0108 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0108 turn=18..18
ORX opt_page_0108_0/opt_page_0108_0_r1 -> page_0109 | O:Advance the doctrine | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)) | D:C(1)
ORX opt_page_0108_1/opt_page_0108_1_r1 -> page_0109 | O:Advance, but hide the seams | E:SET char_civ.Hedonism_Austerity = NUDGE(P(char_civ.Hedonism_Austerity),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0109 turn=18..18
ORX opt_page_0109_0/opt_page_0109_0_r1 -> page_0110 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)) | D:C(1)
ORX opt_page_0109_1/opt_page_0109_1_r1 -> page_0110 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0110 turn=18..18
ORX opt_page_0110_0/opt_page_0110_0_r1 -> page_0111 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)) | D:C(1)
ORX opt_page_0110_1/opt_page_0110_1_r1 -> page_0111 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0111 turn=18..18
ORX opt_page_0111_0/opt_page_0111_0_r1 -> page_0112 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)) | D:C(1)
ORX opt_page_0111_1/opt_page_0111_1_r1 -> page_0112 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(-0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0112 turn=18..18
ORX opt_page_0112_0/opt_page_0112_0_r1 -> page_0113 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0112_1/opt_page_0112_1_r1 -> page_0113 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(-0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0113 turn=18..18
ORX opt_page_0113_to_next/opt_page_0113_to_next_r1 -> page_0114 | O:Let the next Men inherit | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:C(1)

ENC page_0114 turn=19..19
ORX opt_page_0114_0/opt_page_0114_0_r1 -> page_0115 | O:Advance the doctrine | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)) | D:C(1)
ORX opt_page_0114_1/opt_page_0114_1_r1 -> page_0115 | O:Advance, but hide the seams | E:SET char_civ.Risk_Stasis = NUDGE(P(char_civ.Risk_Stasis),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0115 turn=19..19
ORX opt_page_0115_0/opt_page_0115_0_r1 -> page_0116 | O:Advance the doctrine | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)) | D:C(1)
ORX opt_page_0115_1/opt_page_0115_1_r1 -> page_0116 | O:Advance, but hide the seams | E:SET char_civ.Cohesion_Fragmentation = NUDGE(P(char_civ.Cohesion_Fragmentation),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0116 turn=19..19
ORX opt_page_0116_0/opt_page_0116_0_r1 -> page_0117 | O:Advance the doctrine | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)) | D:C(1)
ORX opt_page_0116_1/opt_page_0116_1_r1 -> page_0117 | O:Advance, but hide the seams | E:SET char_civ.Transgression_Order = NUDGE(P(char_civ.Transgression_Order),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0117 turn=19..19
ORX opt_page_0117_0/opt_page_0117_0_r1 -> page_0118 | O:Advance the doctrine | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)) | D:C(1)
ORX opt_page_0117_1/opt_page_0117_1_r1 -> page_0118 | O:Advance, but hide the seams | E:SET char_civ.Cosmic_Ambition_Humility = NUDGE(P(char_civ.Cosmic_Ambition_Humility),C(0.015)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)) | D:C(1)

ENC page_0118 turn=19..19
ORX opt_page_0118_0/opt_page_0118_0_r1 -> page_0119 | O:Advance the doctrine | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)
ORX opt_page_0118_1/opt_page_0118_1_r1 -> page_0119 | O:Advance, but hide the seams | E:SET char_civ.Embodiment_Virtuality = NUDGE(P(char_civ.Embodiment_Virtuality),C(0.015)); SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.02)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)); SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.005)); SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0119 turn=19..19
ORX opt_page_0119_to_endgame/opt_page_0119_to_endgame_r1 -> page_0120 | O:Open the long horizon | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.02)) | D:C(1)

ENC page_0120 turn=20..29
ORX opt_page_0120_0/opt_page_0120_0_r_mosaic -> page_end_0126 | O:Offer wonder as discipline | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(P(char_civ.Embodiment_Virtuality),P(char_civ.Hedonism_Austerity)),C(0.35)),C(0.05),C(0.9))
ORX opt_page_0120_0/opt_page_0120_0_r_sim -> page_end_0121 | O:Offer wonder as discipline | E:SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(-0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(P(char_civ.Embodiment_Virtuality),P(char_civ.Hedonism_Austerity)),C(0.35)),C(0.95),C(0.05))
ORX opt_page_0120_1/opt_page_0120_1_r_decay -> page_end_0122 | O:Offer endurance as worship | E:SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(ARITHMETIC NEGATION(P(char_civ.Hedonism_Austerity)),P(char_civ.Cohesion_Fragmentation),P(char_civ.Risk_Stasis)),C(0.35)),C(0.95),C(0.05))
ORX opt_page_0120_1/opt_page_0120_1_r_mosaic -> page_end_0126 | O:Offer endurance as worship | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(ARITHMETIC NEGATION(P(char_civ.Hedonism_Austerity)),P(char_civ.Cohesion_Fragmentation),P(char_civ.Risk_Stasis)),C(0.35)),C(0.05),C(0.9))
ORX opt_page_0120_2/opt_page_0120_2_r_hack -> page_end_0124 | O:Offer transgression as method | E:SET char_counter_archivist.Grudge = NUDGE(P(char_counter_archivist.Grudge),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(P(char_civ.Transgression_Order),P(char_civ.Cosmic_Ambition_Humility),P(char_civ.Risk_Stasis)),C(0.35)),C(0.95),C(0.05))
ORX opt_page_0120_2/opt_page_0120_2_r_hole -> page_end_0123 | O:Offer transgression as method | E:SET char_counter_archivist.Influence = NUDGE(P(char_counter_archivist.Influence),C(-0.005)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(P(char_civ.Transgression_Order),P(char_civ.Cosmic_Ambition_Humility),P(char_civ.Risk_Stasis)),C(0.35)),C(0.01),IF THEN(ARITHMETIC COMPARATOR(P(char_civ.Cosmic_Ambition_Humility),C(0.2)),C(0.85),C(0.05)))
ORX opt_page_0120_2/opt_page_0120_2_r_mosaic -> page_end_0126 | O:Offer transgression as method | E:SET char_counter_archivist.Countercraft = NUDGE(P(char_counter_archivist.Countercraft),C(0.01)) | D:IF THEN(ARITHMETIC COMPARATOR(ARITHMETIC MEAN(P(char_civ.Transgression_Order),P(char_civ.Cosmic_Ambition_Humility),P(char_civ.Risk_Stasis)),C(0.35)),C(0.01),IF THEN(ARITHMETIC COMPARATOR(P(char_civ.Cosmic_Ambition_Humility),C(0.2)),C(0.05),C(0.8)))

ENC page_end_0121 turn=20..29

ENC page_end_0122 turn=20..29

ENC page_end_0123 turn=20..29

ENC page_end_0124 turn=20..29

ENC page_end_0125 turn=20..29

ENC page_end_0126 turn=20..29
