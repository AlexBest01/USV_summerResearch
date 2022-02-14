import os

#test_dir = "/home/bestalex/Documents/Cut_2016_maternal_separation_USV_recordings/aif_conv_test"

test_dir = "/home/bestalex/Documents/Cut_2016_maternal_separation_USV_recordings/cut_10s_2016_PND_usv/sml_sample_usv"
new_dir = "/home/bestalex/Documents/Cut_2016_maternal_separation_USV_recordings/10s_mix_sample/"

for file in os.listdir(test_dir):
    if file.endswith(".wav"):
        print(file)
        new_name = file[:-4]
        #print(new_name)
        print("ffmpeg -i " + test_dir + "/" + file + " -f segment -segment_time " + "10" + " -c copy " + test_dir + "/10s_mixed_sample/" + new_name + "_%03d.wav")
        os.system("ffmpeg -i " + test_dir + "/" + file + " -f segment -segment_time " + "10" + " -c copy " + test_dir + "/10s_mixed_sample/" + new_name + "_%03d.wav")
