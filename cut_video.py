from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# 원하는 비디오 파일의 경로
input_video_path = "AlphaPose/input.mp4"

# 출력할 비디오 파일의 경로
output_video_path = "AlphaPose/output.mp4"

# 자르기 시작할 시간 (초)
start_time = 110

# 자르기를 끝낼 시간 (초)
end_time = 160

# 비디오 자르기
ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)

