# ============================================
# SIMPLEST PYTORCH MODEL (LINEAR REGRESSION)
# Goal: Learn y = 2x from data
# ============================================

import torch  # Main PyTorch library
import torch.nn as nn  # Neural network module (models, layers, loss functions)
import torch.optim as optim  # Optimizers (used to update weights)


# ============================================
# STEP 1: CREATE DATA
# ============================================

# Input features (X) → 3 samples, 1 feature each
X = torch.tensor([[1.0],[2.0],[3.0]])

# Target values (y) → expected output
y = torch.tensor([[2.0], [4.0], [6.0]])

# This represents:
# 1 → 2
# 2 → 4
# 3 → 6
# So the model should learn: y = 2x


# ============================================
# STEP 2: CREATE MODEL
# ============================================

# nn.Linear(in_features, out_features)
# Here: 1 input → 1 output
model = nn.Linear(1, 1)

# Internally, this creates:
# y = w*x + b
# where w (weight) and b (bias) are learnable


# ============================================
# STEP 3: DEFINE LOSS FUNCTION
# ============================================

# Mean Squared Error:
# loss = (predicted - actual)^2
loss_fn = nn.MSELoss()


# ============================================
# STEP 4: DEFINE OPTIMIZER
# ============================================

# SGD = Stochastic Gradient Descent
# model.parameters() → gives w and b
# lr = learning rate (step size for updates)
optimizer = optim.SGD(model.parameters(), lr=0.01)


# ============================================
# STEP 5: TRAINING LOOP
# ============================================

for epoch in range(1000):
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








# ============================================
# STEP 6: TEST MODEL
# ============================================

# Test with new input
test_input = 14.0
test = torch.tensor([[test_input]])

# Model should predict ~8.0
prediction = model(test)

print("\nTest Input: " + str(test_input))
print("Predicted Output:", prediction.item())


# ============================================
# OPTIONAL: SEE LEARNED PARAMETERS
# ============================================

# weight (w) and bias (b)
for name, param in model.named_parameters():
    print(f"{name} = {param.data}")
