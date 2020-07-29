from beem import Hive
from beem import Steem
from beem.nodelist import NodeList

nodelist = NodeList()
nodelist.update_nodes()
HIVE_INSTANCE = Hive(node=nodelist.get_hive_nodes())
STEEM_INSTANCE = Steem(node=nodelist.get_steem_nodes())
