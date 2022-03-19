class App:
  # The __init__.py files are required to make Python treat directories containing the file as packages.
  # This prevents directories with a common name, such as string , unintentionally hiding valid modules that occur later on the module search path.
  def __init__(self):
      pass

  __conf = {

    ################################################################################
    # Contour Calculator General Data Configuration
    ################################################################################

    "basedir" : "C:/Users/sense/Documents/Erick",

    ################################################################################
    # Contour Calculator Download Data Configuration
    ################################################################################

    "start_year" : 2008,
    "start_month" : 1,
    "start_day" : 1,

    "end_year": 2008,
    "end_month": 2,
    "end_day": 1,

    "interval" : "8D",

    ################################################################################
    # Contour Calculator Clip Extent Configuration
    ################################################################################

    "lonmin" : -78.406919866,
    "latmin" : 39.203467563,
    "lonmax" : -72.231671993,
    "latmax" : 33.402477136,

    ################################################################################
    # Contour Calculator Filter Pixels Configuration
    ################################################################################

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