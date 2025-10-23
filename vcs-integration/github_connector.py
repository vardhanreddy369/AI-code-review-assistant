"""
GitHub API connector.
Implements GitHub-specific VCS integration.
"""

import logging
import aiohttp
from typing import List, Dict, Any, Optional
from base_connector import BaseVCSConnector

logger = logging.getLogger(__name__)


class GitHubConnector(BaseVCSConnector):
    """GitHub API connector."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: str):
        super().__init__(token)
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    async def get_pr_files(
        self,
        owner: str,
        repo: str,
        pr_number: int
    ) -> List[Dict[str, Any]]:
        """
        Get changed files from GitHub PR.
        
        Args:
            owner: Repository owner
            repo: Repository name
            pr_number: Pull request number
        
        Returns:
            List of files with content
        """
        logger.info(f"Fetching GitHub PR files: {owner}/{repo}#{pr_number}")
        
        async with aiohttp.ClientSession() as session:
            # Get PR files
            files_url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}/files"
            
            try:
                async with session.get(files_url, headers=self.headers) as resp:
                    if resp.status != 200:
                        logger.error(f"GitHub API error: {resp.status}")
                        return []
                    
                    files = await resp.json()
                    
                    # Get file contents
                    results = []
                    for file in files:
                        if file["patch"]:  # Only get changed files
                            content = await self._get_file_content(
                                session, owner, repo, file["filename"]
                            )
                            results.append({
                                "path": file["filename"],
                                "content": content,
                                "status": file["status"],
                                "changes": file["changes"]
                            })
                    
                    return results
            except Exception as e:
                logger.error(f"Error fetching GitHub PR files: {e}")
                return []
    
    async def post_review(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        comments: List[Dict[str, Any]]
    ) -> bool:
        """
        Post review comments on GitHub PR.
        
        Args:
            owner: Repository owner
            repo: Repository name
            pr_number: Pull request number
            comments: List of review comments
        
        Returns:
            Success status
        """
        logger.info(f"Posting GitHub review: {owner}/{repo}#{pr_number}")
        
        async with aiohttp.ClientSession() as session:
            review_url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
            
            try:
                # Prepare review payload
                review_data = {
                    "body": self._format_review_body(comments),
                    "event": "COMMENT",
                    "comments": [
                        {
                            "path": c["file_path"],
                            "line": c["line_number"],
                            "body": c["message"]
                        }
                        for c in comments
                    ]
                }
                
                async with session.post(review_url, json=review_data, headers=self.headers) as resp:
                    return resp.status == 200
            except Exception as e:
                logger.error(f"Error posting GitHub review: {e}")
                return False
    
    async def get_user_info(self) -> Dict[str, str]:
        """Get authenticated GitHub user information."""
        logger.info("Fetching GitHub user info")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.BASE_URL}/user", headers=self.headers) as resp:
                    if resp.status == 200:
                        user = await resp.json()
                        return {
                            "id": user["login"],
                            "name": user.get("name", ""),
                            "email": user.get("email", "")
                        }
            except Exception as e:
                logger.error(f"Error fetching GitHub user: {e}")
            
            return {}
    
    async def get_repositories(self) -> List[Dict[str, str]]:
        """Get list of accessible GitHub repositories."""
        logger.info("Fetching GitHub repositories")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"{self.BASE_URL}/user/repos",
                    headers=self.headers
                ) as resp:
                    if resp.status == 200:
                        repos = await resp.json()
                        return [
                            {
                                "name": repo["name"],
                                "url": repo["html_url"],
                                "owner": repo["owner"]["login"]
                            }
                            for repo in repos
                        ]
            except Exception as e:
                logger.error(f"Error fetching GitHub repos: {e}")
            
            return []
    
    async def setup_webhook(self, repo_url: str, webhook_url: str) -> bool:
        """Setup GitHub webhook."""
        logger.info(f"Setting up GitHub webhook for {repo_url}")
        
        # TODO: Implement webhook setup
        return True
    
    async def _get_file_content(
        self,
        session: aiohttp.ClientSession,
        owner: str,
        repo: str,
        path: str
    ) -> str:
        """Get file content from GitHub."""
        try:
            url = f"{self.BASE_URL}/repos/{owner}/{repo}/contents/{path}"
            async with session.get(url, headers=self.headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("content", "")
        except Exception as e:
            logger.error(f"Error fetching file content: {e}")
        
        return ""
    
    @staticmethod
    def _format_review_body(comments: List[Dict]) -> str:
        """Format comments into review body."""
        body = "## AI Code Review\n\n"
        
        for comment in comments:
            body += f"- **{comment['severity'].upper()}**: {comment['message']}\n"
        
        return body
