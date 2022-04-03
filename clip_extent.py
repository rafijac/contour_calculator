import os

# from osgeo import gdal

from config import App
# uri = 'NETCDF:"C:/Users/Rafi/Downloads/A20060012006008.L3m_8D_CHL_chlor_a_9km.nc":chlor_a'


def clip_extent(extent, file, basedir, netcdf_dir):
    file_name = file[0:15]

    cmnd = "gdal_translate   "
    flags = "-projwin  "
    extent = "{} {} {} {}  ".format(extent[0], extent[1], extent[2], extent[3])
    flag_and_file_type = "-of GTiff \"NETCDF:"
    nc_file_loc = '"""' + netcdf_dir + "/" + file + ' """'
    data_type = "chlor_a  "
    save_location = '"  ' +  netcdf_dir + "/" + file_name + "_check.tif" + '"  '

    clip_gdal_cmd = cmnd + flags + extent + flag_and_file_type + nc_file_loc + ":" + data_type + save_location

    # clip_gdal_cmd = gdal.Translate(cmnd + flags + extent + flag_and_file_type + nc_file_loc + ":" + data_type + save_location)
    os.system(clip_gdal_cmd)
    check = 10

# ##gdal command from qgis
#  gdal_translate -projwin -59.108109779 35.027020388 -5.108108252 -15.324332387 -of GTiff  "NETCDF:"""C:\Users\Rafi\Downloads\A20030092003016.L3m_8D_CHL_chlor_a_4km.nc""":chlor_a" C:\Users\Rafi\Downloads\fdsa.tif


# This function can be used as a staging area to see if the function above works
def main():
    
    cmnd = "gdal_translate "
    flags = "-projwin "
    extent = "-59.108109779 35.027020388 -5.108108252 -15.324332387 "
    flag_and_file_type = "-of GTiff \"NETCDF:"
    nc_file_loc = r'"""' + r"C:\Users\Rafi\Downloads\A20030092003016.L3m_8D_CHL_chlor_a_4km.nc" + r' """'
    data_type = "chlor_a" + '" '
    save_location = r"C:\Users\Rafi\Downloads\checkeroo.tif"

    clip_gdal_cmd = cmnd + flags + extent + flag_and_file_type + nc_file_loc + ":" + data_type + save_location
    
    os.system(clip_gdal_cmd)


if __name__ == "__main__":
    main()
# gdal_translate -projwin -59.108109779 35.027020388 -5.108108252 -15.324332387 -of GTiff "NETCDF:"""C:/Users/Rafi/Downloads/A20030092003016.L3m_8D_CHL_chlor_a_4km.nc""":chlor_a " C:/Users/Rafi/Downloads/check.tif"