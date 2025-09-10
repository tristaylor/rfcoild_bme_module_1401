import matlab.engine
eng = matlab.engine.start_matlab()

result = eng.sqrt(12.0)
print(result)

