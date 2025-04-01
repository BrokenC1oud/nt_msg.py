class DbNotPresentException(Exception):
    """ Raised when database file is not present """


class UnmatchModelException(Exception):
    """ Raised when requesting a model from an invalid database file. """

