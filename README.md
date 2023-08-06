**MP4 to GIF Converter**

This project is a simple Python script that allows you to convert MP4 videos to GIF animations. The script provides a user-friendly interface to select the input MP4 file, choose the time range for video cropping (optional), and specify the desired filename for the output GIF.

**Requirements**

- Python 3.x
- FFmpeg (for video conversion)
- ImageMagick (for GIF creation)

**Installation**

1. Install Python 3.x from the official Python website: https://www.python.org/downloads/

2. Install FFmpeg:
   - Windows: Download FFmpeg from https://www.ffmpeg.org/download.html and add it to your system's PATH.
   - macOS: Install FFmpeg using Homebrew with the command: `brew install ffmpeg`
   - Linux: Install FFmpeg using your package manager (e.g., `sudo apt install ffmpeg` on Ubuntu)

3. Install ImageMagick:
   - Windows: Download ImageMagick from https://imagemagick.org/script/download.php#windows and add it to your system's PATH.
   - macOS: Install ImageMagick using Homebrew with the command: `brew install imagemagick`
   - Linux: Install ImageMagick using your package manager (e.g., `sudo apt install imagemagick` on Ubuntu)

4. Clone or download this repository to your local machine.

**Usage**

1. Run the `mp4_to_gif_converter.py` script using Python.

2. The script will open a file dialog for you to select the input MP4 file.

3. If you want to crop the video, the script will prompt you to enter the start and end times (in seconds) for the time range. If you want to convert the entire video without cropping, simply leave both input fields blank.

4. After video conversion and cropping (if applicable), the script will open another dialog to enter the desired filename for the output GIF.

5. The GIF will be created and saved in the specified output folder. The filename will be in the format 'upsell_(numero).gif', where `(numero)` represents the next available sequence number in the output folder.

**Note**

Please ensure you have read and write permissions for the input MP4 file and the output folder.

**Contributing**

Contributions to this project are welcome! Feel free to open issues or submit pull requests on the GitHub repository.

**License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as per the terms of the license.

**Acknowledgments**

This project was inspired by the need to convert MP4 videos to GIF animations quickly and easily. Special thanks to the developers of FFmpeg and ImageMagick for their amazing tools that make this conversion possible.

If you have any questions or suggestions, please don't hesitate to contact us. Happy video to GIF converting!