import unittest

def design_bolted_lap_joint(P, w, t1, t2, bolt_diameter, material_grade):
    if P <= 0 or bolt_diameter <= 0:
        raise ValueError("Force and bolt diameter must be positive values.")
    
    load_per_bolt = 10000
    
    num_bolts = round(P * 1e3 / load_per_bolt, 0)
    
    return {
        "Number of bolts": num_bolts,
        "Bolt diameter": bolt_diameter,
        "Strength of connection": P * 1e3,
        "Material grade": material_grade
    }

class TestBoltedLapJoint(unittest.TestCase):
    
    def test_bolted_lap_joint_valid_1(self):
        result = design_bolted_lap_joint(50, 200, 10, 10, 12, "E250")
        self.assertEqual(result, {
            "Number of bolts": 5.0,
            "Bolt diameter": 12,
            "Strength of connection": 50000.0,
            "Material grade": "E250"
        })

    def test_bolted_lap_joint_valid_2(self):
        result = design_bolted_lap_joint(100, 250, 12, 10, 16, "E275")
        self.assertEqual(result, {
            "Number of bolts": 10.0,
            "Bolt diameter": 16,
            "Strength of connection": 100000.0,
            "Material grade": "E275"
        })
    
    def test_bolted_lap_joint_invalid_force(self):
        with self.assertRaises(ValueError):
            design_bolted_lap_joint(-50, 200, 10, 10, 12, "E250")
    
    def test_bolted_lap_joint_invalid_bolt_diameter(self):
        with self.assertRaises(ValueError):
            design_bolted_lap_joint(50, 200, 10, 10, 0, "E250")
    
    def test_bolted_lap_joint_edge_case(self):
        result = design_bolted_lap_joint(1, 200, 10, 10, 6, "E300")
        self.assertEqual(result, {
            "Number of bolts": 0.0,
            "Bolt diameter": 6,
            "Strength of connection": 1000.0,
            "Material grade": "E300"
        })

if __name__ == "__main__":
    unittest.main()
