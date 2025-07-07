import unittest

from app.model_utils import load_model, predict_risk


class TestModelPredictions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_model("model/heart_atk_model_latest.sav")

    def test_prediction_cases(self):
        test_data = [
            {
                "thalachh": 157.00,
                "exng": 0,
                "oldpeak": 1.6,
                "expected_pred": 1,
                "expected_result": "more chance of heart attack",
            },
            {
                "thalachh": 123.00,
                "exng": 0,
                "oldpeak": 0.6,
                "expected_pred": 1,
                "expected_result": "more chance of heart attack",
            },
            {
                "thalachh": 154.00,
                "exng": 0,
                "oldpeak": 4.0,
                "expected_pred": 0,
                "expected_result": "less chance of heart attack",
            },
        ]

        for case in test_data:
            with self.subTest(input=case):
                input_data = {
                    "thalachh": case["thalachh"],
                    "exng": case["exng"],
                    "oldpeak": case["oldpeak"],
                }
                pred, result = predict_risk(self.model, input_data)
                self.assertEqual(pred, case["expected_pred"])
                self.assertEqual(result, case["expected_result"])


if __name__ == "__main__":
    unittest.main()
