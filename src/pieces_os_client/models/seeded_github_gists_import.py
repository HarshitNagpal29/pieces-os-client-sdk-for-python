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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema

class SeededGithubGistsImport(BaseModel):
    """
    This is the body of the /github/gists/import,  by default we will look for everything from your private gists, (TODO hook up public gists.)&& get clever  currently we will not ensure that this is a good pieces for you but we will just get you the gist and let you do what you want with it(room for improvement, if we want to layer in advanced pieces discovery)  For the future, we might want to add a max number of assets that are returned from this.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    application: StrictStr = Field(..., description="application id.")
    public: Optional[StrictBool] = Field(None, description="This will default to false.(ie private), currently not supporting pulling public gists.")
    __properties = ["schema", "application", "public"]

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
    def from_json(cls, json_str: str) -> SeededGithubGistsImport:
        """Create an instance of SeededGithubGistsImport from a JSON string"""
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
    def from_dict(cls, obj: dict) -> SeededGithubGistsImport:
        """Create an instance of SeededGithubGistsImport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededGithubGistsImport.parse_obj(obj)

        _obj = SeededGithubGistsImport.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "application": obj.get("application"),
            "public": obj.get("public")
        })
        return _obj


