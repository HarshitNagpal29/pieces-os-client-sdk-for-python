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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from pieces_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_client.models.persons import Persons

class QGPTPersonsRelatedOutput(BaseModel):
    """
    This model is used for the output of the /qgpt/related/persons endpoint.  Explanations here is a custom object with key value pairs, when the key is the personUUId and the value is an explanation as to why this person was reccommended.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    persons: Persons = Field(...)
    explanations: Optional[Dict[str, StrictStr]] = Field(None, description="This is a Map<String, String> where the the key is a person id. and the value is the explanation.")
    __properties = ["schema", "persons", "explanations"]

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
    def from_json(cls, json_str: str) -> QGPTPersonsRelatedOutput:
        """Create an instance of QGPTPersonsRelatedOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTPersonsRelatedOutput:
        """Create an instance of QGPTPersonsRelatedOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTPersonsRelatedOutput.parse_obj(obj)

        _obj = QGPTPersonsRelatedOutput.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "persons": Persons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "explanations": obj.get("explanations")
        })
        return _obj


