top_left_coord = [-3.05, 336.51]
top_right_coord = [-3.05, 336.6]
bottom_left_coord = [-2.1, 336.5]
bottom_right_coord = [-2.1, 336.58]

# Arranged in Lat, Long
anomaly_coordinates = [(-3.0128, 336.5781)]

# Given the top left, top right, bottom left, and bootom right coordinates of a bounding box, locate the corresponding pixel for a given coordinate.

def identify_anomaly_pixels(top_left_coord, top_right_coord, bottom_left_coord, bottom_right_coord, anomaly_coordinates):
    for anomaly in anomaly_coordinates:
        lat = anomaly[0]
        long = anomaly[1]
        # Calculate the pixel location of the anomaly
        # The pixel location is calculated by the following formula:
        # pixel = (coordinate - top_left_coordinate) / (bottom_right_coordinate - top_left_coordinate) * image_size
        # where image_size is the size of the image in pixels
        # The image size is 5064 columns x 52224 rows
        pixel_lat = (lat - top_left_coord[0]) / (bottom_right_coord[0] - top_left_coord[0]) * 52224
        pixel_long = (long - top_left_coord[1]) / (bottom_right_coord[1] - top_left_coord[1]) * 5064
        print("Anomaly at ({}, {}) is located at pixel ({}, {})".format(lat, long, pixel_lat, pixel_long))
        
identify_anomaly_pixels(top_left_coord, top_right_coord, bottom_left_coord, bottom_right_coord, anomaly_coordinates)