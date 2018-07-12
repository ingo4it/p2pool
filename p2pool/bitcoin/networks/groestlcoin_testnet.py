import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '0b110907'.decode('hex')
P2P_PORT = 16634
ADDRESS_VERSION = 111
SEGWIT_ADDRESS_VERSION = 196
RPC_PORT = 16633
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, 'ffbb50fc9898cdd36ec163e6ba23230164c0052a28876255b7dcf2cd36'))
            ))
SUBSIDY_FUNC = lambda height: __import__('groestlcoin_subsidy').getBlockBaseValue(0, height+1)
POW_FUNC = data.hash_groestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'TGRS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Groestlcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Groestlcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.groestlcoin'), 'groestlcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/address.dws?'
TX_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/tx.dws?'
SANE_TARGET_RANGE= (2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF = 256
DUST_THRESHOLD = 0.001e8
HUMAN_READABLE_PART = 'tgrs'
