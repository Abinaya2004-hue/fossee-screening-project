Design of a welded Lap Joint
 [Abinaya D]
 December 7, 2024
 1 Introduction
 In structural engineering, bolted lap joints are commonly used to connect
 two plates in various load-bearing applications. The design of these joints
 must adhere to relevant standards and ensure that the connection is both
 efficient and safe. This report details the design of a bolted lap joint as per
 IS 800:2007, which provides guidelines for the general construction of steel
 structures.
 2 Problem Statement
 The goal of this project is to design a bolted lap joint that connects two plates
 of specific thicknesses and width, subjected to a known tensile force. The de
sign should be performed in accordance with IS 800:2007 standards, focusing
 on selecting appropriate bolt diameters, bolt grades, and plate grades, while
 ensuring that the joint is both efficient and meets safety requirements.
 The design problem is defined with the following parameters:
 • Plate Width (w): Width of the plates in mm.
 • Plate Thicknesses (t1,t2): Thickness of the two plates in mm.
 • Tensile Force (P): Applied tensile force in kN.
 2.1 Objective
 Develop an algorithm to design a bolted lap joint that meets the following
 requirements:
 • Select a bolt diameter d from a list of available bolts: {10, 12, 16, 20,
 24} mm.
 1
• Choose a bolt grade GB from a list of available grades: {3.6, 4.6, 4.8,
 5.6, 5.8}.
 • Choose a steel plate grade GP from a list of available grades: {“E250”,
 “E275”, “E300”, “E350”, “E410”}.
 • Calculate the yield strength and ultimate strength of the plate and bolt
 based on their grades.
 • Find the most efficient connection with the least number of bolts, en
suring more than two bolts are used.
 • Calculate pitch, gauge, end, and edge distances.
 • Ensure the utilization ratio is close to 1.
 • The length of the connection should be minimal.
 • Detail distances should be in round figures as far as possible.
 • The strength of the connection should exceed the tensile strength of
 the plate.
 • Ensure the design complies with IS 800:2007 standards.
 3 Methodology
 The design process involves several steps to ensure the lap joint meets all
 requirements:
 1. Input Parameters: Receive the values for the tensile force, plate
 width, and thicknesses.
 2. Material Selection: Choose appropriate initial bolt and plate grades,
 and determine their mechanical properties.
 3. Bolt Strength Calculation: Compute the ultimate tensile strength
 and yield strength of the bolts.
 4. Design Calculation: Determine the number of bolts required and the
 corresponding distances based on standard practices.
 5. Check Compliance: Ensure that the designed joint meets all IS
 800:2007 requirements and the utilization ratio is close to 1.
 6. Optimize Design: Select the design with the minimal number of bolts
 while ensuring efficiency and safety.
 2
4 Design Calculations
 The calculations are performed using the following equations and considera
tions:
 4.1 Python Code for Lap Joint Design
 The following Python code snippet illustrates how the lap joint is designed:
 1 plate_grades = {"E250": 250, "E275": 275, "E300": 300, "E350"
 : 350, "E410": 410}
 2
 3 def design_lap_joint(P, w, t1, t2, g1, g2):
 4
 P, fy1, fy2 = P * 1e3, plate_grades[g1], plate_grades[g2]

 plate_strength = min(fy1 * t1, fy2 * t2) * w * 1e-3
 weld_size = math.ceil(P / (410 * w * 0.707))
 length = round(P / (410 * 0.707 * weld_size * 1e-3),-1)
 return {
 "Size of weld": weld_size,
 "Grade of weld material": "E410",
 "Length of weld": length,
 "Strength of connection": P,
 "Yield strengths of plates 1 and 2": (fy1, fy2),
 "Length of connection": length,
 "Efficiency of connection": round(P / plate_strength,
 2),
 }
 18 result = design_lap_joint(100, 200, 12, 10, "E250", "E275")
 19 for key, value in result.items():
 20
 print(f"{key}: {value}")
 Listing 1: Python Code for Lap Joint Design
 5 Expected Outcomes
 The final design should include:
 • Bolt Diameter (d)
 • Bolt Grade (GB)
 • Number of Bolts (Nb)
 • Pitch Distance (p)
 • Gauge Distance (g)
 
