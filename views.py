from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from quiz.models import Question, UserProfile, Quiz
from django.shortcuts import render
from training.models import Training
from django.db import IntegrityError
from django.http import Http404


def load_login(request):
    return render(request, 'registration/login.html')


def instruction(request, QuizNo):
    # Fetching username
    User = request.user.username  # Username
    User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()
    for Userdata in User_Profile:
        c = Userdata['Program_Code_id']  # Program Code id

    # Fetching his/her program name based on username
    b = Training.objects.values()
    ProgCode = ""
    for i in b:
        (i.get('id'))
        if i.get('id') == c:
            ProgCode = i.get("Program_Code")  # Program Code

    # Fetching number of questions per quiz
    Query_Quiz = Quiz.objects.filter(training__Program_Code=ProgCode).values()
    # print(Query_Quiz)
    for quiz_data in Query_Quiz:
        Instructions = quiz_data["Instruction"]
        QperQuiz = (quiz_data['Question_per_quiz'])  # Number of questions per quiz
        TperQuiz = (quiz_data['Timer_per_quiz'])  # Number of questions per quiz

    return render(request, 'quiz/instruction.html',
                  {"QuizNo": QuizNo, "ProgCode": ProgCode, "Instructions": Instructions, "Time": TperQuiz,
                   'QperQuiz': QperQuiz})


@login_required
def load_dashboard(request):
    User = request.user.username  # Username
    User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()
    for Userdata in User_Profile:
        c = Userdata['Program_Code_id']  # Program Code id
        Quiz1 = Userdata['Quiz1']
        Quiz2 = Userdata['Quiz2']
        Quiz3 = Userdata['Quiz3']

        Q1_status = Userdata['Quiz1_response']
        Q2_status = Userdata['Quiz2_response']
        Q3_status = Userdata['Quiz3_response']

        Q1_Score = Userdata["Quiz_1_Score"]
        Q2_Score = Userdata["Quiz_2_Score"]
        Q3_Score = Userdata["Quiz_3_Score"]

    comp_status = 0
    if Q1_status == "":
        comp_status += 1
    if Q2_status == "":
        comp_status += 1
    if Q3_status == "":
        comp_status += 1

    # Fetching his/her program name based on username
    b = Training.objects.values()
    ProgCode = ""

    for i in b:
        (i.get('id'))
        if i.get('id') == c:
            ProgCode = i.get("Program_Code")  # Program Code

    return render(request, 'quiz/dashboard.html',
                  {'user_identity': request.user, 'user_profile': User, "ProgCode": ProgCode, "Quiz1": Quiz1,
                   "Quiz2": Quiz2, "Quiz3": Quiz3, 'Quizzes_Completed': 3 - comp_status, "Q_remaining": comp_status,
                   "Avg_Score": round((Q1_Score + Q2_Score + Q3_Score) / 3, 2), 'Q1': Q1_status, 'Q2': Q2_status,
                   'Q3': Q3_status})


