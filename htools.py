#!/usr/bin/python
# -*- coding: UTF-8 -*-
from optparse import OptionParser
from optparse import OptionGroup
from libs.defaults import defaults
from libs.single import ScanPortThread
import thread
import threading
import logging
import sys
import Queue


def parse_args():

    parser = OptionParser(usage="By:HaiChecker Hack Tools")

    parser.add_option("--version", dest="showVersion", action="store_true",
                      help="Show program's version number and exit")

    # parser.add_option("-T","--threads",dest="threads",type="int",help="Show HTools help message and exit")

    # Target options
    target = OptionGroup(parser, "Target", "At least one of these "
                         "options has to be provided to define the target(s)")
    target.add_option("-a", "--address", dest="address",
                      help="Port scan (Web site or IP)")

    target.add_option("-p", "--port", dest="port", action="store_true",
                      help="Port List (1801,808,8080 or 88-1024)")
    target.add_option("-w", "--web", dest="WEB", action="store_true",
                      help="WEB scan (Web Path - example http:www.haichecker.com)")

    # Optimization options
    optimization = OptionGroup(
        parser, "Optimization", "These options can be used to optimize the performance of HTools")
    optimization.add_option("--threads", dest="threads", type="int", default=defaults.threads,
                            help="Max number of concurrent "
                            "requests (default %d)" % defaults.threads)
    optimization.add_option("--timeout", dest="timeout", type="int", default=defaults.timeout,
                            help="Seconds to wait before timeout connection (default %d)" % defaults.timeout)

    parser.add_option_group(target)
    parser.add_option_group(optimization)
    (options, args) = parser.parse_args()
    return options


if __name__ == '__main__':
    q = Queue.Queue()
    args = parse_args()
    logger = logging.getLogger("App")
    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
    if(args.address != None):
        url = args.address
    if(args.port != None):
        port = args.port
    threads = args.threads
