# Reason for "-nolisten tcp", not documented within Xvfb manpages (for who knows what reason)
# https://superuser.com/questions/855019/make-xvfb-listen-only-on-local-ip
Xvfb :99 -screen 0 1280x720x24+32 -nolisten tcp &
python3 test.py