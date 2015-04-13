
def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
            fns,
            data)

