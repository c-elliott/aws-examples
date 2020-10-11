#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example App

This is just an example of how an application
could be structured using a class, including
a seperate settings file, reliable log rotation
and MySQL database connection handling.
"""
import time
import logging
import logging.handlers
import mysql.connector
from configuration import settings
from __future__ import print_function

try:
    from cloghandler import ConcurrentRotatingFileHandler as RFHandler
except ImportError:
    from logging.handlers import RotatingFileHandler as RFHandler

__date__ = 'Saturday, October 10th, 2020'
__version__ = '0.1'
__revision__ = __version__

class ClassExample(object):

    def __init__(self):
        """ Setup configuration and logging """
        try:
            debug = getattr(settings, 'DEBUG', False)
            self.mysql_host = getattr(settings, 'MYSQL_HOST')
            self.mysql_db = getattr(settings, 'MYSQL_DB')
            self.mysql_user = getattr(settings, 'MYSQL_USER')
            self.mysql_pass = getattr(settings, 'MYSQL_PASS')
            self.mysql_ssl = getattr(settings, 'MYSQL_SSL_CA', None)
        except AttributeError as ex:
            print('Missing or invalid configuration. Check settings.py')
            print(str(ex))
        if debug:
            ltype = 'DEBUG'
            level = logging.DEBUG
        else:
            ltype = 'INFO'
            level = logging.INFO
        maxsize = 16 * 1024 * 1024
        handler = RFHandler(logfile, 'a', maxBytes=maxsize, backupCount=9)
        form = '%(asctime)s [%(process)d] %(levelname)s: %(message)s'
        fmat = logging.Formatter(form)
        fmat.converter = time.gmtime
        global logg
        logg = logging.getLogger('ClassExample')
        logg.propagate = True
        logg.setLevel(level)
        handler.setFormatter(fmat)
        logg.addHandler(handler)
        form = 'ClassExample %s process starting in %s mode'
        args = (__version__, ltype)
        logg.info(form % args)

    def mysql_disconnect(self):
        """ Disconnect from MySQL """
        try:
            self.con.close()
        except: # pylint: disable=bare-except
            pass

    def mysql_connect(self):
        """ Connect to MySQL, optionally via TLS """
        try:
            self.mysql_disconnect()
            defs = {'host': self.mysql_host,
                    'user': self.mysql_user,
                    'password': self.mysql_pass,
                    'database': self.mysql_db,
                    'charset': 'utf8'}
            if self.mysql_ssl:
                defs['ssl_ca'] = self.mysql_ssl
            self.con = mysql.connector.connect(**defs)
            self.cur = self.con.cursor(buffered=True)
            return True
        except Exception as ex: # pylint: disable=broad-except
            logg.info('Error - Failed connecting to MySQL')
            logg.info('excp: %s', ex)
            return False

    def mysql_exec(self, msql, args):
        """ Execute a MySQL query with no results """
        try:
            self.cur.execute(msql, args)
            self.con.commit()
            return True
        except Exception as ex: # pylint: disable=broad-except
            logg.info('Error - Exception during mysql_exec()')
            logg.info('msql: %s', msql)
            logg.info('args: %s', args)
            logg.info('excp: %s', ex)
            return False

    def mysql_query(self, msql, args=None):
        """ Query something, return all results """
        try:
            self.cur.execute(msql, args)
            self.con.commit()
            rows = self.cur.fetchall()
            return rows
        except Exception as ex: # pylint: disable=broad-except
            logg.info('Error - Exception during mysql_query()')
            logg.info('msql: %s', msql)
            logg.info('args: %s', args)
            logg.info('excp: %s', ex)
            return None

    def run(self):
        """ Main application logic here """
        pass

def main():
    service = ClassExample()
    service.run()

if __name__ == '__main__':
    main()
