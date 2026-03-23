[pyserde](https://github.com/yukinarit/pyserde) extension for `zoneinfo.ZoneInfo`.

```python
import serde_timedelta
from serde import serde
from serde.json import to_json, from_json
from zoneinfo import ZoneInfo

# Initialize serde_zoneinfo extension.
serde_zoneinfo.init()


@serde
class Foo:
    a: ZoneInfo


f = Foo(ZoneInfo("America/New_York"))
json = to_json(f)
print(json)                  # Prints '{"a": "America/New_York"}'
print(from_json(Foo, json))  # Prints Foo(a=ZoneInfo(key='America/New_York'))
```
