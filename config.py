
class App:
  # The __init__.py files are required to make Python treat directories containing the file as packages.
  # This prevents directories with a common name, such as string , unintentionally hiding valid modules that occur later on the module search path.
  def __init__(self):
      pass

  __conf = {
    # TODO add chlor_a as a config

    ################################################################################
    # Contour Calculator General Data Configuration
    ################################################################################
    # todo change name to more general i.e  download location
    "basedir" : "C:/Users/Rafi/Erick/netcdf_files",
    "netcdf_files" : "C:/Users/Rafi/Erick/netcdf_files",

    ################################################################################
    # Contour Calculator Download Data Configuration
    ################################################################################

    "start_year" : 2008,
    "start_month" : 1,
    "start_day" : 1,

    "end_year": 2008,
    "end_month": 2,
    "end_day": 1,

    # 8 days e.g. -- 8D = 8 days ....
    # todo reference for different options
    "interval" : "8D",

    ################################################################################
    # Contour Calculator Clip Extent Configuration
    ################################################################################

    # left bottom
    "lonmin" : -78.406919866,
    "latmin" : 39.203467563,

    # right top
    "lonmax" : -72.231671993,
    "latmax" : 33.402477136,

    ################################################################################
    # Contour Calculator Filter Pixels Configuration
    ################################################################################

    # todo break it up based on names pixel threshold / formula put formula in script. here all need is threshold
    "pixel_filter_range" : "A * (A >= 2.5)"

  }

  # HERE IS THE IMPLEMENTATION OF SETTER IF WE NEED
  # __setters = ["username", "password"]

  # __setters = ["username", "password"]
  #
  @staticmethod
  def config(name):
    return App.__conf[name]

  # @staticmethod
  # def set(name, value):
  #   if name in App.__setters:
  #     App.__conf[name] = value
  #   else:
  #     raise NameError("Name not accepted in set() method")

  # AND HERE IS HOW IT WOULD BE USED
  # if __name__ == "__main__":
  #    # from config import App
  #    App.config("MYSQL_PORT")     # return 3306
  #    App.set("username", "hi")    # set new username value
  #    App.config("username")       # return "hi"
  #    App.set("MYSQL_PORT", "abc") # this raises NameError