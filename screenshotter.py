#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:57:25 2021

@author: qdimarellis-adc
"""
import pyscreenshot
import json


conf_file = "conf.json"
with open(conf_file) as f:
    conf = json.load(f)
X = conf.get("x", 0)
Y = conf.get("y", 0)
W = conf.get("width", 100)
H = conf.get("heigth", 100)
img = pyscreenshot.grab(bbox=(X, Y, W, H))
img.save("img.png")
