import streamlit as st
from IPython.display import display
import os


output_folder = "animations"


    


st.title("LivePortrait App")

## Image upload
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_image is not None:
  with open("temp_image.jpg", "wb") as f:
    f.write(uploaded_image.read())
  # run_live_portrait("temp_image.jpg",video)
  # st.write("Process complete. Find the output in the current directory.")

## Selecting emotions  
emotions = st.selectbox("select emotion",
("anger","anger1","sad","happy","sad1","sad2","sad3","sad4","sad5","smile"),
index=None,placeholder="choose You option..",
)


video = f"{emotions}.mp4"
output_video = f"temp_image--{emotions}.mp4"
output_path = os.path.join(output_folder,output_video)
  # if output_path is not None:
  #   st.video(output_path,format="video/mp4")

def run_live_portrait(image_path, video_path):
  # Assuming the necessary libraries and models are already set up
  if image_path is not None and video_path is not None:
    os.system(f"python inference.py -s {image_path} -d {video_path}")
    display(f"LivePortrait generated with {image_path} and {video_path}")
    if output_path is not None:
      st.video(output_path,format="video/mp4")
  

if st.button("animate"):
  run_live_portrait(image_path="temp_image.jpg",video_path=video)
