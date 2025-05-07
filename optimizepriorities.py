from typing import List, Dict

class OptimizePriorities:
    def __init__(self):
        self.task_queue: List[Dict] = []

    def add_task(self, name: str, impact: int, urgency: int, feasibility: int):
        score = self.compute_score(impact, urgency, feasibility)
        self.task_queue.append({
            "name": name,
            "impact": impact,
            "urgency": urgency,
            "feasibility": feasibility,
            "score": score
        })
        self.task_queue.sort(key=lambda x: x["score"], reverse=True)

    def compute_score(self, impact: int, urgency: int, feasibility: int) -> float:
        return round((impact * 0.5 + urgency * 0.3 + feasibility * 0.2), 2)

    def get_top_tasks(self, limit: int = 5) -> List[Dict]:
        return self.task_queue[:limit]

    def recommend_pause(self) -> bool:
        return any(task["impact"] > 7 and task["feasibility"] < 3 for task in self.task_queue)
