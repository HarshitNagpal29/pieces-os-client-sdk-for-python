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
from pydantic import BaseModel, Field, StrictStr, validator
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema

class TrackedFormatEventIdentifierDescriptionPairs(BaseModel):
    """
    This is a model that allows us to send send over super specific format related events such as copied, deleted, downloaded, etc  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    format_created: Optional[StrictStr] = Field(None, description="The key value pair for an asset being created.")
    format_copied: Optional[StrictStr] = Field(None, description="If a format was copied entirely")
    format_partially_copied: Optional[StrictStr] = Field(None, description="If a format was copied partially")
    format_downloaded: Optional[StrictStr] = Field(None, description="If a format was downloaded")
    format_deleted: Optional[StrictStr] = Field(None, description="If an format was deleted")
    format_generic_classification_updated: Optional[StrictStr] = Field(None, description="If a generic classification was changed on a format")
    format_specific_classification_updated: Optional[StrictStr] = Field(None, description="If a specific classification was changed on a format")
    format_updated: Optional[StrictStr] = Field(None, description="a format was updated, generic update.")
    format_inserted: Optional[StrictStr] = Field(None, description="a format was inserted")
    format_value_edited: Optional[StrictStr] = Field(None, description="a format's value was update ie, the text, etc...")
    __properties = ["schema", "format_created", "format_copied", "format_partially_copied", "format_downloaded", "format_deleted", "format_generic_classification_updated", "format_specific_classification_updated", "format_updated", "format_inserted", "format_value_edited"]

    @validator('format_created')
    def format_created_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_format_was_created'):
            raise ValueError("must be one of enum values ('a_format_was_created')")
        return value

    @validator('format_copied')
    def format_copied_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_format_was_entirely_copied'):
            raise ValueError("must be one of enum values ('if_a_format_was_entirely_copied')")
        return value

    @validator('format_partially_copied')
    def format_partially_copied_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_format_was_partially_copied'):
            raise ValueError("must be one of enum values ('if_a_format_was_partially_copied')")
        return value

    @validator('format_downloaded')
    def format_downloaded_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_format_was_downloaded'):
            raise ValueError("must be one of enum values ('if_a_format_was_downloaded')")
        return value

    @validator('format_deleted')
    def format_deleted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_format_was_deleted'):
            raise ValueError("must be one of enum values ('if_a_format_was_deleted')")
        return value

    @validator('format_generic_classification_updated')
    def format_generic_classification_updated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_generic_classification_was_changed_on_a_format'):
            raise ValueError("must be one of enum values ('if_a_generic_classification_was_changed_on_a_format')")
        return value

    @validator('format_specific_classification_updated')
    def format_specific_classification_updated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('if_a_specific_classification_was_changed_on_a_format'):
            raise ValueError("must be one of enum values ('if_a_specific_classification_was_changed_on_a_format')")
        return value

    @validator('format_updated')
    def format_updated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_format_was_updated'):
            raise ValueError("must be one of enum values ('a_format_was_updated')")
        return value

    @validator('format_inserted')
    def format_inserted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_format_was_inserted'):
            raise ValueError("must be one of enum values ('a_format_was_inserted')")
        return value

    @validator('format_value_edited')
    def format_value_edited_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a_format_value_was_edited'):
            raise ValueError("must be one of enum values ('a_format_value_was_edited')")
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
    def from_json(cls, json_str: str) -> TrackedFormatEventIdentifierDescriptionPairs:
        """Create an instance of TrackedFormatEventIdentifierDescriptionPairs from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TrackedFormatEventIdentifierDescriptionPairs:
        """Create an instance of TrackedFormatEventIdentifierDescriptionPairs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackedFormatEventIdentifierDescriptionPairs.parse_obj(obj)

        _obj = TrackedFormatEventIdentifierDescriptionPairs.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "format_created": obj.get("format_created"),
            "format_copied": obj.get("format_copied"),
            "format_partially_copied": obj.get("format_partially_copied"),
            "format_downloaded": obj.get("format_downloaded"),
            "format_deleted": obj.get("format_deleted"),
            "format_generic_classification_updated": obj.get("format_generic_classification_updated"),
            "format_specific_classification_updated": obj.get("format_specific_classification_updated"),
            "format_updated": obj.get("format_updated"),
            "format_inserted": obj.get("format_inserted"),
            "format_value_edited": obj.get("format_value_edited")
        })
        return _obj


