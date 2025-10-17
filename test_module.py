import unittest
import demographic_data_analyzer
import pandas as pd

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_calculate_demographic_data(self):
        result = demographic_data_analyzer.calculate_demographic_data(False)

        self.assertAlmostEqual(result['average_age_men'], 39.4)
        self.assertAlmostEqual(result['percentage_bachelors'], 16.4)
        self.assertAlmostEqual(result['higher_education_rich'], 46.5)
        self.assertAlmostEqual(result['lower_education_rich'], 17.4)
        self.assertEqual(result['min_work_hours'], 1)
        self.assertAlmostEqual(result['rich_percentage'], 10.0)
        self.assertEqual(result['highest_earning_country'], 'Iran')
        self.assertAlmostEqual(result['highest_earning_country_percentage'], 41.9)
        self.assertEqual(result['top_IN_occupation'], 'Prof-specialty')

if __name__ == "__main__":
    unittest.main()
