import logging
import re
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_tasks(task_list_str):
    tasks = []
    lines = re.split(r"\n", task_list_str)
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^\d+\.\s*|^-\s*|^\*\s*", "", line)
        importance = "Medium"
        importance_match = re.search(r"\[(High|Medium|Low)\]", line, re.IGNORECASE)
        if importance_match:
            importance = importance_match.group(1).capitalize()
            line = line.replace(importance_match.group(0), "").strip()
        urgency = "Normal"
        urgency_match = re.search(r"\((Urgent|Soon|Later|Normal)\)", line, re.IGNORECASE)
        if urgency_match:
            urgency = urgency_match.group(1).capitalize()
            line = line.replace(urgency_match.group(0), "").strip()
        
        tasks.append({
            "task": line,
            "importance": importance,
            "urgency": urgency,
            "score": 0
        })
    
    return tasks

def run(params):
    try:
        task_list = params.get("task_list", "")
        if not task_list:
            return {"error": "No task list provided", "success": False}
        tasks = parse_tasks(task_list)
        return {
            "success": True,
            "tasks": tasks,
            "count": len(tasks)
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": f"Error processing tasks: {str(e)}", "success": False}