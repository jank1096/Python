from datetime import datetime
from zoneinfo import ZoneInfo

anruf_berlin = datetime(2026, 12, 24, 10, 0, tzinfo=ZoneInfo("Europe/Berlin"))

anruf_tokyo = anruf_berlin.astimezone(ZoneInfo("Asia/Tokyo"))

print(f"""
Du rufst an am:                {anruf_berlin.strftime('%d.%m.%Y um %H:%M Uhr')} (Berlin)
Bei deinem Freund in Tokyo:    {anruf_tokyo.strftime('%H:%M Uhr')}
""")
