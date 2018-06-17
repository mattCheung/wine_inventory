import time
import json

from framework.test_base import RESTTests


class WineAPITests(RESTTests):
    route = 'wine_list/api/v1.0/winelist'
    post_route = 'wine_list/api/v1.0/winelist'

    def setUp(self):
        super().setUp()
        self.wine_id = None
        self.wine_data = {
            'year': 1996,
            'type': 'experimental',
            'winery': 'no name',
            'name': 'experiment',
            'notes': self.test_case_id
        }
        self.RunTestCaseSpecificSetup()

    def add_wine(self):
        """
        Adds a wine to DB
        """
        response = self.client.Post(route=self.post_route, json=self.wine_data)
        if response.status_code == 201:
            self.wine_id = response.json()['wine']['_id']
        else:
            # TODO: Need to figure out something better, this should not be treated as failure
            self.fail('Could not insert wine!, response code is {0}'.format(response.status_code))

    def delete_wine(self):
        """
        Deletes wine added from custom setUps
        """
        full_route = '{0}/{1}'.format(self.route, self.wine_id)
        self.client.Delete(route=full_route)

    def setUp_get_wine(self):
        self.add_wine()

    def tearDown_get_wine(self):
        self.delete_wine()

    def test_get_wine(self):
        """
        Test to make sure GET works

        Also tests out WineListAPI's INSERT as well
        """
        full_route = '{0}/{1}'.format(self.route, self.wine_id)

        response = self.client.Get(route=full_route)
        self.assertEqual(200, response.status_code)
        wine = response.json()['wine']
        self.assertEqual(wine['year'], self.wine_data['year'])
        self.assertEqual(wine['type'], self.wine_data['type'])
        self.assertEqual(wine['winery'], self.wine_data['winery'])
        self.assertEqual(wine['name'], self.wine_data['name'])
        self.assertEqual(wine['notes'], self.wine_data['notes'])

    def test_get_nonexistant_wine(self):
        """
        Test to make sure GET on nonexistant wine returns error
        """
        full_route = '{0}/idonotexist'.format(self.route)
        response = self.client.Get(route=full_route)
        self.assertEqual(404, response.status_code)

    def setUp_patch_wine(self):
        """
        Does custom setup for test_patch_wine
        """
        self.add_wine()

    def tearDown_patch_wine(self):
        """
        Cleans up after test_patch_wine
        """
        self.delete_wine()

    def test_patch_wine(self):
        """
        Test to make sure PATCH works
        """
        modified_wine_data = {
            'year': 2010,
            'type': 'new experimental',
            'winery': 'has a name',
            'name': 'another experiment',
            'notes': 'woo hoo!',
            'quantity': 99,
            'tags': []
        }
        modified_wine_data_sorted = json.dumps(modified_wine_data, sort_keys=True, indent=2)
        full_route = '{0}/{1}'.format(self.route, self.wine_id)
        response = self.client.Get(route=full_route)
        self.assertEqual(200, response.status_code)
        response_json = response.json()['wine']
        del response_json['_id']
        original_sorted = json.dumps(response_json, sort_keys=True, indent=2)
        response = self.client.Patch(route=full_route, json=modified_wine_data)
        self.assertEqual(200, response.status_code)
        response_json = response.json()['wine']
        del response_json['_id']
        modified_sorted = json.dumps(response_json, sort_keys=True, indent=2)
        self.assertEqual(modified_sorted, modified_wine_data_sorted)
        self.assertNotEqual(original_sorted, modified_sorted)

    def setUp_delete_wine(self):
        """
        Does custom setup for test_delete_wine
        """
        self.add_wine()

    def test_delete_wine(self):
        """
        Test to make sure DELETE works
        """
        full_route = '{0}/{1}'.format(self.route, self.wine_id)
        response = self.client.Get(route=full_route)
        self.assertEqual(200, response.status_code)
        response = self.client.Delete(route=full_route)
        self.assertEqual(200, response.status_code)
        response = self.client.Get(route=full_route)
        self.assertEqual(404, response.status_code)

    def test_delete_nonexistant_wine(self):
        """
        Test to make sure error returned when DELETE a non-existing wine
        """
        full_route = '{0}/idotexistsothisshouldfail'.format(self.route)
        response = self.client.Delete(route=full_route)
        self.assertEqual(404, response.status_code)
