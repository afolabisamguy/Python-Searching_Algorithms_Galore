from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image

# Load the video file
video = VideoFileClip("C:/Users/Samguy/Downloads/Video/JimRohn_completeLostSeminar.mp4")

# # Extract the audio from the video
audio = video.audio
#
# # Write the audio to mp3 file
audio.write_audiofile("C:/Users/Samguy/Downloads/Video/JimRohn_completeLostSeminar.mp3")

# Close the video file
video.close()

# video_files = ["C:/Users/Samguy/Downloads/Video/Ep. 1- INTRO - Jim Rohn's LOST SEMINAR- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 2- Effective Communication Skills - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 3- Communication - 4 Key Words to be Aware of - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 4- The 4 Steps to Communication - Jim Rohn's Lost Seminar - The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 5- The 4 Steps To Communication #2 Say It Well - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 5- The 4 Steps To Communication #2 Say It Well - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 6- The 4 Steps To Communication #3 The Effect - Jim Rohn's Lost Seminar- The Making of a Leader_3.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 7- The 4 Steps To Communication #4 INTENSITY Strong Feelings - Jim Rohn's Lost Seminar- Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 8- Communication - How to Make a Presentation - IDENTIFICATION - Jim Rohn's Lost Seminar- Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 9- The Ability to SHARE - Personal Development - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 10- How to LIFESTYLE - Personal Development - Jim Rohn's Lost Seminar- The Making of a Leader_2.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 11- Goal Setting 2024 - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 12- Leadership - The Great Challenge - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 13- Leadership - THE 20% 80% RULE - Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 14- THE LAW OF AVERAGES The Parable of The Sower Jim Rohn's Lost Seminar- The Making of a Leader.mp4",
#                "C:/Users/Samguy/Downloads/Video/Ep. 15- How To Build a Successful Team of People - Business Hire - Jim Rohn's Lost Seminar- Leader.mp4"]
#
#
# clips = [VideoFileClip(file) for file in video_files]
# #
# # first_clip = clips[0]
# # clips_resized = [clip.resize(newsize=(first_clip.w, first_clip.h)) for clip in clips]
#
# clips_with_transition = [clip.crossfadein(2) for clip in clips]
#
#
# final_clip = concatenate_videoclips(clips_with_transition, method="compose")
#
# final_clip.write_videofile("C:/Users/Samguy/Downloads/Video/JimRohn_completeLostSeminar.mp4", codec="libx264")

