# This file is part of the Trezor project.
#
# Copyright (C) 2025 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from typing import TYPE_CHECKING

from . import messages
from .tools import workflow

if TYPE_CHECKING:
    from .client import Session
    from .protobuf import MessageType
    from .tools import Address


@workflow(capability=messages.Capability.Ecash)
def sign_stake(
    session: "Session",
    address_n: "Address",
    txid: bytes,
    index: int,
    amount: int,
    height: int,
    is_coinbase: bool,
    expiration_time: int,
    master_pubkey: bytes,
) -> "MessageType":
    """Sign an avalanche stake.

    Returns the signature and its public key.
    """

    return session.call(
        messages.EcashSignStake(
            address_n=address_n,
            txid=txid,
            index=index,
            amount=amount,
            height=height,
            is_coinbase=is_coinbase,
            expiration_time=expiration_time,
            master_pubkey=master_pubkey,
        ),
        expect=messages.EcashStakeSignature,
    )
