"""
Nose tests for acp_times.py

This is an automated test suite to ensure that controle opening
and closing times are calculated correctly based on the RUSA
specifications.
"""

from acp_times import close_time
from acp_times import open_time

#  January 1, 2017 at midnight. Default for the pages, so it's easy to test.
start_time = "2017-01-01T00:00:00-08:00"

# 200 km brevet test

def test_200_general():
    assert open_time( 0, 200, start_time ) == "2017-01-01T00:00:00-08:00"
    assert close_time( 0, 200, start_time ) == "2017-01-01T01:00:00-08:00"
    assert open_time( 40, 200, start_time ) == "2017-01-01T01:11:00-08:00"
    assert close_time( 40, 200, start_time ) == "2017-01-01T02:40:00-08:00"
    assert open_time( 90, 200, start_time ) == "2017-01-01T02:39:00-08:00"
    assert close_time( 90, 200, start_time ) == "2017-01-01T06:00:00-08:00"
    assert open_time( 120, 200, start_time ) == "2017-01-01T03:32:00-08:00"
    assert close_time( 120, 200, start_time ) == "2017-01-01T08:00:00-08:00"
    assert open_time( 200, 200, start_time ) == "2017-01-01T05:53:00-08:00"
    assert close_time( 200, 200, start_time ) == "2017-01-01T13:30:00-08:00"

# 300 km brevet test

def test_300_general():
    assert open_time( 0, 300, start_time ) == "2017-01-01T00:00:00-08:00"
    assert close_time( 0, 300, start_time ) == "2017-01-01T01:00:00-08:00"
    assert open_time( 40, 300, start_time ) == "2017-01-01T01:11:00-08:00"
    assert close_time( 40, 300, start_time ) == "2017-01-01T02:40:00-08:00"
    assert open_time( 90, 300, start_time ) == "2017-01-01T02:39:00-08:00"
    assert close_time( 90, 300, start_time ) == "2017-01-01T06:00:00-08:00"
    assert open_time( 120, 300, start_time ) == "2017-01-01T03:32:00-08:00"
    assert close_time( 120, 300, start_time ) == "2017-01-01T08:00:00-08:00"
    assert open_time( 200, 300, start_time ) == "2017-01-01T05:53:00-08:00"
    assert close_time( 200, 300, start_time ) == "2017-01-01T13:20:00-08:00"
    assert open_time( 300, 300, start_time ) == "2017-01-01T09:00:00-08:00"
    assert close_time( 300, 300, start_time ) == "2017-01-01T20:00:00-08:00"

# 400 km brevet test

def test_400_general():
    assert open_time( 0, 400, start_time ) == "2017-01-01T00:00:00-08:00"
    assert close_time( 0, 400, start_time ) == "2017-01-01T01:00:00-08:00"
    assert open_time( 40, 400, start_time ) == "2017-01-01T01:11:00-08:00"
    assert close_time( 40, 400, start_time ) == "2017-01-01T02:40:00-08:00"
    assert open_time( 90, 400, start_time ) == "2017-01-01T02:39:00-08:00"
    assert close_time( 90, 400, start_time ) == "2017-01-01T06:00:00-08:00"
    assert open_time( 120, 400, start_time ) == "2017-01-01T03:32:00-08:00"
    assert close_time( 120, 400, start_time ) == "2017-01-01T08:00:00-08:00"
    assert open_time( 200, 400, start_time ) == "2017-01-01T05:53:00-08:00"
    assert close_time( 200, 400, start_time ) == "2017-01-01T13:20:00-08:00"
    assert open_time( 300, 400, start_time ) == "2017-01-01T09:00:00-08:00"
    assert close_time( 300, 400, start_time ) == "2017-01-01T20:00:00-08:00"
    assert open_time( 325, 400, start_time ) == "2017-01-01T09:47:00-08:00"
    assert close_time( 325, 400, start_time ) == "2017-01-01T21:40:00-08:00"
    assert open_time( 375, 400, start_time ) == "2017-01-01T11:21:00-08:00"
    assert close_time( 375, 400, start_time ) == "2017-01-02T01:00:00-08:00"
    assert open_time( 400, 400, start_time ) == "2017-01-01T12:08:00-08:00"
    assert close_time( 400, 400, start_time ) == "2017-01-02T03:00:00-08:00"

# 600 km brevet test