@login_required
def home(request, QuizNo, QuesNo):
    if request.method == 'POST':

        questions = Question.objects.all()
        wrong = 0
        correct = 0

        User = request.user.username
        User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()

        for userdata in User_Profile:
            Code = userdata['User_Code']
            Value = UserProfile.objects.get(User_Code=Code)
            c = userdata['Program_Code_id']  # Program Code id

            if int(QuizNo) == 1:
                k = userdata['Quiz1_response']
                Value.Quiz1 = False
                Value.Quiz2 = True
                Value.save()

            elif int(QuizNo) == 2:
                k = userdata['Quiz2_response']
                Value.Quiz2 = False
                Value.Quiz3 = True
                Value.save()

            elif int(QuizNo) == 3:
                k = userdata['Quiz3_response']
                Value.Quiz3 = False
                Value.save()

        QuizModels = Quiz.objects.filter(training_id=c).values()
        for a in QuizModels:
            total = a['Question_per_quiz']
            QperQuiz = a['Question_per_quiz']

        array = []
        for i in range(1, len(k), 3):
            print(k[i])
            array.append(int(k[i]))
        print('Array', array)

        flag = 0
        Start = int((QuizNo - 1) * QperQuiz + 1)
        End = int(QuizNo * QperQuiz) + 1
        J = 0

        for q in questions:
            temp = [q.Option_1, q.Option_2, q.Option_3, q.Option_4, q.Option_5, q.Option_6]

            if flag == len(array):
                break
            elif flag != len(array) and len(array) != 0:

                if J >= Start-1:
                    print(q.Ques_No, q.Correct_Option, temp[array[flag] - 1])
                    if q.Correct_Option == temp[array[flag] - 1]:
                        print("correct")
                        correct += 1
                        flag += 1
                    else:
                        print("incorrect")
                        wrong += 1
                        flag += 1
                elif J == End:
                    break
                J += 1

        print('total ', total)
        print('correct', correct)
        percent = correct / total * 100

        if int(QuizNo) == 1:
            Value.Quiz_1_Score = correct
            Value.save()

        elif int(QuizNo) == 2:
            Value.Quiz_2_Score = correct
            Value.save()

        elif int(QuizNo) == 3:
            Value.Quiz_3_Score = correct
            Value.save()

        context = {
            'questions': questions,
            'correct': correct,
            "QuizNo": QuizNo,
            'QuesNo': QuesNo,
            'wrong': wrong,
            'percent': round(percent, 2),
            'total': total,
        }

        return render(request, 'quiz/result_display.html', context)

    else:
        # Fetching username
        User = request.user.username  # Username
        User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()
        for Userdata in User_Profile:
            c = Userdata['Program_Code_id']  # Program Code id

        # Fetching his/her program name based on username
        b = Training.objects.values()
        ProgCode = ""

        for i in b:
            (i.get('id'))
            if i.get('id') == c:
                ProgCode = i.get("Program_Code")  # Program Code

        # Fetching number of questions per quiz
        Query_Quiz = Quiz.objects.filter(training__Program_Code=ProgCode).values()
        # print(Query_Quiz)
        for quiz_data in Query_Quiz:
            QperQuiz = (quiz_data['Question_per_quiz'])  # Number of questions per quiz
            TperQuiz = (quiz_data['Timer_per_quiz'])  # Number of questions per quiz
            filename = quiz_data['file']
        print(filename)

        questions = Question.objects.filter(training__Program_Code=ProgCode).values()

        # Appending all questions to QArray list
        QArray = []
        for i in questions:
            QArray.append(i)

        # reading data from the QBank file and saving it to models ---------------------------------------->
        import csv

        fileCodes = {2: 'DASM', 3: 'DASSM', 4: 'PMP', 5: 'CAPM', 6: 'PgMP', 7: 'ACP', 8: 'ICAgile', 9: 'SAFe Agilist',
                    10: 'Six Sigma', 12: 'EDPM', 14: 'PfMP'}

        try:
            file = open('media/' + filename)
        except:
            FileNotFoundError
        else:
            a = len(file.readlines())
            file.seek(0)

            data = csv.reader(file, delimiter=',')  # Reading the file
            for j in range(1, a - 1):
                for i in data:  # Pulling out rows of questions from csv file as list
                    try:
                        csv_ques = Question.objects.create(training_id=int(c), Ques_No=i[0])  # TODO
                    except:
                        IntegrityError
                    else:
                        csv_ques.Ques = i[1]
                        csv_ques.Option_1 = i[2]
                        csv_ques.Option_2 = i[3]
                        csv_ques.Option_3 = i[4]
                        csv_ques.Option_4 = i[5]
                        csv_ques.Option_5 = i[6]
                        csv_ques.Option_6 = i[7]

                        csv_ques.Correct_Option = i[8]
                        csv_ques.Answer_Description = i[9]
                        csv_ques.save()

        # reading and saving ends here  ------------------------------------------------------------>

        # # Preparing individual quizzes as list of dictionary from the question array (QArray) based on numOfQues/per
        # # stored in a list QuizArray [[{},{},{},{}], [{},{}.{},{}]]

        QuizArray = []
        while len(QArray) >= QperQuiz:
            flag = []
            for i in range(QperQuiz):
                flag.append(QArray[i])

            QuizArray.append(flag)
            QArray[0:QperQuiz] = []

        if len(QuizArray) >= QuizNo:
            # print(QuizNo, QuesNo)
            context = {
                'a': QuizArray[QuizNo - 1][QuesNo - 1],
                "ProgCode": ProgCode,
                "time": TperQuiz,
                "QperQuiz": QperQuiz,
                'QuesNo': QuesNo,
                "QuizNo": QuizNo

            }

            return render(request, 'quiz/quiz_instance.html', context)
        else:
            raise Http404()


