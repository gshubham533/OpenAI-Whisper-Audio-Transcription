from pydub import AudioSegment
import openai

class WhisperAudioTranscriber:
    def __init__(self,openai_api_key:str) -> None:
        self.api_key = openai_api_key
        openai.api_key = self.api_key
        self.total_chunks = 0
        self.chunk_size = 0
        self.audio = None
        self.ext = None
        self.chunks_filename = []
    
    def load_file(self,file_path:str,chunk_size_in_min:int=10):
        # Load input audio file
        if '.' in file_path:
            self.ext = file_path.split('.')[-1]
        else:
            raise "File does not have extention type"
        try:
            self.audio = AudioSegment.from_mp3(file_path)
        except Exception as e:
            raise e
        # Define the chunk size in milliseconds (default 10 minutes)
        chunk_size  = chunk_size_in_min * 60 * 1000
        self.chunk_size = chunk_size
        # Calculate the total number of chunks
        total_chunks = len(self.audio) // chunk_size + 1
        self.total_chunks = total_chunks
        return self.audio
    
    def create_audio_chunks(self,chunk_file_name:str='chunk') -> bool:
        if not self.total_chunks or not self.chunk_size or not self.audio or not self.ext:
            raise "Please load_file first to create chunks"
        try:
            # Split the audio into chunks and export them
            for i in range(self.total_chunks):
                start_time = i * self.chunk_size
                end_time = (i + 1) * self.chunk_size
                chunk = self.audio[start_time:end_time]
                
                # Export each chunk with a unique filename
                file_name = f"{chunk_file_name}_{i + 1}.{self.ext}"
                chunk.export(file_name, format=self.ext)
                self.chunks_filename.append(file_name)
                
        except Exception as e:
            print(e)
            return False
        return True
    
    def start_transcribing(self,output_filename='output_transcript') -> str:
        if len(self.chunks_filename) == 0:
            raise "Please create_audio_chunks first to start transcribing"
        try:
            output_file_name = f"{output_filename}.txt"
            with open(output_file_name,'w', encoding="utf-8") as file:
                for i in range(self.total_chunks):
                    chunk_file_name = self.chunks_filename[0]
                    audio_file= open(chunk_file_name, "rb")
                    transcript = openai.Audio.transcribe("whisper-1", audio_file)
                    file.write(transcript['text'])
        except Exception as e:
            print(e)
            return None
        return output_file_name
        