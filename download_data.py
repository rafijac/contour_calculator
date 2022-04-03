import os
from datetime import date

url = 'https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/Mapped/8-Day/9km/chlor_a/'

# todo make generic for different os and add overaly to tell the difference
def download_data(start_date, end_date, interval, netcdf_dir):
    # https://gist.github.com/aolinto/1a54c5d35b5f1bc5f96a4f363a64956f
    cmd = """wget -q --post-data="sensor=aqua&sdate={}&edate={}8&dtype=L3m&addurl=1&results_as_file=1&search=A*L3m_{}_CHL_chlor_a_4km.nc" -O - https://oceandata.sci.gsfc.nasa.gov/api/file_search \
    |wget --directory-prefix={} -i -""".format(start_date, end_date, interval, netcdf_dir)
    os.system(cmd)


#################################################################################################################
#                           FROM HERE ON WAS THE OLD WAY OF BUILDING FILE NAMES WITHOUT USING WGET
#################################################################################################################

def round_nearest_eight(x):
    return (x + 7) & (-8)


def build_file_names(start_date, end_date):
    # A20060012006008.L3m_8D_CHL_chlor_a_9km.nc
    # A20060092006016.L3m_8D_CHL_chlor_a_9km.nc
    # A20060172006024.L3m_8D_CHL_chlor_a_9km.nc
    # A20070012007008.L3m_8D_CHL_chlor_a_9km.nc

    res = []

    # account for dates crossing years
    for i in range(start_date.year, end_date.year + 1):
        first_day_of_year = date(i, 1, 1)
        last_day_of_year = date(i, 12, 31)

        if i == start_date.year and i == last_day_of_year:
            iterate_year(start_date, end_date, res)
        elif i == start_date.year:
            iterate_year(start_date, last_day_of_year, res)
        elif i == end_date.year:
            iterate_year(first_day_of_year, end_date, res)
        elif i != start_date.year and i != last_day_of_year:
            iterate_year(first_day_of_year, last_day_of_year, res)

    return res


def iterate_year(start_date, end_date, res):
    interval = (end_date - start_date).days

    start = start_date.timetuple().tm_yday
    # iterate the total amount of days by 8
    # the number as to start from the nearest multiple of 8
    for i in range(round_nearest_eight(start), round_nearest_eight(start + interval) + 1, 8):
        # fill number
        index = (str(i).zfill(3))
        number = (str(i - 7).zfill(3))
        # for some reason last number ends by 5 and not 8
        if (index == "368"):
            index = "365"
        current_name = """{}/A{}{}{}{}.L3m_8D_CHL_chlor_a_9km.nc""".format(start_date.year, start_date.year, number,
                                                                           end_date.year, index)
        res.append(current_name)

    return



