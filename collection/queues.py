from collections import deque
queue = deque(["Fed","Nat","Dem"])
queue.append("Lib")
queue.append("Rats")
print(queue)
queue.popleft()

print ("after popleft", queue)