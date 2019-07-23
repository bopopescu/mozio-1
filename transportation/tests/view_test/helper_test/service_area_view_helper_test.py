from django.test import TestCase
from transportation.views.helper import coord_in_polygon


class ServiceAreaViewHelperTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.los_angeles_coord = [-118.286686, 34.033919]
        self.san_francisco_coord = [-122.446357, 37.752399]
        self.sf_geojson = {"type":"FeatureCollection","properties":{"kind":"state","state":"CA"},"features":[
                           {"type":"Feature","properties":{"kind":"county","name":"San Francisco","state":"CA"},
                           "geometry":{"type":"MultiPolygon","coordinates":[[[[-122.4281,37.7068],
                           [-122.5048,37.7068],[-122.5158,37.7835],[-122.4062,37.8108],[-122.3569,37.7287],
                           [-122.3898,37.7068]]]]}}]}

    def test_given_coord_in_polygon_will_pass(self):
        """Test coord is in the given GeoJson polygon."""
        self.assertTrue(coord_in_polygon(self.san_francisco_coord, self.sf_geojson))

    def test_given_coord_in_polygon_will_fail(self):
        """Test coord is not in the given GeoJson polygon."""
        self.assertFalse(coord_in_polygon(self.los_angeles_coord, self.sf_geojson))
