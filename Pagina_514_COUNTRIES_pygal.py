#from pygal.i18n import population_data

from pygal_maps_world import i18n
#import pygal.maps.world.COUNTRIES
from pygal_maps_world.i18n import COUNTRIES

"""
The i18n module was removed in pygal-2.0.0, however, it can now be found in the pygal_maps_world plugin.

You can install that with pip install pygal_maps_world. Then you can access COUNTRIES as pygal.maps.world.COUNTRIES:

from pygal.maps.world import COUNTRIES
Whats left of the i18n module can be imported with:

from pygal_maps_world import i18n

"""
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
