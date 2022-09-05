def decor_result(result_function):
          def distinction(marks):
                    for m in marks:
                              if m>=75:
                                        print("Distinction")
                    result_function(marks)
          return distinction

@decor_result
def result(marks):
          for m in marks:
                    if m>=33:
                              pass
                    else:
                              print("Fail")
                              break
          else:
                    print("Pass")
result([50,60,70,80,75])