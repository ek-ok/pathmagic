# -*- coding: UTF-8 -*-
"""Path hack to make tests work."""
import os
import sys

par_dir = os.path.dirname(os.getcwd())
sys.path.insert(0, par_dir)
