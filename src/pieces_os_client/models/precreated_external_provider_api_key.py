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
from pieces_client.models.auth0_open_ai_user_metadata import Auth0OpenAIUserMetadata
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema

class PrecreatedExternalProviderApiKey(BaseModel):
    """
    This is the input model for /external_provider/api_key/create  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    user: StrictStr = Field(..., description="This is the ID of the User.")
    open_ai: Optional[Auth0OpenAIUserMetadata] = Field(None, alias="open_AI")
    __properties = ["schema", "user", "open_AI"]

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
    def from_json(cls, json_str: str) -> PrecreatedExternalProviderApiKey:
        """Create an instance of PrecreatedExternalProviderApiKey from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of open_ai
        if self.open_ai:
            _dict['open_AI'] = self.open_ai.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrecreatedExternalProviderApiKey:
        """Create an instance of PrecreatedExternalProviderApiKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PrecreatedExternalProviderApiKey.parse_obj(obj)

        _obj = PrecreatedExternalProviderApiKey.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "user": obj.get("user"),
            "open_ai": Auth0OpenAIUserMetadata.from_dict(obj.get("open_AI")) if obj.get("open_AI") is not None else None
        })
        return _obj


