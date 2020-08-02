from datetime import datetime

ACTOR_SETTINGS = [
    {"GPIO": 18, "ON": datetime.strptime('11:00', '%H:%M'), "OFF": datetime.strptime('12:00', '%H:%M')},
    {"GPIO": 23, "ON": datetime.strptime('14:00', '%H:%M'), "OFF": datetime.strptime('15:00', '%H:%M')}
]
