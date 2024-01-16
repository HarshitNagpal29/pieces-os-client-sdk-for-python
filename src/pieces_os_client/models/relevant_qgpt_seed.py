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
from pydantic import BaseModel, Field, StrictStr
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_client.models.referenced_asset import ReferencedAsset
from pieces_client.models.seed import Seed

class RelevantQGPTSeed(BaseModel):
    """
    This is a generic model used, to wrap a seed, as well as give an identifier used to further identifiy this snippet.  Seed is optional here because you may just want to provide the id, and not the original seed.  id is also optional here as you may provide an id or not here.(however with specific endpoint this ID is a guarentee.)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    id: Optional[StrictStr] = None
    seed: Optional[Seed] = None
    path: Optional[StrictStr] = Field(None, description="This is an optional file path")
    asset: Optional[ReferencedAsset] = None
    __properties = ["schema", "id", "seed", "path", "asset"]

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
    def from_json(cls, json_str: str) -> RelevantQGPTSeed:
        """Create an instance of RelevantQGPTSeed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of seed
        if self.seed:
            _dict['seed'] = self.seed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RelevantQGPTSeed:
        """Create an instance of RelevantQGPTSeed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RelevantQGPTSeed.parse_obj(obj)

        _obj = RelevantQGPTSeed.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "seed": Seed.from_dict(obj.get("seed")) if obj.get("seed") is not None else None,
            "path": obj.get("path"),
            "asset": ReferencedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None
        })
        return _obj


