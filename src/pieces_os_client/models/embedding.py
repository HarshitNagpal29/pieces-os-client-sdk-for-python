# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from pieces_client.models.grouped_timestamp import GroupedTimestamp
from pieces_client.models.model import Model

class Embedding(BaseModel):
    """
      # noqa: E501
    """
    raw: conlist(Union[StrictFloat, StrictInt]) = Field(..., description="this is the raw value of the embedding")
    model: Model = Field(...)
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    __properties = ["raw", "model", "created", "updated", "deleted"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Embedding:
        """Create an instance of Embedding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Embedding:
        """Create an instance of Embedding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Embedding.parse_obj(obj)

        _obj = Embedding.parse_obj({
            "raw": obj.get("raw"),
            "model": Model.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None
        })
        return _obj


