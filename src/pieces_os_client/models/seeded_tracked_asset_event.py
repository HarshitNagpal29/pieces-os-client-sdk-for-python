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
from pydantic import BaseModel, Field
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_client.models.tracked_asset_event_identifier_description_pairs import TrackedAssetEventIdentifierDescriptionPairs

class SeededTrackedAssetEvent(BaseModel):
    """
    This seeded tracked asset event will be recieved by a context on the OS Server side, which will then be able to look up the asset id and structure the asset for shipment to Segment aka a fully built TrackedAssetEvent  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    asset: ReferencedAsset = Field(...)
    identifier_description_pair: TrackedAssetEventIdentifierDescriptionPairs = Field(...)
    metadata: Optional[TrackedAssetEventMetadata] = None
    __properties = ["schema", "asset", "identifier_description_pair", "metadata"]

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
    def from_json(cls, json_str: str) -> SeededTrackedAssetEvent:
        """Create an instance of SeededTrackedAssetEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identifier_description_pair
        if self.identifier_description_pair:
            _dict['identifier_description_pair'] = self.identifier_description_pair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededTrackedAssetEvent:
        """Create an instance of SeededTrackedAssetEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededTrackedAssetEvent.parse_obj(obj)

        _obj = SeededTrackedAssetEvent.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "asset": ReferencedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "identifier_description_pair": TrackedAssetEventIdentifierDescriptionPairs.from_dict(obj.get("identifier_description_pair")) if obj.get("identifier_description_pair") is not None else None,
            "metadata": TrackedAssetEventMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj

from pieces_client.models.referenced_asset import ReferencedAsset
from pieces_client.models.tracked_asset_event_metadata import TrackedAssetEventMetadata
SeededTrackedAssetEvent.update_forward_refs()

