def google_docstrings(num1, num2
                      ) -> int:
    """Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Args:
        num1 (int) : First number to add.
        num2 (int) : Second number to add.

    Returns:
        The sum of ``num1`` and ``num2``.

    Raises:
        AnyError: If anything bad happens.
    """
    return num1 + num2


def numpy_docstrings(num1, num2) -> int:
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    Raises
    ======
     MyException
        if anything bad happens

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


def sphinx_docstrings(num1, num2) -> int:
    """Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    :param int num1: First number to add.
    :param int num2: Second number to add.
    :returns:  The sum of ``num1`` and ``num2``.
    :rtype: int
    :raises AnyError: If anything bad happens.
    """
    return num1 + num2
