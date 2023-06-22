# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_ga6")

# populate package namespace
from pycounts_ga6.pycounts_ga6 import count_words
from pycounts_ga6.plotting import plot_words
