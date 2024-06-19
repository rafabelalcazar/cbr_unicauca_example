from caseController import Case, CaseBase

# Example usage
if __name__ == "__main__":
    
    # Define the MongoDB database and collection names
    db_name = "cbr_db"
    collection_name = "cases"
    
    # Create a case base connected to MongoDB
    # case_base = CaseBase(db_name=db_name, collection_name=collection_name)
    case_base = CaseBase()

    # Define some cases
    case1 = Case(problem={"feature1": 1.0, "feature2": 2.0}, solution="Solution 1")
    case2 = Case(problem={"feature1": 2.0, "feature2": 3.0}, solution="Solution 2")

    # Add cases to the MongoDB case base
    case_base.add_case(case1)
    case_base.add_case(case2)

    # Define a new problem
    new_problem = {"feature1": 1.6, "feature2": 2.5}

    # Retrieve the most similar case
    similar_case = case_base.find_most_similar_case(new_problem)

    # Print the retrieved case's solution
    print(f"The most similar case solution is: {similar_case.solution}")