from pprint import pprint

import nt_msg
import db


def main():
    gms = db.session.query(db.GroupMessage)
    for _ in gms:
        m = nt_msg.Message.from_db(_)
        for __ in m.elements:
            if isinstance(__, nt_msg.ForwardedMessagesXMLElement):
                pprint(m)
                exit()

if __name__ == "__main__":
    main()
