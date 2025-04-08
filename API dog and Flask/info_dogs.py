# Data of breeds stored in a dictionary
def get_breed_details(request):

    dog_breeds_info = {
        "affenpinscher": {
            "origin": "Germany",
            "estimated_life": "12-14 years",
            "height": "9-12 inches (23-30 cm)",
            "weight": "7-10 lbs (3-4.5 kg)",
            "temperament": '''Curious, confident, playful,
            independent, affectionate'''
        },
        "african": {
            "origin": "Sub-Saharan Africa",
            "estimated_life": "10-12 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "40-70 lbs (18-32 kg)",
            "temperament": '''Social, energetic, pack-oriented,
            loyal, reserved around strangers'''
            },
        "airedale": {
            "origin": "England",
            "estimated_life": "11-14 years",
            "height": "21-23 inches (53-61 cm)",
            "weight": "40-65 lbs (18-29 kg)",
            "temperament": '''Intelligent, energetic, friendly,
            strong-willed, independent'''
        },
        "akita": {
            "origin": "Japan",
            "estimated_life": "10-15 years",
            "height": "24-28 inches (61-71 cm)",
            "weight": "70-130 lbs (32-59 kg)",
            "temperament": '''Courageous, dignified, loyal,
            protective, aloof around strangers'''
        },
        "appenzeller": {
            "origin": "Switzerland",
            "estimated_life": "12-14 years",
            "height": "19-23 inches (48-61 cm)",
            "weight": "50-70 lbs (23-32 kg)",
            "temperament": '''Intelligent, energetic,
            hardworking, loyal, protective'''
        },
        "australian": {
            "origin": "United States",
            "estimated_life": "12-15 years",
            "height": "18-23 inches (46-61 cm)",
            "weight": "40-65 lbs (18-29 kg)",
            "temperament": '''Intelligent, energetic, highly trainable,
            requires mental and physical stimulation'''
        },
        "bakharwal": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "24-28 inches (61-71 cm)",
            "weight": "50-90 lbs (23-41 kg)",
            "temperament": '''Loyal, protective, courageous,
            independent, good with family'''
        },
        "basenji": {
            "origin": "Central Africa",
            "estimated_life": "12-16 years",
            "height": "16-17 inches (41-43 cm)",
            "weight": "20-24 lbs (9-11 kg)",
            "temperament": '''Independent, intelligent, curious,
            energetic, not overly affectionate'''
        },
        "beagle": {
            "origin": "England",
            "estimated_life": "12-15 years",
            "height": "13-15 inches (33-38 cm)",
            "weight": "20-30 lbs (9-14 kg)",
            "temperament": '''Friendly, curious, merry,
            good with children and other dogs'''
        },
        "bluetick": {
            "origin": "United States",
            "estimated_life": "11-12 years",
            "height": "22-27 inches (56-69 cm)",
            "weight": "45-80 lbs (20-36 kg)",
            "temperament": '''Energetic, intelligent, friendly,
            independent, good hunting instincts'''
        },
        "borzoi": {
            "origin": "Russia",
            "estimated_life": "10-12 years",
            "height": "28-32 inches (71-81 cm)",
            "weight": "60-105 lbs (27-48 kg)",
            "temperament": "Independent, dignified, friendly, calm"
        },
        "bouvier": {
            "origin": "Belgium",
            "estimated_life": "10-12 years",
            "height": "23.5-27.5 inches (60-70 cm)",
            "weight": "60-110 lbs (27-50 kg)",
            "temperament": "Loyal, intelligent, protective, friendly"
        },
        "boxer": {
            "origin": "Germany",
            "estimated_life": "10-12 years",
            "height": "21-25 inches (53-64 cm)",
            "weight": "50-80 lbs (23-36 kg)",
            "temperament": "Energetic, playful, loyal, affectionate"
        },
        "brabancon": {
            "origin": "Belgium",
            "estimated_life": "12-15 years",
            "height": "8-10 inches (20-25 cm)",
            "weight": "8-12 lbs (4-5.5 kg)",
            "temperament": "Alert, affectionate, loyal, curious"
        },
        "briard": {
            "origin": "France",
            "estimated_life": "12-16 years",
            "height": "22-27 inches (56-69 cm)",
            "weight": "50-90 lbs (23-41 kg)",
            "temperament": "Loyal, intelligent, protective, courageous"
        },
        "buhund": {
            "origin": "Norway",
            "estimated_life": "12-16 years",
            "height": "16-18 inches (40-46 cm)",
            "weight": "25-40 lbs (11-18 kg)",
            "temperament": "Friendly, energetic, loyal, alert"
        },
        "bulldog": {
            "origin": "England",
            "estimated_life": "8-12 years",
            "height": "12-16 inches (30-41 cm)",
            "weight": "40-50 lbs (18-23 kg)",
            "temperament": "Calm, courageous, affectionate, loyal"
        },
        "bullterrier": {
            "origin": "England",
            "estimated_life": "10-14 years",
            "height": "21-22 inches (53-56 cm)",
            "weight": "50-70 lbs (23-32 kg)",
            "temperament": "Playful, energetic, courageous, loving"
        },
        "cattledog": {
            "origin": "Australia",
            "estimated_life": "12-16 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "35-50 lbs (16-23 kg)",
            "temperament": "Loyal, intelligent, energetic, protective"
        },
        "cavapoo": {
            "origin": "United States",
            "estimated_life": "12-15 years",
            "height": "9-14 inches (23-36 cm)",
            "weight": "10-20 lbs (4.5-9 kg)",
            "temperament": "Affectionate, friendly, intelligent, gentle"
        },
        "chihuahua": {
            "origin": "Mexico",
            "estimated_life": "12-20 years",
            "height": "6-9 inches (15-23 cm)",
            "weight": "2-6 lbs (0.9-2.7 kg)",
            "temperament": "Loyal, energetic, courageous, alert"
        },
        "chippiparai": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "55-75 lbs (25-34 kg)",
            "temperament": "Loyal, intelligent, energetic, friendly"
        },
        "chow": {
            "origin": "China",
            "estimated_life": "8-12 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "45-70 lbs (20-32 kg)",
            "temperament": "Aloof, independent, confident, loyal"
        },
        "clumber": {
            "origin": "England",
            "estimated_life": "12-14 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "55-85 lbs (25-39 kg)",
            "temperament": "Calm, gentle, affectionate, loyal"
        },
        "cockapoo": {
            "origin": "United States",
            "estimated_life": "12-15 years",
            "height": "10-15 inches (25-38 cm)",
            "weight": "12-24 lbs (5.4-10.9 kg)",
            "temperament": "Friendly, intelligent, affectionate, playful"
        },
        "collie": {
            "origin": "Scotland",
            "estimated_life": "12-14 years",
            "height": "22-26 inches (56-66 cm)",
            "weight": "50-75 lbs (23-34 kg)",
            "temperament": "Loyal, friendly, intelligent, gentle"
        },
        "coonhound": {
            "origin": "United States",
            "estimated_life": "10-12 years",
            "height": "21-27 inches (53-69 cm)",
            "weight": "40-75 lbs (18-34 kg)",
            "temperament": "Independent, energetic, friendly, loyal"
        },
        "corgi": {
            "origin": "Wales",
            "estimated_life": "12-15 years",
            "height": "10-12 inches (25-30 cm)",
            "weight": "25-30 lbs (11-14 kg)",
            "temperament": "Affectionate, energetic, intelligent, friendly"
        },
        "cotondetulear": {
            "origin": "Madagascar",
            "estimated_life": "14-16 years",
            "height": "9-11 inches (23-28 cm)",
            "weight": "9-13 lbs (4-6 kg)",
            "temperament": "Affectionate, playful, alert, friendly"
        },
        "dachshund": {
            "origin": "Germany",
            "estimated_life": "12-16 years",
            "height": "8-9 inches (20-23 cm)",
            "weight": "16-32 lbs (7-14.5 kg)",
            "temperament": "Curious, courageous, playful, affectionate"
        },
        "dalmatian": {
            "origin": "Croatia",
            "estimated_life": "10-13 years",
            "height": "19-24 inches (48-61 cm)",
            "weight": "45-70 lbs (20-32 kg)",
            "temperament": "Energetic, intelligent, friendly, playful"
        },
        "dane": {
            "origin": "Germany",
            "estimated_life": "7-10 years",
            "height": "28-34 inches (71-86 cm)",
            "weight": "110-175 lbs (50-79 kg)",
            "temperament": "Friendly, gentle, confident, loyal"
        },
        "danish": {
            "origin": "Denmark",
            "estimated_life": "7-10 years",
            "height": "28-34 inches (71-86 cm)",
            "weight": "100-175 lbs (45-79 kg)",
            "temperament": "Gentle, friendly, confident, affectionate"
        },
        "deerhound": {
            "origin": "Scotland",
            "estimated_life": "8-11 years",
            "height": "28-32 inches (71-81 cm)",
            "weight": "75-110 lbs (34-50 kg)",
            "temperament": "Gentle, loyal, independent, friendly"
        },
        "dhole": {
            "origin": "Asia",
            "estimated_life": "10-12 years",
            "height": "16-20 inches (41-51 cm)",
            "weight": "35-55 lbs (16-25 kg)",
            "temperament": "Energetic, social, intelligent, loyal"
        },
        "dingo": {
            "origin": "Australia",
            "estimated_life": "10-15 years",
            "height": "17-23 inches (43-58 cm)",
            "weight": "24-44 lbs (11-20 kg)",
            "temperament": "Independent, intelligent, alert, loyal"
        },
        "doberman": {
            "origin": "Germany",
            "estimated_life": "10-13 years",
            "height": "24-28 inches (61-71 cm)",
            "weight": "60-100 lbs (27-45 kg)",
            "temperament": "Intelligent, loyal, energetic, protective"
        },
        "elkhound": {
            "origin": "Norway",
            "estimated_life": "12-15 years",
            "height": "19-23 inches (48-61 cm)",
            "weight": "40-55 lbs (18-25 kg)",
            "temperament": "Friendly, energetic, loyal, independent"
        },
        "entlebucher": {
            "origin": "Switzerland",
            "estimated_life": "12-14 years",
            "height": "16-21 inches (41-53 cm)",
            "weight": "40-50 lbs (18-23 kg)",
            "temperament": "Energetic, intelligent, confident, loyal"
        },
        "eskimo": {
            "origin": "United States",
            "estimated_life": "12-14 years",
            "height": "15-20 inches (38-51 cm)",
            "weight": "35-50 lbs (16-23 kg)",
            "temperament": "Friendly, playful, alert, intelligent"
        },
        "finnish": {
            "origin": "Finland",
            "estimated_life": "12-14 years",
            "height": "16-20 inches (41-51 cm)",
            "weight": "33-53 lbs (15-24 kg)",
            "temperament": "Friendly, intelligent, energetic, alert"
        },
        "frise": {
            "origin": "France",
            "estimated_life": "12-15 years",
            "height": "9-11 inches (23-28 cm)",
            "weight": "7-13 lbs (3-6 kg)",
            "temperament": "Friendly, playful, affectionate, intelligent"
        },
        "gaddi": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "55-80 lbs (25-36 kg)",
            "temperament": "Loyal, protective, energetic, intelligent"
        },
        "germanshepherd": {
            "origin": "Germany",
            "estimated_life": "9-13 years",
            "height": "22-26 inches (56-66 cm)",
            "weight": "50-90 lbs (23-41 kg)",
            "temperament": "Confident, courageous, intelligent, loyal"
        },
        "greyhound": {
            "origin": "England",
            "estimated_life": "10-14 years",
            "height": "27-30 inches (69-76 cm)",
            "weight": "60-70 lbs (27-32 kg)",
            "temperament": "Gentle, friendly, intelligent, independent"
        },
        "groenendael": {
            "origin": "Belgium",
            "estimated_life": "12-14 years",
            "height": "24-26 inches (61-66 cm)",
            "weight": "60-75 lbs (27-34 kg)",
            "temperament": "Confident, intelligent, loyal, alert"
        },
        "havanese": {
            "origin": "Cuba",
            "estimated_life": "14-16 years",
            "height": "8-12 inches (20-30 cm)",
            "weight": "7-13 lbs (3-6 kg)",
            "temperament": "Friendly, intelligent, playful, affectionate"
        },
        "hound": {
            "origin": "Various regions",
            "estimated_life": "10-15 years",
            "height": "22-27 inches (56-69 cm)",
            "weight": "40-65 lbs (18-29 kg)",
            "temperament": "Energetic, independent, loyal, friendly"
        },
        "husky": {
            "origin": "Siberia",
            "estimated_life": "12-15 years",
            "height": "20-24 inches (51-61 cm)",
            "weight": "35-60 lbs (16-27 kg)",
            "temperament": "Friendly, energetic, independent, playful"
        },
        "keeshond": {
            "origin": "Germany",
            "estimated_life": "12-15 years",
            "height": "17-19 inches (43-48 cm)",
            "weight": "35-45 lbs (16-20 kg)",
            "temperament": "Friendly, affectionate, alert, energetic"
        },
        "kelpie": {
            "origin": "Australia",
            "estimated_life": "12-15 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "30-50 lbs (14-23 kg)",
            "temperament": "Energetic, intelligent, loyal, hardworking"
        },
        "kombai": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "60-100 lbs (27-45 kg)",
            "temperament": "Loyal, protective, courageous, intelligent"
        },
        "komondor": {
            "origin": "Hungary",
            "estimated_life": "10-12 years",
            "height": "25-30 inches (64-76 cm)",
            "weight": "80-130 lbs (36-59 kg)",
            "temperament": "Loyal, protective, intelligent, calm"
        },
        "kuvasz": {
            "origin": "Hungary",
            "estimated_life": "10-12 years",
            "height": "26-30 inches (66-76 cm)",
            "weight": "70-115 lbs (32-52 kg)",
            "temperament": "Loyal, protective, independent, intelligent"
        },
        "labradoodle": {
            "origin": "Australia",
            "estimated_life": "12-14 years",
            "height": "21-24 inches (53-61 cm)",
            "weight": "50-65 lbs (23-29 kg)",
            "temperament": "Friendly, intelligent, energetic, affectionate"
        },
        "labrador": {
            "origin": "Canada",
            "estimated_life": "10-12 years",
            "height": "21-24 inches (53-61 cm)",
            "weight": "55-80 lbs (25-36 kg)",
            "temperament": "Friendly, outgoing, energetic, intelligent"
        },
        "leonberg": {
            "origin": "Germany",
            "estimated_life": "8-9 years",
            "height": "26-31 inches (66-79 cm)",
            "weight": "90-170 lbs (41-77 kg)",
            "temperament": "Gentle, friendly, intelligent, calm"
        },
        "lhasa": {
            "origin": "Tibet",
            "estimated_life": "12-14 years",
            "height": "10-11 inches (25-28 cm)",
            "weight": "12-15 lbs (5.4-6.8 kg)",
            "temperament": "Affectionate, intelligent, outgoing, independent"
        },
        "malamute": {
            "origin": "Alaska",
            "estimated_life": "10-14 years",
            "height": "23-26 inches (58-66 cm)",
            "weight": "75-100 lbs (34-45 kg)",
            "temperament": "Friendly, independent, loyal, energetic"
        },
        "malinois": {
            "origin": "Belgium",
            "estimated_life": "12-14 years",
            "height": "22-26 inches (56-66 cm)",
            "weight": "40-80 lbs (18-36 kg)",
            "temperament": "Energetic, intelligent, alert, confident"
        },
        "maltese": {
            "origin": "Malta",
            "estimated_life": "12-15 years",
            "height": "7-9 inches (18-23 cm)",
            "weight": "4-7 lbs (1.8-3.2 kg)",
            "temperament": "Affectionate, playful, intelligent, lively"
        },
        "mastiff": {
            "origin": "England",
            "estimated_life": "6-10 years",
            "height": "27-34 inches (69-86 cm)",
            "weight": "110-230 lbs (50-104 kg)",
            "temperament": "Gentle, courageous, protective, loyal"
        },
        "mexicanhairless": {
            "origin": "Mexico",
            "estimated_life": "10-15 years",
            "height": "18-25 inches (46-64 cm)",
            "weight": "15-30 lbs (7-14 kg)",
            "temperament": "Loyal, affectionate, alert, intelligent"
        },
        "mix": {
            "origin": "Varies",
            "estimated_life": "Varies",
            "height": "Varies",
            "weight": "Varies",
            "temperament": "Varies"
        },
        "mountain": {
            "origin": "Switzerland",
            "estimated_life": "8-12 years",
            "height": "23-30 inches (58-76 cm)",
            "weight": "80-120 lbs (36-54 kg)",
            "temperament": "Loyal, gentle, calm, friendly"
        },
        "mudhol": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "45-60 lbs (20-27 kg)",
            "temperament": "Energetic, intelligent, loyal, independent"
        },
        "newfoundland": {
            "origin": "Canada",
            "estimated_life": "8-10 years",
            "height": "26-28 inches (66-71 cm)",
            "weight": "100-150 lbs (45-68 kg)",
            "temperament": "Gentle, friendly, intelligent, calm"
        },
        "otterhound": {
            "origin": "England",
            "estimated_life": "10-13 years",
            "height": "24-27 inches (61-69 cm)",
            "weight": "65-115 lbs (29-52 kg)",
            "temperament": "Friendly, intelligent, energetic, independent"
        },
        "ovcharka": {
            "origin": "Russia",
            "estimated_life": "10-12 years",
            "height": "27-30 inches (69-76 cm)",
            "weight": "90-150 lbs (41-68 kg)",
            "temperament": "Protective, confident, loyal, independent"
        },
        "papillon": {
            "origin": "France",
            "estimated_life": "12-16 years",
            "height": "8-11 inches (20-28 cm)",
            "weight": "5-10 lbs (2.3-4.5 kg)",
            "temperament": "Friendly, energetic, intelligent, playful"
        },
        "pariah": {
            "origin": "India",
            "estimated_life": "12-14 years",
            "height": "18-25 inches (46-64 cm)",
            "weight": "30-50 lbs (14-23 kg)",
            "temperament": "Loyal, independent, intelligent, alert"
        },
        "pekinese": {
            "origin": "China",
            "estimated_life": "12-15 years",
            "height": "6-9 inches (15-23 cm)",
            "weight": "7-14 lbs (3-6.4 kg)",
            "temperament": "Affectionate, courageous, independent, friendly"
        },
        "pembroke": {
            "origin": "Wales",
            "estimated_life": "12-15 years",
            "height": "10-12 inches (25-30 cm)",
            "weight": "25-30 lbs (11-14 kg)",
            "temperament": "Friendly, energetic, intelligent, loyal"
        },
        "pinscher": {
            "origin": "Germany",
            "estimated_life": "12-16 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "25-45 lbs (11-20 kg)",
            "temperament": "Energetic, intelligent, alert, confident"
        },
        "pitbull": {
            "origin": "United States",
            "estimated_life": "12-14 years",
            "height": "17-21 inches (43-53 cm)",
            "weight": "30-85 lbs (14-39 kg)",
            "temperament": "Loyal, energetic, intelligent, affectionate"
        },
        "pointer": {
            "origin": "England",
            "estimated_life": "12-14 years",
            "height": "23-28 inches (58-71 cm)",
            "weight": "45-75 lbs (20-34 kg)",
            "temperament": "Energetic, friendly, intelligent, loyal"
        },
        "pomeranian": {
            "origin": "Germany/Poland",
            "estimated_life": "12-16 years",
            "height": "7-8 inches (18-20 cm)",
            "weight": "3-7 lbs (1.4-3.2 kg)",
            "temperament": "Energetic, intelligent, friendly, extroverted"
        },
        "poodle": {
            "origin": "Germany/France",
            "estimated_life": "12-15 years",
            "height": "10-24 inches (25-61 cm)",
            "weight": "4-70 lbs (1.8-32 kg)",
            "temperament": "Intelligent, active, friendly, alert"
        },
        "pug": {
            "origin": "China",
            "estimated_life": "12-15 years",
            "height": "10-13 inches (25-33 cm)",
            "weight": "14-18 lbs (6-8 kg)",
            "temperament": "Affectionate, playful, intelligent, charming"
        },
        "puggle": {
            "origin": "United States",
            "estimated_life": "12-15 years",
            "height": "10-15 inches (25-38 cm)",
            "weight": "15-30 lbs (7-14 kg)",
            "temperament": "Friendly, playful, curious, affectionate"
        },
        "pyrenees": {
            "origin": "France/Spain",
            "estimated_life": "10-12 years",
            "height": "25-32 inches (64-81 cm)",
            "weight": "85-115 lbs (39-52 kg)",
            "temperament": "Gentle, loyal, protective, independent"
        },
        "rajapalayam": {
            "origin": "India",
            "estimated_life": "10-12 years",
            "height": "24-30 inches (61-76 cm)",
            "weight": "60-100 lbs (27-45 kg)",
            "temperament": "Loyal, brave, intelligent, alert"
        },
        "redbone": {
            "origin": "United States",
            "estimated_life": "10-12 years",
            "height": "22-27 inches (56-69 cm)",
            "weight": "45-70 lbs (20-32 kg)",
            "temperament": "Friendly, energetic, intelligent, loyal"
        },
        "retriever": {
            "origin": "United Kingdom",
            "estimated_life": "10-12 years",
            "height": "21-24 inches (53-61 cm)",
            "weight": "55-75 lbs (25-34 kg)",
            "temperament": "Friendly, intelligent, energetic, loyal"
        },
        "ridgeback": {
            "origin": "South Africa",
            "estimated_life": "10-12 years",
            "height": "24-27 inches (61-69 cm)",
            "weight": "70-85 lbs (32-39 kg)",
            "temperament": "Loyal, independent, intelligent, courageous"
        },
        "rottweiler": {
            "origin": "Germany",
            "estimated_life": "8-10 years",
            "height": "22-27 inches (56-69 cm)",
            "weight": "80-135 lbs (36-61 kg)",
            "temperament": "Loyal, confident, courageous, protective"
        },
        "saluki": {
            "origin": "Middle East",
            "estimated_life": "12-14 years",
            "height": "23-28 inches (58-71 cm)",
            "weight": "35-65 lbs (16-29 kg)",
            "temperament": "Independent, loyal, intelligent, reserved"
        },
        "samoyed": {
            "origin": "Siberia",
            "estimated_life": "12-16 years",
            "height": "19-23 inches (48-61 cm)",
            "weight": "35-65 lbs (16-29 kg)",
            "temperament": "Friendly, energetic, playful, gentle"
        },
        "schipperke": {
            "origin": "Belgium",
            "estimated_life": "13-15 years",
            "height": "10-13 inches (25-33 cm)",
            "weight": "10-20 lbs (4.5-9 kg)",
            "temperament": "Curious, energetic, intelligent, confident"
        },
        "schnauzer": {
            "origin": "Germany",
            "estimated_life": "12-16 years",
            "height": "12-27 inches (30-69 cm)",
            "weight": "11-85 lbs (5-39 kg)",
            "temperament": "Loyal, alert, intelligent, confident"
        },
        "segugio": {
            "origin": "Italy",
            "estimated_life": "12-14 years",
            "height": "18-22 inches (46-56 cm)",
            "weight": "30-55 lbs (14-25 kg)",
            "temperament": "Energetic, intelligent, independent, loyal"
        },
        "setter": {
            "origin": "United Kingdom",
            "estimated_life": "10-12 years",
            "height": "24-27 inches (61-69 cm)",
            "weight": "45-80 lbs (20-36 kg)",
            "temperament": "Friendly, energetic, intelligent, loyal"
        },
        "sharpei": {
            "origin": "China",
            "estimated_life": "8-12 years",
            "height": "18-20 inches (46-51 cm)",
            "weight": "40-55 lbs (18-25 kg)",
            "temperament": "Independent, confident, calm, loyal"
        },
        "sheepdog": {
            "origin": "United Kingdom",
            "estimated_life": "10-12 years",
            "height": "18-22 inches (46-56 cm)",
            "weight": "60-100 lbs (27-45 kg)",
            "temperament": "Intelligent, energetic, friendly, loyal"
        },
        "shiba": {
            "origin": "Japan",
            "estimated_life": "12-15 years",
            "height": "13.5-16.5 inches (34-42 cm)",
            "weight": "17-23 lbs (7.7-10.4 kg)",
            "temperament": "Independent, courageous, alert, confident"
        },
        "shihtzu": {
            "origin": "China",
            "estimated_life": "10-16 years",
            "height": "9-10.5 inches (23-27 cm)",
            "weight": "9-16 lbs (4-7 kg)",
            "temperament": "Affectionate, playful, friendly, loyal"
        },
        "spaniel": {
            "origin": "Various regions",
            "estimated_life": "12-14 years",
            "height": "12-18 inches (30-46 cm)",
            "weight": "15-30 lbs (7-14 kg)",
            "temperament": "Friendly, playful, intelligent, affectionate"
        },
        "spitz": {
            "origin": "Various regions",
            "estimated_life": "12-16 years",
            "height": "9-22 inches (23-56 cm)",
            "weight": "12-60 lbs (5-27 kg)",
            "temperament": "Loyal, energetic, independent, friendly"
        },
        "springer": {
            "origin": "United Kingdom",
            "estimated_life": "12-14 years",
            "height": "18-20 inches (46-51 cm)",
            "weight": "40-50 lbs (18-23 kg)",
            "temperament": "Friendly, energetic, intelligent, affectionate"
        },
        "stbernard": {
            "origin": "Switzerland",
            "estimated_life": "8-10 years",
            "height": "25-30 inches (64-76 cm)",
            "weight": "120-180 lbs (54-82 kg)",
            "temperament": "Gentle, friendly, loyal, intelligent"
        },
        "terrier": {
            "origin": "Various regions",
            "estimated_life": "12-16 years",
            "height": "8-15 inches (20-38 cm)",
            "weight": "8-20 lbs (3.6-9 kg)",
            "temperament": "Energetic, courageous, intelligent, independent"
        },
        "tervuren": {
            "origin": "Belgium",
            "estimated_life": "12-14 years",
            "height": "22-26 inches (56-66 cm)",
            "weight": "40-65 lbs (18-29 kg)",
            "temperament": "Intelligent, active, alert, loyal"
        },
        "vizsla": {
            "origin": "Hungary",
            "estimated_life": "10-14 years",
            "height": "21-24 inches (53-61 cm)",
            "weight": "40-60 lbs (18-27 kg)",
            "temperament": "Energetic, affectionate, intelligent, loyal"
        },
        "waterdog": {
            "origin": "Spain",
            "estimated_life": "12-14 years",
            "height": "17-20 inches (43-51 cm)",
            "weight": "35-60 lbs (16-27 kg)",
            "temperament": "Energetic, intelligent, loyal, affectionate"
        },
        "weimaraner": {
            "origin": "Germany",
            "estimated_life": "10-14 years",
            "height": "23-27 inches (58-69 cm)",
            "weight": "55-90 lbs (25-41 kg)",
            "temperament": "Friendly, energetic, intelligent, loyal"
        },
        "whippet": {
            "origin": "United Kingdom",
            "estimated_life": "12-15 years",
            "height": "18-22 inches (46-56 cm)",
            "weight": "25-40 lbs (11-18 kg)",
            "temperament": "Friendly, gentle, energetic, intelligent"
        },
        "wolfhound": {
            "origin": "Ireland",
            "estimated_life": "6-10 years",
            "height": "30-35 inches (76-89 cm)",
            "weight": "105-180 lbs (48-82 kg)",
            "temperament": "Gentle, friendly, courageous, loyal"
        }
        }
    if request in dog_breeds_info:
        print("Find :D")

    else:
        print("TRY AGAIN!!! FAILED")
        return "Error"
    # print(dog_breeds_info[request])
    return dog_breeds_info[request]
