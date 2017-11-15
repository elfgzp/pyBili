import sys
from pybili import bili, bili_sender, bili_config
from pybili.DanMuJi import initHandlers


def main():
    argv = sys.argv
    roomid = 234024
    if len(argv) >= 2:
        roomid = int(argv[1])
    if len(argv) >= 3:
        path = argv[2]
        config = bili_config.Config(path=path)
        bili.BiliHelper(roomid, *initHandlers(roomid, config_path=path))

    else:
        config = bili_config.Config()
    cookies = config.cookies
    sender = bili_sender.Sender(cookies)
    sender.startFreeSilverThread()
    while 1:
        cmd = raw_input()
        sender.sendDanmaku(roomid, cmd)


if __name__ == '__main__':
    main()
