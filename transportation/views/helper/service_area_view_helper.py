from shapely.geometry import shape, Point


def coord_in_polygon(coord, geojson):
    """
    This function take a lat/lng coord and GeoJson polygon info
    return True if polygon that include the given coord, else False
    """
    pt = Point(coord[0], coord[1])
    for feature in geojson['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(pt):
            return True
    return False
