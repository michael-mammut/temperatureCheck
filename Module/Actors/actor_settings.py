from datetime import datetime

ACTOR_SETTINGS = [
    {"GPIO": 22, "ON": datetime.strptime('11:00', '%H:%M'), "OFF": datetime.strptime('14:00', '%H:%M')},
    {"GPIO": 18, "ON": datetime.strptime('15:00', '%H:%M'), "OFF": datetime.strptime('18:00', '%H:%M')}
]
