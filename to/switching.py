#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib


class SwichToPort():
    host_array = ['192.168.127.151', '192.168.127.154', '192.168.127.156', '192.168.127.150', '192.168.127.153',
                  '192.168.127.152', '192.168.127.155', '192.168.127.157']

    @staticmethod
    def to_port_1(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_2(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_3(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_4(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_5(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_6(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_7(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_8(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_9(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_10(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_11(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_12(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_13(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_14(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_15(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_16(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_17(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_18(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_19(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_20(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_21(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_22(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_23(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_24(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pcl 5 0\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_25(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_26(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_27(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_28(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_29(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_30(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_31(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_32(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_33(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_34(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_35(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_36(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_37(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_38(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_39(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_40(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pcl 4 0\r")
        tn.read_until(">")
        tn.write("pst 3 1\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_41(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_42(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_43(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_44(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pcl 2 0\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_45(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_46(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pcl 1 0\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_47(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pcl 0 0\r")
        tn.read_until(">")
        tn.close()
        return

    @staticmethod
    def to_port_48(host_number):
        tn = telnetlib.Telnet(SwichToPort.host_array[host_number], 23)
        tn.write("pinger\r")
        tn.read_until(">")
        tn.write("pst 5 1\r")
        tn.read_until(">")
        tn.write("pst 4 1\r")
        tn.read_until(">")
        tn.write("pcl 3 0\r")
        tn.read_until(">")
        tn.write("pst 2 1\r")
        tn.read_until(">")
        tn.write("pst 1 1\r")
        tn.read_until(">")
        tn.write("pst 0 1\r")
        tn.read_until(">")
        tn.close()
        return


class SwithToUs(SwichToPort):
    @staticmethod
    def switch_2():
        SwichToPort.to_port_3(0)
        return

    @staticmethod
    def switch_3():
        SwichToPort.to_port_4(0)
        return

    @staticmethod
    def switch_4():
        SwichToPort.to_port_1(0)
        return

    @staticmethod
    def switch_5():
        SwichToPort.to_port_1(0)
        SwichToPort.to_port_4(3)
        return

    @staticmethod
    def switch_6():
        SwichToPort.to_port_2(0)
        return

    @staticmethod
    def switch_7():
        SwichToPort.to_port_2(0)
        SwichToPort.to_port_1(5)
        return

    @staticmethod
    def switch_8():
        SwichToPort.to_port_1(0)
        SwichToPort.to_port_48(3)
        return


class Switching():
    host_array = ['192.168.127.151', '192.168.127.154', '192.168.127.156', '192.168.127.150', '192.168.127.153',
                  '192.168.127.152', '192.168.127.155', '192.168.127.157']

    def switch(self, switch, port):
        error = ""
        switch = int(switch)
        port = int(port)
        if switch == 2:
            SwithToUs.switch_2()
        elif switch == 3:
            SwithToUs.switch_3()
        elif switch == 4:
            SwithToUs.switch_4()
        elif switch == 5:
            SwithToUs.switch_5()
        elif switch == 6:
            SwithToUs.switch_6()
        elif switch == 7:
            SwithToUs.switch_7()
        elif switch == 8:
            SwithToUs.switch_8()
        elif switch != 1 and switch != 2 and switch != 3 and switch != 4 \
                and switch != 5 and switch != 6 and switch != 7 and switch != 8:
            error = "Введите коректный номер коммутатора"
        if port == 1:
            SwichToPort.to_port_1(switch - 1)
        elif port == 2:
            SwichToPort.to_port_2(switch - 1)
        elif port == 3:
            SwichToPort.to_port_3(switch - 1)
        elif port == 4:
            SwichToPort.to_port_4(switch - 1)
        elif port == 5:
            SwichToPort.to_port_5(switch - 1)
        elif port == 6:
            SwichToPort.to_port_6(switch - 1)
        elif port == 7:
            SwichToPort.to_port_7(switch - 1)
        elif port == 8:
            SwichToPort.to_port_8(switch - 1)
        elif port == 9:
            SwichToPort.to_port_9(switch - 1)
        elif port == 10:
            SwichToPort.to_port_10(switch - 1)
        elif port == 11:
            SwichToPort.to_port_11(switch - 1)
        elif port == 12:
            SwichToPort.to_port_12(switch - 1)
        elif port == 13:
            SwichToPort.to_port_13(switch - 1)
        elif port == 14:
            SwichToPort.to_port_14(switch - 1)
        elif port == 15:
            SwichToPort.to_port_15(switch - 1)
        elif port == 16:
            SwichToPort.to_port_16(switch - 1)
        elif port == 17:
            SwichToPort.to_port_17(switch - 1)
        elif port == 18:
            SwichToPort.to_port_18(switch - 1)
        elif port == 19:
            SwichToPort.to_port_19(switch - 1)
        elif port == 20:
            SwichToPort.to_port_20(switch - 1)
        elif port == 21:
            SwichToPort.to_port_21(switch - 1)
        elif port == 22:
            SwichToPort.to_port_22(switch - 1)
        elif port == 23:
            SwichToPort.to_port_23(switch - 1)
        elif port == 24:
            SwichToPort.to_port_24(switch - 1)
        elif port == 25:
            SwichToPort.to_port_25(switch - 1)
        elif port == 26:
            SwichToPort.to_port_26(switch - 1)
        elif port == 27:
            SwichToPort.to_port_27(switch - 1)
        elif port == 28:
            SwichToPort.to_port_28(switch - 1)
        elif port == 29:
            SwichToPort.to_port_29(switch - 1)
        elif port == 30:
            SwichToPort.to_port_30(switch - 1)
        elif port == 31:
            SwichToPort.to_port_31(switch - 1)
        elif port == 32:
            SwichToPort.to_port_32(switch - 1)
        elif port == 33:
            SwichToPort.to_port_33(switch - 1)
        elif port == 34:
            SwichToPort.to_port_34(switch - 1)
        elif port == 35:
            SwichToPort.to_port_35(switch - 1)
        elif port == 36:
            SwichToPort.to_port_36(switch - 1)
        elif port == 37:
            SwichToPort.to_port_37(switch - 1)
        elif port == 38:
            SwichToPort.to_port_38(switch - 1)
        elif port == 39:
            SwichToPort.to_port_39(switch - 1)
        elif port == 40:
            SwichToPort.to_port_40(switch - 1)
        elif port == 41:
            SwichToPort.to_port_41(switch - 1)
        elif port == 42:
            SwichToPort.to_port_42(switch - 1)
        elif port == 43:
            SwichToPort.to_port_43(switch - 1)
        elif port == 44:
            SwichToPort.to_port_44(switch - 1)
        elif port == 45:
            SwichToPort.to_port_45(switch - 1)
        elif port == 46:
            SwichToPort.to_port_46(switch - 1)
        elif port == 47:
            SwichToPort.to_port_47(switch - 1)
        elif port == 48:
            SwichToPort.to_port_48(switch - 1)
        else:
            error = 'Введите корректный порт.' + 'Сейчас переданы' + ' коммутатор № ' + str(
                switch) + ' и порт № ' + str(port)
        if error:
            message = error
        else:
            message = 'Выполнено переключение на ' + str(port) + ' порт ' + '  коммутатора №  ' + str(switch)

        return message

