from django.db.models import Count
from django.db.models.functions import TruncWeek
from datetime import datetime, timedelta, timezone

from main.models import WorkoutData

def get_workout_statistics(user_id):
    current_date = datetime.now(timezone.utc).date()
    start_date = current_date - timedelta(days=current_date.weekday())

    workout_statistics = (
        WorkoutData.objects
        .filter(user_id=user_id, date__gte=start_date - timedelta(weeks=9))
        .annotate(week_start=TruncWeek('date'))
        .values('week_start')
        .annotate(workout_count=Count('id'))
        .order_by('week_start')
    )

    result_dict = {(start_date - timedelta(weeks=i)).strftime("%m.%d"): 0 for i in range(0, 7)}

    for entry in workout_statistics:
        week_start_str = entry['week_start'].strftime("%m.%d")
        result_dict[week_start_str] = entry['workout_count']

    return result_dict