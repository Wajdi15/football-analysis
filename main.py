import random
from utils import read_video,save_video
from trackers import Tracker
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner

def main():
    print("hello wajdi !")
    #read video
    video_frames,fps= read_video('inputs_vid/08fd33_0.mp4')
    #init tracker
    tracker = Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path="stubs/track_stubs.pkl")
    #interpolate ball positions
    tracks['ball'] = tracker.interpoation_ball_positions(tracks['ball'])

    # Assign Player Teams
    team_assigner = TeamAssigner()
    random_frame = random.randint(0, len(video_frames))
    team_assigner.assign_team_color(video_frames[random_frame],tracks['players'][random_frame])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],track['bbox'], player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    #Assign Ball Aquisition
    player_assigner = PlayerBallAssigner()
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)
        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            
    #draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames,tracks)
    #save video
    save_video(output_video_frames,'output_videos/output_video.avi',fps)
if __name__ == '__main__' :
    main()