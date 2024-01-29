# Python-Country-List
script for return country list by json format<br>
This is not for installation for the code.<br>
This code are write with python and modules with pytz and pycountry,<br>
check the usage for how to return the formate for you code.<br>
<br>
# Usage
This example are make for python modules.<br>
1. Save the ,py file for example name: `CountryList.py` and exapmle you code as 'run.py'<br>

```
import asyncio
from .CountryList import CountryList

async def main():
  ctyList = await CountryList()
  print(ctyList)

def main():
  ctyList = asyncio.run(CountryList())
  print(ctyList)
```

2. for example you can see our code are build with `async` in the function,<br>
so if you are useing 'def' in your `main.py` you need to add `asyncio` at the top like this.<br>
3. In the `CountryList.py`, you can config the return data as you need.<br>

```
_data = {
  "code": country.alpha_2,
  "name": country.name,
  "offset": offset,
  "timezone": timezone,
}
```

This is the part of `pycountry` return datas.<br>
it had already get timezone[Country/City], offset[+04:00], name[Country Name], code[CA,GB,FR...etc]<br>
as you need to change the return id also config it in `CountryList.py`<br>
<br>
It use the pytz for for faster short the offset formate, you can menu install by pip<br>
```python3 -m pip install -U pytz pycountry```<br>
Any cusntom API need with the modules, you can edit with you free!
