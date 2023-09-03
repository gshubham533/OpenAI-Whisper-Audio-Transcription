# OpenAI Whisper Audio Transcription for Large Files

This repository provides a Python class, `WhisperAudioTranscriber`, and associated documentation for efficiently transcribing large audio files to text using OpenAI's Whisper ASR system. Whisper is a state-of-the-art Automatic Speech Recognition (ASR) system capable of converting spoken language into written text with high accuracy, making it ideal for handling large audio files.

Features:
1. **WhisperAudioTranscriber Class**: This Python class, `WhisperAudioTranscriber`, simplifies the process of transcribing large audio files into text. It includes methods for loading audio files, creating audio chunks, and initiating the transcription process.

2. **Easy Configuration**: The class allows you to set your OpenAI API key for easy integration with OpenAI's Whisper ASR service.

3. **Automatic Chunking**: You can specify the chunk size in minutes, and the class automatically divides the input audio file into smaller manageable chunks for efficient processing.

4. **Transcription Output**: The transcribed text is saved to a text file, making it convenient to access and use for further analysis or applications.


## Installation

To use the `WhisperAudioTranscriber` class for transcribing large audio files, follow these steps:

1. **Install Python Packages**:

   Install the required Python packages using the following command:

   ```bash
   pip install openai pydub openai-whisper
   ```

2. **Install FFmpeg**:

   The code relies on the FFmpeg command-line tool for audio processing. Ensure FFmpeg is installed on your system using one of the following methods:

   - **Ubuntu or Debian**:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```

   - **Arch Linux**:
     ```bash
     sudo pacman -S ffmpeg
     ```

   - **macOS using Homebrew** (https://brew.sh/):
     ```bash
     brew install ffmpeg
     ```

   - **Windows using Chocolatey** (https://chocolatey.org/):
     ```bash
     choco install ffmpeg
     ```

   - **Windows using Scoop** (https://scoop.sh/):
     ```bash
     scoop install ffmpeg
     ```

## Usage for Large Audio Files

Transcribing large audio files with `WhisperAudioTranscriber` is straightforward. Here's an example of how to use the class:

```python
from whisper_audio_transcriber import WhisperAudioTranscriber

# Replace '<api_key>' with your actual OpenAI API key
api_key = '<api_key>'

# Initialize the WhisperAudioTranscriber instance
transcriber = WhisperAudioTranscriber(api_key)

# Load the large input audio file (e.g., 'large_audio.mp3')
transcriber.load_file('sample_audio.mp3')

# Create audio chunks automatically for efficient processing
transcriber.create_audio_chunks()

# Start the transcription process and save the output to a text file
transcriber.start_transcribing('output_transcript_large')
```

Refer to the complete documentation for detailed usage instructions and options, specifically tailored for transcribing large audio files.

## Repository Structure

- `whisper_audio_transcriber.py`: The Python script containing the `WhisperAudioTranscriber` class and associated methods.
- `requirements.txt`: A list of Python dependencies required to run the code.
- `example.py`: An example script demonstrating the usage of the `WhisperAudioTranscriber` class with large audio files.
- `sample_large_audio/`: A folder containing sample large audio files for testing and demonstration purposes.
- `output_large/`: A folder where the transcribed text output files for large audio files are stored.