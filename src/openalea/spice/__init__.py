from openalea.spice import *
try:
    from .libspice_core import *
except ImportError:
    try:
        from .spice_core import *
    except ImportError:
        print("Could not import spice_core c++ library")
