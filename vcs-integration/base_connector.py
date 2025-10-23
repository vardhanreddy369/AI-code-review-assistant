"""
Base connector class for version control systems.
Provides interface for implementing VCS-specific logic.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class BaseVCSConnector(ABC):
    """Abstract base class for VCS connectors."""
    
    def __init__(self, token: str):
        """
        Initialize connector.
        
        Args:
            token: Authentication token for VCS
        """
        self.token = token
    
    @abstractmethod
    async def get_pr_files(self, owner: str, repo: str, pr_number: int) -> List[Dict[str, Any]]:
        """Get files from a pull request."""
        pass
    
    @abstractmethod
    async def post_review(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        comments: List[Dict[str, Any]]
    ) -> bool:
        """Post review comments."""
        pass
    
    @abstractmethod
    async def get_user_info(self) -> Dict[str, str]:
        """Get authenticated user information."""
        pass
    
    @abstractmethod
    async def get_repositories(self) -> List[Dict[str, str]]:
        """Get list of accessible repositories."""
        pass
    
    @abstractmethod
    async def setup_webhook(self, repo_url: str, webhook_url: str) -> bool:
        """Setup webhook for the repository."""
        pass
