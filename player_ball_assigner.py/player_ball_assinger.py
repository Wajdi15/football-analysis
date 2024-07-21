import sys
sys.path.append('../')
from utils import get_center_of_bbox,measure_dist

class PlayerBallAssigner() :
    def __init__(self):
        self.max_player_ball_distance = 70
    
    def assign_ball_to_player(self,player,ball_bbox) :
        ball_position = get_center_of_bbox(ball_bbox)

        for player_id,player in player.items() :
            player_bbox = player['bbox']
            minimum_distance = 99999
            assigned_player = -1
            dist_left = measure_dist((player_bbox[0],player_bbox[-1]),ball_position)
            dist_right = measure_dist((player_bbox[2],player_bbox[-1]),ball_position)
            distance = min(dist_left,dist_right)

            if distance < self.max_player_ball_distance :
                if distance < minimum_distance :
                    minimum_distance = distance
                    assigned_player = player_id
        return assigned_player        