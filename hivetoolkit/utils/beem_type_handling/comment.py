from beem.comment import Comment
from . import amount as amt


def get_reward_dict(com):
    """return the rewards formated as a dict for the comment "com"

    Args:
        com (beem.comment.Comment): comment

    Raises:
        TypeError: wrong arg type
    """
    if not isinstance(com, Comment):
        raise TypeError(f"com argument must be an instance of Beem.comment.Comment")
    result = dict()
    for temporal_key, temporal_amount in com.get_rewards().items():
        result[temporal_key : amt.amount_to_dict(temporal_amount)]
