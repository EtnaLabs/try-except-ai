from try_except_ai import TryExceptAI


def test_function():
    try:
        # Code that might raise an exception
        result = 1 / 0
        print(result)
    except Exception as e:
        TryExceptAI().handle_exception(e)


if __name__ == "__main__":
    test_function()
