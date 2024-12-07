import math
plate_grades = {"E250": 250, "E275": 275, "E300": 300, "E350": 350, "E410": 410}
def design_lap_joint(P, w, t1, t2, g1, g2):
    P, fy1, fy2 = P * 1e3, plate_grades[g1], plate_grades[g2]
    plate_strength = min(fy1 * t1, fy2 * t2) * w * 1e-3
    weld_size = math.ceil(P / (410 * w * 0.707))
    length = round(P / (410 * 0.707 * weld_size * 1e-3), -1)
    return {
        "Size of weld": weld_size,
        "Grade of weld material": "E410",
        "Length of weld": length,
        "Strength of connection": P,
        "Yield strengths of plates 1 and 2": (fy1, fy2),
        "Length of connection": length,
        "Efficiency of connection": round(P / plate_strength, 2),
    }

result = design_lap_joint(100, 200, 12, 10, "E250", "E275")
for key, value in result.items():
    print(f"{key}: {value}")
