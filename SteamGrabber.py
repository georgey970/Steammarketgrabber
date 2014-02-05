# Steam Market Grabber
# Written by georgey970 and TronLaser

# Uses https://github.com/smiley/steamapi
# Uses https://pypi.python.org/pypi/requests

import steamapi
import ConfigParser

config = ConfigParser.ConfigParser()
apikey = config.get('api', 'key')
