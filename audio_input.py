import pyaudio
import wave
import time
import numpy
import scipy
import threading
import queue

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "recorded_audio.wav"
TIME_TO_RECORD = 2

#instantiate
audio = pyaudio.PyAudio()
#set up stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
#read incoming audio
frames = []

start_time = time.time()
fft_queue = queue.Queue()
finished_recording = False
output_frequencies = []

#A function that will run on a thread that utilizes a queue to process data using fft.
#All the frequencies will be put into the output_frequencies array
def fft_thread():
    while not finished_recording or fft_queue.qsize() > 0:
        if fft_queue.qsize() > 0:
            N = CHUNK
            R = RATE

            queue_data = fft_queue.get()
            queue_data = numpy.frombuffer(queue_data, dtype=numpy.int16)

            fft_result = scipy.fft.fft(queue_data)
            # absolute value result to avoid imaginary numbers
            fft_result = numpy.abs(fft_result)
            #normalize result
            fft_max = numpy.max(fft_result)
            normalized_fft_result = fft_result / fft_max

            relative_maximums, _ = scipy.signal.find_peaks(normalized_fft_result, height=.9)
            # inverse of sample rate
            d = 1 / R
            frequencies = scipy.fft.fftfreq(N, d)
            maximum_frequencies = frequencies[relative_maximums]
            positive_maximum_frequencies = maximum_frequencies[maximum_frequencies > 0]
            #add output frequencies to the list
            output_frequencies.append(positive_maximum_frequencies)

def freq_to_note(frequency):
    if frequency == 0:
        return
    #key number = 12 log_2 (f/440) + 49:
    computer_shift = 1
    key_number = int(12 * numpy.log2(frequency/440)+49+computer_shift)
    note_dict = {
        1: "A",
        2: "A#",
        3: "B",
        4: "C",
        5: "C#",
        6: "D",
        7: "D#",
        8: "E",
        9: "F",
        10: "F#",
        11: "G",
        12: "G#"
    }
    note_name = note_dict[key_number % 12]
    note_number = (key_number//12) + 1
    note = note_name + str(note_number)
    return note


#start thread to begin processing data
fft_thread = threading.Thread(target=fft_thread, args=[])
fft_thread.start()

#start recording
while True:
    try:
        #perform fft here
        data = stream.read(CHUNK)
        frames.append(data)
        fft_queue.put(data)

    except Exception as e:
        print("Exception Occured: ", e)
        break

    if time.time() - start_time >= TIME_TO_RECORD:
        break

finished_recording = True
fft_thread.join()

for freq in output_frequencies:
    try:
        print(freq_to_note(freq[0]))
    except:
        print("issue processing")


#close up the stream
stream.stop_stream()
stream.close()
audio.terminate()

#write to audio file
waveFile = wave.open(OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
