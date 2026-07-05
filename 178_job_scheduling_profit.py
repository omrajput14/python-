class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def print_job_scheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j].profit < arr[j + 1].profit:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t
    job = ['-1'] * t

    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i].deadline - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i].id
                break

    print("Following is maximum profit sequence of jobs:")
    print(job)

if __name__ == '__main__':
    arr = [Job('a', 2, 100),
           Job('b', 1, 19),
           Job('c', 2, 27),
           Job('d', 1, 25),
           Job('e', 3, 15)]
           
    print_job_scheduling(arr, 3)
