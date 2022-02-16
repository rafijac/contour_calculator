import os
# uri = 'NETCDF:"C:/Users/Rafi/Downloads/A20060012006008.L3m_8D_CHL_chlor_a_9km.nc":chlor_a'


def clip_extent(extent, netcdf_dir, extent_dir, data_type):
    for file in os.listdir(netcdf_dir):
        file_name = file[0:15]
        gdalCmd = (""" gdal_translate -projwin\
        {} {} {} {} \
        -of GTiff\
        """.format(extent[0], extent[1], extent[2], extent[3])\
        + '"' + netcdf_dir + '\\' + file + '":' + data_type +
         """\
        \{}\{}_extent.tif\
        """.format(extent_dir, file_name))
        os.system(gdalCmd)
