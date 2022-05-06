def reverse_string(str):
  return str[::-1]

def sort_number(num, descending = False):
  num_as_str = str(num)
  sorted_str = ''.join(sorted(num_as_str))

  if descending:
    sorted_str = reverse_string(sorted_str)

  return int(sorted_str)

def kaprekar_routine(num):
  highest = sort_number(num, True)
  lowest = sort_number(num)
  return (highest - lowest)

