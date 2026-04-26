
import torch  # Main PyTorch library
from common import FareModel  # Optimizers (used to update weights)

    
model = FareModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

print("Model loaded Successfully.")



# Test with new input
test = torch.tensor([[8.11, 25.55, 1.0]]) 
# model.eval() # Good practice: set to evaluation mode
# with torch.no_grad():
prediction = model(test)

print("\nTest Input:", test)
print("Predicted Fare:", prediction.item()) # Just take the raw value
