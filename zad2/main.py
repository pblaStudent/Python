import time

#Iteracja 

iterable = range(1, 101)
start_time_iteration = time.time()
result_iteration = [x for x in iterable]
end_time_iteration = time.time()
print("Iteration style for loop result:", result_iteration)

#Cpp
start_time_cpp = time.time()
result_cpp = []
for i in range(len(iterable)):
    result_cpp.append(iterable[i])
end_time_cpp = time.time()
print("C++-style for loop result:", result_cpp)

results_match = result_iteration == result_cpp
execution_time_iteration = end_time_iteration - start_time_iteration
execution_time_cpp = end_time_cpp - start_time_cpp

print("Do results match?", results_match)
print(f"Iteration-style for loop execution time: {execution_time_iteration:.10f} seconds")
print(f"C++-style for loop execution time: {execution_time_cpp:.10f} seconds")
