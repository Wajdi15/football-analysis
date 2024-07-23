import sys
sys.path.append('../')
from utils import get_center_of_bbox,measure_dist

class PlayerBallAssigner() :
    def __init__(self):
        self.max_player_ball_distance = 70
    
    def assign_ball_to_player(self,players,ball_bbox) :
        ball_position = get_center_of_bbox(ball_bbox)
        minimum_distance = 9999
        assigned_player = -1

        for player_id,player in players.items() :
            player_bbox = player['bbox']
            player_position = get_center_of_bbox(player_bbox)
            distance = measure_dist(player_position,ball_position)

            if  distance <= self.max_player_ball_distance and distance < minimum_distance:
                minimum_distance = distance
                assigned_player = player_id
            
        return assigned_player        