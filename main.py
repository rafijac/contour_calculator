import os.path
from datetime import date

import clip_extent
import config
import download_data
import filter_pixels
from pathlib import Path

import pass_data_qgis

import config



# # TODO delete. want to transition to single file execution
# extent_dir = os.path.join(basedir, "extent_files")


# # TODO delete. want to transition to single file execution
# pixel_filter_dir = os.path.join(basedir, "pixel_filter_files")

################################################################################
# 1. Download Data
################################################################################
netcdf_diR = (config.App.config("netcdf_files"))

basediR = (config.App.config("basedir"))

start_date = date(config.App.config("start_year"), config.App.config("start_month"), config.App.config("start_day"))
end_date = date(config.App.config("end_year"), config.App.config("end_month"), config.App.config("end_day"))
interval = config.App.config("interval")


# download_data.download_data(start_date, end_date, interval, netcdf_dir)

# # pass_data_qgis.pass_data_qgis(netcdf_dir)
# #todo fix looping
for file in os.listdir((netcdf_diR)):
#     ################################################################################
#     # 2. Clip Extent
#     ################################################################################

    extent = [config.App.config("lonmin"), config.App.config("latmin"), config.App.config("lonmax"),config.App.config("latmax") ]
    clip_extent.clip_extent(extent=extent, file=file, basedir=basediR,  netcdf_dir=netcdf_diR)

#     ################################################################################
#     # 3. Filter Pixels
#     ################################################################################

#     # filter_pixels.filter_pixels(App.config("pixel_filter_range"), extent_dir, pixel_filter_dir)
