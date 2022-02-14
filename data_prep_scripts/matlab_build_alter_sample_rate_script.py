import os

test_dir = "/home/bestalex/Documents/Cut_2016_maternal_separation_USV_recordings/aif_conv_test"

wav_dir = "/local/scratch/cut_10s_2016_PND_usv"
new_dir = "/local/scratch/cut_10s_2016_PND_usv/"

for file in os.listdir(wav_dir):
    if file.endswith(".wav"):
        print(file)
        new_file_name = new_dir + file
        print(new_file_name)

        script_file = open(test_dir + "/matlab_resample_script.txt", "a")
        script_file.write('[x,fs] = audioread(\'' + file + '\');\n')
        script_file.write('fs2 = 16000;audiowrite(\'' + new_file_name + '\',x,fs2);\n')
        script_file.close()
