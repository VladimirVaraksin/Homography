import numpy as np
import cv2


class ViewTransformer:
    """
    A class to transform image coordinates (pixel) to real-world coordinates (meters)
    using perspective transformation, based on known dimensions and corner mappings.
    """
    def __init__(self, pixel_vertices=None, target_vertices=None):
        """
        Initializes the ViewTransformer by defining real-world dimensions, pixel coordinates,
        and computing the perspective transformation matrix.
        """

        #Pixel coordinates of the corners in the input image
        self.pixel_vertices = pixel_vertices
        #Corresponding real-world coordinates (in meters) for the camera
        self.target_vertices = target_vertices

        # Compute the perspective transformation matrix
        self.perspective_transformer = cv2.getPerspectiveTransform(
            self.pixel_vertices,
            self.target_vertices
        )


    def transform_point(self, point):
        """
        Transforms a point from pixel coordinates to real-world coordinates.

        Parameters:
        - point: A NumPy array of shape (1, 2), representing the (x, y) pixel coordinates.

        Returns:
        - A NumPy array of the shape (1, 2) with the transformed real-world coordinates,
          or None if the point lies outside the defined court polygon.
        """
        # Convert to integer coordinates for point-in-polygon test
        p = (int(point[0]), int(point[1]))
        # Reshape point to a required format for cv2.perspectiveTransform and convert to float32
        reshaped_point = point.reshape(-1, 1, 2).astype(np.float32)
        is_inside = cv2.pointPolygonTest(self.pixel_vertices, p, False) >= 0
        # Check if the point lies within the defined court polygon
        if is_inside:
                transformed_point = cv2.perspectiveTransform(reshaped_point, self.perspective_transformer)
        else:
            return None

        return transformed_point.reshape(-1, 2)