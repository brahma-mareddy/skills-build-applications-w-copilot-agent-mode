from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='captain@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.set([ironman, batman])
        running.suggested_for.set([captain, superman])

        # Create Activities
        Activity.objects.create(user=ironman, type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=captain, type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Running', duration=60, date=timezone.now().date())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
