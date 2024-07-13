from utils import read_video,save_video
from trackers import Tracker
def main():
    print("hello wajdi !")
    #read video
    video_frames = read_video('inputs_vid/08fd33_0.mp4')

    #init tracker
    tracker = Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path="stubs/track_stubs.pkl")

if __name__ == '__main__' :
    main()