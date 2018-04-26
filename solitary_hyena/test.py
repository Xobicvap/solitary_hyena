from loader.loader import Loader
import os

lo = Loader("projects", ".yml", os.path.realpath(__file__))
files = lo.load_files()
