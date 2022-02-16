import os

# from qgis.core import *
def pass_data_qgis(basedir):
    for file in os.listdir(basedir):
        rlayer = QgsRasterLayer(file, 'temp')
        if not rlayer.isValid():
            return
