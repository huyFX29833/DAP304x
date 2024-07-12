answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')
while True:
  file_name = input("Enter a class file to grade (i.e. class1 for class1.txt):")
  if '.txt' not in file_name:
    file_name += '.txt'
  try:
    with open("/Data Files/"+file_name,"r") as class_file:
      print("Successfully opened "+file_name)
      num_lines = 0
      invalid_lines = 0
      scores = []
      studentID = []
      highscore = 0
      question_skips = {i: 0 for i in range(1, 26)}
      question_wrong = {i: 0 for i in range(1, 26)}
      print("\n***** ANALYZING *****")
      for line in class_file:
        num_lines += 1
        rubric = line.strip().split(',')
        studentID.append(rubric[0])
        if len(rubric) != 26:
          print("Line",num_lines,"does not contain exactly 26 values")
          print(line)
          invalid_lines += 1
        elif rubric[0][0] != 'N' or len(rubric[0]) != 9 or not rubric[0][1:].isdigit():
          print("Line",num_lines,"contains invalid ID N#")
          print(line)
          invalid_lines += 1
        else:
          answers = rubric[1:]
          score = 0
          for idx, answer in enumerate(answers):
            if answer == "":
              question_skips[idx+1] += 1
            elif answer != answer_key[idx]:
              score -= 1
              question_wrong[idx+1] += 1
            else:
              score += 4
          if score > 80:
            highscore += 1
          scores.append(score)
      if invalid_lines == 0:
        print("No errors found!")
      print("\n***** REPORTS *****")
      print("Number of lines in the file:",num_lines)
      print("Number of invalid lines:",invalid_lines)
      print("\nTotal number of students with highscore (>80): ", highscore)

      print("Mean (average) score: ", sum(scores)/len(scores))
      print("Highest score: ", max(scores))
      print("Lowest score: ", min(scores))
      print("Range of scores: ", max(scores)-min(scores))
      sorted_scores = sorted(scores)
      n = len(sorted_scores)
      if n % 2 == 0:
        median1 = sorted_scores[n//2]
        median2 = sorted_scores[n//2 - 1]
        median_score = (median1 + median2)/2
      else:
        median_score = sorted_scores[n//2]
      print("Median score: ", median_score)

      max_skip = max(question_skips.values())
      skip_ratio = max_skip / len(answers)
      print("\nMost skipped questions: question - number of skips - ratio")
      for question, skip in question_skips.items():
        if skip == max_skip:
          print(' ',question, max_skip, skip_ratio)

      max_wrong = max(question_wrong.values())
      wrong_ratio = max_wrong / len(answers)
      print("\nMost wrong questions: question - number of wrongs - ratio")
      for question, wrong in question_wrong.items():
        if wrong == max_wrong:
          print(' ',question, max_wrong, wrong_ratio)
    class_file.close()

    file_result = file_name.replace(".txt","_grades.txt")
    with open("/Data Files/"+file_result,"w") as result_file:
      for i in range(len(studentID)):
        result_file.write(studentID[i] + ", " + str(scores[i]) + "\n")
      result_file.close()

    break
  except FileNotFoundError:
    print("File cannot be found. Please try again!")
