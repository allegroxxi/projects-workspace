"""
Domain objects for observations in the Observation-Evaluation Protocol.

This module defines the core observation types and structures used
in the non-deterministic discovery phase of the protocol.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class ObservationType(Enum):
    """Enumeration of different observation types."""

    ENVIRONMENT = "environment"
    CODEBASE = "codebase"
    RESEARCH = "research"
    USER_INPUT = "user_input"
    SYSTEM_STATE = "system_state"


@dataclass
class RawObservation:
    """
    Represents a raw observation from the environment.

    This is the "What" - the factual data collected during the discovery phase.
    """

    type: ObservationType
    content: Any
    metadata: dict[str, Any] | None = None
    timestamp: float | None = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> dict[str, Any]:
        """Convert observation to dictionary representation."""
        return {
            "type": self.type.value,
            "content": self.content,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }


@dataclass
class ObservationContext:
    """
    Context information for observations.

    Provides additional context about when and where an observation was made.
    """

    source: str
    environment: str
    task_id: str | None = None
    agent_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert context to dictionary representation."""
        return {
            "source": self.source,
            "environment": self.environment,
            "task_id": self.task_id,
            "agent_id": self.agent_id,
        }
