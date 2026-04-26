
import torch  # Main PyTorch library
from common import XORModel  # Optimizers (used to update weights)

    
model = XORModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

print("Model loaded Successfully.")



# Test with new input
test = torch.tensor([[1.0,1.0]]) 

# Model should predict ~8.0
prediction = model(test)

print("\nTest Input: " + str(test))
print("Predicted Output:", torch.sigmoid(prediction))

