from .basecriteria import BaseCriteria
from ...utils import arguments
from builtins import setattr


class CommentCriteria(BaseCriteria):
    RULES = {
        "allowed_authors": {"type": list, "sub_type": str},
        "unallowed_authors": {"type": list, "sub_type": str},
        "allowed_tags": {"type": list, "sub_type": str},
        "unallowed_tags": {"type": list, "sub_type": str},
        "in_communities": {"type": list, "sub_type": str},
        "not_in_communities": {"type": list, "sub_type": str},
    }
