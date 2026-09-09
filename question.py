# question.py

DISEASES = [
    # --- RICE (Oryza sativa) ---
    {
        "crop": "Rice",
        "disease_name": "Blast",
        "causative_organism": "Magnaporthe oryzae (= Pyricularia oryzae, syn. P. grisea)",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Sordariomycetes",
            "Order": "Magnaporthales",
            "Family": "Magnaportheae",
            "Genus": "Magnaporthe (teleomorph); Pyricularia (anamorph)",
            "Species": "Magnaporthe oryzae"
        },
        "symptoms": [
            "Leaf blast: spindle/eye-shaped spots with grey-white necrotic centre and dark brown margin.",
            "Node blast: nodes turn black/brown and break easily.",
            "Neck blast: rotten neck phase, neck node turns blackish-brown and breaks producing chalky/unfilled grains."
        ],
        "disease_cycle": "Fungus overwinters as mycelium/conidia in seed, residue, and collateral weed hosts. Conidia are wind-disseminated, germinating and forming melanized appressoria to force penetration pegs through the cuticle.",
        "epidemiology": "High RH (>90%), 8-10 hrs leaf wetness/dew, optimum temp 25-28°C, cloudy weather with rain, excess N application.",
        "management": {
            "cultural": "Hot water seed treatment (52-54°C for 10 min), split N application with K & Si, destroy stubble.",
            "host_resistance": "Resistant varieties like Tetep, IR64, CO 39, Improved Samba Mahsuri.",
            "chemical": "Seed treatment with Tricyclazole/Carbendazim (2 g/kg). Spray Tricyclazole 75WP (0.6 g/L) or Isoprothiolane at boot-leaf and 50% flowering.",
            "biological": "Pseudomonas fluorescens and Trichoderma viride/harzianum."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "Brown Spot",
        "causative_organism": "Bipolaris oryzae (= Helminthosporium oryzae); teleomorph Cochliobolus miyabeanus",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Pleosporales",
            "Family": "Pleosporaceae",
            "Genus": "Bipolaris (anamorph); Cochliobolus (teleomorph)",
            "Species": "Bipolaris oryzae"
        },
        "symptoms": [
            "Small circular to oval brown spots with lighter grey-white centre resembling sesame seeds.",
            "Coalescence causing blighting of leaves.",
            "Spots on glumes and grains ('brown spot of grain') lowering quality."
        ],
        "disease_cycle": "Survives as mycelium in infected seed and straw/stubble. Conidia produced on old lesions are wind- and rain-dispersed.",
        "epidemiology": "Nutrient-deficient soils (K, Zn, Si-poor), drought-stressed or waterlogged soils, RH high with temp 25-30°C.",
        "management": {
            "cultural": "Balanced fertilization (potash & silicate), healthy seed, proper water management.",
            "host_resistance": "Moderately tolerant varieties combined with soil fertility management.",
            "chemical": "Seed treatment with Captan or Thiram (2-3 g/kg). Foliar spray of Mancozeb (0.25%) or Propiconazole.",
            "biological": "Trichoderma viride / Pseudomonas fluorescens seed treatment."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "Bacterial Blight (BLB)",
        "causative_organism": "Xanthomonas oryzae pv. oryzae",
        "taxonomic_classification": {
            "Kingdom": "Bacteria",
            "Phylum": "Pseudomonadota (Proteobacteria)",
            "Class": "Gammaproteobacteria",
            "Order": "Xanthomonadales",
            "Family": "Xanthomonadaceae",
            "Genus": "Xanthomonas",
            "Species": "Xanthomonas oryzae pv. oryzae"
        },
        "symptoms": [
            "Leaf blight phase: water-soaked lesions at margins enlarging with a wavy yellow-to-white margin.",
            "Kresek phase: seedling wilting and death via roots/wounds.",
            "Milky-white bacterial ooze on lesions in early morning drying into yellowish beads."
        ],
        "disease_cycle": "Survives in seed, stubble, and weed hosts. Bacteria multiply in guttation fluid at hydathodes and spread via wind-driven rain and irrigation water.",
        "epidemiology": "Standing water/flood irrigation, high humidity, warm temps (25-34°C), storms/winds causing leaf wounds, excess nitrogen.",
        "management": {
            "cultural": "Avoid clipping seedling tips, balanced N, shallow intermittent irrigation, field sanitation.",
            "host_resistance": "Varieties with Xa genes (Xa4, xa5, Xa7, Xa21).",
            "chemical": "Seed treatment with bleaching powder (100 ppm) or Streptocycline (100 ppm). Spray Streptocycline (0.01%) + Copper oxychloride (0.3%).",
            "biological": "Seedling root dip in Pseudomonas fluorescens suspension."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "Sheath Blight",
        "causative_organism": "Rhizoctonia solani; teleomorph Thanatephorus cucumeris",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Basidiomycota",
            "Class": "Agaricomycetes",
            "Order": "Cantharellales",
            "Family": "Ceratobasidiaceae",
            "Genus": "Rhizoctonia (anamorph); Thanatephorus (teleomorph)",
            "Species": "Rhizoctonia solani"
        },
        "symptoms": [
            "Oval to irregular greyish-green water-soaked lesions on leaf sheath near water line with 'snake-skin' pattern.",
            "Spreads up to flag leaf and panicle causing incomplete grain filling."
        ],
        "disease_cycle": "Sclerotia float on irrigation water, lodge at water line on leaf sheaths, germinate, and penetrate directly. Spreads horizontally by direct leaf-to-leaf contact.",
        "epidemiology": "High nitrogen, dense planting/high tillering, temp 28-32°C, RH >96%, continuous flooding.",
        "management": {
            "cultural": "Optimum spacing, alternate wetting-and-drying, stubble removal/burning, balanced N.",
            "host_resistance": "Moderately tolerant lines (e.g., Jasmine 85, Tetep).",
            "chemical": "Validamycin A or Hexaconazole spray at early tillering and booting stage.",
            "biological": "Trichoderma harzianum soil application."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "False Smut",
        "causative_organism": "Ustilaginoidea virens; teleomorph Villosiclava virens",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Sordariomycetes",
            "Order": "Hypocreales",
            "Family": "Clavicipitaceae",
            "Genus": "Ustilaginoidea (anamorph); Villosiclava (teleomorph)",
            "Species": "Ustilaginoidea virens"
        },
        "symptoms": [
            "Individual grains in panicle transformed into velvety smut balls, changing from yellow through orange/olive-green to black."
        ],
        "disease_cycle": "Sclerotia in soil and chlamydospores on straw germinate around flowering to release airborne spores that infect open florets.",
        "epidemiology": "High nitrogen, dense planting, high humidity, moderate temp (25-30°C) during flowering window.",
        "management": {
            "cultural": "Avoid excess N, field sanitation, summer ploughing.",
            "host_resistance": "Tolerant varieties.",
            "chemical": "Spray Propiconazole or Copper oxychloride at boot-leaf stage just before panicle emergence.",
            "biological": "Trichoderma-based soil treatments."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "Khaira Disease",
        "causative_organism": "Zinc (Zn) deficiency (Physiological Disorder — Not Pathogen-Induced)",
        "taxonomic_classification": None,
        "symptoms": [
            "Chlorotic (yellowish-white) streaks/patches on lower/older leaves near midrib, developing rusty-brown bronzed blotches.",
            "Stunted growth, reduced tillering, delayed maturity."
        ],
        "disease_cycle": "Non-infectious; recurs each season on zinc-deficient soils unless corrected.",
        "epidemiology": "Calcareous/alkaline soils (pH > 7.5), sandy soils, continuous flooding, excess phosphatic fertilization.",
        "management": {
            "cultural": "Soil application of zinc sulphate (25 kg/ha) as basal treatment; avoid excess phosphatic fertilizer.",
            "host_resistance": "Not applicable.",
            "chemical": "Foliar spray of 0.5% zinc sulphate + 0.25% hydrated lime solution at first symptom.",
            "biological": "Not applicable."
        }
    },
    {
        "crop": "Rice",
        "disease_name": "Tungro",
        "causative_organism": "RTBV (Rice Tungro Bacilliform Virus) + RTSV (Rice Tungro Spherical Virus) vector: Green leafhopper (Nephotettix virescens)",
        "taxonomic_classification": {
            "Component 1": "RTBV — Family Caulimoviridae, Genus Tungrovirus",
            "Component 2": "RTSV — Family Secoviridae, Genus Waikavirus",
            "Vector": "Nephotettix virescens (Hemiptera)"
        },
        "symptoms": [
            "Yellow-orange to golden-yellow leaf discoloration starting from tip.",
            "Stunting of growth, reduced tillering, delayed flowering, panicle sterility."
        ],
        "disease_cycle": "Viruses survive in infected rice/ratoon/weeds. Green leafhoppers acquire and transmit both viruses semi-persistently.",
        "epidemiology": "Continuous/overlapping rice cropping, high leafhopper vector populations, warm weather, lush N-rich growth.",
        "management": {
            "cultural": "Synchronous planting, crop-free/fallow period, avoid ratooning.",
            "host_resistance": "Cultivation of leafhopper/virus resistant varieties.",
            "chemical": "Control leafhoppers with systemic insecticides (Imidacloprid, Thiamethoxam).",
            "biological": "Conservation of natural predators (spiders, mirid bugs)."
        }
    },

    # --- MAIZE (Zea mays) ---
    {
        "crop": "Maize",
        "disease_name": "Downy Mildew",
        "causative_organism": "Peronosclerospora sorghi / P. maydis",
        "taxonomic_classification": {
            "Kingdom": "Chromista (Straminipila)",
            "Phylum": "Oomycota",
            "Class": "Oomycetes",
            "Order": "Peronosporales",
            "Family": "Peronosporaceae",
            "Genus": "Peronosclerospora",
            "Species": "Peronosclerospora sorghi / P. maydis"
        },
        "symptoms": [
            "Chlorotic striping parallel to leaf veins on young leaves.",
            "White downy fungal growth on lower leaf surface in early morning.",
            "Severe stunting, 'witches' broom' of leaves, failure of cob formation."
        ],
        "disease_cycle": "Systemic infection from soil-borne oospores or airborne sporangia entering growing points of seedlings.",
        "epidemiology": "High humidity, cool nights (20-23°C) with heavy dew, continuous cereal cropping.",
        "management": {
            "cultural": "Crop rotation, roguing infected seedlings before 30 days, weed removal.",
            "host_resistance": "Use downy-mildew-resistant hybrids.",
            "chemical": "Seed treatment with Metalaxyl (Apron 35 SD, 6 g/kg).",
            "biological": "Primarily relies on resistant hybrids and seed treatment."
        }
    },
    {
        "crop": "Maize",
        "disease_name": "Turcicum Leaf Blight (Northern Corn Leaf Blight)",
        "causative_organism": "Exserohilum turcicum (= Helminthosporium turcicum); teleomorph Setosphaeria turcica",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Pleosporales",
            "Family": "Pleosporaceae",
            "Genus": "Exserohilum (anamorph); Setosphaeria (teleomorph)",
            "Species": "Exserohilum turcicum"
        },
        "symptoms": [
            "Long, elliptical, greyish-green to tan 'cigar-shaped' lesions (2.5-15 cm) parallel to leaf veins.",
            "Dark, olivaceous sporulation on lower leaf surface."
        ],
        "disease_cycle": "Overwinters as mycelium/conidia in leaf debris. Conidia dispersed by wind and rain splash.",
        "epidemiology": "Cool, moist weather (18-27°C), heavy dew, RH >6 hrs leaf wetness, continuous monocropping.",
        "management": {
            "cultural": "Crop rotation with non-cereals, deep ploughing, avoid close spacing.",
            "host_resistance": "Resistant hybrids carrying Ht1, Ht2, Ht3, or HtN genes.",
            "chemical": "Foliar spray of Mancozeb (0.25%) or Propiconazole (0.1%).",
            "biological": "Trichoderma-based residue treatment."
        }
    },
    {
        "crop": "Maize",
        "disease_name": "Maydis Leaf Blight (Southern Corn Leaf Blight)",
        "causative_organism": "Bipolaris maydis (= Helminthosporium maydis); teleomorph Cochliobolus heterostrophus",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Pleosporales",
            "Family": "Pleosporaceae",
            "Genus": "Bipolaris (anamorph); Cochliobolus (teleomorph)",
            "Species": "Bipolaris maydis"
        },
        "symptoms": [
            "Small, tan-to-greyish-brown rectangular lesions restricted by leaf veins.",
            "Race T attacks husk, ear, and stalk on T-cms hybrids."
        ],
        "disease_cycle": "Survives as mycelium/conidia on crop debris; spread by wind/rain splash.",
        "epidemiology": "Warm temperatures (25-32°C), high humidity, continuous maize, use of T-cms cytoplasm.",
        "management": {
            "cultural": "Crop rotation, residue management.",
            "host_resistance": "Avoid T-cms cytoplasm; use resistant hybrids.",
            "chemical": "Spray Mancozeb or Propiconazole.",
            "biological": "Trichoderma-based residue treatment."
        }
    },
    {
        "crop": "Maize",
        "disease_name": "Curvularia Leaf Spot",
        "causative_organism": "Curvularia lunata",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Pleosporales",
            "Family": "Pleosporaceae",
            "Genus": "Curvularia",
            "Species": "Curvularia lunata"
        },
        "symptoms": [
            "Small, circular to oval tan spots with narrow yellow halo.",
            "Black discoloration of embryo/pericarp on seeds."
        ],
        "disease_cycle": "Seed- and debris-borne; conidia wind- and rain-dispersed.",
        "epidemiology": "Warm, humid weather, stressed or poorly nourished plants.",
        "management": {
            "cultural": "Disease-free seed, field sanitation, crop rotation.",
            "host_resistance": "Moderately tolerant hybrids.",
            "chemical": "Seed treatment with Captan or Thiram; foliar spray of Mancozeb.",
            "biological": "Trichoderma viride seed treatment."
        }
    },
    {
        "crop": "Maize",
        "disease_name": "Stalk Rot Complex",
        "causative_organism": "Fusarium verticillioides, F. graminearum / Macrophomina phaseolina",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Order": "Hypocreales / Botryosphaeriales",
            "Family": "Nectriaceae / Botryosphaeriaceae",
            "Species": "Fusarium verticillioides, Macrophomina phaseolina"
        },
        "symptoms": [
            "Internal pith shredding and discoloration (pink for Fusarium, grey-black with microsclerotia for Charcoal rot).",
            "Hollow stalks, premature death, lodging near maturity."
        ],
        "disease_cycle": "Survives in soil/residue as chlamydospores/microsclerotia; enters roots or wounds under carbohydrate-remobilisation stress.",
        "epidemiology": "Drought stress during grain fill, high plant density, high N low K fertilization.",
        "management": {
            "cultural": "Balanced K fertilization, optimum density, timely harvest.",
            "host_resistance": "Hybrids with strong stalk rind thickness.",
            "chemical": "Seed treatment with Carbendazim or Thiram.",
            "biological": "Trichoderma spp. soil application."
        }
    },

    # --- GROUNDNUT (Arachis hypogaea) ---
    {
        "crop": "Groundnut",
        "disease_name": "Early Leaf Spot",
        "causative_organism": "Cercospora arachidicola; teleomorph Mycosphaerella arachidicola",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Capnodiales",
            "Family": "Mycosphaerellaceae",
            "Genus": "Cercospora (anamorph); Mycosphaerella (teleomorph)",
            "Species": "Cercospora arachidicola"
        },
        "symptoms": [
            "Circular to irregular brown lesions with a distinct chlorotic yellow halo on upper leaf surface."
        ],
        "disease_cycle": "Overwinters as conidia/stromata in residue. Conidia wind and rain-splash dispersed.",
        "epidemiology": "Warm, humid weather (25-30°C) with alternating wet-dry spells, dense canopy.",
        "management": {
            "cultural": "Crop rotation (2-3 yrs), deep summer ploughing, balanced fertilizer.",
            "host_resistance": "Tolerant/resistant varieties.",
            "chemical": "Foliar sprays of Chlorothalonil (0.2%), Mancozeb (0.25%), or Carbendazim+Mancozeb.",
            "biological": "Trichoderma viride or Pseudomonas fluorescens."
        }
    },
    {
        "crop": "Groundnut",
        "disease_name": "Late Leaf Spot",
        "causative_organism": "Cercosporidium personatum; teleomorph Mycosphaerella berkeleyi",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Capnodiales",
            "Family": "Mycosphaerellaceae",
            "Genus": "Cercosporidium (anamorph); Mycosphaerella (teleomorph)",
            "Species": "Cercosporidium personatum"
        },
        "symptoms": [
            "Darker, almost black spots generally without yellow halo; rough, velvety sporulation on lower leaf surface.",
            "Extensive premature defoliation."
        ],
        "disease_cycle": "Overwinters on crop debris; conidia rain/wind-dispersed causing secondary spread.",
        "epidemiology": "Warm humid weather (25-30°C), dense canopy, continuous groundnut monoculture.",
        "management": {
            "cultural": "Crop rotation (2-3 yrs), debris destruction, timely sowing.",
            "host_resistance": "Tolerant/resistant varieties.",
            "chemical": "Chlorothalonil (0.2%), Mancozeb (0.25%), or Carbendazim+Mancozeb from 30 DAS.",
            "biological": "Trichoderma viride / Pseudomonas fluorescens."
        }
    },
    {
        "crop": "Groundnut",
        "disease_name": "Rust",
        "causative_organism": "Puccinia arachidis",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Basidiomycota",
            "Class": "Pucciniomycetes",
            "Order": "Pucciniales",
            "Family": "Pucciniaceae",
            "Genus": "Puccinia",
            "Species": "Puccinia arachidis"
        },
        "symptoms": [
            "Small orange-brown powdery pustules (uredinia) mainly on lower leaf surface.",
            "Leaves turn brown, dry up, and drop prematurely."
        ],
        "disease_cycle": "Autoecious; survives as urediniospores on volunteer groundnut plants and debris, spread by wind.",
        "epidemiology": "Moderate temp (20-25°C), RH >95%, heavy dew, light rains alternating with sun.",
        "management": {
            "cultural": "Remove volunteer plants, crop rotation, timely sowing.",
            "host_resistance": "Moderately resistant varieties.",
            "chemical": "Wettable sulphur (0.2%), Mancozeb (0.25%), Chlorothalonil or Hexaconazole (0.1%).",
            "biological": "Trichoderma-based treatments."
        }
    },

    # --- GREEN GRAM & BLACK GRAM ---
    {
        "crop": "Green Gram & Black Gram",
        "disease_name": "Cercospora Leaf Spot",
        "causative_organism": "Cercospora canescens",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Capnodiales",
            "Family": "Mycosphaerellaceae",
            "Genus": "Cercospora",
            "Species": "Cercospora canescens"
        },
        "symptoms": [
            "Circular to angular reddish-brown spots with grey centre and reddish margin.",
            "Premature yellowing and defoliation."
        ],
        "disease_cycle": "Survives in seed and debris; wind- and rain-splash spread.",
        "epidemiology": "Warm temp (25-30°C), high humidity, rain/dew during pod filling.",
        "management": {
            "cultural": "Crop rotation, field sanitation, clean seed.",
            "host_resistance": "Tolerant varieties.",
            "chemical": "Foliar spray of Mancozeb (0.25%) or Carbendazim.",
            "biological": "Trichoderma viride seed treatment."
        }
    },
    {
        "crop": "Green Gram & Black Gram",
        "disease_name": "Anthracnose",
        "causative_organism": "Colletotrichum truncatum",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Sordariomycetes",
            "Order": "Glomerellales",
            "Family": "Glomerellaceae",
            "Genus": "Colletotrichum",
            "Species": "Colletotrichum truncatum"
        },
        "symptoms": [
            "Dark brown-to-black sunken lesions/cankers on stems and petioles.",
            "Sunken circular lesions on pods with pinkish spore masses."
        ],
        "disease_cycle": "Seed-borne and debris-borne; conidia dispersed in rain-splash via acervuli.",
        "epidemiology": "Warm, humid weather with frequent rain during flowering and pod development.",
        "management": {
            "cultural": "Certified disease-free seed, crop rotation, sanitation.",
            "host_resistance": "Tolerant varieties.",
            "chemical": "Seed treatment with Thiram/Carbendazim; foliar spray of Mancozeb or Carbendazim.",
            "biological": "Trichoderma viride seed treatment."
        }
    },
    {
        "crop": "Green Gram & Black Gram",
        "disease_name": "Web Blight",
        "causative_organism": "Rhizoctonia solani; teleomorph Thanatephorus cucumeris",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Basidiomycota",
            "Class": "Agaricomycetes",
            "Order": "Cantharellales",
            "Family": "Ceratobasidiaceae",
            "Genus": "Rhizoctonia (anamorph); Thanatephorus (teleomorph)",
            "Species": "Rhizoctonia solani"
        },
        "symptoms": [
            "Water-soaked lesions; cobweb-like mycelium binds infected leaves together giving a scorched appearance."
        ],
        "disease_cycle": "Sclerotia in soil germinate to infect lower leaves; spreads by direct leaf-to-leaf hyphal contact.",
        "epidemiology": "High humidity, warm temp (28-32°C), dense plant spacing, excess N.",
        "management": {
            "cultural": "Wider spacing, avoid excess N, improve drainage, destroy infected debris.",
            "host_resistance": "Moderately tolerant varieties.",
            "chemical": "Foliar spray of Validamycin A or Hexaconazole.",
            "biological": "Trichoderma harzianum soil application."
        }
    },
    {
        "crop": "Green Gram & Black Gram",
        "disease_name": "Yellow Mosaic Virus Disease",
        "causative_organism": "Mungbean yellow mosaic virus (MYMV) / MYMIV; vector: Whitefly (Bemisia tabaci)",
        "taxonomic_classification": {
            "Group": "Group II (ssDNA viruses)",
            "Family": "Geminiviridae",
            "Genus": "Begomovirus",
            "Vector": "Bemisia tabaci"
        },
        "symptoms": [
            "Irregular yellow and green mosaic patches on leaves, progressing to complete leaf yellowing.",
            "Leaves small, puckered; pods distorted with mottled seeds."
        ],
        "disease_cycle": "Transmitted in a persistent circulative manner by whiteflies from infected weed/crop hosts.",
        "epidemiology": "Warm, dry weather (30-35°C), high whitefly populations, continuous legume cropping.",
        "management": {
            "cultural": "Adjust sowing dates, roguing in early stages, field sanitation.",
            "host_resistance": "Resistant varieties (e.g., ML 5, SML 668, Pusa Vishal, T9, Pant U-19).",
            "chemical": "Control whitefly with Imidacloprid (0.3 mL/L) or Thiamethoxam; yellow sticky traps.",
            "biological": "Neem-based formulations (Azadirachtin 1500 ppm)."
        }
    },

    # --- BANANA (Musa spp.) ---
    {
        "crop": "Banana",
        "disease_name": "Panama Wilt (Fusarium Wilt)",
        "causative_organism": "Fusarium oxysporum f. sp. cubense",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Sordariomycetes",
            "Order": "Hypocreales",
            "Family": "Nectriaceae",
            "Genus": "Fusarium",
            "Species": "Fusarium oxysporum f. sp. cubense"
        },
        "symptoms": [
            "Yellowing of oldest leaves first from margin inward; petiole snaps, forming a 'skirt' around pseudostem.",
            "Splitting at base of pseudostem; dark brown-to-black vascular discoloration in corm."
        ],
        "disease_cycle": "Soil-borne chlamydospores infect root tips/wounds, blocking xylem vessels. Spread by infected suckers/tools.",
        "epidemiology": "Acidic sandy soils (pH <6), poor drainage, nematode damage, continuous monoculture.",
        "management": {
            "cultural": "Certified tissue-culture plants, farm sanitation, crop rotation, manage nematodes.",
            "host_resistance": "Resistant/tolerant cultivars.",
            "chemical": "Soil drenches generally uneconomical/ineffective.",
            "biological": "Organic manure, Trichoderma spp., Pseudomonas fluorescens, liming to raise pH."
        }
    },
    {
        "crop": "Banana",
        "disease_name": "Bacterial Wilt (Moko Disease)",
        "causative_organism": "Ralstonia solanacearum, Race 2",
        "taxonomic_classification": {
            "Kingdom": "Bacteria",
            "Phylum": "Pseudomonadota (Proteobacteria)",
            "Class": "Betaproteobacteria",
            "Order": "Burkholderiales",
            "Family": "Burkholderiaceae",
            "Genus": "Ralstonia",
            "Species": "Ralstonia solanacearum"
        },
        "symptoms": [
            "Yellowing/wilting from younger to older leaves (if insect-borne) or oldest-first (if root-borne).",
            "Vascular discoloration with milky bacterial ooze (bacterial streaming test positive).",
            "Blackening of fruit pulp and collapse of male bud."
        ],
        "disease_cycle": "Survives in soil and suckers. Spread by tools, insects visiting male flowers, and water.",
        "epidemiology": "Warm wet soil conditions, contaminated tools, insect pollinator activity.",
        "management": {
            "cultural": "Disease-free suckers, tool disinfection, debudding male flower, destroying infected mats.",
            "host_resistance": "No commercial resistance available.",
            "chemical": "No effective curative chemical treatment.",
            "biological": "Not applicable."
        }
    },
    {
        "crop": "Banana",
        "disease_name": "Sigatoka Leaf Spot",
        "causative_organism": "Mycosphaerella musicola (Yellow) / Mycosphaerella fijiensis (Black)",
        "taxonomic_classification": {
            "Kingdom": "Fungi",
            "Phylum": "Ascomycota",
            "Class": "Dothideomycetes",
            "Order": "Capnodiales",
            "Family": "Mycosphaerellaceae",
            "Genus": "Mycosphaerella",
            "Species": "Mycosphaerella fijiensis / M. musicola"
        },
        "symptoms": [
            "Yellow-brown streaks expanding into oval spots with grey-tan centre and dark brown margin.",
            "Severe leaf blighting reducing photosynthetic area."
        ],
        "disease_cycle": "Ascospores wind-dispersed for primary spread; conidia rain-splashed for secondary spread.",
        "epidemiology": "Warm temp (25-28°C), high rainfall/RH, dense poorly drained stands.",
        "management": {
            "cultural": "De-leafing (removing infected leaves), wider spacing, proper drainage, adequate K.",
            "host_resistance": "Resistant cultivars where available.",
            "chemical": "Rotational sprays of Propiconazole, Mancozeb, Chlorothalonil, or mineral oils.",
            "biological": "Trichoderma-based leaf litter treatment."
        }
    },
    {
        "crop": "Banana",
        "disease_name": "Bunchy Top",
        "causative_organism": "Banana bunchy top virus (BBTV); vector: Banana aphid (Pentalonia nigronervosa)",
        "taxonomic_classification": {
            "Group": "Group II (ssDNA viruses)",
            "Family": "Nanoviridae",
            "Genus": "Babuvirus",
            "Vector": "Pentalonia nigronervosa"
        },
        "symptoms": [
            "Dark green 'Morse code' streaks along midrib and leaf veins.",
            "Narrow upright leaves forming a rosette/'bunchy top' appearance; severe stunting."
        ],
        "disease_cycle": "Transmitted in persistent circulative manner by aphids and spread via infected suckers.",
        "epidemiology": "High aphid populations, movement of infected suckers, proximity to old stands.",
        "management": {
            "cultural": "Certified virus-free tissue-culture plants, immediate roguing and destruction of infected mats.",
            "host_resistance": "No commercial resistance available.",
            "chemical": "Control aphid vector with systemic aphicides (Imidacloprid, Dimethoate).",
            "biological": "Rely primarily on clean planting material and vector exclusion."
        }
    },

    # --- PAPAYA (Carica papaya) ---
    {
        "crop": "Papaya",
        "disease_name": "Foot Rot",
        "causative_organism": "Phytophthora palmivora",
        "taxonomic_classification": {
            "Kingdom": "Chromista (Straminipila)",
            "Phylum": "Oomycota",
            "Class": "Oomycetes",
            "Order": "Peronosporales",
            "Family": "Peronosporaceae",
            "Genus": "Phytophthora",
            "Species": "Phytophthora palmivora"
        },
        "symptoms": [
            "Water-soaked lesions girdling stem base causing plant to wilt and collapse.",
            "Root decay and white cottony fungal growth on rotting fruit."
        ],
        "disease_cycle": "Zoospores swim through water films to infect roots/collar. Chlamydospores survive in soil.",
        "epidemiology": "Waterlogging, poor drainage, warm temp (28-32°C), heavy rainfall.",
        "management": {
            "cultural": "Raised bed planting, good drainage, wider spacing, destruction of infected plants.",
            "host_resistance": "Limited tolerance.",
            "chemical": "Soil drenching with Metalaxyl or Fosetyl-Al; collar painting with Bordeaux mixture.",
            "biological": "Trichoderma soil application."
        }
    },
    {
        "crop": "Papaya",
        "disease_name": "Leaf Curl",
        "causative_organism": "Papaya leaf curl virus (PaLCuV); vector: Whitefly (Bemisia tabaci)",
        "taxonomic_classification": {
            "Group": "Group II (ssDNA viruses)",
            "Family": "Geminiviridae",
            "Genus": "Begomovirus",
            "Vector": "Bemisia tabaci"
        },
        "symptoms": [
            "Upward or downward leaf curling, crinkling, lamina thickening.",
            "Bushy rosetted crown growth, stunting, severely reduced fruit set."
        ],
        "disease_cycle": "Persistently transmitted by whiteflies from infected papaya or weed hosts.",
        "epidemiology": "High whitefly populations, warm weather, proximity to infected crops.",
        "management": {
            "cultural": "Raise seedlings under insect-proof nets, early roguing of infected plants.",
            "host_resistance": "Use tolerant varieties.",
            "chemical": "Control whiteflies with Imidacloprid or Thiamethoxam.",
            "biological": "Neem formulations and yellow sticky traps."
        }
    },
    {
        "crop": "Papaya",
        "disease_name": "Mosaic (Papaya Ring Spot Virus Disease)",
        "causative_organism": "Papaya ringspot virus (PRSV); vector: Aphids (Myzus persicae, Aphis gossypii)",
        "taxonomic_classification": {
            "Group": "Group IV (+ssRNA viruses)",
            "Family": "Potyviridae",
            "Genus": "Potyvirus",
            "Vector": "Aphids (non-persistent, stylet-borne)"
        },
        "symptoms": [
            "Mosaic mottling, leaf distortion ('shoestring' leaves).",
            "Water-soaked dark green streaks on petioles.",
            "Concentric ring spots on fruit surface."
        ],
        "disease_cycle": "Non-persistent transmission by aphids probing host leaves; primary inoculum from infected trees or nearby cucurbits.",
        "epidemiology": "Proximity to cucurbit crops, active aphid flight activity, warm weather.",
        "management": {
            "cultural": "Plant away from cucurbits, prompt roguing, net-house nursery raising.",
            "host_resistance": "Transgenic coat-protein resistant papaya, cross-protection with mild strains.",
            "chemical": "Reflective mulches and mineral-oil sprays (insecticides ineffective due to rapid non-persistent spread).",
            "biological": "Encourage natural aphid predators."
        }
    }
]