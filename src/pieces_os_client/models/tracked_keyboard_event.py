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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema

class TrackedKeyboardEvent(BaseModel):
    """
    This is a model that will hold relavent information in relation to a keyboard(including shortcuts) analytics event (usage).  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    description: StrictStr = Field(..., description="this is a description of the event, optional.")
    shortcut: conlist(StrictInt) = Field(..., description="this is an array of of ascii values that represent numerics on your keyboard.")
    __properties = ["schema", "description", "shortcut"]

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
    def from_json(cls, json_str: str) -> TrackedKeyboardEvent:
        """Create an instance of TrackedKeyboardEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackedKeyboardEvent:
        """Create an instance of TrackedKeyboardEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackedKeyboardEvent.parse_obj(obj)

        _obj = TrackedKeyboardEvent.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "description": obj.get("description"),
            "shortcut": obj.get("shortcut")
        })
        return _obj


