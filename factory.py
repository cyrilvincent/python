from typing import Optional

import config
import db_context

class Db:

    _context: Optional[db_context.FormationContext] = None

    @staticmethod
    def context() -> db_context.FormationContext():
        if Db._context is None:
            Db._context = db_context.FormationContext(config.connection_string)
        return Db._context

