# Road Class

Read this guideline before completing the task:  
[Guideline](https://github.com/ketstap162/tasks-guideline)

## Task

Implement `Road` class that takes one argument - `length`.
Note that:
- `length` should be integer. Otherwise, a `TypeError` must be raised.
- `length` should be greater than `0`. Otherwise, a `ValueError` should be raised.

Implement `magic methods` for `Road`:

- Magic method for `len()` function (`len(road)`)
- Magic method for stack roads or increasing the road (`road + road` or `road + 5`)  
Note: It should work with Road example or integer value!
- Magic methods for compare roads:
```
==
<=
>=
<
>
!=
```

Run command `pytest` in terminal before pushing solution.