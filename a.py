import os
import glob
os.system('rm *.mp4')
os.system('rm *.zip')
os.system('youtube-dl -ci --write-sub --sub-lang en '+\
        '-f \'bestvideo[ext=mp4][height<=?720]+bestaudio[ext=m4a]/mp4\' '+\
        '--embed-subs --merge-output-format mp4 '+\
        'https://www.youtube.com/playlist?list=PLG8RpKAodyTpvZOR0qEma1AmUvMGsvIi0')
for name in glob.glob('*.mp4'):
    command_s = 'ffmpeg -y -i \"' + name + "\" -vf subtitles=\"filename=\'" +\
    name + "\':force_style=\'FontSize=13,FontName=Arial\'\"" +\
    " -c:v libx264 -x264-params crf=22 -preset fast -profile:v high " + "\'hdcode %s\'"%name
    os.system(command_s)
os.system('zip a.zip hdcode*.mp4')
os.system('bypy upload a.zip')
