import matlab.engine
eng = matlab.engine.start_matlab()

result = eng.sqrt(16.0)
print(result)
