from pprint import pprint

import nt_msg
import db


def main():
    dbman = db.DatabaseManager()
    gms = dbman.group_messages().first()
    pprint(nt_msg.extract_message(gms.message))


if __name__ == "__main__":
    main()