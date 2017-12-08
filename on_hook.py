import sys
from pybili import bili, bili_sender, bili_config
from pybili.DanMuJi import initHandlers


def main():
    argv = sys.argv
    if len(argv) >= 2:
        path = argv[1]
        config = bili_config.Config(path=path)
        roomid = int(config.data.keys()[0])
        bili.BiliHelper(roomid, *initHandlers(roomid, config_path=path))

    else:
        config = bili_config.Config()
        roomid = int(config.data.keys()[0])
    cookies = config.cookies
    sender = bili_sender.Sender(cookies)
    sender.startFreeSilverThread()
    while 1:
        cmd = raw_input()
        sender.sendDanmaku(roomid, cmd)


if __name__ == '__main__':
    main()
