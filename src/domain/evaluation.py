"""
Domain objects for evaluation in the Observation-Evaluation Protocol.

This module defines the core evaluation types and structures used
in the deterministic decision-making phase of the protocol.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class EvaluationType(Enum):
    """Enumeration of different evaluation types."""

    SEMANTIC_SCORING = "semantic_scoring"
    HEURISTIC_ROUTING = "heuristic_routing"
    REASONING = "reasoning"
    VALIDATION = "validation"
    ADVERSARIAL_REVIEW = "adversarial_review"


@dataclass
class StructuredInsight:
    """
    Represents a structured insight derived from observations.

    This is the "So What" - the processed, reasoned interpretation
    of raw observations that drives decision-making.
    """

    type: EvaluationType
    content: Any
    confidence: float  # Between 0.0 and 1.0
    metadata: dict[str, Any] | None = None
    source_observations: list[str] | None = None  # References to original observations

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
        if self.source_observations is None:
            self.source_observations = []

    def to_dict(self) -> dict[str, Any]:
        """Convert insight to dictionary representation."""
        return {
            "type": self.type.value,
            "content": self.content,
            "confidence": self.confidence,
            "metadata": self.metadata,
            "source_observations": self.source_observations,
        }


@dataclass
class EvaluationContext:
    """
    Context information for evaluations.

    Provides additional context about the evaluation process and decision-making.
    """

    task_id: str
    evaluation_type: EvaluationType
    agent_id: str | None = None
    dependencies: list[str] | None = None  # Dependencies on other insights

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

    def to_dict(self) -> dict[str, Any]:
        """Convert context to dictionary representation."""
        return {
            "task_id": self.task_id,
            "evaluation_type": self.evaluation_type.value,
            "agent_id": self.agent_id,
            "dependencies": self.dependencies,
        }
