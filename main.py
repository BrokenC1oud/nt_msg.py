from pprint import pprint

import nt_msg
import db


def main():
    gms = db.session.query(db.GroupMessage)
    for _ in gms:
        try:
            m = nt_msg.Message.from_db(_)
        except Exception as e:
            print(_.ID)
            raise e
        for __ in m.elements:
            if isinstance(__, nt_msg.SystemNotificationElement):
                pprint(m)


if __name__ == "__main__":
    main()
