query = """
	"61001"	INTEGER,
	"61002"	INTEGER,
	"61003"	INTEGER,
	"61004"	BLOB,
	"61005"	BLOB,
	"61006"	BLOB,
	"61007"	BLOB,
	"61008"	INTEGER,
	"61009"	BLOB,
	"61010"	TEXT,
	"61011"	TEXT,
"""

data_types = {
    "INTEGER": "int",
    "BLOB": "bytes",
    "TEXT": "str",
}

for idx, line in enumerate(query.split("\n")):
    if line:
        _ = line.strip().removesuffix(",").split("\t")
        print(f"UNK_{idx}: Mapped[{data_types[_[1]]}] = mapped_column({_[0]})")
