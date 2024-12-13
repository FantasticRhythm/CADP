REGISTRY = {}

from .rnn_agent import RNNAgent
REGISTRY["rnn"] = RNNAgent
from .atten_rnn_agent import ATTRNNAgent
REGISTRY["att_rnn"] = ATTRNNAgent
from .n_rnn_agent import NRNNAgent
REGISTRY["n_rnn"] = NRNNAgent
from .hpn_atten_agent import ATTRNNAgent as HPNAttAgent
REGISTRY["hpn_att"] = HPNAttAgent