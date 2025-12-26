from tasks.classify import ClassifyTask

task = ClassifyTask(labels=["billing", "bug", "feature_request", "other"])
inp = task.input_model.model_validate({"text": "I was charged twice"})
print(task.build_prompt(inp))
