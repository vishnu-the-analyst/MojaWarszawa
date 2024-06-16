# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 02:43:21 2024

@author: Vishnu Kumar
"""

def is_within_warsaw(lon, lat):
    # Warsaw bounding box coordinates
    min_lon = 20.8512
    max_lon = 21.2710
    min_lat = 52.0971
    max_lat = 52.3680

    # Check if the coordinates are within the bounding box
    if min_lon <= lon <= max_lon and min_lat <= lat <= max_lat:
        return "Thank you for providing the location."
    else:
        return "I am afraid the location is outside the city limits of warsaw. Please contact the national support."
