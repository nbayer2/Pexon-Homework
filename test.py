from app import Zertifizierungen

try:
    from app import app
    import unittest
    
except Exception as e:
    print('Some Modules are Missing {}'.format(e))

class FlaskTest(unittest.TestCase):
    # Check for response 200 in the / route
    def test_index(self):
       tester=app.test_client(self)
       response=tester.get('/')
       statuscode=response.status_code
       self.assertEqual(statuscode,200)

    # Check for response 200 in the /update route
    def test_update(self):
        tester=app.test_client(self)
        tester.post('/',data={'post': 'Azure5'}, follow_redirects=True)
        try:
            id = Zertifizierungen.query.first().id
        except:
            return print('Tehre are no objects to update')
        response=tester.get('/update/{}'.format(id), follow_redirects=True)
        statuscode=response.status_code
        self.assertTrue(b'Update Zertifizierung'in response.data)
        self.assertEqual(statuscode,200)

if __name__ == '__main__':
   unittest.main()