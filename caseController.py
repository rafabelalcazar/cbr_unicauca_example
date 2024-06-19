from typing import List, Dict, Any
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from pymongo import MongoClient

class Case:
    def __init__(self, problem: Dict[str, Any], solution: Any):
        self.problem = problem
        self.solution = solution
        
class CaseBase:
    def __init__(self):
        self.cases: List[Case] = []
    # def __init__(self, db_name: str, collection_name: str, uri: str = "mongodb://localhost:27017/"):
    #     self.client = MongoClient(uri)
    #     self.db = self.client[db_name]
    #     self.collection = self.db[collection_name]

    def add_case(self, case: Case):
        self.cases.append(case)
        # self.collection.insert_one({"problem": case.problem, "solution": case.solution})
        
    # def get_all_cases(self) -> List[Case]:
    #     cases = []
    #     for document in self.collection.find():
    #         case = Case(problem=document["problem"], solution=document["solution"])
    #         cases.append(case)
    #     return cases
    
    def find_most_similar_case(self, new_problem: Dict[str, Any]) -> Case:
        distances = []
        for case in self.cases:
            distances.append(self._calculate_distance(new_problem, case.problem))
        min_index = np.argmin(distances)
        return self.cases[min_index]

    # def find_most_similar_case(self, new_problem: Dict[str, Any]) -> Case:
    #     cases = self.get_all_cases()
    #     distances = []
    #     for case in cases:
    #         distances.append(self._calculate_distance(new_problem, case.problem))
    #     min_index = np.argmin(distances)
    #     return cases[min_index]

    def _calculate_distance(self, problem1: Dict[str, Any], problem2: Dict[str, Any]) -> float:
        vec1 = np.array(list(problem1.values())).reshape(1, -1)
        vec2 = np.array(list(problem2.values())).reshape(1, -1)
        return euclidean_distances(vec1, vec2)[0][0]