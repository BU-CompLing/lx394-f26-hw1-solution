# HW 1 Solution

### Problem 1a

The code `hw1.hello_world()` calls the function `hello_world` defined in the `hw1.py` file (a.k.a. the `hw1` module).

To call the function `foo_bar` in `hw1.py`, you would run `hw1.foo_bar()`.

### Problem 1b

If you changed `hw1.py` while running the notebook and you wanted to use the new version of your code, you would _reload_ the `hw1` module by running `importlib.reload(hw1)`.

### Problem 1c

Type hints are optional annotations of a function definition that tell you what type each parameter of the function should be, as well as the type of the function's return value. The Python specifications do not require you to obey type hints; they are merely suggestions, meant to help you and other programmers understand what each function is supposed to do. 

If we were to add type hints to the function definition of `hw1.my_name`, it would look like this:
```python
def my_name() -> None:
    hello_world()
    print("My name is _.")
```
The `hw1.my_name` function does not have any parameters, so there are no parameters to add type hints to. The `hw1.my_name` also does not contain a `return` statement, so its return value (i.e., output) is always `None`.

### Problem 1d

The `dict.keys` method returns a `list`-like object containing the keys of a `dict`.

The `dict.values` method returns a `list`-like object containing the values of a `dict`.

The `dict.items` method returns a `list`-like object containing the key–value pairs of a `dict`, where each key–value pair is represented as a `tuple`.

When you cast a `dict` to a `list` or a `set`, you get a `list` or a `set` (respectively) containing the `dict`'s keys. Thus, if `d` is a `dict`, then `set(d) == set(d.keys())`.

### Problem 1f

First, notice that `FreqDist`s assign a default value of `0` to any key not contained in the `FreqDist`. For example, if you run the following code:
```python
dist1 = FreqDist({"the": 60, "of": 30, "and": 20})
dist1["in"]
```
the result should be `0`.

Now, suppose `fd1` and `fd2` are `FreqDist`s. Then, `fd1 + fd2` is a `FreqDist` whose keys are all the keys appearing in either `fd1` or `fd2`, and whose values are the sum of the corresponding values in `fd1` and `fd2`. That is to say,
```python
# This statement is True...
set(fd1 + fd2) == set(fd1).union(fd2)
```
and 
```python
for k, v in (fd1 + fd2).items():
    # ...these statements are all True.
    v == fd1[k] + fd2[k]
```

### Problem 1g

Yes.

### Problem 1h

Since `x` is a `list`, and `list` is a mutable type, the value of `x` is a _reference_ to the location in memory where the items in the `list` are stored. When you run the following code:
```python
x = [1, 2, 3]
y = [x, [4, 5, 6], x]
```
the `list` items `y[0]` and `y[2]` are references pointing to the same location in memory that `x` is pointing to. The code `x[0] = 7` changes item `0` of the `list` stored at that location in memory, and all variables referencing that location—in this case, `x`, `y[0]`, and `y[2]`—will reflect that change.

On the other hand, if you run this code:
```python
x = [7, 2, 3]
```
the Python interpreter creates a new `list`, and changes the value of `x` to reference the location of that new `list`. The original `list`, which is referenced by `y[0]` and `y[1]`, does not change.

### Problem 2a

Roughly 59.8. 

**Explanation (Optional):** Sophie calculated this using the following code.
```python
w = "delve"
rel_freq_chatgpt = chatgpt_articles.count(w) / len(chatgpt_articles)
rel_freq_wiki = wiki_articles.count(w) / len(wiki_articles)
rel_freq_chatgpt / rel_freq_wiki
```

### Problem 2b

Recall that the goal of this assignment is to "study the statistical characteristics of ChatGPT-generated text" (quoted from [the top of the problem set](https://github.com/BU-LX394/hw1/blob/main/hw1-pset.ipynb)).

[Kilgarriff's](https://www.sketchengine.eu/wp-content/uploads/2015/04/2009-Simple-maths-for-keywords.pdf) first problem concerns whether the Wikipedia corpus is a suitable reference corpus for the ChatGPT corpus. Ideally, we would like for the two corpora to be more or less the same, except in terms of "one particular dimension of difference" (Kilgarriff, 2009, p. 1). That seems to be true for the ChatGPT and Wikipedia corpora; [Singh et al. (2024)](https://www.sciencedirect.com/science/article/pii/S294971912300047X) designed the ChatGPT articles to be similar to the Wikipedia articles in terms of length and content. We can therefore assume that the differences between these corpora are attributable to differences in "statistical characteristics" between ChatGPT-generated text and Wikipedia text.

Kilgarriff's second concern is that the frequency distribution of a text often reflects the topic of that text, rather than the general statistical characteristics of its writer(s). For example, the slides for this course contain many occurrences of the word "Python"; but that is only because this is a course about Python, and not because Sophie has any particular inclination for using that word. This is not a concern for our assignment, however, because Singh et al. (2024) have ensured that the ChatGPT corpus contains one article corresponding to each Wikipedia article, and therefore the two corpora have the same topics in roughly the same proportions.

### Problem 2g

Filming, 18–49, Nielsen, unconnected, theatrically

### Problem 2h

Kilgarriff's fourth problem states that frequency ratios, as a keyness metric, are biased towards token types that are rare in the reference corpus. This is because, for example, it is very easy to find token types (like _delve_) that appear a few times in the target corpus, but 1 or 0 times in the reference corpus. 

Kilgarriff's solution to this problem is to use smoothing with a very large `k`, which reduces frequency ratios for very rare token types. For example, suppose you had two corpora of the same length and vocabulary size, where _delve_ appears 68 times in the target corpus and 1 time in the reference corpus. Then, the frequency ratio for _delve_ would be:

$$\frac{68}{1} = 68$$

But now let's say we used add-1000 smoothing. Then, the frequency ratio for _delve_ would be:

$$\frac{68 + 1000}{1 + 1000} \approx 1.067$$

which is a lot smaller.

When we identify ChatGPT keywords using add-1 and add-1000 smoothing, we get the following results.

|   | Keyword (k = 1) | Count in Wiki Corpus | Keyword (k = 1000) | Count in Wiki Corpus |
|---|-----------------|----------------------|--------------------|----------------------|
| 1 | stunning     | 2 | unique | 265 |
| 2 | reminder     | 3 | significant | 1110 |
| 3 | breathtaking | 0 | challenges | 91 |
| 4 | must-watch   | 0 | ' | 212 |
| 5 | must-visit   | 0 | important | 1006 |
| | **Average** | **1** | **Average** | **536.8** |

Using add-1000 smoothing gives us keywords that are much more common in the Wikipedia corpus, compared to the keywords we get when we use add-1 smoothing.
