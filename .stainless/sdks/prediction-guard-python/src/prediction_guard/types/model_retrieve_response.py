# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ModelRetrieveResponse", "Data", "DataCapabilities"]


class DataCapabilities(BaseModel):
    """The available capabilities of the model."""

    chat_completion: Optional[bool] = None

    chat_with_image: Optional[bool] = None

    completion: Optional[bool] = None

    detokenize: Optional[bool] = None

    embedding: Optional[bool] = None

    embedding_with_image: Optional[bool] = None

    reasoning: Optional[bool] = None

    rerank: Optional[bool] = None

    tokenize: Optional[bool] = None

    tool_calling: Optional[bool] = None


class Data(BaseModel):
    id: Optional[str] = None
    """The id of the model."""

    capabilities: Optional[DataCapabilities] = None
    """The available capabilities of the model."""

    created: Optional[int] = None
    """The date the model was added."""

    description: Optional[str] = None
    """A short description of the model."""

    max_context_length: Optional[int] = None
    """The max context length of the model."""

    object: Optional[str] = None
    """The object type (model)."""

    owned_by: Optional[str] = None
    """The name of the organization that owns the model (from huggingface)."""

    prompt_format: Optional[str] = None
    """The name of the prompt format (if any) the model uses."""


class ModelRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
    """The available models."""

    object: Optional[str] = None
    """Type of object (list)."""
