import matplotlib.pyplot as plt

KAPREKAR_CONSTANT = '6174'

def reverse_string(str):
  return str[::-1]

def sort_number(num_as_str, descending = False):
  sorted_str = ''.join(sorted(num_as_str))

  if descending:
    sorted_str = reverse_string(sorted_str)

  return int(sorted_str)

def kaprekar_routine(num_as_str):
  highest = sort_number(num_as_str, True)
  lowest = sort_number(num_as_str)
  result = str(highest - lowest)
  if len(result) == 3:
    result = '0' + result

  return result

def initialize_nums():
  nums = []
  for i in range(0, 10):
    for j in range(0, 10):
      for k in range(0, 10):
        for l in range(0, 10):
          if i == j == k == l:
            continue

          nums.append(str(i) + str(j) + str(k) + str(l))
          
  return nums

def run_iterations():
  nums = initialize_nums()
  iterations = []
  for num in nums:
    result = num
    iteration = 0
    while result != KAPREKAR_CONSTANT:
      result = kaprekar_routine(result)
      iteration += 1
    
    iterations.append(iteration)

  return nums, iterations

def plot(nums, iterations):
  plt.plot(nums, iterations)
  plt.xlabel('Four digit number')
  plt.ylabel('Kaprekar Routine')
  plt.show()

def main():
  nums, iterations = run_iterations()
  plot(nums, iterations)
  return

if __name__ == "__main__":
  main()
