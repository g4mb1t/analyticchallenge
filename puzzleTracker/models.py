from django.db import models

# Create your models here.
class Status(models.Model):
	NOTSTARTED = 'N'
	WORKING = 'W'
	COMPLETED = 'C'
	PUZZLE_STATUS_CHOICES = (
		(NOTSTARTED, 'N'),
		(WORKING, 'W'),
		(COMPLETED, 'C'),
	)
	status = models.CharField(
		max_length=1,
		choices=PUZZLE_STATUS_CHOICES,
		default=NOTSTARTED,
	)
	puzz = models.PositiveSmallIntegerField()
	team = models.PositiveSmallIntegerField()
	updateTime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return('Team:{0} Puzzle:{1} Status:{2}'.format(str(self.team),str(self.puzz),str(self.status)))