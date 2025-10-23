"""
ML inference service.
Provides real-time predictions from trained models.
"""

import torch
import logging
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class CodeReviewInference:
    """Inference engine for code review models."""
    
    def __init__(
        self,
        model_path: str = "microsoft/codebert-base",
        device: str = "cuda" if torch.cuda.is_available() else "cpu"
    ):
        """
        Initialize inference engine.
        
        Args:
            model_path: Path to model or HuggingFace model ID
            device: cuda or cpu
        """
        self.model_path = model_path
        self.device = device
        self.tokenizer = None
        self.model = None
        
        logger.info(f"Initializing inference engine with {model_path} on {device}")
    
    def load_model(self):
        """Load model and tokenizer."""
        logger.info(f"Loading model: {self.model_path}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_path,
            num_labels=2
        )
        self.model.to(self.device)
        self.model.eval()
    
    def predict(self, code: str) -> Dict[str, Any]:
        """
        Predict if code contains issues.
        
        Args:
            code: Source code to analyze
        
        Returns:
            Prediction with confidence scores
        """
        logger.debug("Running inference on code snippet")
        
        inputs = self.tokenizer(
            code,
            padding="max_length",
            truncation=True,
            max_length=512,
            return_tensors="pt"
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1)
        
        pred_class = torch.argmax(logits, dim=-1).item()
        scores = probabilities[0].cpu().numpy()
        
        return {
            "has_issue": bool(pred_class),
            "confidence": float(scores[pred_class]),
            "no_issue_score": float(scores[0]),
            "issue_score": float(scores[1])
        }
    
    def predict_batch(self, codes: List[str]) -> List[Dict[str, Any]]:
        """
        Predict on multiple code snippets.
        
        Args:
            codes: List of code snippets
        
        Returns:
            List of predictions
        """
        logger.debug(f"Running batch inference on {len(codes)} snippets")
        
        results = []
        for code in codes:
            results.append(self.predict(code))
        
        return results
    
    def analyze_file(self, file_content: str) -> Dict[str, Any]:
        """
        Analyze entire file and identify problematic sections.
        
        Args:
            file_content: Complete file content
        
        Returns:
            File-level analysis with line-by-line insights
        """
        logger.debug("Analyzing file")
        
        lines = file_content.split("\n")
        issues = []
        
        # Analyze in chunks
        for i, line in enumerate(lines):
            if line.strip():  # Skip empty lines
                prediction = self.predict(line)
                if prediction["has_issue"]:
                    issues.append({
                        "line_number": i + 1,
                        "content": line,
                        "confidence": prediction["confidence"]
                    })
        
        return {
            "total_lines": len(lines),
            "total_issues": len(issues),
            "issues": issues,
            "risk_level": self._calculate_risk_level(issues, len(lines))
        }
    
    @staticmethod
    def _calculate_risk_level(issues: List[Dict], total_lines: int) -> str:
        """Calculate risk level based on issue density."""
        if not total_lines:
            return "unknown"
        
        density = len(issues) / total_lines
        
        if density > 0.1:
            return "critical"
        elif density > 0.05:
            return "high"
        elif density > 0.01:
            return "medium"
        elif density > 0:
            return "low"
        else:
            return "none"


if __name__ == "__main__":
    # Example usage
    inference = CodeReviewInference()
    inference.load_model()
    
    code_sample = """
    def unsafe_query(user_id):
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        return db.execute(query)
    """
    
    result = inference.predict(code_sample)
    print(result)
