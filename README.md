# People-Counter-Using-OpenCV

A real-time people counting system using OpenCV, designed to identify and count people entering and exiting a region of interest (ROI) in a video feed. This project intentionally avoids the use of advanced deep learning algorithms, focusing instead on traditional computer vision techniques like background subtraction and contour detection. It is ideal for those who are learning the basics of computer vision and want to understand fundamental concepts before moving on to more complex models.

### Features

- **Background Subtraction**: Efficiently detects moving objects in the video by subtracting the background.
- **Contour Detection and Filtering**: Identifies and tracks objects based on their contours, with filters applied to remove noise and irrelevant objects.
- **Real-time Counting**: Tracks the number of people entering and exiting the defined region, with a visual display of counts on the video feed.
- **Basic Counting Logic**: Uses simple logic to increment counters, demonstrating how basic image processing can achieve people counting without the need for advanced algorithms.

### Tech Stack

- **Programming Languages**: Python
- **Computer Vision**: OpenCV
- **Utility Functions**: imutils
- **Video Processing**: OpenCV

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amandi-udawatta/People-Counter-Using-OpenCV.git
   cd People-Counter-Using-OpenCV

2. **Create a Virtual Environment:**:
   ```bash
   python3 -m venv venv

3. **Activate the Virtual Environment:**
   - On macOS/Linux:
    ```bash
    source venv/bin/activate
   - On Windows:
    ```bash
    .\venv\Scripts\activate

4. Install the Required Libraries:
    
    ```bash
    pip install -r requirements.txt

5. Run the Model:
    ```bash
    python your_script_name.py

### Authors

- [Amandi Udawatta](https://github.com/amandi-udawatta)