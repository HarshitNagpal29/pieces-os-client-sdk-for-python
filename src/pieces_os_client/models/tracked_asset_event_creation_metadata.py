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
from pieces_client.models.tracked_asset_event_creation_metadata_clipboard import TrackedAssetEventCreationMetadataClipboard
from pieces_client.models.tracked_asset_event_creation_metadata_file import TrackedAssetEventCreationMetadataFile

class TrackedAssetEventCreationMetadata(BaseModel):
    """
    Metadata attached to a creation event on an Asset  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    clipboard: Optional[TrackedAssetEventCreationMetadataClipboard] = None
    file: Optional[TrackedAssetEventCreationMetadataFile] = None
    __properties = ["schema", "clipboard", "file"]

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
    def from_json(cls, json_str: str) -> TrackedAssetEventCreationMetadata:
        """Create an instance of TrackedAssetEventCreationMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of clipboard
        if self.clipboard:
            _dict['clipboard'] = self.clipboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackedAssetEventCreationMetadata:
        """Create an instance of TrackedAssetEventCreationMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackedAssetEventCreationMetadata.parse_obj(obj)

        _obj = TrackedAssetEventCreationMetadata.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "clipboard": TrackedAssetEventCreationMetadataClipboard.from_dict(obj.get("clipboard")) if obj.get("clipboard") is not None else None,
            "file": TrackedAssetEventCreationMetadataFile.from_dict(obj.get("file")) if obj.get("file") is not None else None
        })
        return _obj


