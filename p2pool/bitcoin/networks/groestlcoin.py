import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d4'.decode('hex')
P2P_PORT = 5442
ADDRESS_VERSION = 36
SEGWIT_ADDRESS_VERSION = 5
RPC_PORT = 5332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '1b75fb6cfc7ee94f1552595c1e95ba4b149cbbb1d94bd05f23f2d432dce'))
            ))
SUBSIDY_FUNC = lambda height: __import__('groestlcoin_subsidy').getBlockBaseValue(0, height+1)
POW_FUNC = data.hash_groestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'GRS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Groestlcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Groestlcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.groestlcoin'), 'groestlcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/address.dws?'
TX_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/tx.dws?'
SANE_TARGET_RANGE= (2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF = 256
DUST_THRESHOLD = 0.001e8
HUMAN_READABLE_PART = 'grs'
