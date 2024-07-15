from utils import read_video,save_video
from trackers import Tracker

def main():
    print("hello wajdi !")
    #read video
    video_frames,fps= read_video('inputs_vid/08fd33_0.mp4')
    #init tracker
    tracker = Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path="stubs/track_stubs.pkl")
    #draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames,tracks)
    #save video
    save_video(output_video_frames,'output_videos/output_video.avi',fps)
if __name__ == '__main__' :
    main()