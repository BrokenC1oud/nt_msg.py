from pprint import pprint

import nt_msg
import db


def main():
    dbman = db.DatabaseManager()
    print(dbman.group_messages().filter_by(groupUin=974725670).count())


if __name__ == "__main__":
    main()
