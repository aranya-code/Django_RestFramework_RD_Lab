from django.db import models

# Create your models here.
class ScoreCard(models.Model):

    skills = [('batter' , 'Batter'), 
              ('bowler', 'Bowler'),
                ('ar', 'All-Rounder'),
                 ('wk', 'Wicket Keeper'),
                  ('c', 'Captain')]

    id = models.IntegerField(primary_key= True)
    player_name = models.CharField(max_length=100)
    jersey_no = models.IntegerField(unique= True)
    technical_skill = models.CharField(default='batter', choices=skills)
    runs = models.IntegerField(default= 0)
    wickets = models.IntegerField(default= 0)
    catches = models.IntegerField(default= 0)
    status = models.CharField(max_length=50, default='Not Out')


    def __str__(self):
        return self.player_name