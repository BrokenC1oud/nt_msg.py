from pprint import pprint

import nt_msg
import db
import nt_msg.contact


def main():
    dbman = db.DatabaseManager()
    buddy = nt_msg.contact.Buddy.get_by_uin(dbman, 3488229708)
    pprint(buddy)


if __name__ == "__main__":
    main()
