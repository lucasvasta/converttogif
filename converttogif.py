import os
import subprocess
from tkinter import filedialog, simpledialog, Tk
import tkinter as tk

def choose_input_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select MP4 file", filetypes=[("MP4 files", "*.mp4")])
    return file_path

def choose_output_folder():
    root = tk.Tk()
    root.withdraw()
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    return output_folder

def enter_gif_filename():
    root = Tk()
    root.withdraw()
    filename = simpledialog.askstring("GIF Filename", "Enter the desired GIF filename:")
    return filename

def choose_time_range():
    root = Tk()
    root.withdraw()

    start_time = simpledialog.askfloat("Start Time", "Enter the start time (in seconds):")
    end_time = simpledialog.askfloat("End Time", "Enter the end time (in seconds):")

    return start_time, end_time

def convert_mp4_to_image_sequence(input_file, output_folder, target_width=600, start_time=None, end_time=None):
    try:
        # Use FFmpeg to convert cropped MP4 to PNG image sequence with resized frames
        if start_time is not None and end_time is not None:
            ffmpeg_command = f'ffmpeg -i "{input_file}" -ss {start_time} -to {end_time} -vf "fps=10,scale={target_width}:-1" -q:v 1 "{output_folder}/frame-%04d.png"'
        else:
            ffmpeg_command = f'ffmpeg -i "{input_file}" -vf "fps=10,scale={target_width}:-1" -q:v 1 "{output_folder}/frame-%04d.png"'

        subprocess.check_output(ffmpeg_command, shell=True)

        print("Conversion to image sequence successful!")
    except Exception as e:
        print(f"Error converting MP4 to image sequence: {e}")

def get_next_sequence_number(output_folder):
    sequence_number = 1
    while os.path.exists(os.path.join(output_folder, f"{sequence_number}.gif")):
        sequence_number += 1
    return sequence_number

def create_gif_from_image_sequence(image_folder, output_folder, filename, fps=10):
    try:
        # Get the next available sequence number
        sequence_number = get_next_sequence_number(output_folder)

        # Use ImageMagick to create GIF from the image sequence with the specified filename
        output_gif_path = os.path.join(output_folder, f'{filename}.gif')
        imagemagick_command = f'magick -delay {100 // fps} "{image_folder}/frame-*.png" "{output_gif_path}"'
        subprocess.check_output(imagemagick_command, shell=True)

        print("GIF creation successful!")
    except Exception as e:
        print(f"Error creating GIF: {e}")

if __name__ == "__main__":
    input_file_path = choose_input_file()

    if input_file_path:
        output_folder_path = choose_output_folder()
        if not output_folder_path:
            print("Output folder selection cancelled.")
        else:
            output_image_folder = os.path.join(output_folder_path, "output_images")
            os.makedirs(output_image_folder, exist_ok=True)

            frames_per_second = 10

            start_time, end_time = choose_time_range()
            convert_mp4_to_image_sequence(input_file_path, output_image_folder, target_width=600, start_time=start_time, end_time=end_time)

            gif_filename = enter_gif_filename()
            if not gif_filename:
                print("GIF filename not provided.")
            else:
                create_gif_from_image_sequence(output_image_folder, output_folder_path, gif_filename, fps=frames_per_second)

            # Cleanup: Delete the temporary image sequence
            for file in os.listdir(output_image_folder):
                file_path = os.path.join(output_image_folder, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(output_image_folder)

            print("GIF saved with the specified filename.")
