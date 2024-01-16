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


from typing import Optional
from pydantic import BaseModel, Field, constr, validator
from pieces_client.models.interacted_asset_interactions import InteractedAssetInteractions

class InteractedAsset(BaseModel):
    """
    A model that represents an asset that has been interacted with.   # noqa: E501
    """
    asset: Optional[constr(strict=True, max_length=36, min_length=36)] = Field(None, description="A uuid model. 36 Characters (4 Dashes, 32 Numbers/Letters) ")
    interactions: Optional[InteractedAssetInteractions] = None
    __properties = ["asset", "interactions"]

    @validator('asset')
    def asset_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}", value):
            raise ValueError(r"must validate the regular expression /[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}/")
        return value

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
    def from_json(cls, json_str: str) -> InteractedAsset:
        """Create an instance of InteractedAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of interactions
        if self.interactions:
            _dict['interactions'] = self.interactions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InteractedAsset:
        """Create an instance of InteractedAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InteractedAsset.parse_obj(obj)

        _obj = InteractedAsset.parse_obj({
            "asset": obj.get("asset"),
            "interactions": InteractedAssetInteractions.from_dict(obj.get("interactions")) if obj.get("interactions") is not None else None
        })
        return _obj


