from selenium import webdriver
import sys, getopt, time, subprocess, shlex
from xvfbwrapper import Xvfb


def run():
  #driver = webdriver.Chrome(chrome_options=options)
    print('Sreencast website animation')
    xvfb = Xvfb(width=1280, height=720, colordepth=24)
    xvfb.start()
    options = webdriver.chrome.options.Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--kiosk")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=options)
    #browser = webdriver.Firefox()
    url = 'https://clickcall.co.nz/af939c60-79bd-4d92-9785-e58e3944bd4f'
    #destination = 'movie.flv'
    browser.get(url)

    # normal quality, lagging in the first part on the video. filesize ~7MB
    # ffmpeg_stream = 'ffmpeg -f x11grab -s 1280x720 -r 24 -i :%d+nomouse -c:v libx264 -preset superfast -pix_fmt yuv420p -s 1280x720 -threads 0 -f flv "%s"' % (xvfb.new_display, destination)

    # high quality, no lagging but huge file size ~50MB
    ffmpeg_stream = 'ffmpeg -y -r 30 -f x11grab -s 1280x720 -i :%d+nomouse -c:v libx264rgb -crf 15 -preset:v ultrafast -c:a pcm_s16le -af aresample=async=1:first_pts=0 /output/out.mkv'  % xvfb.new_display
    #ffmpeg_stream = 'ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0 -q:v 0 -c:v libx264rgb -crf fast -y /output/screen.mp4' % xvfb.new_display
    args = shlex.split(ffmpeg_stream)
    p = subprocess.Popen(args)
    print("-------------------------------")
    print(p)
    print("-------------------------------")

    time.sleep(30) # record for 30 secs
    browser.quit()
    xvfb.stop()



if __name__ == "__main__":
    run()