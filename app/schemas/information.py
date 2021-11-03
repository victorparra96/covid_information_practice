from tortoise.contrib.pydantic import pydantic_model_creator

from models import Information

Information_Pydantic = pydantic_model_creator(Information)
Information_InPydantic = pydantic_model_creator(
    Information,
    name="InformationIn",
    exclude_readonly=True)
Information_InPydantic = pydantic_model_creator(
    Information,
    name="InformationOut",
    exclude=("id", ))