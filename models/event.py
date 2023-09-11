from datetime import datetime


class Event:
    def __init__(self, id: int, original_text: str, title: str, date: datetime, date_add: datetime, m_id: int = None,
                 p_id: int = None, long_desc: str = None, short_desc: str = None, time_b: datetime = None,
                 time_e: datetime = None, place: str = None, geo_id: int = None, url: str = None,
                 is_online: bool = None, active: bool = None):
        self.id = id
        self.m_id = m_id
        self.p_id = p_id
        self.original_text = original_text
        self.title = title
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.date = date
        self.time_b = time_b
        self.time_e = time_e
        self.place = place
        self.geo_id = geo_id
        self.url = url
        self.is_online = is_online
        self.date_add = date_add
        self.active = active
