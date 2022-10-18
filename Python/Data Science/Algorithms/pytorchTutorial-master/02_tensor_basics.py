import torch

# Everything in pytorch is based on Tensor operations.
# A tensor can have different dimensions
# so it can be 1d, 2d, or even 3d and higher

# scalar, vector, matrix, tensor

# torch.empty(size): uninitiallized
x = torch.empty(1) # scalar
print(x)
x = torch.empty(3) # vector, 1D
print(x)
x = torch.empty(2,3) # matrix, 2D
print(x)
x = torch.empty(2,2,3) # tensor, 3 dimensions
#x = torch.empty(2,2,2,3) # tensor, 4 dimensions
print(x)

# torch.rand(size): random numbers between [0, 1]
x = torch.rand(5, 3)
print(x)

# torch.randn(size): random numbers
x = torch.randn(5, 3)
print(x)

# torch.zeros(size), fill with 0
x = torch.zeros(5, 3)
print(x)

# torch.ones(size), fill with 1
x = torch.ones(5, 3)
print(x)

# check size
print(x.size())

# check data type
print(x.dtype)

# specify types, float32 default
x = torch.zeros(5, 3, dtype=torch.float16) #> other types include torch.int32, torch.double e.t.c.
print(x)

# construct from data
x = torch.tensor([5.5, 3])
print(x.size())

# Operations
y = torch.rand(2, 2)
x = torch.rand(2, 2)

# elementwise addition
z = x + y
# torch.add(x,y)

# in place addition
# Note: Everything with a trailing underscore is an inplace operation ie. it will modify the variable
# y.add_(x)

# substraction
z = x - y
z = torch.sub(x, y)
# y.sub_(x)

# multiplication
z = x * y
z = torch.mul(x,y)
# y.mul_(x)

# division
z = x / y
z = torch.div(x,y)
# y.div_(x)

# Slicing
x = torch.rand(5,3)
print(x)
print(x[:, 0]) # all rows, column 0
print(x[1, :]) # row 1, all columns
print(x[1,1]) # element at row 1, column 1

# Get the actual value if only 1 element in your tensor
print(x[1,1].item())

# Reshape with torch.view()
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
# if -1, pytorch will automatically determine the necessary size from the other dimension
# i.e for size (4, 4), the view (-1, 8) gives us (2, 8)
print(x.size(), y.size(), z.size())

# Numpy
# Converting a Torch Tensor to a NumPy array and vice versa is very easy
a = torch.ones(5)
print(a)

# torch to numpy with .numpy()
b = a.numpy()
print(b)
print(type(b))

# Careful: If the Tensor is on the CPU (not the GPU),
# both objects will share the same memory location, so changing one
# will also change the other
a.add_(1)
print(a)
print(b)

# numpy to torch with .from_numpy(x)
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)

# again be careful when modifying
a += 1
print(a)
print(b)

# requires_grad argument
# This will tell pytorch that it will need to calculate the gradients for this tensor
# later in your optimization steps
# i.e. this is a variable in your model that you want to optimize
x = torch.tensor([5.5, 3], requires_grad=True)

# by default all tensors are created on the CPU,
# but you can also move them to the GPU (only if it's available )
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5)         # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    # z = z.numpy() # not possible because numpy cannot handle GPU tensors
    # move to CPU again
    z.to("cpu")       # ``.to`` can also change dtype together!
    # z = z.numpy()

torch.randperm(n, out=Tensor, dtype=torch.long, device=device, requires_grad=True) # Returns a random permutation of integers from 0 to n - 1.

torch.numel(input) # Returns the total number of elements in the input tensor. The input is a tensor object.
