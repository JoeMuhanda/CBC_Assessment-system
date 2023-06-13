mage file will appear here


class LearnerPortfolio:
    def __init__(self, learner_name):
        self.learner_name = learner_name
        self.artifacts = []
    
    def add_artifact(self, artifact):
        self.artifacts.append(artifact)
    
    def display_artifacts(self):
        if not self.artifacts:
            print(f"No artifacts found for {self.learner_name}.")
        else:
            print(f"Artifacts for {self.learner_name}:")
            for index, artifact in enumerate(self.artifacts, start=1):
                print(f"{index}. {artifact}")
    
    def remove_artifact(self, artifact):
        if artifact in self.artifacts:
            self.artifacts.remove(artifact)
            print(f"Artifact '{artifact}' removed successfully from {self.learner_name}'s portfolio.")
        else:
            print(f"Artifact '{artifact}' not found in {self.learner_name}'s portfolio.")

portfolio = LearnerPortfolio("John Doe")
portfolio.add_artifact("Assignment 1")
portfolio.add_artifact("Project presentation")
portfolio.display_artifacts()

portfolio.remove_artifact("Assignment 1")
portfolio.display_artifacts()
