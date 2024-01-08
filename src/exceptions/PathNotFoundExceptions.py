class PathNotFoundExceptions(FileNotFoundError):
    def __init__(self) -> None:
        super().__init__('please enter your path by running update_component.py and only fill in the PATH_TO_SAVE section and leave everything else blank')