def test_function():
    def inner_function():
        print("Привет, я в области видимости test_function")

    inner_function()

test_function()

inner_function()