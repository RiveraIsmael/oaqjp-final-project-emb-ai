import unittest
from app import app  # Import your Flask app
import json

class EmotionDetectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()  # Flask test client
        self.app.testing = True

    def test_analyze_emotions_valid_text(self):
        # Send valid text for analysis
        response = self.app.post('/analyze', 
                                 data=json.dumps({'text': 'I love this product!'}), 
                                 content_type='application/json')
         # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if emotions are in the response
        response_json = json.loads(response.data)
        self.assertIn('emotions', response_json)
        self.assertGreater(len(response_json['emotions']), 0)

    def test_analyze_emotions_no_text(self):
        # Send request without text
        response = self.app.post('/analyze', 
                                 data=json.dumps({'text': ''}), 
                                 content_type='application/json')

        # Check if the response returns an error (status code 400)
        self.assertEqual(response.status_code, 400)
        response_json = json.loads(response.data)
        self.assertIn('error', response_json)

if __name__ == "__main__":
    unittest.main()
