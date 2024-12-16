from openalea.spice import *

try:
    from openalea.spice.libspice_core import *
except ImportError:
    try:
        from openalea.spice.spice_core import *
    except ImportError:
        print("Could not import spice_core c++ library")
