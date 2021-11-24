python -m nuitka --mingw64 MCEmailVerifier.py --standalone
cd MCEmailVerifier.dist
set PATH=%PATH%;C:\Program Files\7-Zip\
7z a -r ../MCEmailVerifier_Win64.zip *
pause