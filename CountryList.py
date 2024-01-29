import pycountry, pytz
from datetime import datetime as DT , timezone as TZ, timedelta as TD

async def CountryList():
	CountryList = []
	for country in pycountry.countries:
		timezones = pytz.country_timezones.get(country.alpha_2)
		if timezones:
			for timezone in timezones:
				offset = DT.now(pytz.timezone(timezone)).strftime("%z")
				offset = f"{offset[:-2]}:{offset[-2:]}"
				_data = {
					"code": country.alpha_2,
					"name": country.name,
					"offset": offset,
					"timezone": timezone,
				}
				CountryList.append(_data)
			else:
				pass
			return CountryList
