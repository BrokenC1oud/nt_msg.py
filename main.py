from pprint import pprint

import nt_msg
import db


def main():
    dbman = db.DatabaseManager()
    for _ in dbman.group_messages():
        print(nt_msg.Message.from_db(_))


if __name__ == "__main__":
    main()