def test_600_general():
    assert open_time( 0, 600, start_time ) == "2017-01-01T00:00:00-08:00"
    assert close_time( 0, 600, start_time ) == "2017-01-01T01:00:00-08:00"
    assert open_time( 40, 600, start_time ) == "2017-01-01T01:11:00-08:00"
    assert close_time( 40, 600, start_time ) == "2017-01-01T02:40:00-08:00"
    assert open_time( 90, 600, start_time ) == "2017-01-01T02:39:00-08:00"
    assert close_time( 90, 600, start_time ) == "2017-01-01T06:00:00-08:00"
    assert open_time( 120, 600, start_time ) == "2017-01-01T03:32:00-08:00"
    assert close_time( 120, 600, start_time ) == "2017-01-01T08:00:00-08:00"
    assert open_time( 200, 600, start_time ) == "2017-01-01T05:53:00-08:00"
    assert close_time( 200, 600, start_time ) == "2017-01-01T13:20:00-08:00"
    assert open_time( 300, 600, start_time ) == "2017-01-01T09:00:00-08:00"
    assert close_time( 300, 600, start_time ) == "2017-01-01T20:00:00-08:00"
    assert open_time( 325, 600, start_time ) == "2017-01-01T09:47:00-08:00"
    assert close_time( 325, 600, start_time ) == "2017-01-01T21:40:00-08:00"
    assert open_time( 375, 600, start_time ) == "2017-01-01T11:21:00-08:00"
    assert close_time( 375, 600, start_time ) == "2017-01-02T01:00:00-08:00"
    assert open_time( 400, 600, start_time ) == "2017-01-01T12:08:00-08:00"
    assert close_time( 400, 600, start_time ) == "2017-01-02T02:40:00-08:00"
    assert open_time( 450, 600, start_time ) == "2017-01-01T13:48:00-08:00"
    assert close_time( 450, 600, start_time ) == "2017-01-02T06:00:00-08:00"
    assert open_time( 522, 600, start_time ) == "2017-01-01T16:12:00-08:00"
    assert close_time( 522, 600, start_time ) == "2017-01-02T10:48:00-08:00"
    assert open_time( 602, 600, start_time ) == "2017-01-01T18:48:00-08:00"
    assert close_time( 602, 600, start_time ) == "2017-01-02T16:00:00-08:00"

# 1000 km brevet test

def test_1000_general():
    assert open_time( 0, 1000, start_time ) == "2017-01-01T00:00:00-08:00"
    assert close_time( 0, 1000, start_time ) == "2017-01-01T01:00:00-08:00"
    assert open_time( 40, 1000, start_time ) == "2017-01-01T01:11:00-08:00"
    assert close_time( 40, 1000, start_time ) == "2017-01-01T02:40:00-08:00"
    assert open_time( 90, 1000, start_time ) == "2017-01-01T02:39:00-08:00"
    assert close_time( 90, 1000, start_time ) == "2017-01-01T06:00:00-08:00"
    assert open_time( 120, 1000, start_time ) == "2017-01-01T03:32:00-08:00"
    assert close_time( 120, 1000, start_time ) == "2017-01-01T08:00:00-08:00"
    assert open_time( 200, 1000, start_time ) == "2017-01-01T05:53:00-08:00"
    assert close_time( 200, 1000, start_time ) == "2017-01-01T13:20:00-08:00"
    assert open_time( 300, 1000, start_time ) == "2017-01-01T09:00:00-08:00"
    assert close_time( 300, 1000, start_time ) == "2017-01-01T20:00:00-08:00"
    assert open_time( 325, 1000, start_time ) == "2017-01-01T09:47:00-08:00"
    assert close_time( 325, 1000, start_time ) == "2017-01-01T21:40:00-08:00"
    assert open_time( 375, 1000, start_time ) == "2017-01-01T11:21:00-08:00"
    assert close_time( 375, 1000, start_time ) == "2017-01-02T01:00:00-08:00"
    assert open_time( 400, 1000, start_time ) == "2017-01-01T12:08:00-08:00"
    assert close_time( 400, 1000, start_time ) == "2017-01-02T02:40:00-08:00"
    assert open_time( 450, 1000, start_time ) == "2017-01-01T13:48:00-08:00"
    assert close_time( 450, 1000, start_time ) == "2017-01-02T06:00:00-08:00"
    assert open_time( 522, 1000, start_time ) == "2017-01-01T16:12:00-08:00"
    assert close_time( 522, 1000, start_time ) == "2017-01-02T10:48:00-08:00"
    assert open_time( 602, 1000, start_time ) == "2017-01-01T18:52:00-08:00"
    assert close_time( 602, 1000, start_time ) == "2017-01-02T16:11:00-08:00"
    assert open_time( 727, 1000, start_time ) == "2017-01-01T23:20:00-08:00"
    assert close_time( 727, 1000, start_time ) == "2017-01-03T03:07:00-08:00"
    assert open_time( 804, 1000, start_time ) == "2017-01-02T02:05:00-08:00"
    assert close_time( 804, 1000, start_time ) == "2017-01-03T09:51:00-08:00"
    assert open_time( 860, 1000, start_time ) == "2017-01-02T04:05:00-08:00"
    assert close_time( 860, 1000, start_time ) == "2017-01-03T14:45:00-08:00"
    assert open_time( 914, 1000, start_time ) == "2017-01-02T06:01:00-08:00"
    assert close_time( 914, 1000, start_time ) == "2017-01-03T19:29:00-08:00"
    assert open_time( 961, 1000, start_time ) == "2017-01-02T07:42:00-08:00"
    assert close_time( 961, 1000, start_time ) == "2017-01-03T23:35:00-08:00"
    assert open_time( 1017, 1000, start_time ) == "2017-01-02T09:05:00-08:00"
    assert close_time( 1017, 1000, start_time ) == "2017-01-04T03:00:00-08:00"
