def analyze_health(
    age,
    gender,
    height,
    weight,
    symptoms,
    water,
    sleep,
    exercise,
    food_habit,
    stress_level
):

    recommendations = []

    # ==========================================
    # BMI CALCULATION
    # ==========================================

    height_m = height / 100
    bmi = weight / (height_m * height_m)

    if bmi < 18.5:
        bmi_status = "Underweight"
        recommendations.append(
            "Your BMI is below the normal range. "
            "Include nutritious and calorie-rich foods such as milk, eggs, nuts, fruits and whole grains."
        )

    elif bmi < 25:
        bmi_status = "Normal"
        recommendations.append(
            "Your BMI is within the normal range. "
            "Continue maintaining a balanced diet and regular physical activity."
        )

    elif bmi < 30:
        bmi_status = "Overweight"
        recommendations.append(
            "Your BMI is above the normal range. "
            "Focus on balanced meals, portion control and regular exercise."
        )

    else:
        bmi_status = "Obese"
        recommendations.append(
            "Your BMI is in the obesity range. "
            "Consider gradual lifestyle changes and discuss your health goals with a healthcare professional."
        )


    # ==========================================
    # WATER INTAKE
    # ==========================================

    if water < 1.5:
        recommendations.append(
            "💧 Your water intake appears low. Try to drink water regularly throughout the day."
        )

    elif water < 2:
        recommendations.append(
            "💧 Your water intake is moderate. Increasing it gradually may help you stay well hydrated."
        )

    else:
        recommendations.append(
            "💧 Your water intake is good. Continue staying hydrated throughout the day."
        )


    # ==========================================
    # SLEEP
    # ==========================================

    if sleep < 6:
        recommendations.append(
            "😴 You are getting less sleep than recommended for most adults. "
            "Try to maintain a consistent sleep schedule."
        )

    elif sleep < 7:
        recommendations.append(
            "😴 Your sleep duration is slightly low. Try to increase your regular sleep time."
        )

    elif sleep <= 9:
        recommendations.append(
            "😴 Your sleep duration is within a generally healthy range. Keep a consistent sleep routine."
        )

    else:
        recommendations.append(
            "😴 You are sleeping for a long duration. If you regularly feel unusually tired, consider discussing it with a healthcare professional."
        )


    # ==========================================
    # EXERCISE
    # ==========================================

    if exercise < 15:
        recommendations.append(
            "🏃 Your daily physical activity is low. Start with light walking or simple exercises and gradually increase activity."
        )

    elif exercise < 30:
        recommendations.append(
            "🏃 You are getting some physical activity. Try to gradually increase your active time."
        )

    else:
        recommendations.append(
            "🏃 Good job maintaining regular physical activity. Continue exercising safely and consistently."
        )


    # ==========================================
    # FOOD HABIT
    # ==========================================

    if food_habit == "healthy":

        recommendations.append(
            "🍎 Your food habit is marked as healthy. Continue eating a balanced variety of vegetables, fruits, protein and whole grains."
        )

    elif food_habit == "average":

        recommendations.append(
            "🍎 Your food habit is average. Try adding more fruits, vegetables, protein-rich foods and whole grains."
        )

    elif food_habit == "unhealthy":

        recommendations.append(
            "🍎 Consider reducing highly processed foods, excess sugar and fried foods. Choose more nutritious balanced meals."
        )


    # ==========================================
    # STRESS LEVEL
    # ==========================================

    if stress_level == "low":

        recommendations.append(
            "🧘 Your reported stress level is low. Continue healthy relaxation and self-care habits."
        )

    elif stress_level == "medium":

        recommendations.append(
            "🧘 Your reported stress level is moderate. Try relaxation techniques, regular activity and adequate sleep."
        )

    elif stress_level == "high":

        recommendations.append(
            "🧘 Your reported stress level is high. Consider relaxation practices and talking with a trusted person or qualified professional if it continues."
        )


    # ==========================================
    # SYMPTOM ANALYSIS
    # ==========================================

    if not symptoms:

        recommendations.append(
            "✅ No symptoms were selected. Continue regular preventive health habits and routine health check-ups."
        )


    # Heart & Chest

    if "chest_pain" in symptoms:

        recommendations.append(
            "❤️ Chest pain should not be ignored. If it is severe, sudden, persistent, or occurs with breathing difficulty, sweating or fainting, seek urgent medical care."
        )


    if "fast_heartbeat" in symptoms:

        recommendations.append(
            "❤️ Fast heartbeat can have different causes. Rest and monitor the symptom. If it is persistent or accompanied by chest pain, dizziness or breathing difficulty, seek medical care."
        )


    if "irregular_heartbeat" in symptoms:

        recommendations.append(
            "❤️ Irregular heartbeat may need medical evaluation, especially if it is recurrent or associated with dizziness, chest pain or fainting."
        )


    if "breathlessness" in symptoms:

        recommendations.append(
            "🫁 Shortness of breath can have several causes. If breathing difficulty is severe or sudden, seek urgent medical attention."
        )


    if "dizziness" in symptoms:

        recommendations.append(
            "🧠 Dizziness may occur due to dehydration, low blood pressure, lack of food or other causes. Sit or lie down safely and seek medical advice if it is severe or recurring."
        )


    if "excessive_sweating" in symptoms:

        recommendations.append(
            "💧 Excessive sweating can have several causes. Stay hydrated and seek medical advice if it is unexplained or occurs with chest pain or dizziness."
        )


    if "unusual_tiredness" in symptoms:

        recommendations.append(
            "😴 Persistent unusual tiredness may be related to sleep, nutrition, stress or other health conditions. If it continues, consider a medical check-up."
        )


    # Head & Brain

    if "headache" in symptoms:

        recommendations.append(
            "🧠 For mild headaches, maintain hydration, regular meals and adequate rest. Frequent or severe headaches should be discussed with a healthcare professional."
        )


    if "severe_headache" in symptoms:

        recommendations.append(
            "🧠 A severe or sudden headache should be taken seriously. Seek medical attention, especially if it is unusual or occurs with weakness, confusion or vision changes."
        )


    if "migraine" in symptoms:

        recommendations.append(
            "🧠 Migraine-like symptoms may improve with regular sleep, hydration and avoiding known triggers. Consult a healthcare professional for frequent attacks."
        )


    if "blurred_vision" in symptoms:

        recommendations.append(
            "👁️ Blurred vision should be evaluated if it is persistent, sudden or worsening."
        )


    if "difficulty_concentrating" in symptoms:

        recommendations.append(
            "🧠 Difficulty concentrating can be associated with poor sleep, stress, nutrition or other factors. Improve sleep and routine and seek advice if persistent."
        )


    if "fainting" in symptoms:

        recommendations.append(
            "⚠️ Fainting should be medically evaluated, especially if it is repeated or associated with chest pain, breathing difficulty or abnormal heartbeat."
        )


    # Hair & Scalp

    if "hair_fall" in symptoms:

        recommendations.append(
            "💇 Hair fall can be associated with stress, nutrition, hormonal changes or scalp conditions. Maintain adequate protein and a balanced diet and seek advice if persistent."
        )


    if "hair_thinning" in symptoms:

        recommendations.append(
            "💇 Hair thinning may have nutritional, hormonal or genetic causes. A healthcare professional can help identify the cause if it continues."
        )


    if "dandruff" in symptoms:

        recommendations.append(
            "💇 Regular scalp care and an appropriate anti-dandruff shampoo may help with dandruff. Seek medical advice for severe or persistent scalp problems."
        )


    if "itchy_scalp" in symptoms:

        recommendations.append(
            "💇 Avoid harsh hair products and maintain scalp hygiene. Persistent itching may need professional evaluation."
        )


    if "dry_scalp" in symptoms:

        recommendations.append(
            "💇 Use gentle hair-care products and avoid excessive hot-water washing if your scalp feels dry."
        )


    if "oily_scalp" in symptoms:

        recommendations.append(
            "💇 Maintain regular scalp hygiene and avoid excessive use of heavy hair products."
        )


    if "scalp_redness" in symptoms:

        recommendations.append(
            "💇 Scalp redness can occur with irritation or skin conditions. Seek medical advice if it persists or becomes painful."
        )


    # Stomach & Digestion

    if "stomach_pain" in symptoms:

        recommendations.append(
            "🥴 Stomach pain can have many causes. Maintain regular meals and avoid foods that clearly trigger discomfort. Seek medical care for severe or persistent pain."
        )


    if "acidity" in symptoms:

        recommendations.append(
            "🥗 For acidity, avoid very large meals and foods that trigger symptoms. Avoid lying down immediately after eating."
        )


    if "heartburn" in symptoms:

        recommendations.append(
            "🥗 Reduce foods that trigger heartburn and avoid lying down soon after meals. Frequent symptoms should be discussed with a healthcare professional."
        )


    if "nausea" in symptoms:

        recommendations.append(
            "🥴 For mild nausea, take small amounts of fluids and eat light meals. Seek medical advice if persistent or severe."
        )


    if "vomiting" in symptoms:

        recommendations.append(
            "🥴 Maintain fluid intake to reduce dehydration risk. Persistent vomiting or inability to keep fluids down requires medical attention."
        )


    if "bloating" in symptoms:

        recommendations.append(
            "🥗 Eat slowly, maintain hydration and identify foods that trigger bloating."
        )


    if "constipation" in symptoms:

        recommendations.append(
            "🥗 Increase fiber-rich foods, drink adequate fluids and maintain regular physical activity."
        )


    if "diarrhea" in symptoms:

        recommendations.append(
            "💧 Focus on replacing lost fluids. Seek medical care if diarrhea is severe, persistent or associated with signs of dehydration."
        )


    # Respiratory

    if "cough" in symptoms:

        recommendations.append(
            "🫁 Stay hydrated and rest. A persistent, severe or worsening cough should be evaluated by a healthcare professional."
        )


    if "cold" in symptoms:

        recommendations.append(
            "🫁 Rest, stay hydrated and maintain good hygiene. Seek medical advice if symptoms are severe or persistent."
        )


    if "wheezing" in symptoms:

        recommendations.append(
            "🫁 Wheezing can be related to airway problems. Seek medical advice if it is new, persistent or associated with breathing difficulty."
        )


    if "breathing_difficulty" in symptoms:

        recommendations.append(
            "⚠️ Breathing difficulty can be serious. If it is severe or sudden, seek urgent medical care."
        )


    if "sore_throat" in symptoms:

        recommendations.append(
            "🫁 Stay hydrated and use warm fluids for comfort. Seek medical advice if symptoms are severe or persistent."
        )


    if "chest_congestion" in symptoms:

        recommendations.append(
            "🫁 Stay hydrated and rest. Persistent chest congestion or breathing difficulty should be medically evaluated."
        )


    if "runny_nose" in symptoms:

        recommendations.append(
            "🫁 Rest, maintain hydration and practice good hygiene. Seek advice if symptoms persist or worsen."
        )


    # General Health

    if "fever" in symptoms:

        recommendations.append(
            "🌡️ Monitor your temperature, rest and stay hydrated. Seek medical care for high, persistent or worsening fever."
        )


    if "fatigue" in symptoms:

        recommendations.append(
            "😴 Maintain adequate sleep, balanced nutrition, hydration and regular light activity. Persistent fatigue may need medical evaluation."
        )


    if "weakness" in symptoms:

        recommendations.append(
            "💪 Maintain regular meals, hydration and adequate rest. Persistent or severe weakness should be evaluated."
        )


    if "body_pain" in symptoms:

        recommendations.append(
            "💪 Rest, stay hydrated and use gentle movement if comfortable. Persistent or severe body pain should be evaluated."
        )


    if "chills" in symptoms:

        recommendations.append(
            "🌡️ Chills can occur with infections or other conditions. Monitor your temperature and seek medical advice if symptoms persist."
        )


    if "loss_of_appetite" in symptoms:

        recommendations.append(
            "🍎 Try small, nutritious meals and maintain hydration. Persistent loss of appetite should be discussed with a healthcare professional."
        )


    if "dehydration" in symptoms:

        recommendations.append(
            "💧 Increase fluids gradually and monitor for signs of dehydration. Severe dehydration requires medical attention."
        )


    # Women's Health

    if "irregular_periods" in symptoms:

        recommendations.append(
            "🌸 Irregular periods can have several causes including stress, hormonal changes and other conditions. Consider discussing persistent changes with a healthcare professional."
        )


    if "period_pain" in symptoms:

        recommendations.append(
            "🌸 Mild period discomfort may improve with rest and gentle heat. Severe or unusual pain should be evaluated."
        )


    if "heavy_periods" in symptoms:

        recommendations.append(
            "🌸 Heavy menstrual bleeding can sometimes contribute to anemia. Consider medical evaluation if bleeding is unusually heavy or persistent."
        )


    if "acne" in symptoms:

        recommendations.append(
            "🌸 Maintain gentle skin care and avoid repeatedly touching or squeezing acne. Persistent acne may benefit from professional advice."
        )


    if "excess_facial_hair" in symptoms:

        recommendations.append(
            "🌸 Excess facial hair can have different causes, including hormonal factors. Consider professional evaluation if it is new or increasing."
        )


    if "weight_changes" in symptoms:

        recommendations.append(
            "🌸 Unexplained weight changes may have several causes. Maintain regular meals and consider medical evaluation if the change is significant or persistent."
        )


    if "pelvic_discomfort" in symptoms:

        recommendations.append(
            "🌸 Persistent or significant pelvic discomfort should be evaluated by a healthcare professional."
        )


    # Sleep & Stress

    if "stress" in symptoms:

        recommendations.append(
            "🧘 Try breathing exercises, regular physical activity, adequate sleep and relaxation techniques to manage stress."
        )


    if "anxiety" in symptoms:

        recommendations.append(
            "🧘 Relaxation techniques, regular activity and a consistent sleep routine may help. If anxiety interferes with daily life, consider speaking with a qualified professional."
        )


    if "poor_sleep" in symptoms:

        recommendations.append(
            "😴 Maintain a consistent bedtime, reduce screen use before sleep and create a comfortable sleeping environment."
        )


    if "difficulty_sleeping" in symptoms:

        recommendations.append(
            "😴 Try a regular sleep schedule, limit caffeine late in the day and reduce screen exposure before bedtime."
        )


    if "daytime_sleepiness" in symptoms:

        recommendations.append(
            "😴 Daytime sleepiness can be related to insufficient or poor-quality sleep. If persistent despite adequate sleep, consider medical advice."
        )


    if "low_energy" in symptoms:

        recommendations.append(
            "⚡ Maintain regular meals, hydration, adequate sleep and physical activity. Persistent low energy should be evaluated."
        )


    # Muscle & Joint

    if "back_pain" in symptoms:

        recommendations.append(
            "🦴 Maintain good posture, avoid prolonged sitting and try gentle stretching if comfortable. Persistent or severe back pain needs evaluation."
        )


    if "neck_pain" in symptoms:

        recommendations.append(
            "🦴 Check your sitting and screen posture and take regular movement breaks. Persistent neck pain should be evaluated."
        )


    if "joint_pain" in symptoms:

        recommendations.append(
            "🦴 Gentle movement and maintaining a healthy weight may support joint health. Persistent or swollen joints should be medically evaluated."
        )


    if "muscle_cramps" in symptoms:

        recommendations.append(
            "🦴 Stay hydrated and maintain a balanced diet. Frequent or severe cramps should be discussed with a healthcare professional."
        )


    if "muscle_stiffness" in symptoms:

        recommendations.append(
            "🦴 Gentle stretching and regular movement may help reduce stiffness. Persistent stiffness should be evaluated."
        )


    if "leg_pain" in symptoms:

        recommendations.append(
            "🦴 Rest and avoid activities that worsen pain. Seek medical attention for severe, sudden or unexplained leg pain or swelling."
        )


    # Eye Health

    if "eye_strain" in symptoms:

        recommendations.append(
            "👁️ Follow regular screen breaks, adjust screen brightness and maintain a comfortable viewing distance."
        )


    if "dry_eyes" in symptoms:

        recommendations.append(
            "👁️ Take regular screen breaks and avoid direct air blowing toward your eyes. Persistent symptoms may need an eye examination."
        )


    if "red_eyes" in symptoms:

        recommendations.append(
            "👁️ Avoid rubbing your eyes and maintain good hygiene. Seek medical advice if redness is painful or affects vision."
        )


    if "watery_eyes" in symptoms:

        recommendations.append(
            "👁️ Watery eyes can have several causes. Avoid irritants and seek professional advice if persistent."
        )


    if "eye_discomfort" in symptoms:

        recommendations.append(
            "👁️ Reduce prolonged screen exposure and avoid rubbing the eyes. Persistent discomfort should be evaluated."
        )


    # Dental & Oral

    if "toothache" in symptoms:

        recommendations.append(
            "🦷 Maintain oral hygiene and arrange a dental check-up for persistent tooth pain."
        )


    if "gum_bleeding" in symptoms:

        recommendations.append(
            "🦷 Brush gently and maintain regular oral hygiene. Persistent gum bleeding should be checked by a dentist."
        )


    if "bad_breath" in symptoms:

        recommendations.append(
            "🦷 Brush twice daily, clean the tongue and maintain hydration. Persistent bad breath may require dental evaluation."
        )


    if "mouth_ulcers" in symptoms:

        recommendations.append(
            "🦷 Avoid irritating foods and maintain good oral hygiene. Persistent or recurrent ulcers should be evaluated."
        )


    if "tooth_sensitivity" in symptoms:

        recommendations.append(
            "🦷 Avoid very hot or cold foods if they trigger pain and consider a dental examination for persistent sensitivity."
        )


    if "swollen_gums" in symptoms:

        recommendations.append(
            "🦷 Maintain gentle oral hygiene and arrange a dental check-up if swelling persists."
        )


    # Skin Health

    if "skin_acne" in symptoms:

        recommendations.append(
            "🧴 Use gentle skin care, avoid squeezing acne and keep skin clean. Persistent acne may benefit from professional advice."
        )


    if "dry_skin" in symptoms:

        recommendations.append(
            "🧴 Use a gentle moisturizer regularly and avoid very hot showers if they worsen dryness."
        )


    if "skin_itching" in symptoms:

        recommendations.append(
            "🧴 Avoid scratching and use gentle skin products. Persistent or severe itching should be evaluated."
        )


    if "skin_rash" in symptoms:

        recommendations.append(
            "🧴 Avoid possible irritants and monitor the rash. Seek medical advice if it spreads, becomes severe or is accompanied by other concerning symptoms."
        )


    if "skin_redness" in symptoms:

        recommendations.append(
            "🧴 Use gentle skin products and avoid known irritants. Persistent redness should be professionally evaluated."
        )


    if "skin_irritation" in symptoms:

        recommendations.append(
            "🧴 Stop using products that appear to trigger irritation and use gentle skin care. Seek advice if irritation persists."
        )


    # ==========================================
    # FINAL RESULT
    # ==========================================

    return bmi, bmi_status, recommendations