cd pjproject-2.1.0
make distclean
./configure --disable-video --disable-ffmpeg --disable-v4l2
CFLAGS="-fPIC" CXXFLAGS="-fPIC" make dep
CFLAGS="-fPIC" CXXFLAGS="-fPIC" make
## TODO python client not ready yet
cd pjsip-apps/src/python
python setup.py install

