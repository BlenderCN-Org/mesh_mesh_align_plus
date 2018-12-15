"""TODO, exceptions"""


# Exception when adding new items, if we can't get a unique name
class UniqueNameError(Exception):
    pass


class NonMeshGrabError(Exception):
    pass


class InsufficientSelectionError(Exception):
    pass
