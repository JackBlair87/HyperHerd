# HyperHerd: Automating Social Media Follower Tracking

![HyperHerd](./images/hyperherd.png)

HyperHerd is a Python-based project that automates the process of tracking and aggregating your social media follower counts across multiple platforms. It was developed by Jack as a solution to the tedious task of manually checking and updating their personal website's "live" follower count.

## Why HyperHerd?

As a data-driven individual, I wanted to streamline the process of tracking their social media following across various platforms, including LinkedIn, GitHub, YouTube, Instagram, Twitter, Medium, and Facebook. Rather than manually checking each platform and updating a central count, they set out to create a script that could automatically gather this information.

## Features

- **Automated Follower Count Tracking**: HyperHerd visits your social media profiles, captures screenshots, and uses Optical Character Recognition (OCR) to extract the follower count for each platform.
- **Cross-Platform Support**: The script is designed to work on macOS, leveraging AppleScript and Tesseract OCR to handle the automation and text extraction.
- **Customizable Profiles**: You can easily customize the script by updating the links to your own social media profiles.
- **Follower Count Aggregation**: HyperHerd calculates the total number of followers across all your connected accounts and displays the result.
- **Offline Accessibility**: The script can be run locally, without the need for any third-party services or APIs.

## How it Works

HyperHerd follows a multi-step process to gather and aggregate your social media follower counts:

1. **Profile Definition**: The script starts by defining a list of your social media profiles, including the platform, account name, and URL.
2. **Screenshot Capture**: Using AppleScript, the script opens your Chrome browser, navigates to each of your social media profiles, and captures a screenshot of the page.
3. **OCR Processing**: The script then uses the Tesseract OCR engine to extract the text from the screenshots, including the follower count for each platform.
4. **Follower Count Extraction**: A custom function, `extract_follower_count`, is used to parse the OCR-extracted text and identify the follower count for each platform.
5. **Total Follower Aggregation**: Finally, the script sums up the follower counts for all your connected accounts and displays the total.

## Installation and Usage

### Prerequisites

To use HyperHerd, you'll need the following:

- Python 3.x
- The following Python libraries: `os`, `tqdm`, `applescript`, `PIL`, `cv2`, `pytesseract`, `numpy`, `pyautogui`
- Google Chrome installed on your macOS system

### Installation

1. Clone the HyperHerd repository:

   ```
   git clone https://github.com/JackBlair87/HyperHerd.git
   ```

2. Change to the project directory:

   ```
   cd HyperHerd
   ```

3. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

### Usage

1. Open the `HyperHerd.py` file and update the `PROFILE_LINKS` dictionary with your own social media profile URLs.

2. Run the script:

   ```
   python HyperHerd.py
   ```

3. The script will open your Chrome browser, navigate to each of your social media profiles, capture screenshots, and extract the follower counts. The total number of followers will be displayed at the end of the script's execution.

## Limitations and Future Improvements

While HyperHerd is a powerful tool for automating social media follower tracking, it does have some limitations:

- **macOS-only**: The current implementation of HyperHerd only works on macOS systems, as it relies on AppleScript and Tesseract OCR.
- **User Interaction Required**: The script requires the user to be present and have their computer unlocked, as it uses AppleScript to control the Chrome browser.
- **Potential Fragility**: Changes to the social media platform layouts or OCR accuracy could disrupt the script's functionality.

To address these limitations and further enhance HyperHerd, future improvements could include:

- **Cross-platform Support**: Explore alternative methods, such as Selenium or Playwright, to make the script compatible with Windows and Linux.
- **Background Execution**: Investigate the feasibility of running the script as a background process or a scheduled task, reducing the need for user intervention.
- **Robust Parsing**: Implement more advanced text extraction and parsing techniques, potentially utilizing machine learning models, to improve the reliability of follower count extraction.
- **Data Persistence**: Add the capability to store the follower count data over time, enabling trend analysis and historical tracking.
- **Notification System**: Integrate a notification system to alert users of significant changes in their follower counts.

## Contributing

If you find any issues or have ideas for improving HyperHerd, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/JackBlair87/HyperHerd).

## License

HyperHerd is released under the [MIT License](LICENSE).

## Acknowledgments

The development of HyperHerd was inspired by Jack Blair's desire to automate and streamline their social media follower tracking, as well as the insights and techniques shared in the accompanying articles.