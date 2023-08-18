"""
Module provide lists of sql keywords that should trigger or skip
checks for tables an columns
"""

# these keywords are followed by columns reference
from enum import Enum

KEYWORDS_BEFORE_COLUMNS = {
    "SELECT",
    "WHERE",
    "ORDERBY",
    "GROUPBY",
    "ON",
    "SET",
    "USING",
}

# normalized list of table preceding keywords
TABLE_ADJUSTMENT_KEYWORDS = {
    "FROM",
    "JOIN",
    "CROSSJOIN",
    "INNERJOIN",
    "FULLJOIN",
    "FULLOUTERJOIN",
    "LEFTJOIN",
    "RIGHTJOIN",
    "LEFTOUTERJOIN",
    "RIGHTOUTERJOIN",
    "INTO",
    "UPDATE",
    "TABLE",
    "CONVERT",
    "GENERATE",
    "OPTIMIZE",
    "CLONE",
    "DESC",
    "DESCRIBE",
    "DETAIL",
    "HISTORY",
    "VACUUM",
    "CONVERT",
    "DELTA",
}

# next statement beginning after with statement
WITH_ENDING_KEYWORDS = {"UPDATE", "SELECT", "DELETE", "REPLACE", "INSERT"}

# subquery preceding keywords
SUBQUERY_PRECEDING_KEYWORDS = {
    "FROM",
    "JOIN",
    "CROSSJOIN",
    "INNERJOIN",
    "FULLJOIN",
    "FULLOUTERJOIN",
    "LEFTJOIN",
    "RIGHTJOIN",
    "LEFTOUTERJOIN",
    "RIGHTOUTERJOIN",
}

# section of a query in which column can exists
# based on last normalized keyword
COLUMNS_SECTIONS = {
    "SELECT": "select",
    "WHERE": "where",
    "ORDERBY": "order_by",
    "ON": "join",
    "USING": "join",
    "INTO": "insert",
    "SET": "update",
    "GROUPBY": "group_by",
}


class QueryType(str, Enum):
    """
    Types of supported queries
    """

    INSERT = "INSERT"
    REPLACE = "REPLACE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    SELECT = "SELECT"
    CREATE = "CREATE TABLE"
    ALTER = "ALTER TABLE"
    DROP = "DROP TABLE",
    LOCATION = "LOCATION",
    TBLPROPERTIES = "TBLPROPERTIES",
    SHALLOW_CLONE = "SHALLOW CLONE",
    SHOW_COLUMNS = "SHOW COLUMNS",
    REORG = "REORG",
    OPTIMIZE = "OPTIMIZE",
    DROP_CONSTRAINT = "DROP CONSTRAINT",
    ADD_CONSTRAINT = "ADD CONSTRAINT",
    ALTER_TABLE = "ALTER TABLE",
    RESTORE = "RESTORE",
    PARTITIONED_BY = "PARTITIONED BY",
    NO_STATISTICS = "NO STATISTICS",
    CONVERT_TO_DELTA = "CONVERT TO DELTA",
    HISTORY = "HISTORY",
    GENERATE = "GENERATE",
    DETAIL = "DETAIL",
    DESCRIBE = "DESCRIBE",
    DESC = "DESC",
    DRY_RUN = "DRY RUN",
    RETAIN = "RETAIN",
    VACUUM = "VACUUM",


class TokenType(str, Enum):
    """
    Types of SQLTokens
    """

    COLUMN = "COLUMN"
    TABLE = "TABLE"
    COLUMN_ALIAS = "COLUMN_ALIAS"
    TABLE_ALIAS = "TABLE_ALIAS"
    WITH_NAME = "WITH_NAME"
    SUB_QUERY_NAME = "SUB_QUERY_NAME"
    PARENTHESIS = "PARENTHESIS"


# cannot fully replace with enum as with/select has the same key
SUPPORTED_QUERY_TYPES = {
    "INSERT": QueryType.INSERT,
    "REPLACE": QueryType.REPLACE,
    "UPDATE": QueryType.UPDATE,
    "SELECT": QueryType.SELECT,
    "DELETE": QueryType.DELETE,
    "WITH": QueryType.SELECT,
    "CREATETABLE": QueryType.CREATE,
    "ALTERTABLE": QueryType.ALTER,
    "DROPTABLE": QueryType.DROP,
    "GENERATE": QueryType.DROP,
    "RESTORE": QueryType.RESTORE,
    "REORG": QueryType.REORG,
    "OPTIMIZE": QueryType.OPTIMIZE,
    "VACUUM" : QueryType.VACUUM,
    "DESCRIBE": QueryType.DESCRIBE,
    "DESC": QueryType.DESC,
    "CONVERT": QueryType.CONVERT_TO_DELTA,
}

# all the keywords we care for - rest is ignored in assigning
# the last keyword
RELEVANT_KEYWORDS = {
    *KEYWORDS_BEFORE_COLUMNS,
    *TABLE_ADJUSTMENT_KEYWORDS,
    *WITH_ENDING_KEYWORDS,
    *SUBQUERY_PRECEDING_KEYWORDS,
    "LIMIT",
    "OFFSET",
    "RETURNING",
    "VALUES",
    "INDEX",
    "WITH",
    "WINDOW",
    "HISTORY",
    "DETAIL",
    "VACUUM",
    "CONVERT",
}
