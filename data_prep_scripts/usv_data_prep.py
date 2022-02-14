import os
import sys
import argparse
import pathlib
#import matlab.engine


## Set up argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-input', type=str, required=True, metavar='input/path/to/waves', help='soundfile directory')
parser.add_argument('-o', '-output', type=str, required=True, metavar='output/dir', help='processed soundfile directory')
parser.add_argument('--tl', type=str, metavar='trim-lenght', help='lenght of trimmed segments')
parser.add_argument('--ext', type=str, metavar='audio-codex', help='codex to convert audio file to')
parser.add_argument('--hdr', type=str, metavar='sample-rate', help='value to alter header file sample rate' )
args = parser.parse_args()

data_dir = args.i
new_dir = args.o

if data_dir == new_dir:
    os.system( "echo Input directory : " + data_dir + " and output directory : " + new_dir + " are the same." )
    os.system( "echo Please specify a different directory for the output files" )
    sys.exit()

try:
    make_new_dir = os.makedirs(new_dir)
except FileExistsError:
    #directory already exists
    pass
## Convert clips to certain codex

if args.ext is not None:
    try:
        mk = os.makedirs(data_dir + "/temp_convert")
        temp_convert_dir = data_dir + "/temp_convert"
    except FileExistsError:
        #directory already exists
        temp_convert_dir = data_dir + "/temp_convert"
        pass
    for file in os.listdir(data_dir):
         f = os.path.join(args.i, file)
         if os.path.isfile(f):
             name_split = os.path.splitext(file)
             new_name = str(temp_convert_dir) + "/" + name_split[0] + "." + args.ext
             print(name_split[0])
             print(new_name)
             print( "ffmpeg -i " + data_dir + "/" + file + " " + new_name )
             os.system( "ffmpeg -i " + data_dir + "/" + file + " " + new_name )


## Split clips into smaller segments
if args.tl is not None:
    try:
        mk = os.makedirs(data_dir + "/temp_segment")
        temp_segment_dir = data_dir + "/temp_segment"
    except FileExistsError:
        #directory already exists
        temp_segment_dir = args.i + "/temp_segment"
        pass
    if args.ext is not None:
        data_dir = temp_convert_dir
    for file in os.listdir(data_dir):
         f = os.path.join(data_dir, file)
         if os.path.isfile(f):
            name_split = os.path.splitext(file)
            trimmed_clip = str(temp_segment_dir) + "/" + name_split[0] + "_%03d" + name_split[1]
            cur_file = data_dir + "/" + file
            print( "ffmpeg -i " + cur_file + " -f segment -segment_time " + args.tl + " -c copy " + trimmed_clip )
            os.system("ffmpeg -i " + cur_file + " -f segment -segment_time " + args.tl + " -c copy " + trimmed_clip )
    if args.ext is not None:
        print("rm -rf " + data_dir)
        os.system("rm -rf " + str(data_dir) )
        print("Old codec temp file removed")

## Update header file to 16kHz
if args.hdr is not None:
    header_script = os.system("touch " + new_dir + "/matlab_resample_script.txt")
    script_file = open(new_dir + "/matlab_resample_script.txt", "a")
    script_file.write('cd ' + new_dir + ';\n')                                    # Might need to change the semi-colon
    script_file.close()

    if args.tl is not None:
        data_dir = temp_segment_dir
    elif args.ext is not None:
        data_dir = temp_convert_dir
    else:
        pass
    for file in os.listdir(data_dir):
        f = os.path.join(data_dir, file)
        if os.path.isfile(f):
        #if file.endswith(".wav"):
            new_file_name = new_dir + "/" + file
            print(new_file_name)
            script_file = open(new_dir + "/matlab_resample_script.txt", "a")
            script_file.write('[x,fs] = audioread(\'' + file + '\');\n')
            script_file.write('fs2 = 16000;audiowrite(\'' + new_file_name + '\',x,fs2);\n')
            script_file.close()

## Load Matlab script
    print("mv " + new_dir + "/matlab_resample_script.txt " + new_dir + "/matlab_resample_script.m" )
    print("cd " + new_dir )

    os.system("mv " + new_dir + "/matlab_resample_script.txt " + new_dir + "/matlab_resample_script.m" )
    os.system("cd " + new_dir )

## TODO
## Script can be run through matlab till this part of code is complete
'''
    eng = matlab.engine.start_matlab()
    eng.matlab_resample_script(nargout=0)

'''
