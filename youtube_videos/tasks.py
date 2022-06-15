from celery import shared_task
from .utils import useAPIKeys


@shared_task(bind=True)
def fetchYouTubeVideos(self):
    count = useAPIKeys()
    return f"{count} videos added to the database"
