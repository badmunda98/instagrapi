from datetime import timedelta, tzinfo


class CET(tzinfo):
    async def utcoffset(self, dt):
        return timedelta(hours=1)

    async def dst(self, dt):
        return timedelta(hours=2)


class UTC(tzinfo):
    async def utcoffset(self, dt):
        return timedelta(0)

    async def dst(self, dt):
        return timedelta(0)
