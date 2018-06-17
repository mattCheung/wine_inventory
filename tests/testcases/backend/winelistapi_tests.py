import time

from framework.test_base import RESTTests


class WineListAPITests(RESTTests):
    route = 'wine_list/api/v1.0/winelist'

    def setUp(self):
        super().setUp()
        self.wine_id = None

    # TODO: Need to ensure prepopulation of data in DB
    def test_get_winelist(self):
        """
        Test to make sure GET call works for WineListApi
        """
        response = self.client.Get(route=self.route)
        self.assertEqual(200, response.status_code)

    def tearDown_post_winelist(self):
        """
        Runs specific teardown actions for test_post_winelist
        :return:
        """
        full_route = '{0}/{1}'.format(self.route, self.wine_id)
        self.client.Delete(route=full_route)

    def test_post_winelist(self):
        """
        Test to make sure POST will add the new wine data
        """
        wine_data = {
            'year': 1996,
            'type': 'experimental',
            'winery': 'no name',
            'name': 'experiment',
            'notes': 'foobar'
        }
        exists = False

        before = self.client.Get(route=self.route)
        before_count = len(before.json()['wine'])
        response = self.client.Post(route=self.route, json=wine_data)
        self.assertEqual(201, response.status_code, 'Was expecting 201, but got {0}'
                         .format(response.status_code))
        self.wine_id = response.json()['wine']['_id']
        after = self.client.Get(route=self.route)
        self.assertTrue(len(after.json()['wine']) > before_count)
        for wine in after.json()['wine']:
            if wine['_id'] == self.wine_id:
                exists = True
                break
        self.assertTrue(exists)
