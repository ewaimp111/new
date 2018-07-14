#!/usr/bin/env python3
import parsers
import threading as thread
import time



if __name__ == '__main__':
    parser_html = parsers.Timers(30)
    parser_html.start()  #开始循环刷新数据



#main_thread()
