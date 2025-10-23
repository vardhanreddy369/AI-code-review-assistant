"""
Bitbucket API connector.
Implements Bitbucket-specific VCS integration.
"""

import logging
import aiohttp
from typing import List, Dict, Any
from base_connector import BaseVCSConnector

logger = logging.getLogger(__name__)


class BitbucketConnector(BaseVCSConnector):
    """Bitbucket API connector."""
    
    BASE_URL = "https://api.bitbucket.org/2.0"
    
    def __init__(self, token: str, username: str):
        super().__init__(token)
        self.username = username
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    async def get_pr_files(
        self,
        workspace: str,
        repo_slug: str,
        pr_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get changed files from Bitbucket PR.
        
        Args:
            workspace: Bitbucket workspace
            repo_slug: Repository slug
            pr_id: Pull request ID
        
        Returns:
            List of files with content
        """
        logger.info(f"Fetching Bitbucket PR files: {workspace}/{repo_slug}#{pr_id}")
        
        async with aiohttp.ClientSession() as session:
            try:
                diff_url = (
                    f"{self.BASE_URL}/repositories/{workspace}/{repo_slug}/"
                    f"pullrequests/{pr_id}/diffstat"
                )
                
                async with session.get(diff_url, headers=self.headers) as resp:
                    if resp.status != 200:
                        logger.error(f"Bitbucket API error: {resp.status}")
                        return []
                    
                    data = await resp.json()
                    
                    results = []
                    for change in data.get("values", []):
                        results.append({
                            "path": change["new"]["path"],
                            "status": change["status"],
                            "lines_added": change.get("lines_added", 0),
                            "lines_removed": change.get("lines_removed", 0)
                        })
                    
                    return results
            except Exception as e:
                logger.error(f"Error fetching Bitbucket PR files: {e}")
                return []
    
    async def post_review(
        self,
        workspace: str,
        repo_slug: str,
        pr_id: int,
        comments: List[Dict[str, Any]]
    ) -> bool:
        """
        Post review comments on Bitbucket PR.
        
        Args:
            workspace: Bitbucket workspace
            repo_slug: Repository slug
            pr_id: Pull request ID
            comments: List of review comments
        
        Returns:
            Success status
        """
        logger.info(f"Posting Bitbucket review: {workspace}/{repo_slug}#{pr_id}")
        
        async with aiohttp.ClientSession() as session:
            try:
                comments_url = (
                    f"{self.BASE_URL}/repositories/{workspace}/{repo_slug}/"
                    f"pullrequests/{pr_id}/comments"
                )
                
                for comment in comments:
                    comment_data = {
                        "content": {
                            "raw": f"**{comment['severity']}**: {comment['message']}"
                        }
                    }
                    
                    async with session.post(
                        comments_url,
                        json=comment_data,
                        headers=self.headers
                    ) as resp:
                        if resp.status != 201:
                            logger.error(f"Failed to post comment: {resp.status}")
                            return False
                
                return True
            except Exception as e:
                logger.error(f"Error posting Bitbucket review: {e}")
                return False
    
    async def get_user_info(self) -> Dict[str, str]:
        """Get authenticated Bitbucket user information."""
        logger.info("Fetching Bitbucket user info")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"{self.BASE_URL}/user",
                    headers=self.headers
                ) as resp:
                    if resp.status == 200:
                        user = await resp.json()
                        return {
                            "id": user["username"],
                            "name": user.get("display_name", ""),
                            "email": user.get("email", "")
                        }
            except Exception as e:
                logger.error(f"Error fetching Bitbucket user: {e}")
            
            return {}
    
    async def get_repositories(self) -> List[Dict[str, str]]:
        """Get list of accessible Bitbucket repositories."""
        logger.info("Fetching Bitbucket repositories")
        
        async with aiohttp.ClientSession() as session:
            try:
                repos_url = f"{self.BASE_URL}/repositories?role=contributor"
                
                async with session.get(repos_url, headers=self.headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return [
                            {
                                "name": repo["name"],
                                "url": repo["links"]["html"]["href"],
                                "owner": repo["workspace"]["name"]
                            }
                            for repo in data.get("values", [])
                        ]
            except Exception as e:
                logger.error(f"Error fetching Bitbucket repos: {e}")
            
            return []
    
    async def setup_webhook(self, repo_url: str, webhook_url: str) -> bool:
        """Setup Bitbucket webhook."""
        logger.info(f"Setting up Bitbucket webhook for {repo_url}")
        
        # TODO: Implement webhook setup
        return True
