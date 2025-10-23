"""
GitLab API connector.
Implements GitLab-specific VCS integration.
"""

import logging
import aiohttp
from typing import List, Dict, Any
from base_connector import BaseVCSConnector

logger = logging.getLogger(__name__)


class GitLabConnector(BaseVCSConnector):
    """GitLab API connector."""
    
    def __init__(self, token: str, gitlab_url: str = "https://gitlab.com"):
        super().__init__(token)
        self.base_url = gitlab_url
        self.headers = {
            "PRIVATE-TOKEN": token,
            "Content-Type": "application/json"
        }
    
    async def get_mr_files(
        self,
        group: str,
        project: str,
        mr_number: int
    ) -> List[Dict[str, Any]]:
        """
        Get changed files from GitLab MR.
        
        Args:
            group: Project group
            project: Project name
            mr_number: Merge request number
        
        Returns:
            List of files with content
        """
        logger.info(f"Fetching GitLab MR files: {group}/{project}!{mr_number}")
        
        project_id = f"{group}%2F{project}"
        
        async with aiohttp.ClientSession() as session:
            try:
                changes_url = (
                    f"{self.base_url}/api/v4/projects/{project_id}/"
                    f"merge_requests/{mr_number}/changes"
                )
                
                async with session.get(changes_url, headers=self.headers) as resp:
                    if resp.status != 200:
                        logger.error(f"GitLab API error: {resp.status}")
                        return []
                    
                    data = await resp.json()
                    
                    results = []
                    for change in data.get("changes", []):
                        results.append({
                            "path": change["new_path"],
                            "content": change.get("new_file_content", ""),
                            "status": change.get("new_file", "added")
                        })
                    
                    return results
            except Exception as e:
                logger.error(f"Error fetching GitLab MR files: {e}")
                return []
    
    async def post_mr_review(
        self,
        group: str,
        project: str,
        mr_number: int,
        comments: List[Dict[str, Any]]
    ) -> bool:
        """
        Post review comments on GitLab MR.
        
        Args:
            group: Project group
            project: Project name
            mr_number: Merge request number
            comments: List of review comments
        
        Returns:
            Success status
        """
        logger.info(f"Posting GitLab review: {group}/{project}!{mr_number}")
        
        project_id = f"{group}%2F{project}"
        
        async with aiohttp.ClientSession() as session:
            try:
                notes_url = (
                    f"{self.base_url}/api/v4/projects/{project_id}/"
                    f"merge_requests/{mr_number}/notes"
                )
                
                for comment in comments:
                    note_data = {
                        "body": f"**{comment['severity']}**: {comment['message']}"
                    }
                    
                    async with session.post(
                        notes_url,
                        json=note_data,
                        headers=self.headers
                    ) as resp:
                        if resp.status != 201:
                            logger.error(f"Failed to post comment: {resp.status}")
                            return False
                
                return True
            except Exception as e:
                logger.error(f"Error posting GitLab review: {e}")
                return False
    
    async def get_user_info(self) -> Dict[str, str]:
        """Get authenticated GitLab user information."""
        logger.info("Fetching GitLab user info")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"{self.base_url}/api/v4/user",
                    headers=self.headers
                ) as resp:
                    if resp.status == 200:
                        user = await resp.json()
                        return {
                            "id": str(user["id"]),
                            "name": user.get("name", ""),
                            "email": user.get("email", "")
                        }
            except Exception as e:
                logger.error(f"Error fetching GitLab user: {e}")
            
            return {}
    
    async def get_repositories(self) -> List[Dict[str, str]]:
        """Get list of accessible GitLab projects."""
        logger.info("Fetching GitLab projects")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"{self.base_url}/api/v4/projects",
                    headers=self.headers
                ) as resp:
                    if resp.status == 200:
                        projects = await resp.json()
                        return [
                            {
                                "name": project["name"],
                                "url": project["web_url"],
                                "owner": project["namespace"]["name"]
                            }
                            for project in projects
                        ]
            except Exception as e:
                logger.error(f"Error fetching GitLab projects: {e}")
            
            return []
    
    async def setup_webhook(self, repo_url: str, webhook_url: str) -> bool:
        """Setup GitLab webhook."""
        logger.info(f"Setting up GitLab webhook for {repo_url}")
        
        # TODO: Implement webhook setup
        return True
    
    # Implement abstract methods from BaseVCSConnector
    async def get_pr_files(self, owner: str, repo: str, pr_number: int) -> List[Dict[str, Any]]:
        """Redirect to get_mr_files for consistency."""
        return await self.get_mr_files(owner, repo, pr_number)
    
    async def post_review(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        comments: List[Dict[str, Any]]
    ) -> bool:
        """Redirect to post_mr_review for consistency."""
        return await self.post_mr_review(owner, repo, pr_number, comments)
