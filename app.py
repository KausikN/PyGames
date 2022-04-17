"""
Stream lit GUI for hosting PyGames
"""

# Imports
import os
import streamlit as st
import json

from Games.InfiniteCubes import InfiniteCubes
from Games.TestGame import TestGame

# Main Vars
config = json.load(open("./StreamLitGUI/UIConfig.json", "r"))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    "Choose one of the following",
        tuple(
            [config["PROJECT_NAME"]] + 
            config["PROJECT_MODES"]
        )
    )
    
    if selected_box == config["PROJECT_NAME"]:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(" ", "_").lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config["PROJECT_NAME"])
    st.markdown("Github Repo: " + "[" + config["PROJECT_LINK"] + "](" + config["PROJECT_LINK"] + ")")
    st.markdown(config["PROJECT_DESC"])

    # st.write(open(config["PROJECT_README"], "r").read())

#############################################################################################################################
# Repo Based Vars
CACHE_PATH = "StreamLitGUI/CacheData/Cache.json"

# Util Vars
CACHE = {}

# Util Functions
def LoadCache():
    global CACHE
    CACHE = json.load(open(CACHE_PATH, "r"))

def SaveCache():
    global CACHE
    json.dump(CACHE, open(CACHE_PATH, "w"), indent=4)

# Main Functions


# UI Functions


# Repo Based Functions
def infinite_cubes():
    # Title
    st.header("Infinite Cubes")

    # Prereq Loaders

    # Load Inputs
    col1, col2 = st.columns(2)
    USERINPUT_min_distance = col1.slider("Min Distance", 10, 90, 20, 10)
    USERINPUT_max_distance = col2.slider("Max Distance", USERINPUT_min_distance, 200, 100, 10)
    USERINPUT_n_cubes = st.number_input("Number of Cubes", 1, 100, 25, 1)
    col1, col2, col3 = st.columns(3)
    USERINPUT_x_speed = col1.slider("X Speed", 0.1, 2.0, 0.3, 0.1)
    USERINPUT_y_speed = col2.slider("Y Speed", 0.1, 2.0, 0.3, 0.1)
    USERINPUT_z_speed = col3.slider("Z Speed", 1, 5, 2, 1)
    # x and y are distance from camera pos to generate
    # z is multiplied with max_distance for generation
    col1, col2, col3 = st.columns(3)
    USERINPUT_generateBounds = (
        col1.number_input("X Bounds", 1, 100, 25, 5), 
        col2.number_input("Y Bounds", 1, 100, 25, 5), 
        col3.number_input("X Bounds", 1, 25, 2, 1)
    ) 

    # Process Inputs and Display Outputs
    if st.button("Play"):
        try:
            st.markdown("## Logs")
            DisplayWidget = st.empty()
            DisplayObj = lambda x: DisplayWidget.write(x)
            InfiniteCubes.main(
                USERINPUT_x_speed, USERINPUT_y_speed, USERINPUT_z_speed, 
                USERINPUT_n_cubes, 
                USERINPUT_max_distance, USERINPUT_min_distance, USERINPUT_generateBounds,
                displayObj=DisplayObj
            )
        except Exception as e:
            st.error(e)

def test_game():
    # Title
    st.header("Test Game")

    # Prereq Loaders

    # Load Inputs
    col1, col2 = st.columns(2)
    USERINPUT_display_width = col1.slider("Display Width", 50, 1600, 800, 10)
    USERINPUT_display_height = col2.slider("Display Height", 50, 1600, 600, 10)

    # Process Inputs and Display Outputs
    if st.button("Play"):
        try:
            st.markdown("## Logs")
            DisplayWidget = st.empty()
            DisplayObj = lambda x: DisplayWidget.write(x)
            TestGame.main(
                USERINPUT_display_width, USERINPUT_display_height,
                displayObj=DisplayObj
            )
        except Exception as e:
            st.error(e)

#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()