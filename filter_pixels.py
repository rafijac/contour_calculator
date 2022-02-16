import os


def filter_pixels(pixel_filter_range, extent_dir, pixel_filter_dir):
    # script to use raster calc to identify shape
    for file in os.listdir(extent_dir):
        file_name = file[0:15]
        gdalCmd = """gdal_calc.bat --overwrite --calc\
        "{}" --format\
        GTiff --type\
        Float32 --NoDataValue\
        0.0 -A\
        {}{}.tif --A_band\
        1 --outfile\
        \{}\{}_rastered.tif""".format(pixel_filter_range, extent_dir, file, pixel_filter_dir, file_name)
        os.system(gdalCmd)

