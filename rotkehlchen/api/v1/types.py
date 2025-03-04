from dataclasses import dataclass
from enum import auto
from typing import Literal, Optional, TypedDict

from rotkehlchen.accounting.structures.base import HistoryBaseEntryType
from rotkehlchen.types import SUPPORTED_CHAIN_IDS, ChecksumEvmAddress, EVMTxHash
from rotkehlchen.utils.mixins.enums import SerializableEnumNameMixin


class EvmTransactionDecodingApiData(TypedDict):
    evm_chain: SUPPORTED_CHAIN_IDS
    tx_hashes: Optional[list[EVMTxHash]]


class EvmPendingTransactionDecodingApiData(TypedDict):
    evm_chain: SUPPORTED_CHAIN_IDS
    addresses: Optional[list[ChecksumEvmAddress]]


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class IncludeExcludeFilterData:
    values: list[HistoryBaseEntryType]
    operator: Literal['IN', 'NOT IN'] = 'IN'


class ModuleWithStats(SerializableEnumNameMixin):
    """Used to validate the used module to query stats at the API stats endpoint"""
    AAVE = auto()
    COMPOUND = auto()
    LIQUITY = auto()
