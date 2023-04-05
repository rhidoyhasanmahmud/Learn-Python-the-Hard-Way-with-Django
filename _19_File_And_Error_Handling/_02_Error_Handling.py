try:
  # Dangerous stuff
except ValueError:
  # If you use try, at least 1 except block is mandatory!
  # Handle it somehow / ignore
except (BadThingError, HorrbileThingError) as e:
  # Hande it differently
except:
  # This will catch every exception.
else:
  # Else block is not mandatory.
  # Dangerous stuff ended with no exception
finally:
  # Finally block is not mandatory.
  # This will ALWAYS happen after the above blocks.
  
## 

raise Exception("Shouldn't be Odd Number")
