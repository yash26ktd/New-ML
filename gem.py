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

#video previews
tab1, tab2, tab3 = st.tabs(["Anger", "Happy","Sad"])

with tab1:
  col1, col2 = st.columns(2)
  with col1:
    st.header("anger")
    st.video("anger.mp4",format="video/mp4")

  with col2:
    st.header("anger1")
    st.video("anger1.mp4",format="video/mp4")  

with tab2:
  col1, col2 = st.columns(2)
  with col1:
    st.header("happy")
    st.video("happy.mp4",format="video/mp4")
  with col2:
    st.header("smile")
    st.video("smile.mp4",format="video/mp4")

with tab3:
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.header("sad1")
    st.video("sad1.mp4",format="video/mp4")

  with col2:
    st.header("sad2")
    st.video("sad2.mp4",format="video/mp4")

  with col3:
    st.header("sad3")
    st.video("sad3.mp4",format="video/mp4") 

  with col4:
    st.header("sad4")
    st.video("sad4.mp4",format="video/mp4")

  with col5:
    st.header("sad5")
    st.video("sad5.mp4",format="video/mp4")  


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
