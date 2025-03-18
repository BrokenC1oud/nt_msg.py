from pprint import pprint

import nt_msg
import db


def main():
    gm_db = db.session.query(db.models.GroupMessage).first()
    message = nt_msg.Message.from_db(gm_db)
    pprint(messages)


if __name__ == "__main__":
    main()