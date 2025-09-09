BASE_RESOLUTIONS = [
    (1024, 1024),
    (1024, 960),
]

class ResolutionSelector:
    """
    A node to provide a drop-down list of resolutions and returns two int values (width and height).
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Return a dictionary which contains config for all input fields.
        """

        # Create a list of resolution strings for the drop-down menu
        resolution_strings = [
            f"{width} x {height}" for width, height in BASE_RESOLUTIONS
        ]

        return {
            "required": {
                "base_resolution": (resolution_strings,),
            }
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "select_resolution"
    CATEGORY = "NW/utils"

    def select_resolution(self, base_resolution):
        """
        Returns the width and height based on the selected resolution.

        Args:
            base_resolution (str): Selected resolution in the format "width x height".
        
        Returns:
            Tuple[int, int]: Adjusted width and height.
        """
        try:
            width, height = map(int, base_resolution.split(' x '))
        except ValueError:
            raise ValueError("Invalid base_resolution format.")
        
        return width, height
    
NODE_CLASS_MAPPINGS = {
    "ResolutionSelector": ResolutionSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelector": "Resolution Selector",
}