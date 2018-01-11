# -*- coding: utf-8 -*-

# TODO: Do I really have to do that to have relative imports working with .. ?

import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import sample
