from _typeshed import Incomplete
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

import pika.connection
from pika.adapters.utils import nbio_interface

_DeferredQueue: TypeAlias = Any  # TODO: twisted.internet.defer.DeferredQueue
_Protocol: TypeAlias = Any  # TODO: twisted.internet.protocol.Protocol

LOGGER: Incomplete

class ClosableDeferredQueue(_DeferredQueue):
    closed: Incomplete
    def __init__(self, size: Incomplete | None = ..., backlog: Incomplete | None = ...) -> None: ...
    def put(self, obj): ...
    def get(self): ...
    pending: Incomplete
    def close(self, reason) -> None: ...

class ReceivedMessage(NamedTuple):
    channel: Incomplete
    method: Incomplete
    properties: Incomplete
    body: Incomplete

class TwistedChannel:
    on_closed: Incomplete
    def __init__(self, channel) -> None: ...
    @property
    def channel_number(self): ...
    @property
    def connection(self): ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    @property
    def flow_active(self): ...
    @property
    def consumer_tags(self): ...
    def callback_deferred(self, deferred, replies) -> None: ...
    def add_on_return_callback(self, callback): ...
    def basic_ack(self, delivery_tag: int = ..., multiple: bool = ...): ...
    def basic_cancel(self, consumer_tag: str = ...): ...
    def basic_consume(
        self,
        queue,
        auto_ack: bool = ...,
        exclusive: bool = ...,
        consumer_tag: Incomplete | None = ...,
        arguments: Incomplete | None = ...,
    ): ...
    def basic_get(self, queue, auto_ack: bool = ...): ...
    def basic_nack(self, delivery_tag: Incomplete | None = ..., multiple: bool = ..., requeue: bool = ...): ...
    def basic_publish(self, exchange, routing_key, body, properties: Incomplete | None = ..., mandatory: bool = ...): ...
    def basic_qos(self, prefetch_size: int = ..., prefetch_count: int = ..., global_qos: bool = ...): ...
    def basic_reject(self, delivery_tag, requeue: bool = ...): ...
    def basic_recover(self, requeue: bool = ...): ...
    def close(self, reply_code: int = ..., reply_text: str = ...): ...
    def confirm_delivery(self): ...
    def exchange_bind(self, destination, source, routing_key: str = ..., arguments: Incomplete | None = ...): ...
    def exchange_declare(
        self,
        exchange,
        exchange_type=...,
        passive: bool = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        internal: bool = ...,
        arguments: Incomplete | None = ...,
    ): ...
    def exchange_delete(self, exchange: Incomplete | None = ..., if_unused: bool = ...): ...
    def exchange_unbind(
        self,
        destination: Incomplete | None = ...,
        source: Incomplete | None = ...,
        routing_key: str = ...,
        arguments: Incomplete | None = ...,
    ): ...
    def flow(self, active): ...
    def open(self): ...
    def queue_bind(self, queue, exchange, routing_key: Incomplete | None = ..., arguments: Incomplete | None = ...): ...
    def queue_declare(
        self,
        queue,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        arguments: Incomplete | None = ...,
    ): ...
    def queue_delete(self, queue, if_unused: bool = ..., if_empty: bool = ...): ...
    def queue_purge(self, queue): ...
    def queue_unbind(
        self, queue, exchange: Incomplete | None = ..., routing_key: Incomplete | None = ..., arguments: Incomplete | None = ...
    ): ...
    def tx_commit(self): ...
    def tx_rollback(self): ...
    def tx_select(self): ...

class _TwistedConnectionAdapter(pika.connection.Connection):
    def __init__(self, parameters, on_open_callback, on_open_error_callback, on_close_callback, custom_reactor) -> None: ...
    def connection_made(self, transport) -> None: ...
    def connection_lost(self, error) -> None: ...
    def data_received(self, data) -> None: ...

class TwistedProtocolConnection(_Protocol):
    ready: Incomplete
    closed: Incomplete
    def __init__(self, parameters: Incomplete | None = ..., custom_reactor: Incomplete | None = ...) -> None: ...
    def channel(self, channel_number: Incomplete | None = ...): ...
    @property
    def is_open(self): ...
    @property
    def is_closed(self): ...
    def close(self, reply_code: int = ..., reply_text: str = ...): ...
    def dataReceived(self, data) -> None: ...
    def connectionLost(self, reason=...) -> None: ...
    def makeConnection(self, transport) -> None: ...
    def connectionReady(self): ...

class _TimerHandle(nbio_interface.AbstractTimerReference):
    def __init__(self, handle) -> None: ...
    def cancel(self) -> None: ...
