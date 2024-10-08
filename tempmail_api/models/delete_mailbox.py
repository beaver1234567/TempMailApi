import json

from dataclasses import dataclass
from typing import List, Optional, Any

from .rpc import JsonRpcMessage, JsonRpcRequest, JsonRpcResponse


@dataclass
class DeleteEmailParams:
    sid: str = None
    email: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class DeleteEmailResult:
    sid: str = None
    mailbox: str = None

    def __init__(self, data: dict):
        if data is not None:
            self.__dict__ = data


@dataclass
class MailboxDeleteRequest(JsonRpcRequest):
    method: str = "mailbox.delete"
    params: DeleteEmailParams = None

    def __init__(self, params: DeleteEmailParams):
        super().__init__(None)
        self.method = "mailbox.delete"
        self.params = params


@dataclass
class MailboxDeleteResponse(JsonRpcResponse):
    result: DeleteEmailResult
     
    def __init__(self, params: dict):
        super().__init__(params)
        self.result = DeleteEmailResult(self.result)