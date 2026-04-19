import onnxruntime as ort
import numpy as np
import torch

session = ort.InferenceSession("model.onnx")

X = np.array([[1, 1]],dtype=np.float32)

outputs = session.run(None, {"input": X})

outputTensor = torch.tensor(outputs)

print("Predicted Output:", torch.sigmoid(outputTensor))



