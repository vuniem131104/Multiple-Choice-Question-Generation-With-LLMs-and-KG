from __future__ import annotations

from base import BaseModel


class DescriptionInfo(BaseModel):
    uid: str
    embedding: list
    text: str
    type: str


class ClusterInfo(BaseModel):
    description_ids: list[str]
    description_text: list[str]
    text: str
    embedding: list


class ClusterInfos(BaseModel):
    clusters: list[ClusterInfo]
    type: str
