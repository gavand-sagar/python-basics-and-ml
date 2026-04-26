# ============================================
# SIMPLEST PYTORCH MODEL (LINEAR REGRESSION)
# Goal: Learn y = 2x from data
# ============================================

import torch  # Main PyTorch library
import torch.nn as nn  # Neural network module (models, layers, loss functions)
import torch.optim as optim
import pandas as pd

from common import FareModel  # Optimizers (used to update weights)


df = pd.read_csv("data-main.csv")
df = df.dropna() # Remove any rows with empty values

X = torch.tensor(df[["distance","time","night"]].values,dtype=torch.float32)

y = torch.tensor(df["fare"].values, dtype=torch.float32).reshape(-1, 1)

    
model = FareModel()

loss_fn = nn.MSELoss()


# ============================================
# STEP 4: DEFINE OPTIMIZER
# ============================================

# Adam
optimizer = optim.Adam(model.parameters(), lr=0.001)


# ============================================
# STEP 5: TRAINING LOOP
# ============================================

for epoch in range(10000):
    # ---- Step 1: Forward Pass ----
    # Pass input X into model → get predictions
    y_pred = model(X)

    # ---- Step 2: Calculate Loss ----
    # Compare predicted vs actual values
    loss = loss_fn(y_pred, y)

    # ---- Step 3: Clear Old Gradients ----
    # Gradients accumulate in PyTorch, so we reset them
    optimizer.zero_grad()

    # ---- Step 4: Backward Pass ----
    # Compute gradients (how much to change weights)
    loss.backward()

    # ---- Step 5: Update Weights ----
    # Adjust weights using gradients
    optimizer.step()

    # Print loss every 10 epochs
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss = {loss.item()}")



torch.save(model.state_dict(),"model.pth")

# Export to ONNX
dummy_input = torch.randn(1, 3)

torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch_size"}}
)


# ============================================
# STEP 6: TEST MODEL
# ============================================
test = torch.tensor([[8.0, 25.0, 1.0]]) 
model.eval() # Good practice: set to evaluation mode
with torch.no_grad():
    prediction = model(test)

print("\nTest Input:", test)
print("Predicted Fare:", prediction.item()) # Just take the raw value
