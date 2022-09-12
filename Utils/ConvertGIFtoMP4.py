import PySimpleGUI as sg
import os
"""
    Screenshots were in GIF in itially.  This is the utility that converted them to MP4 in this repo

"""


IN_DIR = r'A:\Dropbox\-2022 PySimpleGUI-\DemoScreenshots2022'
def main():


    namesonly = [f for f in os.listdir(IN_DIR) if f.endswith('.gif')]

    for i, file in enumerate(namesonly):
        full_name = os.path.join(IN_DIR, file)
        outfile = file[:-3]+'mp4'
        args = f' -i "{full_name}" -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" {outfile}'
        sp = sg.execute_command_subprocess('ffmpeg', args, wait=True,merge_stderr_with_stdout=True, pipe_output=True, cwd=IN_DIR)
        print(f'{file} done')

if __name__ == '__main__':
    main()
