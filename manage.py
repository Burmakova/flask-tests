import unittest
import os
import coverage

from flask_script import Manager

from project import app, db

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