ResponseArray1 = []
ResponseArray2 = []
ResponseArray3 = []


def test(request):
    QuizNum = request.POST.get("QuizNum")
    QuesNum = request.POST.get("QuesNum")
    OptionNum = request.POST.get("response")
    print("POST: ", request.POST)

    User = request.user.username
    User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()
    for userdata in User_Profile:
        Code = userdata['User_Code']

    Value = UserProfile.objects.get(User_Code=Code)

    if int(QuizNum) == 1:
        ResponseArray1.append(int(OptionNum))
        print("local1: ", ResponseArray1)
        Value.Quiz1_response = ResponseArray1
        Value.save()

    elif int(QuizNum) == 2:
        ResponseArray2.append(int(OptionNum))
        print("local2: ", ResponseArray2)
        Value.Quiz2_response = ResponseArray2
        Value.save()

    elif int(QuizNum) == 3:
        ResponseArray3.append(int(OptionNum))
        print("local3: ", ResponseArray3)
        Value.Quiz3_response = ResponseArray3
        Value.save()

    return HttpResponse('hi')


def result(request, QuizNo, QuesNo):
    # Fetching username
    User = request.user.username  # Username
    User_Profile = UserProfile.objects.filter(User_Identity__username=User).values()
    for Userdata in User_Profile:
        c = Userdata['Program_Code_id']  # Program Code id
        Score1 = Userdata['Quiz_1_Score']
        Score2 = Userdata['Quiz_2_Score']
        Score3 = Userdata['Quiz_3_Score']

        if QuizNo == 1:
            d = Userdata["Quiz1_response"]  # Quiz1 response
        elif QuizNo == 2:
            d = Userdata["Quiz2_response"]  # Quiz2 response
        elif QuizNo == 3:
            d = Userdata["Quiz3_response"]  # Quiz3 response
    Scores = [Score1, Score2, Score3]

    array = []
    for i in range(1, len(d), 3):
        array.append(int(d[i]))
    print(array)

    # Fetching his/her program name based on username
    b = Training.objects.values()
    ProgCode = ""

    for i in b:
        (i.get('id'))
        if i.get('id') == c:
            ProgCode = i.get("Program_Code")  # Program Code

    # Fetching number of questions per quiz
    Query_Quiz = Quiz.objects.filter(training__Program_Code=ProgCode).values()
    # print(Query_Quiz)
    for quiz_data in Query_Quiz:
        QperQuiz = (quiz_data['Question_per_quiz'])  # Number of questions per quiz

    questions = Question.objects.filter(training__Program_Code=ProgCode).values()

    # Appending all questions to QArray list
    flag = 0
    QArray = []

    Start = int((QuizNo - 1) * QperQuiz + 1)
    End = int(QuizNo * QperQuiz) + 1
    J = 0
    for i in questions:
        if Start + J == End:
            break
        elif ProgCode + str(Start + J) in i['Ques_No']:
            i["Response"] = array[J]
            print(i)
            J += 1
            QArray.append(i)

    # for i in questions:
    #     if flag == QperQuiz:
    #         break
    #     else:
    #         i["Response"] = array[flag]
    #         print(array[flag])
    #         flag += 1
    #         QArray.append(i)

    # if QuizNo == 1:
    #     QArray = QArray[0:QperQuiz]
    #     print(QArray)
    # elif QuizNo == 2:
    #     QArray = QArray[QperQuiz: 2 * QperQuiz]
    #     print(QArray)
    #
    # elif QuizNo == 3:
    #     QArray = QArray[2 * QperQuiz:3 * QperQuiz]
    #     print(QArray)

    context = {
        'QuizArray': QArray[QuesNo - 1],
        'Scores': Scores[QuizNo - 1],
        "ProgCode": ProgCode,
        'QperQuiz': QperQuiz,
        'QuesNo': QuesNo,
        'Next': QuesNo + 1,
        'Previous': QuesNo - 1,
        "QuizNo": QuizNo
    }

    return render(request, 'quiz/ans-reason.html', context)
