from collections import deque


def math_operations(*nums, **kwargs):
    nums = deque(nums)
    operations = deque(['a', 's', 'd', 'm'])
    while nums:
        val = operations[0]
        if val == 'a':
            kwargs[val] += nums.popleft()
        elif val == 's':
            kwargs[val] -= nums.popleft()
        elif val == 'd':
            try:
                kwargs[val] /= nums[0]
                nums.popleft()
            except ZeroDivisionError:
                nums.popleft()
        elif val == 'm':
            kwargs[val] *= nums.popleft()
        operations.append(operations.popleft())
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
