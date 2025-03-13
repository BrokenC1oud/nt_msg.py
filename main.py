from pprint import pprint

import nt_msg
import db


def main():
    gm_db = db.session.query(db.GroupMessage)[114514:191981]
    messages = [nt_msg.Message.from_db(_) for _ in gm_db]
    pprint(messages)


if __name__ == "__main__":
    main()
