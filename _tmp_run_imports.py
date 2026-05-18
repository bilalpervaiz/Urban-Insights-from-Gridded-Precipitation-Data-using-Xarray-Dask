import os, sys, traceback
os.environ.pop("MPLBACKEND", None)
try:
    import pandas as pd
    import geopandas as gpd
    import xarray as xr
    import numpy as np
    import xagg
    import matplotlib
    import seaborn as sns
    import plotly.express as px
    from tqdm.notebook import tqdm
    print("OK")
    print("pandas", pd.__version__)
    print("geopandas", gpd.__version__)
    print("xarray", xr.__version__)
    print("numpy", np.__version__)
    print("matplotlib", matplotlib.__version__)
    print("seaborn", sns.__version__)
    print("plotly", px.__version__)
except Exception:
    traceback.print_exc()
    sys.exit(1)
