# In the MVC paradigm of coding, most of the code that parses data and does computations shouldn't be written in the
# View, but rather in the Model. However, FlaskClassy objects blur that line and you can functionally write all three
# pieces in the route methods. We choose to offload large blocks of computational code into these
# pseudo model/controller files, import the functions into the View that calls them, and then call the method name. By
# doing so, we keep the View files relatively short and easy to read through. It also helps keep the View imports as
# sparse as we can. This also allows us to create methods that are called by other Controllers or multiple Views that
# share a common theme, like database or caching functions.


def large_computational_function(end):
    return sum(range(end))
