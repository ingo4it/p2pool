from p2pool.bitcoin import networks

PARENT = networks.nets['groestlcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//15 # shares
REAL_CHAIN_LENGTH = 24*60*60//15 # shares
TARGET_LOOKBEHIND = 60 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'a15320ffb197c089'.decode('hex')
PREFIX = '867c36a56116e81e'.decode('hex')
P2P_PORT = 11331
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 11330
BOOTSTRAP_ADDRS = 'grs.altmine.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-grs'
VERSION_CHECK = lambda v: None if 2130300 <= v else 'Groestlcoin version too old. Upgrade to 2.13.3 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 16