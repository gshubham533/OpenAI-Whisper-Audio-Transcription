from whisper_audio_transcriber import WhisperAudioTranscriber

# Replace '<api_key>' with your actual OpenAI API key
api_key = '<api_key>'

# Initialize the WhisperAudioTranscriber instance
T = WhisperAudioTranscriber(api_key)

# Load the input audio file
T.load_file('sample_audio.mp3')

# Create audio chunks
T.create_audio_chunks()

# Start the transcription process and save the output to a text file
T.start_transcribing()